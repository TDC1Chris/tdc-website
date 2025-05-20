<?php
 /** @var Array $subscriptions */
 /** @var Array $config */
?>
<div class="ff_subscriptions">
    <?php
    foreach ($subscriptions as $subscription): ?>
        <div class="ff_subscription">
            <div class="ff_subscription_header">
                <div class="ff_pay_info">
                    <div class="ff_form_name"><span class="ff_sub_id">#<?php echo $subscription->id; ?></span> <?php echo $subscription->title; ?></div>
                    <div class="ff_sub_name"><?php echo $subscription->plan_name; ?>
                        <span class="ff_sub_input_name">(<?php echo $subscription->item_name ?>)</span>
                    </div>
                    <div class="head_payment_amount">
                        <span class="pay_amount"><?php echo $subscription->formatted_recurring_amount; ?></span>
                        <span>/<?php echo $subscription->billing_interval; ?></span>
                        <span class="ff_pay_status_badge ff_pay_status_<?php echo $subscription->status; ?>">
                            <?php echo $subscription->status; ?>
                        </span>
                        <?php if ($subscription->billing_text): ?>
                            <p class="ff_billing_text"><?php echo $subscription->billing_text; ?></p>
                        <?php endif; ?>
                    </div>
                </div>
                <div class="ff_plan_info">
                    <p class="ff_billing_dates">
                        <span class="ff_sub_start"><?php _e('Started:', 'fluentform') ?> <?php echo $subscription->starting_date_formated; ?></span>
                    </p>
                    <div class="ff_payment_count_btn">
                        <button data-subscription_id="<?php echo $subscription->id; ?>" class="ff_show_payments"><?php _e('View Payments', 'fluentform'); ?>
                        </button>
                        <?php if($subscription->can_cancel): ?>
                        <button data-submission_id="<?php echo $subscription->submission_id; ?>" data-subscription_id="<?php echo $subscription->id; ?>" class="ff_cancel_subscription"><?php _e('Cancel', 'fluentform'); ?>
                        </button>
                        <?php endif; ?>
                    </div>
                </div>
            </div>
            <?php if($subscription->can_cancel): ?>
            <div style="display: none;" class="ff_sub_cancel_confirmation">
                <h4><?php echo $config['sub_cancel_confirm_heading']; ?></h4>
                <div class="sub_cancel_btns">
                    <button class="ff_confirm_subscription_cancel"><?php echo $config['sub_cancel_confirm_btn']; ?></button>
                    <button class="ff_cancel_close"><?php echo $config['sub_cancel_close']; ?></button>
                    <p class="ff_sub_message_notices"></p>
                </div>
            </div>
            <?php endif; ?>
            <div class="ff_subscription_payments"></div>
        </div>
    <?php endforeach; ?>
</div>