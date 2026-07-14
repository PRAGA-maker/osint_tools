---
id: user-sherlock
name: User Sherlock
description: Use when you have a `username` and want a legacy web-based namechecker to see which social sites host that handle — returns candidate social-profile links and display names.
url: http://www.usersherlock.com
category: username
path:
- username
bestFor: A quick browser-based check of one username across a batch of social/registration sites.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free web tool; no account required. At last check the site returned HTTP 503, so availability is intermittent — verify it loads before relying on it.
opsec: passive
opsecNote: The lookup queries third-party sites from the tool's servers, not yours, so it is passive against the target. Do not enter your own accounts; results are public-presence checks only.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legacy, lightly-documented namechecker of unknown maintainership; results should be confirmed by loading each claimed profile directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- usersherlock.com
- User Sherlock namechecker
tags:
- username
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# User Sherlock

> A legacy browser-based username enumerator — type a handle, see which sites report it taken — but availability is flaky, so keep a maintained alternative ready.

## When to use
You have a `username` / handle and want a fast, no-install check of which social and registration sites have an account under it, to map a subject's cross-platform footprint. Reach for this only as a convenience web check; for anything thorough prefer a maintained enumerator (`[[user-sherlock]]` covers a narrower, older site list than modern tools).

## How to use it (`bestInteractionPattern`: web-manual)
1. Confirm the site loads — `http://www.usersherlock.com` intermittently returns 503; if it's down, switch to a maintained tool rather than waiting.
2. Enter the target `username` and run the check.
3. Read the results: each "taken" hit is a *candidate* profile URL. Open each one directly to confirm it is genuinely your subject and not a same-handle stranger.
4. Pivot: confirmed profiles feed `[[social-profiles-finder]]` for cross-network expansion, and the display `name` on a profile feeds people-search.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` candidate links, display `name` where a profile exposes it
- **Empty/negative result looks like:** all sites report the handle available/unclaimed, or the tool 503s — neither proves the person has no accounts; the covered site list is old and misses many current platforms.

## Gotchas & OpSec
- Human-in-the-loop: name-availability checks produce false positives (a claimed handle may be a different person) and false negatives (privacy settings, unlisted platforms). Always verify each hit manually.
- Reliability: legacy tool, intermittent 503s; do not build a workflow that assumes it is up.

## Overlaps ("do both")
- Pairs with `[[social-profiles-finder]]` and username-permutation work (`[[username-generation-guide]]`) — generate handle variants first, then run them through multiple checkers because no single namechecker covers every site.

## Trust & verifiability
`trust: unverified` — unknown maintainer, thin documentation, and flaky uptime; treat every hit as a lead to confirm by loading the actual profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-sherlock |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
