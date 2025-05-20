<?php

namespace FluentForm\App\Modules\Payments\Migrations;

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

class Transactions
{
    /**
     * Migrate the table.
     *
     * @return void
     */
    public static function migrate()
    {
        global $wpdb;

        $charsetCollate = $wpdb->get_charset_collate();

        $table = $wpdb->prefix . 'fluentform_transactions';

        if ($wpdb->get_var("SHOW TABLES LIKE '$table'") != $table) {
            $sql = "CREATE TABLE $table (
			    id int(11) NOT NULL AUTO_INCREMENT,
			    transaction_hash varchar(255) NULL,
			    payer_name varchar(255) NULL,
			    payer_email varchar(255) NULL,
			    billing_address varchar(255) NULL,
			    shipping_address varchar(255) NULL,
				form_id int(11) NOT NULL,
				user_id int(11) DEFAULT NULL,
				submission_id int(11) NULL,
				subscription_id int(11) NULL,
				transaction_type varchar(255) DEFAULT 'onetime',
				payment_method varchar(255),
				card_last_4 int(4),
				card_brand varchar(255),
				charge_id varchar(255),
				payment_total BIGINT UNSIGNED DEFAULT 1,
				status varchar(255),
				currency varchar(255),
				payment_mode varchar(255),
				payment_note longtext,
				created_at timestamp NULL,
				updated_at timestamp NULL,
				PRIMARY  KEY  (id)
			  ) $charsetCollate;";

            require_once(ABSPATH . 'wp-admin/includes/upgrade.php');

            dbDelta($sql);
        } else {
            self::maybeAlterColumns();
        }
    }

    public static function maybeAlterColumns()
    {
        global $wpdb;
        $table = $wpdb->prefix . 'fluentform_transactions';

        // find the data types of each column
        $results = $wpdb->get_results("DESCRIBE $table");
        $items = [];
        foreach ($results as $result) {
            $items[$result->Field] = $result->Type;
        }

        $paymentTotalMigrated = strpos($items['payment_total'], 'bigint') !== false;
        if (!$paymentTotalMigrated) {
            $wpdb->query("ALTER TABLE $table MODIFY payment_total BIGINT UNSIGNED DEFAULT 1");
        }
        
    }
}
