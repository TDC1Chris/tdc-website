<ul class="ffp_payment_info_table">
    <li>
        <b><?php _e('Amount:', 'fluentform');?></b> <?php echo $orderTotal; ?></b>
    </li>
    <?php
    $paymentMethod = $submission->payment_method;
    if($paymentMethod): ?>
        <li>
            <b><?php _e('Payment Method:', 'fluentform');?></b> <?php
            $paymentMethod = apply_filters_deprecated(
                'fluentform_payment_method_public_name_' . $paymentMethod,
                [
                    $paymentMethod
                ],
                FLUENTFORM_FRAMEWORK_UPGRADE,
                'fluentform/payment_method_public_name_' . $paymentMethod,
                'Use fluentform/payment_method_public_name_' . $paymentMethod . ' instead of fluentform_payment_method_public_name_' . $paymentMethod
            );
            echo ucfirst(
                apply_filters(
                    'fluentform/payment_method_public_name_' . $paymentMethod,
                    $paymentMethod
                )
            ); ?></b>
        </li>
    <?php endif; ?>
    <?php
    if ($submission->payment_status):
        $allStatus = \FluentForm\App\Modules\Payments\PaymentHelper::getPaymentStatuses();
        if (isset($allStatus[$submission->payment_status])) {
            $submission->payment_status = $allStatus[$submission->payment_status];
        }
        ?>
        <li>
            <b><?php _e('Payment Status:', 'fluentform');?></b> <?php echo $submission->payment_status; ?></b>
        </li>
    <?php endif; ?>
</ul>
