---
id: osint-toolkit
name: OSINT Toolkit (Email/Username)
url: https://one-plus.github.io/EmailUsername
category: username
path:
- username
description: Use when you have a `username` or `email` and want a one-page dashboard of cross-platform search links — returns ready-made queries resolving to `social-profile`s.
bestFor: A free client-side dashboard that turns one username/email into search links across many social and people-search platforms.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free static web page (GitHub Pages); it only builds links to third-party services, so no account or payment on the tool itself.
opsec: passive
opsecNote: The page generates links in your browser and does not itself query the target; exposure comes from the third-party services you click through to. Follow the generated links from a sock-puppet browser to avoid attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple community-built link-generator hosted on GitHub Pages; it does no matching itself, so reliability depends entirely on the destination services it points to.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- EmailUsername toolkit
- one-plus OSINT Toolkit
tags:
- username-enumeration
- osint-dashboard
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# OSINT Toolkit (Email/Username)

> A free, single-page link dashboard: type a username or email and it hands you ready-made search queries across social platforms and people-search services.

## When to use
You have a `username` or `email` and want a quick, no-install sweep of where to look — the page builds search links for Facebook, Twitter/X, Instagram, YouTube, LinkedIn, Snapchat, Kik and people-search/aggregator services. A convenient low-effort first pass to scope a handle before reaching for automated enumerators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one-plus.github.io/EmailUsername.
2. Enter the `username` or `email` (without @ / # symbols).
3. Click the generated per-platform links; each opens a search on that third-party service.
4. Work through the results, noting which platforms resolve to a real profile.
5. Pivot: confirmed `social-profile`s feed avatar reverse-image search; handles embedding a real name feed name-based people search.

## Inputs → Outputs
- **In:** `username` or `email`
- **Out:** search links resolving to `social-profile`s and `name` mentions
- **Empty/negative result looks like:** the linked searches return nothing — and per the tool's own disclaimer, a negative result does NOT prove the handle is unused (especially on messaging apps). Treat misses as inconclusive.

## Gotchas & OpSec
- It only builds links; you still click through and read each service manually.
- Its own caveat: username/email results are approximations and negatives are unreliable — corroborate.
- OpSec: link-building is passive; following links queries third parties tied to your session — use a puppet browser.

## Overlaps ("do both")
- Pairs with `[[username-search-tool]]` and `[[deepfind-me]]` — this is another link-based dashboard, while active enumerators check platform existence directly; running several improves recall.

## Trust & verifiability
`trust: community` — a lightweight community link-generator; it performs no matching of its own, so verify every hit on the destination service before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-toolkit |
| category | username |
| selectorsIn → selectorsOut | username, email → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
