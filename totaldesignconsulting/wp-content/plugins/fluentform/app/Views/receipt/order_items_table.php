<table style="width: 100%;border: 1px solid #cbcbcb;" class="table ffp_order_items_table ffp_table table_bordered">
    <thead>
    <tr>
        <th><?php _e('Item', 'fluentform'); ?></th>
        <th><?php _e('Quantity', 'fluentform'); ?></th>
        <th><?php _e('Price', 'fluentform'); ?></th>
        <th><?php _e('Line Total', 'fluentform'); ?></th>
    </tr>
    </thead>
    <tbody>
    <?php foreach ($items as $order_item): ?>
        <tr>
            <td><?php echo $order_item->item_name; ?></td>
            <td><?php echo $order_item->quantity; ?></td>
            <td><?php echo $order_item->formatted_item_price; ?></td>
            <td><?php echo $order_item->formatted_line_total; ?></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
    <tfoot>
    <?php if($discount_items): ?>
        <tr class="ffp_total_row">
            <th style="text-align: right" colspan="3"><?php _e('Sub-Total', 'fluentform'); ?></th>
            <td><?php echo $subTotal; ?></td>
        </tr>
        <?php foreach ($discount_items as $discount_item): ?>
        <tr class="ffp_total_row">
            <th style="text-align: right" colspan="3"><?php _e('Discount:', 'fluentform'); ?> <?php echo $discount_item->item_name; ?></th>
            <td>-<?php echo $discount_item->formatted_line_total; ?></td>
        </tr>
        <?php endforeach; ?>
    <?php endif; ?>

        <tr class="ffp_total_row">
            <th style="text-align: right" colspan="3"><?php _e('Total', 'fluentform'); ?></th>
            <td><?php echo $orderTotal; ?></td>
        </tr>
    </tfoot>

</table>