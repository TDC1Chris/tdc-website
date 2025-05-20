<div class="ffp_payment_info">
    <div class="ffp_payment_info_item ffp_payment_info_item_order_id">
        <div class="ffp_item_heading"><?php _e('Transaction #', 'fluentform');?></div>
        <div class="ffp_item_value">#<?php echo $transaction->id; ?></div>
    </div>
    <div class="ffp_payment_info_item ffp_payment_info_item_date">
        <div class="ffp_item_heading"><?php _e('Date:' ,'fluentform');?></div>
        <div class="ffp_item_value"><?php echo date(get_option( 'date_format' ), strtotime($transaction->created_at)); ?></div>
    </div>
    <?php if($transaction->payment_method): ?>
        <div class="ffp_payment_info_item ffp_payment_info_item_payment_method">
            <div class="ffp_item_heading"><?php _e('Payment Method:','fluentform');?></div>
            <div class="ffp_item_value"><?php
                $method = $transaction->payment_method;
                $method = apply_filters_deprecated(
                    'fluentform_payment_method_public_name_' . $method,
                    [
                        $method
                    ],
                    FLUENTFORM_FRAMEWORK_UPGRADE,
                    'fluentform/payment_method_public_name_' . $method,
                    'Use fluentform/payment_method_public_name_' . $method . ' instead of fluentform_payment_method_public_name_' . $method
                );
                echo ucfirst(
                    apply_filters(
                        'fluentform/payment_method_public_name_' . $method,
                        $method
                    )
                ); ?></div>
        </div>
    <?php endif; ?>
    <?php if($transaction->status): ?>
        <div class="ffp_payment_info_item ffp_payment_info_item_payment_status">
            <div class="ffp_item_heading"><?php _e('Payment Status:','fluentform');?></div>
            <div class="ffp_item_value"><?php echo ucfirst($transaction->status); ?></div>
        </div>
    <?php endif; ?>
</div>
