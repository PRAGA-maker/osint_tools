---
id: user-searcher
name: User Searcher
description: Use when you have a `username` and want to find every account reusing it — returns matching social-profile links, avatars and bios across ~2,000+ sites.
url: https://www.user-searcher.com
category: username
path:
- username
bestFor: Fast, no-login reverse-username sweep across thousands of social, dating, forum and gaming sites.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free web tool, no subscription, payment, or account required; results exportable to Excel/JSON.
opsec: passive
opsecNote: User Searcher performs the site checks server-side, so the queries appear to come from its infrastructure, not you — the target's platforms do not see your IP. You do disclose the username of interest to a third-party service; use a sock-puppet browser and assume queries may be logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Free third-party Sherlock-style aggregator; convenient but unverified provenance, and like all username scanners it produces false positives on sites that return soft-404 profile pages.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- user-searcher.com
tags:
- username-check
- reverse-username
- account-discovery
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# User Searcher

> A free, no-login reverse-username engine that checks one handle against ~2,000+ sites and returns the live profiles it finds.

## When to use
You have a `username`/handle (from an email prefix, a social bio, a forum post, a gamertag) and want to map the subject's wider footprint — every other platform where the same handle is registered. Ideal early in an identity workflow to turn one handle into a spread of `social-profile`s that can reveal a real `name`, `image`, and further selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.user-searcher.com in a sock-puppet browser.
2. Enter the `username` and run the search.
3. Wait as it queries thousands of sites (social networks, dating, forums, gaming, blogs) and groups hits by category.
4. Read the results: each hit shows a direct `social-profile` link plus, where available, an avatar (`image`) and bio; open each to confirm it is really the same person, not just a coincidental handle reuse.
5. Export to Excel/JSON if you want to work the list offline.
6. Pivot: a confirmed profile with a real `name` feeds people-search; an avatar feeds `[[reverse-image-search]]`; a linked site feeds domain/WHOIS.

## Inputs → Outputs
- **In:** `username`
- **Out:** matching `social-profile` links across many platforms, plus avatar `image` and display `name` where exposed
- **Empty/negative result looks like:** few or no hits — either a rare/unique handle with little reuse, or the person varies handles across sites. Absence is not proof of no accounts.

## Gotchas & OpSec
- False positives: username scanners often flag a site as "found" when it actually returns a generic/placeholder page. Always open and eyeball each hit — matching handle ≠ same human.
- Common handles (e.g. "john", "shadow") return huge noisy lists dominated by unrelated people; distinctive handles are far more reliable.
- OpSec: **passive** — checks run server-side, so your IP isn't exposed to the target's platforms; still use a sock puppet since your query hits a third party.

## Overlaps ("do both")
- Pairs with Sherlock/WhatsMyName-class scanners and other `[[username]]` tools — coverage lists differ, so run at least two and union the results; each catches sites the other misses.

## Trust & verifiability
`trust: community` — a free aggregator with no disclosed maintainer; treat every hit as a candidate to verify by opening the profile, and confirm identity by cross-referencing avatar, bio, and linked accounts rather than the handle alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-searcher |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
