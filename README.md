# WebODM Website

The official website for [WebODM](https://webodm.org), built with [Zola](https://www.getzola.org/) — a fast static site generator written in Rust.

## Prerequisites

- [Zola](https://www.getzola.org/documentation/getting-started/installation/) (v0.17+)
- Git

### Installing Zola

See the [official installation docs](https://www.getzola.org/documentation/getting-started/installation/).

## Getting Started

```bash
git clone https://github.com/WebODM/webodm-web.git
cd webodm-web
zola serve
```

**Open your browser** at [http://127.0.0.1:1111](http://127.0.0.1:1111).

The site will live-reload automatically whenever you save a file.

## Project Structure

```
webodm-web/
├── config.toml        # Zola site configuration
├── start.sh           # Helper script to run the dev server
├── content/           # Markdown pages and blog posts
│   └── blog/          # Blog entries
├── data/              # JSON data files (e.g. datasets)
├── public/            # Pre-built static assets (CSS, images)
├── static/            # Static files copied as-is to the output
├── templates/         # Tera HTML templates
│   ├── base.html      # Base layout
│   ├── index.html     # Homepage
│   ├── page.html      # Generic page template
│   ├── download.html  # Download page
│   └── datasets.html  # Datasets page
└── themes/            # Zola themes (if any)
```

## Building for Production

To generate the static site into the `public/` directory:

```bash
zola build
```

## Contributing

1. Fork the repository and create a feature branch.
2. Run `zola serve` to preview your changes locally.
3. Commit your changes and open a pull request.

## License

See the repository for license details.
