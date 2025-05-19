<?php
/**
 * Theme setup functions for Total Design Consulting
 */

// Set up theme defaults and register support for various WordPress features.
function tdc_theme_setup() {

    // Let WordPress manage the document title.
    add_theme_support('title-tag');

    // Enable featured images for posts and pages.
    add_theme_support('post-thumbnails');

    // Enable HTML5 markup for common elements.
    add_theme_support('html5', [
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script'
    ]);

    // Register navigation menus.
    register_nav_menus([
        'main_menu'   => __('Main Menu', 'tdc'),
        'footer_menu' => __('Footer Menu', 'tdc')
    ]);
}
add_action('after_setup_theme', 'tdc_theme_setup');