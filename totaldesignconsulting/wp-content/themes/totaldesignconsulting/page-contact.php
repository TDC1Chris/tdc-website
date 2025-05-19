<?php
/*
Template Name: Contact Page
*/
get_header(); ?>

<main id="main" class="site-main" style="padding: 2rem;">
    <header style="text-align: center; margin-bottom: 2rem;">
        <h1>Contact Us</h1>
        <p>Get in touch with our engineering and cybersecurity experts.</p>
    </header>

    <!-- Contact Info and Form -->
    <section class="contact-section" style="max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <!-- Contact Details -->
        <div class="contact-details" style="font-size: 1rem;">
            <h2>Business Details</h2>
            <p><strong>Total Design Consulting LLC</strong></p>
            <p>Email: <a href="mailto:info@totaldesignconsulting.com">info@totaldesignconsulting.com</a></p>
            <p>Phone: <a href="tel:+1234567890">(123) 456-7890</a></p>
            <p>Location: Raleigh, NC (Remote & On-Site Available)</p>
        </div>

        <!-- Contact Form Placeholder -->
        <div class="contact-form">
            <h2>Send a Message</h2>
            <!-- Replace this with WPForms, Fluent Forms, or other plugin shortcode -->
            <form action="#" method="post" style="display: flex; flex-direction: column; gap: 1rem;">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email" required>
                <textarea name="message" rows="5" placeholder="Your Message" required></textarea>
                <button type="submit" style="background-color: #0056b3; color: white; padding: 0.75rem; border: none; border-radius: 4px;">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Map Placeholder -->
    <section style="margin-top: 3rem; text-align: center;">
        <h2>Our Service Area</h2>
        <div style="margin-top: 1rem;">
            <!-- Embed a real Google Map or image if needed -->
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/map-placeholder.png" alt="Service Area Map" style="width: 100%; max-width: 700px; border-radius: 8px;">
        </div>
    </section>
</main>

<?php get_footer(); ?>