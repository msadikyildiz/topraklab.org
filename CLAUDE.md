# Toprak Lab Website

Source for topraklab.org, the website of the Toprak Lab at UT Southwestern. It is an Astro static site
deployed to Cloudflare Pages. This file is for anyone, or any coding agent, working on the site.

## Layout

- `src/pages/`: one `.astro` file per page (`index`, `people`, `publications`, `funding`, `news`,
  `contact`, `science/`, `404`).
- `src/components/`, `src/layouts/`, `src/styles/`: shared components, page layouts, and styles.
- `src/data/*.json`: the site's content (people, publications, funding, media, visitors). Most edits
  to what the site says are edits to these files.
- `public/`: static files served as they are, including `fonts/`, `papers/`, `videos/`, and
  `_redirects` (Cloudflare Pages redirect rules).

## Build and preview

```sh
bun install
bun run dev        # local preview with live reload
bun run build      # static output in dist/
bun run preview    # serve the built dist/
```

`wrangler.toml` names the Cloudflare Pages project; `pages_build_output_dir` is `dist`.

## Style

The site is dense and plain: tight vertical rhythm, information-rich sections, little whitespace
between them. Copy is written by scientists for scientists, precise and understated, with no
marketing language.
