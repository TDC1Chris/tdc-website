<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<header style="background-color: #f8f9fa; padding: 1rem 2rem;">
    <nav class="main-nav" style="max-width: 1200px; margin: 0 auto;">
        <?php
        wp_nav_menu([
            'theme_location' => 'main_menu',
            'container' => false,
            'menu_class' => 'nav-menu',
        ]);
        ?>
    </nav>
</header>