<table style="width: 100%;border: 1px solid #cbcbcb;margin-top: 0; margin-bottom: 15px;" class="table ffp_order_items_table ffp_table table_bordered">
    <thead>
    <tr>
        <th><?php _e('Item', 'fluentform'); ?></th>
        <th><?php _e('Status', 'fluentform'); ?></th>
    </tr>
    </thead>
    <tbody>
    <?php foreach ($subscriptions as $subscription): ?>
        <tr>
            <td>
                <?php echo $subscription->plan_name . ' (' . $subscription->item_name . ')'; ?>
                <?php if($subscription->original_plan): ?>
                <p style="margin: 5px 0px 0px;font-size: 90%;"><?php echo \FluentForm\App\Modules\Payments\PaymentHelper::getPaymentSummaryText($subscription->original_plan, $subscription->form_id, $submission->currency, false); ?></p>
                <?php endif; ?>
            </td>
            <td><span class="ff_trial_badge"><?php echo ucfirst($subscription->status); ?></span></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
