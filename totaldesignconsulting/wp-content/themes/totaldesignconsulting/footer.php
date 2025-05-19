
<footer>
    <p>&copy; <?php echo date('Y'); ?> Total Design Consulting LLC. All rights reserved.</p>
    <?php wp_nav_menu(['theme_location' => 'footer_menu']); ?>
</footer>
<?php wp_footer(); ?>
</body>
</html>


/* === index.php === */
<?php get_header(); ?>
<main>
    <section>
        <h1>Welcome to Total Design Consulting</h1>
        <p>This is the index page. Content will appear here.</p>
    </section>
</main>
<?php get_footer(); ?>
