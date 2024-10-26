# ApesUnchained Website

This repository contains the source code for the ApesUnchained website, built using a custom Python-based static site generator.

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/mon-key-mike/ApesUnchained.git
   cd ApesUnchained
   ```

2. Install the required dependencies:
   ```
   pip install markdown
   ```

3. Build the site:
   ```
   python makesite.py
   ```

4. The generated site will be in the `_site` directory. You can serve it locally using a simple HTTP server:
   ```
   python -m http.server -d _site
   ```

   Then visit `http://localhost:8000` in your web browser.

## Adding Content

To add new pages, create Markdown files in the `content` directory. The site will be automatically rebuilt and deployed when changes are pushed to the `main` branch.

## Customizing

- Modify the layouts in the `layout` directory to change the site's structure.
- Update the CSS in `static/css/style.css` to change the site's appearance.
- Add any JavaScript functionality in `static/js/main.js`.

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch. The GitHub Actions workflow in `.github/workflows/deploy.yml` handles the build and deployment process.

## License

This project is open source and available under the [MIT License](LICENSE).# ApesUnchained
.
