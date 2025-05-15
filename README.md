# My Business Theme

Custom WordPress starter theme for small business websites. GitHub ready.

## 📁 Folder Structure
```
mybusinesstheme/
├── index.php
├── style.css
├── functions.php
├── header.php
├── footer.php
├── README.md
├── .gitignore
```
<<<<<<< HEAD
### Git Ignore
---
# .gitignore
=======

## 🚀 Setup
1. Clone into `wp-content/themes/`
2. Activate via WordPress admin
3. Customize and extend as needed

## ✅ Features
- Responsive HTML base
- Theme setup (menus, thumbnails)
- Basic style + layout structure
- Docker-based local development

## 🔄 Reuse
Use this repo as a template for future client/business websites.

## 🧾 Automatically Ignored Files (.gitignore)
The following files and directories are excluded using `.gitignore`:

```
>>>>>>> e3b4d71 (Updated README with clean .gitignore section; Docker YML, and Workflow Actions.)
/node_modules/
/vendor/
*.log
*.zip
wp-content/uploads/
wp-content/upgrade/
wp-content/cache/
<<<<<<< HEAD

=======
>>>>>>> e3b4d71 (Updated README with clean .gitignore section; Docker YML, and Workflow Actions.)
.env
.DS_Store
.idea/
.vscode/
<<<<<<< HEAD
---
=======
```

---

# GitHub Actions Workflow (Optional Setup: .github/workflows/deploy.yml)
# Replace with actual hosting deploy steps (FTP, rsync, etc)

name: Deploy Theme

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3

      # Insert deployment logic here (e.g. rsync to remote server)
      - name: Deploy via rsync (example)
        run: |
          rsync -avz --delete ./ user@yourhost:/path/to/wp-content/themes/mybusinesstheme
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}

---

# docker-compose.yml
version: '3.8'

services:
  wordpress:
    image: wordpress:6.5-php8.1
    ports:
      - "8000:80"
    volumes:
      - ./wp-content:/var/www/html/wp-content
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wpdb

  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: wpdb
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
      MYSQL_ROOT_PASSWORD: rootpass
    volumes:
      - db_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin
    restart: always
    ports:
      - "8080:80"
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: rootpass

volumes:
  db_data:
>>>>>>> e3b4d71 (Updated README with clean .gitignore section; Docker YML, and Workflow Actions.)
