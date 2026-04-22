# Contributing to ASHC

Thank you for helping improve the Awesome Static Hosting and CMS directory!

All changes to the directory go through a community review process: a proposal (GitHub issue) → a community vote → a pull request → merge.

## How it works

1. **Open an issue** using the appropriate template
2. **The community votes** using 👍/👎 reactions (30-day window)
3. **A maintainer** updates the status label to `status: accepted` or `status: rejected`
4. **If accepted**, open a PR to edit the correct TOML file
5. **Once the PR is merged**, the issue is closed

## What would you like to do?

- [Adding to ASHC](../adding/) — propose a new hosting provider or CMS
- [Removing from ASHC](../removing/) — propose removing an outdated or broken entry

## Previewing a PR locally

Maintainers and contributors can preview any open PR's generated site without leaving their machine.
Requires [just](https://just.systems/), [git](https://git-scm.com/), and [uv](https://docs.astral.sh/uv/) installed.

```
just preview-pr <PR_number>
```

This checks out the PR into a temporary directory (a `git worktree`), builds the site, and launches the dev server.
Your current branch and working tree are never touched.

**Options:**

| Argument | Effect |
|---|---|
| `no-serve=1` | Build only — skips launching the dev server |
| `keep-dir=1` | Keep the worktree directory after exit (default: cleaned up automatically) |

Example — build only, keep output to inspect:

```
just preview-pr 42 no-serve=1 keep-dir=1
```

---

Have a question? Check the [FAQ](../faq/) first.
