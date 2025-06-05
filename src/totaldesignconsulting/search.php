<?php get_header(); ?>
<main style="padding: 2rem;">
    <h1>Search Results for: "<?php echo get_search_query(); ?>"</h1>

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
        <p>No results found. Try another search.</p>
        <?php get_search_form(); ?>
    <?php endif; ?>
</main>
<?php get_footer(); ?>