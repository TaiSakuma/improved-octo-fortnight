# improved-octo-fortnight

[![GitHub Release][release-badge]][release-url]
[![GitHub Pages][pages-badge]][pages-url]

[![Deploy dev docs][dev-badge]][dev-url]
[![Deploy release docs][release-docs-badge]][release-docs-url]
[![Build docs preview][preview-badge]][preview-url]

[release-badge]: https://img.shields.io/github/v/release/TaiSakuma/improved-octo-fortnight
[release-url]: https://github.com/TaiSakuma/improved-octo-fortnight/releases/latest
[pages-badge]: https://img.shields.io/website?url=https://taisakuma.github.io/improved-octo-fortnight/
[pages-url]: https://taisakuma.github.io/improved-octo-fortnight/
[dev-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-dev.yml/badge.svg
[dev-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-dev.yml
[release-docs-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-release.yml/badge.svg
[release-docs-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-release.yml
[preview-badge]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-pr-build.yml/badge.svg
[preview-url]: https://github.com/TaiSakuma/improved-octo-fortnight/actions/workflows/docs-pr-build.yml

A reference implementation of documentation workflows.

📚 [Demo site](https://taisakuma.github.io/improved-octo-fortnight/)

## Features

### Content

- Built with [zensical](https://zensical.org/)
- API reference auto-generated using [mkdocstrings](https://mkdocstrings.github.io/)

This repo documents a Python package. The setup should work for other languages with minor modifications.

### Deployment

- Deployed to [GitHub Pages](https://pages.github.com/) via [GitHub
  Actions](https://github.com/features/actions)
- Separate docs for each release and development branch
- Docs preview for each PR

## GitHub Pages structure

The deployed site is structured as follows:

```text
/
├── index.html          # auto-generated version index
├── latest/             # copy of the latest release
├── dev/                # built from main
├── 2.0.0/              # release versions
├── 1.1.0/
├── 1.0.0/
└── pr/
    ├── 14/             # PR preview
    └── 13/
```

## GitHub Actions workflows

These workflows build, deploy, and clean up the documentation:

| Workflow                | Trigger           | Deploys to                              |
| ----------------------- | ----------------- | --------------------------------------- |
| [`docs-dev.yml`]        | Push to `main`    | `/dev/`, `index.html`                   |
| [`docs-release.yml`]    | Release           | `/<version>/`, `/latest/`, `index.html` |
| [`docs-pr-build.yml`]   | PR opened/updated | builds docs, uploads artifact           |
| [`docs-pr-deploy.yml`]  | Build completed   | `/pr/<number>/`                         |
| [`docs-pr-cleanup.yml`] | PR closed         | removes `/pr/<number>/`                 |

[`docs-dev.yml`]: .github/workflows/docs-dev.yml
[`docs-release.yml`]: .github/workflows/docs-release.yml
[`docs-pr-build.yml`]: .github/workflows/docs-pr-build.yml
[`docs-pr-deploy.yml`]: .github/workflows/docs-pr-deploy.yml
[`docs-pr-cleanup.yml`]: .github/workflows/docs-pr-cleanup.yml

The workflows require the GitHub settings

- `Settings` > `Pages` > `Source` > `Deploy from a branch` > `gh-pages` (root `/`)
