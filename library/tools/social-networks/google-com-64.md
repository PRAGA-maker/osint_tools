---
id: google-com-64
name: Google site-search for XING
description: Use when you have a `name` or `username` of a German-speaking professional and want their XING profile — returns XING (the German-speaking LinkedIn) profiles Google has indexed via a `site:xing.com` dork.
url: https://www.google.com/search?q=site%3Axing.com
category: social-networks
path:
- social-networks
bestFor: Finding a subject's professional profile on XING (DACH region) through Google's index, without logging into XING.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- name
status: live
pricing: free
costNote: Free; plain Google web search with a site: operator. No account needed.
opsec: passive
opsecNote: Queries hit Google, not XING, so the subject is not notified and you avoid XING's "who viewed your profile" logging (XING, like LinkedIn, surfaces profile visitors). Google logs your searches — use a sock-puppet/logged-out browser. Clicking into XING itself is a more exposing step; consider a sock-puppet XING account or Google's cache.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Google web search with a site: operator — a first-party engine indexing public XING profile pages. Reliability is bounded by Google's crawl coverage of XING.
missingPersonsRelevance: high
coverage:
- de
- at
- ch
auth: none
api: false
localInstall: false
registration: false
aliases:
- XING Google dork
- site:xing.com search
tags:
- linkedin
- LinkedIn & Similar Sites
- xing
- google-dork
- dach
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Google site-search for XING

> A Google dork (`site:xing.com …`) that surfaces public XING profiles — the professional network for the German-speaking (DACH) world — without touching XING's own login-gated, visitor-logging search.

## When to use
Your subject is a professional in Germany, Austria or Switzerland and may be on XING (the regional equivalent of LinkedIn) rather than, or in addition to, LinkedIn. Query Google's index for their profile to get employer, role and career history — the standard employment/identity pivot for DACH subjects — while avoiding XING's own search and its "who viewed your profile" exposure.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out/sock-puppet browser, run a Google search scoped with `site:xing.com`.
2. Narrow it: `site:xing.com "Full Name"` or `site:xing.com <city/employer>` to disambiguate.
3. Read titles/snippets — Google caches the profile's name, current role and employer, often visible without opening XING.
4. Open XING only when needed (more exposing; may hit a login wall) — or use Google's cached copy.
5. Pivot: employer (`employer-org`) and role feed company-registry and news searches; the profile corroborates identity; a photo feeds reverse-image/face tools.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** XING `social-profile`, `employer-org`/role, confirmed `name`
- **Empty/negative result looks like:** no `site:xing.com` hits — the subject isn't on XING, has a private/closed profile, or uses LinkedIn instead. Absence in Google isn't conclusive; also try LinkedIn and Bing with the same operator.

## Gotchas & OpSec
- Google's XING coverage is partial and XING has tightened public visibility over time — a live profile may not be indexed.
- XING logs profile visitors (like LinkedIn) — prefer Google's cache/snippet; if you must open XING, use a sock-puppet.
- Focus is DACH/German-language; a non-DACH subject likely isn't here.

## Overlaps ("do both")
- Pairs with LinkedIn search, `[[google-com-53]]`-style dorks and DACH company registries — XING and LinkedIn cover overlapping-but-different professionals, so run both for a DACH subject.

## Trust & verifiability
`trust: trusted` — plain Google search; the mechanism is sound and first-party. The caveat is XING's declining public index coverage, not data authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-64 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
