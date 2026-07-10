---
id: ello
name: Ello
description: Use when a historical lead points to an `ello.co` profile — returns nothing live; the network shut down in 2023 and the domain is now hijacked, so treat only as archival context.
url: https://ello.co/
category: social-networks
path:
- social-networks
bestFor: Recognising that an old ello.co reference is dead and pivoting to web archives instead of the live domain.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: The service is defunct; there is nothing to pay for or query.
opsec: passive
opsecNote: Do NOT visit the live ello.co domain for research — as of 2025-2026 it changed hands and redirects to casino/spam sites; use web.archive.org instead so you never touch the hijacked domain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The original creative-focused network is gone (servers began failing June 2023, permanently shut down that year); the current domain is unrelated spam, so nothing served there can be trusted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-reverse-image-search
aliases:
- ello.co
tags:
- toddington
- curated-directory
- social-media
- defunct
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Ello

> A defunct ad-free social network for creatives (2014–2023) — kept here only so an agent recognises that an `ello.co` lead is dead and the live domain is now hijacked spam.

## When to use
You encounter an old reference to an `ello.co/<username>` profile in someone's link history, an archived bio, or a curated directory, and need to know whether it is worth chasing. The answer is: the platform permanently shut down in 2023, so there is no live profile to view. Your only route to any surviving content is a web archive — and you should avoid the live domain entirely.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do **not** open the live `ello.co` domain — since 2025 it resolves to unrelated casino/spam content.
2. Instead, query the Wayback Machine: `https://web.archive.org/web/*/ello.co/<username>` to see if the profile was ever captured.
3. If a snapshot exists, read the archived bio, posts and image links for `name`, other-account links, or photos.
4. Pivot: run any archived `image` through `[[google-reverse-image-search]]`, and chase linked handles on still-live platforms.

## Inputs → Outputs
- **In:** `name` or `username` (from a historical reference)
- **Out:** at best an archived `social-profile` snapshot via Wayback; nothing from the live site
- **Empty/negative result looks like:** no Wayback capture for the handle — the trail ends here; the live domain returning spam is expected, not a finding.

## Gotchas & OpSec
- The live domain is compromised/spam — treat any content it serves as hostile; never enter data there.
- Archives are partial; a missing snapshot doesn't prove the person had no Ello, only that it wasn't captured.
- OpSec: passive, and using web.archive.org keeps you off the hijacked domain entirely.

## Overlaps ("do both")
- Pairs with `[[google-reverse-image-search]]` — any image recovered from an archived Ello profile should be reverse-searched to find the subject on platforms that still exist.

## Trust & verifiability
`trust: unverified` — the platform is gone and the domain is now third-party spam; only archived captures carry any evidentiary value, and even those should be corroborated elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ello |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
