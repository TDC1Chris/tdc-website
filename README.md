# Total Design Consulting Website

This is a custom-built, modern static website for Total Design Consulting LLC.

## Structure Overview

This is the static marketing site for [Total Design Consulting LLC](https://www.totaldesignconsulting.com).

## Live Site

[https://tdc1chris.github.io/tdc-website/](https://tdc1chris.github.io/tdc-website/)

## Structure
```bash
- `/docs/`: Static files for GitHub Pages (main site source)
    - index.html
    - contact.html
    - services.html
    - testimonials.html
    - 404.html
    - favicon.ico
    - /assets/
        - /css/
            - style.css
        - /images/
            - icon-cybersecurity.png
            - icon-network.png
            - icon-plc.png
            - icon-globe.png
            - banner.png
        - /js/
    - /[lang]/index.html   # NATO language support (e.g. /de/, /es/, /fr/, etc.)
- `/src/`: WordPress theme and development source (optional)
- `.github/`: GitHub workflows (CI/CD, linting)
- `.gitignore`: GitHub Workflow security
- README.md: Repo purpose, deployment instructions
- LICENSE
```

## Design & Features

- **Modern, cohesive design**: All pages use a unified, professional style with a consistent color palette, typography, and layout.
- **Responsive**: Layouts adapt for desktop and mobile.
- **Hero section**: Prominent call-to-action on the homepage.
- **Service cards**: Visual, icon-based service overviews.
- **Testimonials**: Card-based client feedback with icons/photos.
- **Contact page**: Multiple contact methods (email, SMS, phone), with a pre-filled email template.
- **404 page**: Friendly, branded error page.
- **CSS**: All custom styles are in `assets/css/style.css` and used across all pages.
- **Assets**: Place all images, CSS, and JS in the `assets/` folder.
- **Accessibility**: Skip links are present but visually subtle (positioned off-screen until focused), semantic HTML, and accessible navigation.
- **SEO**: Meta tags, Open Graph, and structured data included.
- **Internationalization**: Language switcher for English and NATO languages (e.g. `/de/index.html`, `/es/index.html`, `/fr/index.html`, etc.). Ensure translated files exist as needed.
- **Uniformity**: All pages (home, services, contact, testimonials, 404, and language variants) use the same header, navigation, language switcher (top right), footer, and CSS for a consistent look and feel.

## Deployment

All files in `docs/` are automatically served by GitHub Pages.

## Notes

- Use the `assets/` folder for all CSS, JS, and media files.
- To add a favicon, place `favicon.ico` in `/docs/` and add the appropriate `<link rel="icon" ...>` tag to each HTML `<head>`.
- All HTML pages are hand-coded for performance and maintainability.
- For language support, copy and translate `index.html` to `/[lang]/index.html` for each supported NATO language.
