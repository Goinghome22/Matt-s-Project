# Docs

This folder powers a small documentation site (Jekyll-compatible structure) with pages for about, projects, resume, and contact.

## Key Files

- `_config.yml`: site configuration
- `index.md`: landing page
- `about.md`, `projects.md`, `resume.md`, `contact.md`, `404.md`
- `_includes/`, `assets/`, `data/`: theme components, media, and data files

## Local Preview (optional)

If you have Ruby and Jekyll:

```bash
# from repo root
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000` to preview.

If you do not use Jekyll locally, you can still open the Markdown files directly for content. 