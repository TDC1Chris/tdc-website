<?php if($transaction->payer_name || $transaction->payer_email) : ?>
<div class="ffp_customer_details">
    <h4><?php _e('Customer Details', 'fluentform'); ?></h4>
    <div  class="ffp_submission_details">
        <ul>
            <?php if($transaction->payer_name): ?>
            <li><?php _e('Customer Name:', 'fluentform');?> <?php echo $transaction->payer_name; ?></li>
            <?php endif; ?>
            <?php if($transaction->payer_email): ?>
            <li><?php _e('Customer Email:', 'fluentform');?> <?php echo $transaction->payer_email; ?></li>
            <?php endif; ?>
            <?php if($transaction->billing_address && strlen($transaction->billing_address) > 2): ?>
            <li><?php _e('Billing Address:', 'fluentform');?> <?php echo $transaction->billing_address; ?></li>
            <?php endif; ?>
            <?php if($transaction->shipping_address && strlen($transaction->shipping_address) > 2): ?>
            <li><?php _e('Shipping Address:', 'fluentform');?> <?php echo $transaction->shipping_address; ?></li>
            <?php endif; ?>
        </ul>
    </div>
</div>
<?php endif; ?>
