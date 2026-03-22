# improved-octo-fortnight

[![GitHub Release][release-badge]][release-url]
[![GitHub Pages][pages-badge]][pages-url]

[![Deploy dev docs][dev-badge]][dev-url]
[![Deploy release docs][release-docs-badge]][release-docs-url]
[![Deploy docs preview][preview-badge]][preview-url]

[release-badge]: https://img.shields.io/github/v/release/TaiSakuma/improved-octo-fortnight
[release-url]: https://github.com/TaiSakuma/improved-octo-fortnight/releases/latest
[pages-badge]: https://img.shields.io/website?url=https://taisakuma.github.io/improved-octo-fortnight/
[pages-url]: https://taisakuma.github.io/improved-octo-fortnight/
[dev-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-dev.yml/badge.svg
[dev-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-dev.yml
[release-docs-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-release.yml/badge.svg
[release-docs-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-release.yml
[preview-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-pr-preview.yml/badge.svg
[preview-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-pr-preview.yml

A reference implementation of a documentation workflow using [zensical](https://zensical.org/) and GitHub Pages.

- [latest](https://taisakuma.github.io/improved-octo-fortnight/latest/)
- [dev](https://taisakuma.github.io/improved-octo-fortnight/dev/)

## Features

- **Versioned docs** -- Release docs at `/<version>/`, dev docs at `/dev/`, and a `/latest/` alias
- **PR previews** -- Every PR gets a preview deployment at `/pr/<number>/` with an automatic comment linking to it
- **PR cleanup** -- Preview deployments are removed when PRs are closed
- **Version index** -- An auto-generated root `index.html` lists all available versions
- **Deploy verification** -- The preview URL is polled before posting the PR comment; a note is added if the site isn't ready yet
- **Custom domain support** -- Works with both default GitHub Pages URLs and custom domains
- **API reference** -- Auto-generated from Python docstrings using [mkdocstrings](https://mkdocstrings.github.io/). Add `:::` directives in Markdown to render any module (see `docs/api.md` for an example)

## How it works

Documentation is built with [zensical](https://zensical.org/) and deployed by pushing subdirectories to a `gh-pages` branch. Four workflows handle the different deployment scenarios:

| Workflow              | Trigger                          | Deploys to                                |
| --------------------- | -------------------------------- | ----------------------------------------- |
| `docs-dev.yml`        | Push to `main`                   | `/dev/`                                   |
| `docs-release.yml`    | Release (via changelog workflow) | `/<version>/` + `/latest/` + `index.html` |
| `docs-pr-preview.yml` | PR opened/updated (incl. forks)  | `/pr/<number>/`                           |
| `docs-pr-cleanup.yml` | PR closed                        | removes `/pr/<number>/`                   |

The `gh-pages` branch has the following structure:

```
gh-pages
├── .nojekyll
├── index.html          # auto-generated version index
├── latest/             # copy of the latest release
├── dev/                # built from main
├── 0.2.1/              # release versions
├── 0.2.0/
└── pr/
    ├── 14/             # PR preview
    └── 13/
```

Shared logic is extracted into two composite actions:

- **`.github/actions/build-docs`** -- Overrides `site_url` for the target subdirectory, builds the site, and stages the output
- **`.github/actions/deploy-to-gh-pages`** -- Checks out (or creates) the `gh-pages` branch and pushes the built site to a target subdirectory

A Python script (`.github/actions/build-docs/override_site_url.py`) uses [tomlkit](https://github.com/sdispater/tomlkit) to modify `site_url` in `zensical.toml` so that navigation and search work correctly in each subdirectory.

## Setup

1. Install [uv](https://docs.astral.sh/uv/)
2. Build docs locally:
   ```
   uv run --group docs zensical serve
   ```
3. Set GitHub Pages source to **Deploy from a branch** > `gh-pages` (root `/`)
