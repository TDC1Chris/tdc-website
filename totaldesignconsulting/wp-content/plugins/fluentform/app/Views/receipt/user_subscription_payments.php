<div class="ff_subscription_payments">
    <table style="width: 100%;border: 1px solid #cbcbcb;margin-top: 0;" class="table ffp_order_items_table ffp_table table_bordered">
        <thead>
        <tr>
            <th><?php _e('Amount', 'fluentform'); ?></th>
            <th><?php _e('Date', 'fluentform'); ?></th>
            <?php if($config['has_view_action']): ?>
            <th><?php _e('Actions', 'fluentform'); ?></th>
            <?php endif; ?>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($transactions as $transaction): ?>
        <tr>
            <td>
                <span class="table_payment_amount"><?php echo $transaction->formatted_amount; ?> <?php echo strtoupper($transaction->currency) ?></span>
                <span class="ff_pay_status_badge ff_pay_status_<?php echo $transaction->status; ?>">
                    <?php echo $transaction->status; ?>
                </span>
            </td>
            <td>
                <?php echo $transaction->formatted_date; ?>
            </td>
            <?php if($transaction->view_url): ?>
            <td>
                <a class="ff_pat_action_view" href="<?php echo $transaction->view_url ?>"><?php echo $config['view_text']; ?></a>
            </td>
            <?php endif; ?>
        </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
</div>