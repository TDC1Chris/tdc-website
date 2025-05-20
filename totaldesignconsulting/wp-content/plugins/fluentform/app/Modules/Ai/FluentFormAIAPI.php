<?php

namespace FluentForm\App\Modules\Ai;

/**
 *  Handling AI Api.
 * @since 6.0.0
 */
class FluentFormAIAPI
{
    private $url = 'https://ai.fluentforms.com/';
    
    public function makeRequest($requestData = [])
    {
        $headers = [
            'Content-Type' => 'application/json',
        ];
    
        $originalTimeout = apply_filters('http_request_timeout', 5);
    
        add_filter('http_request_timeout', function ($timeout) {
            return 60;
        });
    
        $response = wp_remote_post($this->url, [
            'headers' => $headers,
            'body'    => json_encode($requestData),
        ]);
    
        add_filter('http_request_timeout', function ($timeout) use ($originalTimeout) {
            return $originalTimeout;
        });
    
        if (is_wp_error($response)) {
            return new \WP_Error(423, $response->get_error_message());
        }
    
        $body = json_decode(wp_remote_retrieve_body($response), true);
        $code = wp_remote_retrieve_response_code($response);
    
        $error_message = __('Something went wrong.', 'fluentform');
        if (isset($body['error']['message'])) {
            $error_message = __($body['error']['message'], 'fluentform');
        }
    
        if ($code !== 200) {
            return new \WP_Error(423, $error_message);
        }
    
        return $body;
    }
}
