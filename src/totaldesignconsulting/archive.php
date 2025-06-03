<?php get_header(); ?>
<main style="padding: 2rem;">
    <h1><?php the_archive_title(); ?></h1>
    <p><?php the_archive_description(); ?></p>

    <?php if (have_posts()) : ?>
        <ul>
            <?php while (have_posts()) : the_post(); ?>
                <li>
                    <a href="<?php the_permalink(); ?>"><strong><?php the_title(); ?></strong></a><br>
                    <?php the_excerpt(); ?>
                </li>
            <?php endwhile; ?>
        </ul>
    <?php else : ?>
        <p>No posts found in this archive.</p>
    <?php endif; ?>
</main>
<?php get_footer(); ?>