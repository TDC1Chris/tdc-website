# Total Design Consulting Website

This is a custom-built, modern static website for Total Design Consulting LLC.

## Structure Overview

This is the static marketing site for [Total Design Consulting LLC](https://www.totaldesignconsulting.com).

## Live Site

[https://tdc1chris.github.io/tdc-website/](https://tdc1chris.github.io/tdc-website/)

## Structure
```bash
 - `/docs/`: Static files that GitHub Pages serves as the website
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
- `/jekyll-site/`: (optional) source Jekyll project. Build here and output to
  `docs/`.
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
- **CSS**: All pages load `assets/css/style.css` for the main theme.
- **Assets**: Place all images, CSS, and JS in the `assets/` folder.
- **Accessibility**: Select pages provide visually subtle skip links (positioned off-screen until focused). Semantic HTML and accessible navigation are used throughout.
- **SEO**: Meta tags, Open Graph, and structured data included.
- **Internationalization**: Language switcher for English and NATO languages (e.g. `/de/index.html`, `/es/index.html`, `/fr/index.html`, etc.). Ensure translated files exist as needed.
- **Uniformity**: All pages (home, services, contact, testimonials, 404, and language variants) use the same header, navigation, language switcher (top right), footer, and CSS for a consistent look and feel.

## Deployment

GitHub Pages is configured to serve the contents of `docs/`. The
`.nojekyll` file inside that folder disables GitHub's default Jekyll
processing so the HTML is served exactly as committed.

If you maintain the site using Jekyll, place your Jekyll project in a
`jekyll-site/` directory and build it into `docs/`:

```bash
cd jekyll-site
bundle install
bundle exec jekyll build -d ../docs
```

These steps copy the generated `_site` output into `docs/`, which GitHub
Pages then publishes. You can automate this with a GitHub Action that runs
the above commands whenever changes are pushed.

## Development & Continuous Integration

Run `npm install` to install the Node.js tooling. Two npm scripts are provided:

```bash
npm run build    # compile and minify assets into docs/assets/
npm run lint     # check HTML and validate links
```

A GitHub Action defined at `.github/workflows/ci.yml` runs these commands on
every pull request to ensure the site builds and passes the linters.

Install the Python packages used by `auto_translate_site.py`:

```bash
pip install -r requirements.txt
```

## Running Tests

Unit tests are written with [pytest](https://pytest.org). After installing
`pytest`, run the test suite from the repository root:

```bash
pytest
```

## Notes

- Use the `assets/` folder for all CSS, JS, and media files.
- To add a favicon, place `favicon.ico` in `/docs/` and add the appropriate `<link rel="icon" ...>` tag to each HTML `<head>`.
- All HTML pages are hand-coded for performance and maintainability.
- For language support, copy and translate `index.html` to `/[lang]/index.html` for each supported NATO language.

## Testing

Install `pytest` and run the test suite from the repository root:

```bash
pip install pytest
pytest
```
