<?php
function tdc_theme_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'gallery', 'caption', 'style', 'script']);

    register_nav_menus([
        'main_menu'   => __('Main Menu', 'tdc'),
        'footer_menu' => __('Footer Menu', 'tdc'),
    ]);
}
add_action('after_setup_theme', 'tdc_theme_setup');
