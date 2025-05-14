<?php
function mybusinesstheme_scripts() {
    wp_enqueue_style('style', get_stylesheet_uri());
}
add_action('wp_enqueue_scripts', 'mybusinesstheme_scripts');

function mybusinesstheme_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    register_nav_menus([
        'primary' => __('Primary Menu', 'mybusinesstheme')
    ]);
}
add_action('after_setup_theme', 'mybusinesstheme_setup');
