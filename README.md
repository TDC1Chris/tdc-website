# Total Design Consulting Website

This is a custom-built website with themes for Total Design Consulting LLC.

## Structure Overview

This is the static marketing site for [Total Design Consulting LLC](https://www.totaldesignconsulting.com).

## Live Site

[https://tdc1chris.github.io/tdc-website/](https://tdc1chris.github.io/tdc-website/)

## Structure

- `public/`: Static files for GitHub Pages
- `src/`: WordPress theme and development source (optional)
- `.github/`: GitHub Pages and automation

tdc-website/
├── public/                 ← GitHub Pages deploy folder (only static site here)
│   ├── index.html
│   ├── contact.html
│   ├── services.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── 404.html
│   └── favicon.ico
├── src/                    ← Original theme or WordPress files (optional backup)
│   └── dev/
├── .github/                ← GitHub workflows (CI/CD, linting)
├── .gitignore
├── README.md              ← Repo purpose, deployment instructions
└── LICENSE


## Deployment

All files in `public/` are automatically served by GitHub Pages.


## Notes
- Use the `assets/` folder for all CSS, JS, and media files.
