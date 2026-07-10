---
id: socialscan
name: socialscan
description: Use when you have a `username` or `email` and want to know which platforms it is registered on — returns per-platform available/taken/invalid status (a social-profile map).
url: https://pypi.org/project/socialscan/
category: username
path:
- username
bestFor: Fast, false-positive-free checking of whether a username/email is taken across many platforms by querying their registration endpoints directly.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (MPL 2.0). No account or API key; you run it locally via pip.
opsec: passive
opsecNote: It queries platforms' registration/availability endpoints from your machine, not the target. Route through a proxy (supported) and a sock-puppet network context for sensitive work, since you are hitting many services in quick succession.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Open-source tool by iojw (latest 2.0.1, Jan 2024). Because it checks registration endpoints rather than profile pages, it avoids the false positives common to name-scanners — but individual platform checks break when sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- epieos
aliases:
- socialscan pip
tags:
- username
- email
- account-existence
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# socialscan

> A local CLI/library that asks platforms directly "is this username/email taken?" — mapping where a selector is registered without the false positives of profile-page scanning.

## When to use
You have a candidate `username` or `email` and want to know, quickly and accurately, which platforms it exists on. Unlike scanners that guess from profile-page HTTP codes, socialscan queries each platform's actual registration/availability endpoint, so "taken" reliably means an account exists. Ideal for confirming a handle is in use before deep-diving, and for spotting which networks to pivot into.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install socialscan`.
2. CLI: `socialscan username1 user@email.com` — add `--platforms`, `--json`, an input file for bulk, or `--proxy` as needed.
3. Or in Python:
   ```python
   from socialscan.util import Platforms, sync_execute_queries
   results = sync_execute_queries(["handle", "a@gmail.com"], [Platforms.GITHUB, Platforms.INSTAGRAM])
   ```
4. Read results: each query returns available / taken / invalid per platform (Instagram, Twitter, GitHub, Tumblr, Lastfm, Snapchat, GitLab, Reddit, Yahoo, Pinterest, Firefox).
5. Pivot: a "taken" handle → go view that profile; a "taken" email → feed into `[[epieos]]`/account-existence tools.

## Inputs → Outputs
- **In:** `username` and/or `email` (single or bulk)
- **Out:** `social-profile` existence map — per-platform available / taken / invalid
- **Empty/negative result looks like:** all "available" (nothing registered) or "invalid" (malformed) results. A platform that has changed its endpoint may error out — a single-platform failure is a tooling break, not a confirmed "available."

## Gotchas & OpSec
- Platform coverage is fixed to those it supports; it won't check sites outside that list.
- Individual checks rot as platforms change registration flows — cross-check surprising negatives manually.
- Rapid multi-platform queries can trip rate limits; use the proxy option for volume.
- OpSec: passive toward the subject (endpoints, not profiles), but your IP hits many services — use a proxy for sensitive work.

## Overlaps ("do both")
- Pairs with `[[epieos]]` and web-based username-search tools — socialscan gives fast, accurate *existence* across its supported platforms; broader scanners (e.g. Sherlock/Maigret-style) cover more sites with more noise. Run socialscan first for high-confidence hits.

## Trust & verifiability
`trust: community` — a respected open-source tool whose endpoint-based method is more reliable than profile-scraping scanners. Still, checks depend on unchanged platform behavior, so verify important negatives by hand.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialscan |
</content>
