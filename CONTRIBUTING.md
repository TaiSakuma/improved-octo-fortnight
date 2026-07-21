# Contributing

## Docstrings

This project uses [mkdocstrings] to generate API documentation from docstrings.
Write docstrings in the [Numpydoc style].

[mkdocstrings]: https://mkdocstrings.github.io/
[Numpydoc style]: https://mkdocstrings.github.io/griffe/reference/docstrings/#numpydoc-style

## PR Title Convention

This project uses [Conventional Commits] for **PR titles**. Since we squash-merge, the PR title becomes the final commit message.

[Conventional Commits]: https://www.conventionalcommits.org/

### Format

```text
type: description
```

### Allowed Types

| Type       | Purpose                                                 |
| ---------- | ------------------------------------------------------- |
| `feat`     | A new feature                                           |
| `fix`      | A bug fix                                               |
| `docs`     | Documentation only                                      |
| `style`    | Code style (formatting, semicolons, etc.)               |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf`     | Performance improvement                                 |
| `test`     | Adding or updating tests                                |
| `build`    | Build system or external dependencies                   |
| `ci`       | CI configuration                                        |
| `chore`    | Other changes that don't modify src or test files       |
| `revert`   | Reverts a previous commit                               |

Append `!` to indicate breaking changes (e.g., `feat!: description`).

### Examples

- `feat: add user authentication`
- `fix: handle empty input`
- `docs: update installation instructions`
- `feat!: remove get_user()`

### Individual Commits

Individual commit messages within a PR are free-form. Only the PR title is enforced.

## Releasing

Releases use a two-tag flow. The `u` tag triggers changelog generation, which in turn creates the `v` tag, the GitHub Release, and the versioned docs deployment.

### Steps

1. **Check out the commit to release:**

   ```bash
   git switch main && git pull
   ```

   Or, to release from an older commit, `git switch --detach <commit>`. The chosen commit must already contain the release workflow files: a tag push runs the workflows as of the tagged commit.

2. **Bump the version:**

   ```bash
   hatch version <rule>
   ```

   Where `<rule>` is `patch`, `minor`, or `major`. This updates `src/improved_octo_fortnight/__about__.py`, creates a commit, and tags it `u<version>`.

3. **Push only the tag:**

   ```bash
   git push origin u<version>
   ```

   Not `main --tags`: a stale local `latest` tag makes `--tags` fail. GitHub Actions pushes the changelog commit and the other tags back to you.

4. **Wait for CI:**
   - The **Generate changelog** workflow creates a `release/<version>` branch at the tagged commit, generates `CHANGELOG.md` and the `v` tag on it, then merges the branch back into `main` and deletes it (a fast-forward when released from `main`'s head, a merge commit otherwise). A backport — a release cut from a commit off `main`'s line — skips the merge-back with a warning and keeps the branch as the maintenance line; `main` is untouched.
   - The **Release a new version** workflow creates a GitHub Release with categorized notes, marked as the latest release only when the version is the newest by version order.
   - The **Deploy release docs** workflow publishes the docs under `/<version>/`, refreshes `/latest/` only when the version is the newest, and regenerates the version index.

5. **Pull the results:** after a merge-back, `git pull --tags --force origin main` (`--force` lets the moved `latest` tag update). After a backport, `main` has nothing new; `git fetch --tags --force origin` retrieves the branch and the tags.

### Backports

A release whose merge-back was skipped keeps its `release/<version>` branch as the maintenance line. To cut the next release on that line, check out its `v`-tagged commit (`git switch --detach v<version>`) and follow the same steps. `main`'s `CHANGELOG.md` never lists backports, and `/latest/` stays on the newest release. Run one release at a time.

### If the release fails

A failed **Generate changelog** run leaves a skipped **Release a new version** run and no release. Delete the trigger tag (`git push origin --delete u<version>`), plus the `release/<version>` branch and the `v<version>` tag if the failed run created them. Fix the cause and push the trigger tag again. A pre-existing `release/<version>` ref makes the branch creation fail loudly by design.
