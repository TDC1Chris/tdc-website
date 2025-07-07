# Repository Structure

This document outlines the organized structure of the Total Design Consulting website repository.

## 📁 Root Directory Structure

```
tdc-website/
├── .github/                    # GitHub workflows and templates
├── docs/                       # Production website files (GitHub Pages)
├── documentation/              # Project documentation and guides
├── scripts/                    # Automation and utility scripts
├── archive/                    # Archived and legacy files
├── src/                        # Source files and development assets
├── assets/                     # Root-level development assets
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── CHANGELOG.md              # Version history and changes
├── README.md                 # Main project documentation
└── .gitignore                # Git ignore patterns

```

## 📚 Documentation (`/documentation/`)

### `/documentation/guides/`
- `LOCALIZATION-STRATEGY.md` - Strategy for multilingual implementation
- `TRANSLATION-GUIDE.md` - Guidelines for content translation
- `SECURITY-GUIDE.md` - Security best practices and protocols
- `NATO-TRANSLATION-SUMMARY.md` - NATO language translation capabilities
- `IP-PROTECTION.md` - Intellectual property protection guidelines
- `SOFTWARE-PROTECTION-SUMMARY.md` - Software protection measures

### `/documentation/project-status/`
- `LOCALIZATION-PROGRESS.md` - Current status of localization efforts
- `VERSION-CONTROL-SUMMARY-v1.4.0.md` - Version control documentation
- `LEAD-GENERATION-IMPROVEMENTS.md` - Lead generation enhancement tracking

### `/documentation/release-notes/`
- Future release notes will be organized here by version

## 🔧 Scripts (`/scripts/`)

### `/scripts/development/`
- `auto_translate_site.py` - Automated translation tooling for development

### `/scripts/utilities/`
- `validate_translation_setup.py` - Validation tools for translation setup
- `add_analytics.py` - Analytics integration utilities
- `update_copyright.py` - Copyright date update automation
- `update_footers.py` - Footer update utilities
- `update_footers_with_logo.py` - Logo integration for footers

## 🌐 Production Website (`/docs/`)

### Main Pages
- `index.html` - Homepage
- `about-me.html` - About page
- `services.html` - Services overview
- `portfolio.html` - Project portfolio
- `testimonials.html` - Client testimonials
- `contact.html` - Contact information

### Service Detail Pages
- `cybersecurity-consulting.html` - Cybersecurity services
- `network-infrastructure.html` - Network infrastructure services
- `industrial-automation.html` - Industrial automation services
- `safety-compliance.html` - Safety and compliance services
- `translation-technology.html` - Translation technology showcase

### Localized Sites
- `/de/` - German language site (Deutsch)
- `/es/` - Spanish language site (Español)
- `/hi/` - Hindi language index page
- `/ur/` - Urdu language index page
- `/zh/` - Chinese language index page (中文)
- `/sv/` - Swedish language index page (Svenska)

### Assets (`/docs/assets/`)
- `/css/` - Stylesheets
- `/images/` - Website images and icons
- `/documents/` - Downloadable documents (resumes, PDFs)
- `/templates/` - Email and SMS templates

### Technical Files
- `sitemap.html` - HTML sitemap
- `sitemap.xml` - XML sitemap for search engines
- `robots.txt` - Search engine crawling instructions
- `404.html` - Custom 404 error page
- `.nojekyll` - GitHub Pages configuration
- `CNAME` - Domain configuration

## 🗄️ Archive (`/archive/`)

### `/archive/old-tests/`
- Legacy test files and experimental content
- Preserved for reference but not part of active development

## 🛠️ Development (`/src/`)

- Development-specific files
- Docker configurations
- SCSS source files
- Development environment setup

## 🔧 Configuration Files

- `package.json` - Node.js dependencies and scripts
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore patterns
- `.env.example` - Environment variable template

## 📋 File Naming Conventions

### Documentation
- Use descriptive, uppercase names with hyphens: `LOCALIZATION-STRATEGY.md`
- Include version numbers where applicable: `VERSION-CONTROL-SUMMARY-v1.4.0.md`

### Scripts
- Use lowercase with underscores: `validate_translation_setup.py`
- Group by functionality in appropriate subdirectories

### Website Files
- Use lowercase with hyphens for HTML files: `cybersecurity-consulting.html`
- Language codes follow ISO standards: `/de/`, `/es/`, `/zh/`

## 🚀 Deployment

The `/docs/` directory is served directly by GitHub Pages. All production-ready files must be placed in this directory structure.

## 📝 Maintenance

- Update `CHANGELOG.md` for all significant changes
- Maintain this structure document when adding new directories
- Archive old files rather than deleting them
- Keep scripts organized by function and frequency of use

---

**Last Updated:** July 7, 2025
**Repository Version:** v2.0.1
