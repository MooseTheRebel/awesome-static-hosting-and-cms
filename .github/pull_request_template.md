## Summary

<!-- Describe what this PR changes and why. -->

## Checklist

- [ ] TOML entries are sorted (`just check-toml`)
- [ ] Tested locally (`just dev`)

## Preview

To preview this PR's site locally:

```
just preview-pr <PR_number>
```

Pass `no-serve=1` to build only (no dev server), or `keep-dir=1` to keep the build output after exit.
Requires [just](https://just.systems/), [git](https://git-scm.com/), and [uv](https://docs.astral.sh/uv/) to be installed.
