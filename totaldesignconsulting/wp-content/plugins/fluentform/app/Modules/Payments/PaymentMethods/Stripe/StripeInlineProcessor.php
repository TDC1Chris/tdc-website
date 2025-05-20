<?php

namespace FluentForm\App\Modules\Payments\PaymentMethods\Stripe;

use FluentForm\App\Helpers\Helper;
use FluentForm\App\Modules\Payments\PaymentHelper;
use FluentForm\Framework\Helpers\ArrayHelper;
use FluentForm\App\Modules\Payments\PaymentMethods\Stripe\API\SCA;
use FluentForm\App\Modules\Payments\PaymentMethods\Stripe\API\Plan;
use FluentForm\App\Modules\Payments\PaymentMethods\Stripe\API\Invoice;
use FluentForm\App\Modules\Payments\PaymentMethods\Stripe\API\Customer;

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

class StripeInlineProcessor extends StripeProcessor
{
    
    public function init()
    {
        /*
         * After form submission this hooks fire to start Making payment
         */
        add_action('fluentform/process_payment_stripe_inline', [$this, 'handlePaymentAction'], 10, 6);

        /*
         * Mainly for single payment items
         */
        add_action('wp_ajax_fluentform_sca_inline_confirm_payment', [$this, 'confirmScaPayment']);
        add_action('wp_ajax_nopriv_fluentform_sca_inline_confirm_payment', [$this, 'confirmScaPayment']);

        /*
         * For Subscription payment + maybe single payment items
         */
        add_action('wp_ajax_fluentform_sca_inline_confirm_payment_setup_intents', array($this, 'confirmScaSetupIntentsPayment'));
        add_action('wp_ajax_nopriv_fluentform_sca_inline_confirm_payment_setup_intents', array($this, 'confirmScaSetupIntentsPayment'));
    }

    public function handlePaymentAction($submissionId, $submissionData, $form, $methodSettings, $hasSubscriptions, $totalPayable)
    {
        $this->setSubmissionId($submissionId);
        $this->form = $form;
        $submission = $this->getSubmission();
        $paymentTotal = $this->getAmountTotal();
        
        if (!$paymentTotal && !$hasSubscriptions) {
            return false;
        }

        // Create the initial transaction here
        $transaction = $this->createInitialPendingTransaction($submission, $hasSubscriptions);

        $paymentMethodId = ArrayHelper::get($submissionData['response'], '__stripe_payment_method_id');
        $customerArgs = $this->customerArguments($paymentMethodId, $submission);

        $customer = Customer::createCustomer($customerArgs, $this->form->id);

        if (is_wp_error($customer)) {
            // We have errors
            $this->handlePaymentChargeError($customer->get_error_message(), $submission, $transaction);
        }

        if ($transaction->transaction_type == 'subscription') {
            $this->handleSetupIntent($submission, $paymentMethodId, $customer, $transaction, $totalPayable);
        } else {
            // Let's create the one time payment first
            // We will handle One-Time Payment Here only
            $paymentSettings = PaymentHelper::getFormSettings($form->id, 'admin');
            $intentArgs = [
                'payment_method'              => $paymentMethodId,
                'amount'                      => $transaction->payment_total,
                'currency'                    => $transaction->currency,
                'confirmation_method'          => 'manual',
                'confirm'                      => 'true',
                'description'                 => $this->getProductNames(),
                'statement_descriptor_suffix' => StripeSettings::getPaymentDescriptor($form),
                'metadata'                    => $this->getIntentMetaData($submission, $form, $transaction, $paymentSettings),
                'customer'                    => $customer->id
            ];

            $intentArgs = apply_filters('fluentform/stripe_checkout_args_inline', $intentArgs, $submission, $transaction, $form);

            // If FluentForm Pro is not installed, apply the fee 1.9% of the total amount
            if (!Helper::hasPro()) {
                $applicationFeeAmount = (int) ($totalPayable * 0.019);
                $intentArgs['application_fee_amount'] = $applicationFeeAmount;
            }
            $this->handlePaymentIntent($transaction, $submission, $intentArgs);
        }
    }

    // This is only for Subscription Payment
    protected function handleSetupIntent($submission, $paymentMethodId, $customer, $transaction, $totalPayable)
    {
        if (is_wp_error($customer)) {
            $this->handlePaymentChargeError($customer->get_error_message(), $submission, $transaction, false, 'customer');
        }

        $subscriptions = $this->getSubscriptions();

        $subscription = $subscriptions[0];

        $subscriptionTransactionArgs = Plan::getPriceIdsFromSubscriptionTransaction($subscription, $transaction);

        if(is_wp_error($subscriptionTransactionArgs)) {
            $this->handlePaymentChargeError($customer->get_error_message(), $submission, $transaction, false, 'customer');
        }

        $subscriptionArgs = [
            'customer'         => $customer->id,
            'metadata'         => $this->getIntentMetaData($submission, $this->getForm(), $transaction),
            'payment_behavior' => 'allow_incomplete',
        ];

        $subscriptionArgs['items'] = $subscriptionTransactionArgs['items'];

        if ($signupFee = $subscriptionTransactionArgs['signup_fee']) {
            Invoice::createItem([
                'amount'      => $signupFee,
                'currency'    => $submission->currency,
                'customer'    => $customer->id,
                'description' => __('Signup fee for ', 'fluentform') . $subscription->plan_name
            ], $submission->form_id);
        }

        // Maybe we have to set a cancel_at parameter to subscription args
        if ($cancelledAt = Plan::getCancelledAtTimestamp($subscription)) {
            $subscriptionArgs['cancel_at'] = $cancelledAt;
        }

        if ($subscription->trial_days) {
            $dateTime = current_datetime();
            $localtime = $dateTime->getTimestamp() + $dateTime->getOffset();
            $subscriptionArgs['trial_end'] = $localtime + $subscription->trial_days * 86400;
        }

        $subscriptionArgs = apply_filters('fluentform/stripe_subscription_args_inline', $subscriptionArgs, $submission, $transaction, $this->getForm());

        // If FluentForm Pro is not installed, apply the fee 1.9%
        if (!Helper::hasPro()) {
            $subscriptionArgs['application_fee_percent'] = 1.9;
        }

        $subscriptionPayment = Plan::subscribe($subscriptionArgs, $submission->form_id);

        if (is_wp_error($subscriptionPayment)) {
            $this->handlePaymentChargeError($subscriptionPayment->get_error_message(), $submission, $transaction, false, 'subscription');
        }

        $invoice = Invoice::retrieve(
            $subscriptionPayment->latest_invoice,
            $this->form->id,
            [
                'expand' => ['payment_intent.charges']
            ]
        );
        if (is_wp_error($invoice)) {
            $this->handlePaymentChargeError($invoice->get_error_message(), $submission, $transaction, false, 'invoice');
        }

        if (
            $invoice->payment_intent &&
            $invoice->payment_intent->status == 'requires_action' &&
            $invoice->payment_intent->next_action->type == 'use_stripe_sdk'
        ) {
            $transactionId = false;
            if ($transaction) {
                $transactionId = $transaction->id;
            }
            $this->processScaBeforeVerification($submission->form_id, $submission->id, $transactionId, $invoice->payment_intent->id);

            wp_send_json_success([
                'nextAction'             => 'payment',
                'actionName'             => 'stripeSetupIntent',
                'stripe_subscription_id' => $subscriptionPayment->id,
                'payment_method_id'      => $paymentMethodId,
                'intent'                 => $invoice->payment_intent,
                'submission_id'          => $submission->id,
                'customer_name'          => ($transaction) ? $transaction->payer_name : '',
                'customer_email'         => ($transaction) ? $transaction->payer_email : '',
                'client_secret'          => $invoice->payment_intent->client_secret,
                'message'                => __('Verifying your card details. Please wait...', 'fluentform'),
                'result'                 => [
                    'insert_id' => $submission->id
                ]
            ], 200);
        }

        // now this payment is successful. We don't need anything else
        $this->handlePaidSubscriptionInvoice($invoice, $submission);
    }

    protected function customerArguments($paymentMethodId, $submission)
    {
        $customerArgs = [
            'payment_method'   => $paymentMethodId,
            'invoice_settings' => [
                'default_payment_method' => $paymentMethodId
            ],
            'metadata'         => [
                'submission_id' => $submission->id,
                'form_id'       => $submission->form_id,
                'form_name'     => strip_tags($this->form->title)
            ]
        ];

        $receiptEmail = PaymentHelper::getCustomerEmail($submission, $this->form);

        if ($receiptEmail) {
            $customerArgs['email'] = $receiptEmail;
        }

        $receiptName = PaymentHelper::getCustomerName($submission, $this->form);

        if ($receiptName) {
            $customerArgs['name'] = $receiptName;
            $customerArgs['description'] = $receiptName;
        }

		$address = PaymentHelper::getCustomerAddress($submission);
		if ($address) {
			$customerArgs['address'] = [
				'city'        => ArrayHelper::get($address, 'city'),
				'country'     => ArrayHelper::get($address, 'country'),
				'line1'       => ArrayHelper::get($address, 'address_line_1'),
				'line2'       => ArrayHelper::get($address, 'address_line_2'),
				'postal_code' => ArrayHelper::get($address, 'zip'),
				'state'       => ArrayHelper::get($address, 'state'),
			];
		}

        return $customerArgs;
    }

    protected function handlePaidSubscriptionInvoice($invoice, $submission)
    {
        if ($invoice->status !== 'paid') {
            wp_send_json([
                'errors' => __('Stripe Error: Payment Failed! Please try again.', 'fluentform')
            ], 423);
        }

        // Submission status as paid
        $this->changeSubmissionPaymentStatus('paid');

        $subscriptions = $this->getSubscriptions();

        $this->processSubscriptionSuccess($subscriptions, $invoice, $submission);

        $transaction = $this->getLastTransaction($submission->id);

        $paymentStatus = $this->getIntentSuccessName($invoice->payment_intent);
        $this->processOnetimeSuccess($invoice, $transaction, $paymentStatus);

        $this->recalculatePaidTotal();

        $this->sendSuccess($submission);
    }

    protected function handlePaymentIntent($transaction, $submission, $intentArgs)
    {
        $formSettings = PaymentHelper::getFormSettings($submission->form_id);

        if (PaymentHelper::isZeroDecimal($transaction->currency)) {
            $intentArgs['amount'] = intval($transaction->payment_total / 100);
        }

        $receiptEmail = PaymentHelper::getCustomerEmail($submission, $this->form);

        if ($receiptEmail && ArrayHelper::get($formSettings, 'disable_stripe_payment_receipt') != 'yes') {
            $intentArgs['receipt_email'] = $receiptEmail;
        }

        $intent = SCA::createPaymentIntent($intentArgs, $this->form->id);

        if (is_wp_error($intent)) {
            $this->handlePaymentChargeError($intent->get_error_message(), $submission, $transaction, false, 'payment_intent');
        }

        if (
            $intent->status == 'requires_action' &&
            $intent->next_action &&
            $intent->next_action->type == 'use_stripe_sdk'
        ) {
            $this->processScaBeforeVerification($submission->form_id, $submission->id, $transaction->id, $intent->id);

            # Tell the client to handle the action
            wp_send_json_success([
                'nextAction'    => 'payment',
                'actionName'    => 'initStripeSCAModal',
                'submission_id' => $submission->id,
                'client_secret' => $intent->client_secret,
                'message'       => apply_filters('fluentform/stripe_strong_customer_verify_waiting_message', __('Verifying strong customer authentication. Please wait...', 'fluentform')),
                'result'        => [
                    'insert_id' => $submission->id
                ]
            ], 200);

        } else if ($intent->status == 'succeeded') {
            // Payment is succeeded here
            $charge = $intent->charges->data[0];

            $this->handlePaymentSuccess($charge, $transaction, $submission);
        } else {
            $message = __('Payment Failed! Your card may have been declined.', 'fluentform');

            if (!empty($intent->error->message)) {
                $message = $intent->error->message;
            }

            $this->handlePaymentChargeError($message, $submission, $transaction, false, 'payment_intent');
        }
    }

    protected function handlePaymentSuccess($charge, $transaction, $submission)
    {
        $transactionData = [
            'charge_id'      => $charge->payment_intent,
            'payment_method' => 'stripe',
            'payment_mode'   => $this->getPaymentMode(),
            'payment_note'   => maybe_serialize($charge)
        ];

        $methodDetails = $charge->payment_method_details;
        if ($methodDetails && !empty($methodDetails->card)) {
            $transactionData['card_brand'] = $methodDetails->card->brand;
            $transactionData['card_last_4'] = $methodDetails->card->last4;
        }

        $this->updateTransaction($transaction->id, $transactionData);

        $this->changeTransactionStatus($transaction->id, 'paid');

        $logData = [
            'parent_source_id' => $submission->form_id,
            'source_type'      => 'submission_item',
            'source_id'        => $submission->id,
            'component'        => 'Payment',
            'status'           => 'info',
            'title'            => __('Payment Status changed', 'fluentform'),
            'description'      => __('Payment status changed to paid', 'fluentform')
        ];

        do_action('fluentform/log_data', $logData);

        $this->updateSubmission($submission->id, [
            'payment_status' => 'paid',
            'payment_method' => 'stripe',
        ]);

        $logData = [
            'parent_source_id' => $submission->form_id,
            'source_type'      => 'submission_item',
            'source_id'        => $submission->id,
            'component'        => 'Payment',
            'status'           => 'success',
            'title'            => __('Payment Complete', 'fluentform'),
            'description'      => __('One time Payment Successfully made via Stripe. Charge ID: ', 'fluentform') . $charge->id
        ];

        do_action('fluentform/log_data', $logData);

        $this->recalculatePaidTotal();

        $this->sendSuccess($submission);
    }

    public function confirmScaPayment()
    {
        $formId = intval($_REQUEST['form_id']);
        $submissionId = intval($_REQUEST['submission_id']);
        $paymentMethod = sanitize_text_field($_REQUEST['payment_method']);
        $paymentIntentId = sanitize_text_field($_REQUEST['payment_intent_id']);

        $this->setSubmissionId($submissionId);
        $submission = $this->getSubmission();
        $this->form = $this->getForm();

        $transaction = $this->getLastTransaction($submissionId);

        $confirmation = SCA::confirmPayment($paymentIntentId, [
            'payment_method' => $paymentMethod
        ], $formId);

        if (is_wp_error($confirmation)) {
            $message = 'Payment has been failed. ' . $confirmation->get_error_message();
            $this->handlePaymentChargeError($message, $submission, $transaction, $confirmation, 'payment_error');
        }

        if ($confirmation->status == 'succeeded') {
            $charge = $confirmation->charges->data[0];;
            $this->handlePaymentSuccess($charge, $transaction, $submission);
        } else {
            $this->handlePaymentChargeError('We could not verify your payment. Please try again', $submission, $transaction, $confirmation, 'payment_error');
        }
    }

    public function confirmScaSetupIntentsPayment()
    {
        $formId = intval($_REQUEST['form_id']);
        $submissionId = intval($_REQUEST['submission_id']);
        $intentId = sanitize_text_field($_REQUEST['payment_intent_id']);

        $this->setSubmissionId($submissionId);
        $this->form = $this->getForm();

        $submission = $this->getSubmission();

        // Let's retrieve the intent
        $intent = SCA::retrievePaymentIntent($intentId, [
            'expand' => [
                'invoice.payment_intent'
            ]
        ], $formId);

        if (is_wp_error($intent)) {
            $this->handlePaymentChargeError($intent->get_error_message(), $submission, false, false, 'payment_intent');
        }

        $invoice = $intent->invoice;

        $this->handlePaidSubscriptionInvoice($invoice, $submission);
    }

    protected function sendSuccess($submission)
    {
        try {
            $returnData = $this->getReturnData();
            wp_send_json_success($returnData, 200);
    
        } catch (\Exception $e) {
            wp_send_json([
                'errors' => $e->getMessage()
            ], 423);
        }
      
    }

    protected function processScaBeforeVerification($formId, $submissionId, $transactionId, $chargeId)
    {
        if ($transactionId) {
            $this->updateTransaction($transactionId, [
                'charge_id'    => $chargeId,
                'payment_mode' => $this->getPaymentMode()
            ]);

            $this->changeTransactionStatus($transactionId, 'intended');
        }

        $logData = [
            'parent_source_id' => $formId,
            'source_type'      => 'submission_item',
            'source_id'        => $submissionId,
            'component'        => 'Payment',
            'status'           => 'info',
            'title'            => __('Stripe SCA Required', 'fluentform'),
            'description'      => __('SCA is required for this payment. Requested SCA info from customer', 'fluentform')
        ];

        do_action('fluentform/log_data', $logData);
    }
    
    /**
     * Products name comma separated
     * @return string
     */
    public function getProductNames()
    {
        $orderItems = $this->getOrderItems();
        $itemsHtml = '';
        foreach ($orderItems as $item) {
            $itemsHtml != "" && $itemsHtml .= ", ";
            $itemsHtml .=  $item->item_name ;
        }
        
        return $itemsHtml;
    }
    
}
