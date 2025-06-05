<?php get_header(); ?>

<main id="main" class="site-main">
    <!-- Hero Section -->
    <section class="hero" style="padding: 4rem 2rem; text-align: center; background-color: #f8f9fa;">
        <h1>Innovative Engineering Solutions</h1>
        <p style="max-width: 700px; margin: 1rem auto;">
            Empowering your business with cutting-edge technology in cybersecurity, OT & IT engineering, safety systems, and PLC automation.
        </p>
        <a href="/contact" class="button" style="display: inline-block; margin-top: 1rem; padding: 0.75rem 1.5rem; background: #0056b3; color: white; border-radius: 5px; text-decoration: none;">
            Get in Touch
        </a>
    </section>

    <!-- Services Overview -->
    <section class="services" style="padding: 4rem 2rem; background-color: #ffffff;">
        <h2 style="text-align: center;">Our Core Services</h2>
        <div class="service-grid" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem;">
            <div class="service-box" style="flex: 1 1 200px; max-width: 250px; text-align: center;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-cybersecurity.png" alt="Cybersecurity Icon" style="width: 60px;">
                <h3>Cybersecurity</h3>
                <p>Comprehensive threat defense, risk assessment, and compliance strategies.</p>
            </div>
            <div class="service-box" style="flex: 1 1 200px; max-width: 250px; text-align: center;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-network.png" alt="OT & IT Icon" style="width: 60px;">
                <h3>IT & OT Engineering</h3>
                <p>Robust infrastructure design, network segmentation, and system integration.</p>
            </div>
            <div class="service-box" style="flex: 1 1 200px; max-width: 250px; text-align: center;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-safety.png" alt="Safety Icon" style="width: 60px;">
                <h3>Safety Systems</h3>
                <p>Functional safety assessments, system design, and process reliability.</p>
            </div>
            <div class="service-box" style="flex: 1 1 200px; max-width: 250px; text-align: center;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-plc.png" alt="PLC Icon" style="width: 60px;">
                <h3>PLC Automation</h3>
                <p>Custom PLC programming, diagnostics, and industrial automation solutions.</p>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="cta" style="padding: 4rem 2rem; background-color: #0056b3; color: white; text-align: center;">
        <h2>Ready to Improve Your Operational Security and Efficiency?</h2>
        <p>Schedule a consultation with our engineering experts today.</p>
        <a href="/contact" class="button" style="display: inline-block; margin-top: 1rem; padding: 0.75rem 1.5rem; background: white; color: #0056b3; border-radius: 5px; text-decoration: none;">
            Schedule Now
        </a>
    </section>
</main>

<?php get_footer(); ?>