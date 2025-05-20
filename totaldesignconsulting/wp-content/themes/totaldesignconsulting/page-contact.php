/* === page-contact.php === */
<?php
/* Template Name: Contact Page */
get_header(); ?>

<main id="main" class="site-main" style="padding: 2rem;">
    <header style="text-align: center; margin-bottom: 3rem;">
        <h1>Contact Us</h1>
        <p>We’re here to answer your questions and help your operations succeed.</p>
    </header>

    <section style="max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <!-- Company Contact Info -->
        <div>
            <h2>Contact Details</h2>
            <p><strong>Total Design Consulting LLC</strong></p>
            <p>Email: <a href="mailto:info@totaldesignconsulting.com">info@totaldesignconsulting.com</a></p>
            <p>Phone: <a href="tel:+1234567890">(123) 456-7890</a></p>
            <p>Location: Raleigh, NC (Remote & On-Site)</p>
            <p>Hours: Monday–Friday, 9 AM–5 PM (EST)</p>
        </div>

        <!-- Contact Form Placeholder -->
        <div>
            <h2>Send a Message</h2>
            <!-- Replace with actual plugin shortcode -->
            <?php echo do_shortcode('[fluentform id="1"]'); ?>
            <!-- Alternative: Fluent Forms, WPForms, etc. -->
        </div>
    </section>

    <!-- Optional Map or Location Visual -->
    <section style="margin-top: 3rem; text-align: center;">
        <h2>Service Area</h2>
        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/map-placeholder.png" alt="Service Area Map" style="max-width: 700px; width: 100%; border-radius: 8px;">
    </section>
</main>

<?php get_footer(); ?>