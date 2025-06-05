<footer style="background-color: #f8f9fa; padding: 2rem 1rem; text-align: center; font-size: 0.9rem; border-top: 1px solid #ddd;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <p>&copy; <?php echo date('Y'); ?> <strong>Total Design Consulting LLC</strong>. All rights reserved.</p>
        <nav>
            <?php wp_nav_menu([
                'theme_location' => 'footer_menu',
                'container' => false,
                'menu_class' => 'footer-nav',
            ]); ?>
        </nav>
    </div>
    <?php wp_footer(); ?>
</footer>
</body>
</html>