<?php
/*
Template Name: Resources Page
*/
get_header(); ?>

<main id="main" class="site-main" style="padding: 2rem;">
    <header style="text-align: center; margin-bottom: 3rem;">
        <h1>Educational Resources</h1>
        <p>Knowledge hub for cybersecurity, safety, automation, and compliance insights.</p>
    </header>

    <!-- Resource Grid -->
    <section class="resource-list" style="max-width: 1000px; margin: 0 auto; display: grid; gap: 2rem;">
        <!-- Resource Example 1 -->
        <article style="border: 1px solid #ccc; border-radius: 6px; padding: 1.5rem;">
            <h2>NIST Framework for OT Environments</h2>
            <p>Understand how the NIST CSF can be tailored to legacy control systems and hybrid infrastructures.</p>
            <a href="#" style="color: #0056b3; text-decoration: underline;">Read More →</a>
        </article>

        <!-- Resource Example 2 -->
        <article style="border: 1px solid #ccc; border-radius: 6px; padding: 1.5rem;">
            <h2>PLC Fault Isolation Checklist</h2>
            <p>A practical PDF guide to help engineers troubleshoot automation issues step-by-step in the field.</p>
            <a href="#" style="color: #0056b3; text-decoration: underline;">Download PDF →</a>
        </article>

        <!-- Resource Example 3 -->
        <article style="border: 1px solid #ccc; border-radius: 6px; padding: 1.5rem;">
            <h2>Top OT Cyber Threats in 2025</h2>
            <p>An evolving list of the latest threats, vulnerabilities, and mitigation strategies for critical infrastructure operators.</p>
            <a href="#" style="color: #0056b3; text-decoration: underline;">Explore Trends →</a>
        </article>
    </section>
    <!-- Private Vault Section -->
    <section class="private-vault" style="margin-top: 4rem; padding: 2rem; background: #f1f1f1; border-radius: 6px;">
    <h2>🛡️ Private Resource Vault</h2>
    <p style="margin-bottom: 1rem;">
        Access your internal guides, configurations, and engineering documentation.
        This area is password-protected and for internal use only.
    </p>
    <a href="https://vault.youroffice.com" target="_blank" style="display: inline-block; padding: 0.75rem 1.25rem; background-color: #0056b3; color: white; text-decoration: none; border-radius: 5px;">
        Go to Private Vault
    </a>
    </section>
</main>

<?php get_footer(); ?>
