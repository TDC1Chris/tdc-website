<?php
/*
Template Name: Services Page
*/
get_header(); ?>

<main id="main" class="site-main" style="padding: 2rem;">
    <header style="text-align: center; margin-bottom: 3rem;">
        <h1>Our Services</h1>
        <p>We deliver secure, reliable, and compliant engineering solutions across multiple industries.</p>
    </header>

    <section class="service-details" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        <article class="service-block" style="padding: 1.5rem; border: 1px solid #ccc; border-radius: 8px;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-cybersecurity.png" alt="Cybersecurity" style="width: 48px;">
            <h2>Cybersecurity</h2>
            <p>Security audits, risk management, NIST/ISA compliance, and intrusion detection for IT and OT networks.</p>
        </article>

        <article class="service-block" style="padding: 1.5rem; border: 1px solid #ccc; border-radius: 8px;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-network.png" alt="OT & IT Engineering" style="width: 48px;">
            <h2>IT & OT Engineering</h2>
            <p>System architecture, legacy integration, remote access control, and scalable infrastructure planning.</p>
        </article>

        <article class="service-block" style="padding: 1.5rem; border: 1px solid #ccc; border-radius: 8px;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-safety.png" alt="Safety Systems" style="width: 48px;">
            <h2>Safety Systems</h2>
            <p>Machine safety consulting, SIL/PL verification, fail-safe design, and safety instrumentation systems.</p>
        </article>

        <article class="service-block" style="padding: 1.5rem; border: 1px solid #ccc; border-radius: 8px;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/icon-plc.png" alt="PLC Automation" style="width: 48px;">
            <h2>PLC Automation</h2>
            <p>PLC/HMI programming, SCADA integration, control panel testing, and post-deployment support.</p>
        </article>
    </section>
</main>

<?php get_footer(); ?>