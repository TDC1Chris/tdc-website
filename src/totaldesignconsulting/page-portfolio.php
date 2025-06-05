<?php
/*
Template Name: Portfolio Page
*/
get_header(); ?>

<main id="main" class="site-main" style="padding: 2rem;">
    <header style="text-align: center; margin-bottom: 3rem;">
        <h1>Project Portfolio</h1>
        <p>See how we solve technical challenges for clients in critical sectors.</p>
    </header>

    <!-- Case Study Grid -->
    <section class="portfolio-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; max-width: 1200px; margin: 0 auto;">
        <!-- Example Case Study #1 -->
        <article style="border: 1px solid #ccc; border-radius: 8px; padding: 1.5rem;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/portfolio-ot-network.png" alt="OT Network Upgrade" style="width: 100%; border-radius: 6px;">
            <h2 style="margin-top: 1rem;">OT Network Upgrade</h2>
            <p style="font-size: 0.95rem;">Redesigned and segmented an industrial OT network for a large utility provider, improving security posture and availability.</p>
        </article>

        <!-- Example Case Study #2 -->
        <article style="border: 1px solid #ccc; border-radius: 8px; padding: 1.5rem;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/portfolio-plc-upgrade.png" alt="PLC Upgrade" style="width: 100%; border-radius: 6px;">
            <h2 style="margin-top: 1rem;">PLC Control Upgrade</h2>
            <p style="font-size: 0.95rem;">Migrated legacy PLC infrastructure to modern, fault-tolerant controllers, reducing downtime by 60% at a food production facility.</p>
        </article>

        <!-- Example Case Study #3 -->
        <article style="border: 1px solid #ccc; border-radius: 8px; padding: 1.5rem;">
            <img src="<?php echo get_template_directory_uri(); ?>/assets/images/portfolio-cybersecurity.png" alt="Cyber Risk Assessment" style="width: 100%; border-radius: 6px;">
            <h2 style="margin-top: 1rem;">Cyber Risk Assessment</h2>
            <p style="font-size: 0.95rem;">Performed NIST-aligned cybersecurity assessment across distributed operations for a multi-site manufacturer.</p>
        </article>
    </section>
</main>

<?php get_footer(); ?>