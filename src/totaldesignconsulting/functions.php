<?php
require_once get_template_directory() . '/inc/setup.php';

function tdc_enqueue_assets() {
    wp_enqueue_style('tdc-style', get_stylesheet_uri(), [], filemtime(get_stylesheet_directory() . '/style.css'));
    wp_enqueue_style('tdc-custom', get_template_directory_uri() . '/assets/css/style.css', [], filemtime(get_template_directory() . '/assets/css/style.css'));
    wp_enqueue_script('tdc-main', get_template_directory_uri() . '/assets/js/main.js', [], false, true);
}
add_action('wp_enqueue_scripts', 'tdc_enqueue_assets');