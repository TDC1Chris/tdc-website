# Total Design Consulting Website

## 🚀 Version 1.2.0 - Real-World Testimonials Integration

This is a custom-built, modern static website for Total Design Consulting LLC, featuring professional branding, international focus, and comprehensive portfolio showcase.

## Overview

This is the static marketing site for [Total Design Consulting LLC](https://www.totaldesignconsulting.com), showcasing multilingual cyber-OT engineering services with Fortune 50 client experience.

## Live Site

[https://tdc1chris.github.io/tdc-website/](https://tdc1chris.github.io/tdc-website/)

## Structure
```bash
 - `/docs/`: Production static files served by GitHub Pages
    - index.html                    # Homepage with hero section and company overview
    - services.html                 # Service offerings with international focus
    - portfolio.html                # Professional experience and client showcase
    - contact.html                  # Multi-channel contact with pre-filled templates
    - testimonials.html             # Client testimonials and success stories
    - legal-terms-conditions.html   # Legal compliance and terms
    - 404.html                      # Branded error page
    - robots.txt                    # SEO configuration
    - CNAME                         # Custom domain configuration
    - /assets/
        - /css/
            - style.css             # Main stylesheet with TDC branding
            - custom.css            # Additional customizations
        - /images/                  # Professional icons and branding assets
            - color-logo-*.png      # TDC logo variants
            - icon-*.png            # Service and capability icons
        - Resume_*.pdf              # Downloadable resume versions
        - email-template.txt        # Pre-filled client contact template
        - sms-template.txt          # SMS contact template
- `/src/`: Development source files
- `/tests/`: Testing and validation files
- `.github/`: GitHub workflows for CI/CD
```

## Key Features

### Professional Branding & Design
- **Modern, cohesive design**: Unified professional style with consistent TDC branding
- **Responsive layout**: Optimized for desktop, tablet, and mobile devices
- **Professional color palette**: Success green (#198754) with clean, modern typography

### Content & Messaging
- **Authentic experience**: Real Fortune 50 client references (GM, John Deere, ABB, TRUMPF, etc.)
- **International focus**: 8-language capability prominently featured with flags
- **Security clearance**: Properly documented TS/SCI status (Inactive) for legal compliance
- **Comprehensive portfolio**: Detailed project experience and measurable results
- **Professional credentials**: All certifications and expertise accurately represented

### Functional Features
- **Multi-channel contact**: Email, SMS, and phone with pre-filled templates
- **Downloadable resume**: Professional PDF and HTML versions
- **SEO optimized**: Meta tags, structured data, and search engine friendly
- **Legal compliance**: Terms & conditions, privacy considerations
- **Performance focused**: Fast loading, minimal dependencies

### International Business Ready
- **Multilingual capabilities**: Native-level German, Hindi, Urdu, plus 4 additional languages
- **Global client focus**: Fortune 50 and international manufacturer experience
- **Cross-cultural communication**: Technical translation and global standards expertise
- **Time zone considerations**: 24/7 international support capability
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
