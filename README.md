# Total Design Consulting Website

This repository contains the source code for the official website of **Total Design Consulting LLC**, a firm specializing in Cybersecurity, IT/OT Engineering, Safety, and PLC Automation.

## 🌐 Live Website

[https://www.totaldesignconsulting.com](https://www.totaldesignconsulting.com)

---

## ✅ Features

### 🌍 Multilingual Support
- Full support for **NATO languages** via dedicated subdirectories (`/en/`, `/de/`, `/es/`, etc.).
- Language selector replaced with a **globe icon** that links to a centralized [language selection page](languages.html).
- SEO-friendly, static file structure ensures compatibility with GitHub Pages.

### 🛡️ Accessibility
- ARIA labels added to all interactive elements.
- High-contrast color scheme for improved readability.
- Semantic HTML with a consistent heading structure.

### 🚀 Performance
- All images optimized and converted to WebP where appropriate.
- File structure and HTML modularized for maintainability.
- Minimal inline styles; styles are externalized.

### 🔍 SEO Enhancements
- Meta titles and descriptions added to all key pages.
- Correct heading hierarchy (`<h1>` to `<h3>`) for improved semantic structure.
- Language-specific pages use proper `lang` attributes.

### 🧱 Page Structure
- `/index.html` and `/en/index.html`: Home (English)
- `/services.html`, `/contact.html`, `/testimonials.html`: Core service pages
- Language folders include placeholder index pages with return links to `/en/`

---

## 🛠️ Improvements in v10

- Refactored legacy inline code
- Fixed language switcher recursive path bug
- Created language-specific folders for all NATO member languages
- Replaced dropdown language menu with globe icon
- Added `languages.html` with links to all language versions
- Accessibility and SEO compliance patches

---

## 📁 Deployment

Deployed via GitHub Pages:
```
https://tdc1chris.github.io/tdc-website/
```

GitHub Pages automatically serves files from the `docs/` directory.

---

## 📦 Version History

- `v9`: Multilingual support introduced with language folders and selector
- `v10`: Full audit, accessibility fixes, SEO, image optimization, UI improvements

---

## 📧 Contact

For questions or feedback, contact [support@totaldesignconsulting.com](mailto:support@totaldesignconsulting.com)
