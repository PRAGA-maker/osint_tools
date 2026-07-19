---
id: cse-utopia
name: CSE Utopia
description: Use when you have any selector and want a big curated set of Google Custom Search Engines to pivot it — returns links to purpose-built CSEs for OSINT.
url: https://start.me/p/EL84Km/cse-utopia
category: search-engines
path:
- search-engines
bestFor: A one-stop start.me dashboard of Google Custom Search Engines (by platform, selector, and topic) to run targeted OSINT searches.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free start.me page linking to free Google Custom Search Engines; no account needed to use the linked CSEs.
opsec: passive
opsecNote: The dashboard itself is a passive link list. The searches you then run happen on Google/CSE infrastructure (passive toward the subject). Standard sock-puppet browser hygiene applies; nothing here contacts a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known curated collection maintained by Dean Da Costa, a respected OSINT practitioner; the value is curation — the underlying CSEs are third-party and vary in freshness.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- geoint
- osint-assassin
- socmint
- start-me
aliases:
- CSE Utopia start.me
- Dean Da Costa CSE
tags:
- custom-search-engine
- osint-dashboard
- curated-directory
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# CSE Utopia

> A large curated dashboard of Google Custom Search Engines for OSINT — hundreds of purpose-built CSEs (social platforms, usernames, images, leaks, regions) collected in one start.me page.

## When to use
You have a selector — a `name`, `username`, `email`, phone, image, etc. — and want a CSE tuned to the platform or data type you're pivoting into, without hand-building the search yourself. CSE Utopia is a launchpad: pick the relevant custom search engine (e.g. social-account search, Telegram, TikTok, breach/paste search) and run your selector through it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://start.me/p/EL84Km/cse-utopia (start.me may 403 automated fetchers but loads in a browser).
2. Browse the categorized tiles to the CSE matching your target platform/selector.
3. Open that CSE and run your selector; the CSE constrains Google to a curated set of relevant sites.
4. Pivot: results are normal web hits — profiles, mentions, files — that feed the rest of your workflow. Try several CSEs, since each scopes a different site set.

## Inputs → Outputs
- **In:** `name`, `username`, `email` (or other selectors, depending on the chosen CSE)
- **Out:** targeted search hits → `social-profile`s, mentions, documents
- **Empty/negative result looks like:** a CSE returning nothing — its site list may be stale or too narrow; try a broader CSE or a plain scoped Google dork instead.

## Gotchas & OpSec
- It's a curated link list, not a search itself — quality depends on each linked CSE, some of which age out.
- Google Programmable Search coverage/quotas can limit results; don't treat an empty CSE as definitive.
- OpSec: passive; standard search-engine footprint only.

## Overlaps ("do both")
- Complements other CSE collections and manual Google dorking — run the same selector through multiple CSE sets, since each sees different sites.

## Trust & verifiability
`trust: community` — a respected practitioner's curation; reliable as a launchpad, but verify hits at their source since the CSEs are third-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cse-utopia |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
