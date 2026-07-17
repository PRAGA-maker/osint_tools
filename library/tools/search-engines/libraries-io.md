---
id: libraries-io
name: Libraries.io
description: Use when you have a developer `name`/`username` or a package/project name and want to find the source repo, maintainers and contact points — returns social-profile, email, domain.
url: https://libraries.io/
category: search-engines
path:
- search-engines
bestFor: Pivoting from an open-source package or its maintainer to source repos, homepages and maintainer contact points across 30+ package ecosystems.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- email
- domain
status: live
pricing: free
costNote: Free to search and browse ~12M packages; a paid Tidelift tier adds curated/validated data and higher API limits, but the public search and package pages are free.
opsec: passive
opsecNote: Read-only queries against a public package index; nothing is sent to the target. Safe from any browser. The optional API needs a free key tied to an account, so use a research account if you call it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Tidelift; data is scraped from public registries (npm, PyPI, Maven, RubyGems, etc.) and explicitly "not validated or curated" in the free tier, so treat maintainer fields as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- libraries.io
- Tidelift Libraries
tags:
- toddington
- curated-directory
- specialty-search
- packages
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Libraries.io

> A cross-ecosystem index of ~12M open-source packages that turns a package or developer handle into source repos, homepages and maintainer contacts.

## When to use
Your subject is a software developer, or you have a package/project they publish. You have a `name` or `username` (or the package name) and want to enumerate what they maintain, then pivot to the linked GitHub/GitLab repo, project homepage (`domain`), and any maintainer `email` exposed in registry metadata. Useful for corroborating a technical identity or finding a fresh contact channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://libraries.io/ and search the package name, or search a maintainer handle.
2. Open a package page: it lists the source repository, homepage, licences, and maintainer/owner handles.
3. Follow the `Repository` link to the GitHub/GitLab profile (a `social-profile`), and the `Homepage` to the project `domain`.
4. For package managers that publish maintainer email in metadata (npm, RubyGems), the address may appear on the page or in the underlying registry — pivot that `email` onward.
5. Pivot: feed a discovered GitHub handle to a username search, or the homepage domain to WHOIS/`[[whoxy-whois-history]]`-style lookups.

## Inputs → Outputs
- **In:** `name` or `username` (or a package/project name)
- **Out:** `social-profile` (source repo), `domain` (project homepage), sometimes maintainer `email`
- **Empty/negative result looks like:** no matching package, or a package page with only a registry link and no repo/homepage/maintainer — meaning no pivot beyond the package itself.

## Gotchas & OpSec
- Free-tier data is scraped and unvalidated; a listed maintainer may be stale or a bot account. Confirm on the live registry/repo.
- Coverage is package metadata, not people — it only helps if the subject actually publishes open source.
- The API requires a free account key; register with a research identity if you automate.

## Overlaps ("do both")
- Pairs with a GitHub-focused search because Libraries.io names the repo but the repo's commit history/emails give the deeper identity trail.

## Trust & verifiability
`trust: community` — a well-known, long-running Tidelift service, but the free data is explicitly uncurated, so use package/maintainer fields as leads and verify on the source registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | libraries-io |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
