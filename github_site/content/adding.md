# Adding to ASHC

Proposals to add new entries are tracked as GitHub issues. Each proposal must include the required justification bullets, go through a community vote, and — if accepted — be implemented via a pull request.

---

## Adding a Hosting Provider

Hosting providers are listed at [/hosting-providers/](hosting-providers).

### Process

1. **Open an issue** using the **"Add: Hosting Provider"** template
2. The issue is automatically labeled `add: hosting-provider` and `status: proposed`
3. The community votes with 👍/👎 over a 7-day window
4. A maintainer updates the label to `status: accepted` or `status: rejected`
5. If accepted, open a PR that adds the new entry to **`Hosting Providers.toml`** at the repo root
6. Once the PR is merged, the issue is closed

### Required justification (3 bullets)

Your issue must address all three:

1. **Actively maintained** — link to a recent commit, release, changelog, blog, or official update showing the provider is still active
2. **Supports static site hosting** — explain how the provider hosts static files or supports static site deployments
3. **Meaningfully different** — explain how this provider differs from entries already in the directory

### TOML entry format

```toml
[[providers]]
name = "Provider Name"
url = "https://example.com"
description = "One or two sentence description."
tags = ["free", "CDN", "git-based"]
issue = "https://github.com/MooseTheRebel/awesome-static-hosting-and-cms/issues/NUMBER"
```

The `issue` field must be set to the URL of the proposal issue opened in step 1. Do not leave it blank or use a placeholder — the PR that adds the entry should include the correct issue URL in this field.

---

## Adding a CMS

Content Management Systems are listed at [/cms/](cms).

### Process

1. **Open an issue** using the **"Add: CMS"** template
2. The issue is automatically labeled `add: cms` and `status: proposed`
3. The community votes with 👍/👎 over a 7-day window
4. A maintainer updates the label to `status: accepted` or `status: rejected`
5. If accepted, open a PR that adds the new entry to **`Content Management Systems.toml`** at the repo root
6. Once the PR is merged, the issue is closed

### Required justification (4 bullets)

Your issue must address all four:

1. **Open source** — the source code must be publicly available (e.g., on GitHub, GitLab, Forgejo, Codeberg, sourcehut, or similar)
2. **Actively maintained** — link to a recent commit, release, or changelog showing the CMS is still active
3. **Works with static site generators** — explain how the CMS integrates with or supports static site generators
4. **Meaningfully different** — explain how this CMS differs from entries already in the directory

### TOML entry format

```toml
[[systems]]
name = "CMS Name"
source_url = "https://github.com/example/cms"
description = "One or two sentence description."
tags = ["git-based", "open-source", "headless"]
issue = "https://github.com/MooseTheRebel/awesome-static-hosting-and-cms/issues/NUMBER"
```

The `issue` field must be set to the URL of the proposal issue opened in step 1. Do not leave it blank or use a placeholder — the PR that adds the entry should include the correct issue URL in this field.

---

Back to [Contributing](contributing)
