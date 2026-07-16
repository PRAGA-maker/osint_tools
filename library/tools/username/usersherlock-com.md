---
id: usersherlock-com
name: UserSherlock
description: Use when you have a `username` and want a quick web check of which popular sites have an account under that handle — returns social-profile links and candidate name.
url: http://www.usersherlock.com/usersearch
category: username
path:
- username
bestFor: Fast, no-install browser check of a username across ~20+ popular social/web services.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free to use in the browser; no account required.
opsec: passive
opsecNote: The service checks each site for you server-side, so the target is not notified. Because it is an older, single-site service its results can lag; treat "found" links as candidates to verify, not confirmations. Only your IP touches UserSherlock.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running but dated username-checker; no transparency about how/when it probes each site, and it returned a server error during verification. Reliability is inconsistent — corroborate with a maintained tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- User Sherlock
- usersherlock.com
tags:
- username
- username-enumeration
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- user-sherlock
---

# UserSherlock

> A veteran browser-based username checker that reports which of ~20+ popular sites have an account under a given handle.

## When to use
You have a `username` and want a fast, install-free first look at where that handle exists across common social and web services. It is best as a quick breadth pass to generate candidate profiles; because it is an older tool with an opaque and sometimes flaky backend, treat it as a lead generator rather than an authoritative enumeration, and always confirm the hits.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.usersherlock.com/usersearch (if it returns a 5xx error, retry later — the service is intermittently down).
2. Enter the `username` and run the search.
3. Read the results: a list of supported sites with links to accounts found under the handle. Open each reported link and confirm the profile actually exists and matches your subject.
4. Pivot: confirmed profiles feed platform-specific enrichment; a matching display `name` on a profile becomes a new selector; run the same handle through a maintained cross-site tool to fill the gaps UserSherlock misses.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` links across popular sites, candidate `name` from matched profiles
- **Empty/negative result looks like:** no matches, a timeout, or a server error — none of these prove the handle is unused; the tool's site coverage is narrow and its checks unreliable.

## Gotchas & OpSec
- **Degraded:** the endpoint returned an HTTP 503 during verification and its site list is dated; false negatives (and stale false positives) are likely. Do not treat its output as complete.
- Always click through and verify each reported account — automated username checkers commonly report a "hit" for sites that show a placeholder for any handle.
- Passive toward the target; only your IP is exposed to the service.

## Overlaps ("do both")
- Pairs with a maintained cross-site username tool (e.g. the modern Sherlock project or WhatsMyName-style checkers) — run both, because UserSherlock's small, dated site list will miss platforms a current tool covers.

## Trust & verifiability
`trust: unverified` — an old service with no documentation of its probing method and demonstrated availability problems. Useful only as a supplementary lead source; never rely on it alone for presence or absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usersherlock-com |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
