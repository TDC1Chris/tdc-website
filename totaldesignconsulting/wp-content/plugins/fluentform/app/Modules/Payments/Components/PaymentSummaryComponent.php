<?php

namespace FluentForm\App\Modules\Payments\Components;

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

use FluentForm\App\Services\FormBuilder\BaseFieldManager;
use FluentForm\App\Services\FormBuilder\Components\CustomHtml;
use FluentForm\App\Services\FormBuilder\Components\Text;

class PaymentSummaryComponent extends BaseFieldManager
{
    public function __construct(
        $key = 'payment_summary_component',
        $title = 'Payment Summary',
        $tags = ['payment', 'summary', 'cart'],
        $position = 'payments'
    )
    {
        parent::__construct(
            $key,
            $title,
            $tags,
            $position
        );
    }


    public function register()
    {
        add_filter('fluentform/editor_components', array($this, 'pushComponent'));
        add_filter('fluentform/editor_element_settings_placement', array($this, 'pushEditorElementPositions'));
        add_filter('fluentform/editor_element_search_tags', array($this, 'pushTags'), 10, 2);
        add_action('fluentform/render_item_' . $this->key, array($this, 'render'), 10, 2);

        add_filter('fluentform/editor_element_customization_settings', function ($settings) {
            if ($customSettings = $this->getEditorCustomizationSettings()) {
                $settings = array_merge($settings, $customSettings);
            }

            return $settings;
        });


       // add_filter('fluentform/supported_conditional_fields', array($this, 'pushConditionalSupport'));

    }

    function getComponent()
    {
        return array(
            'index' => 7,
            'element' => $this->key,
            'attributes' => array(),
            'settings' => array(
                'html_codes' => __('<p>Payment Summary will be shown here</p>', 'fluentform'),
                'cart_empty_text' => __('No payment items has been selected yet', 'fluentform'),
                'conditional_logics' => array(),
                'container_class' => ''
            ),
            'editor_options' => array(
                'title' => __('Payment Summary', 'fluentform'),
                'icon_class' => 'ff-edit-html',
                'template' => 'customHTML'
            ),
        );
    }

    public function getGeneralEditorElements()
    {
        return [
            'cart_empty_text'
        ];
    }

    public function generalEditorElement()
    {
        return [
            'cart_empty_text' => [
                'template' => 'inputHTML',
                'label' => __('Empty Payment Selected Text', 'fluentform'),
                'help_text' => __('The provided text will show if no payment item is selected yet', 'fluentform'),
                'hide_extra' => 'yes'
            ]
        ];
    }

    public function getAdvancedEditorElements()
    {
        return [
            'conditional_logics',
            'container_class'
        ];
    }

    function render($data, $form)
    {
        $fallBack =  $data['settings']['cart_empty_text'];
        $data['settings']['html_codes'] = '<div class="ff_dynamic_value ff_dynamic_payment_summary" data-ref="payment_summary"><div class="ff_payment_summary"></div><div class="ff_payment_summary_fallback">'.$fallBack.'</div></div>';
        return (new CustomHtml())->compile($data, $form);
    }
}
