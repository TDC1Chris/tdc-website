<?php
require_once get_template_directory() . '/inc/setup.php';

function tdc_enqueue_assets() {
    wp_enqueue_style('tdc-style', get_stylesheet_uri(), [], filemtime(get_stylesheet_directory() . '/style.css'));
    wp_enqueue_script('tdc-main', get_template_directory_uri() . '/assets/js/main.js', [], false, true);
}
add_action('wp_enqueue_scripts', 'tdc_enqueue_assets');


/* === inc/setup.php === */
<?php
function tdc_theme_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'gallery']);

    register_nav_menus([
        'main_menu' => __('Main Menu', 'tdc'),
        'footer_menu' => __('Footer Menu', 'tdc'),
    ]);
}
add_action('after_setup_theme', 'tdc_theme_setup');


/* === header.php === */
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<header>
    <nav>
        <?php wp_nav_menu(['theme_location' => 'main_menu']); ?>
    </nav>
</header>


