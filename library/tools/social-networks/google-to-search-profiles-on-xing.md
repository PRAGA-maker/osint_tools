---
id: google-to-search-profiles-on-xing
name: Google to search profiles on Xing
description: Use when you have a `name`/role in the German-speaking business world and want their Xing profile — builds a Google X-ray query that returns Xing `social-profile`s and `employer-org` detail.
url: https://recruitin.net/xing.php
category: social-networks
path:
- social-networks
bestFor: Building targeted Google X-ray searches for Xing (DACH-region professional network) profiles by name, role, company, or location.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free query-builder (recruitin.net); it just constructs a Google search — no account. Xing itself gates full profile detail behind login/membership.
opsec: passive
opsecNote: The builder runs no search itself; the resulting Google query is a normal web search that doesn't touch Xing directly. Clicking into a Xing profile may require login and can leave a footprint on Xing — do that from a sock-puppet Xing account, not your real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple, reliable Google dork generator (recruiter tool); its usefulness depends on Google's index of public Xing pages, which is partial.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-to-search-profiles-on-dribbble
- the-dots
aliases:
- recruitin Xing
- Xing X-ray search
tags:
- xing
- google-dork
- recruiter
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Google to search profiles on Xing

> A one-page query-builder that assembles a Google X-ray search for Xing — the German-speaking world's professional network — so you can find a subject's work profile by name, role, company, or location.

## When to use
Your subject is in Germany, Austria, or Switzerland (or works for a DACH company) and likely has a Xing profile — the region's LinkedIn equivalent. Because Xing's own search is login-gated and clunky, X-raying it via Google surfaces public profile pages more freely, revealing role, employer (`employer-org`), and career detail to corroborate a professional identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://recruitin.net/xing.php.
2. Fill in what you know — `name`, job title, company (`employer-org`), location, keywords.
3. The tool builds a Google query (site:xing.com plus your terms); run it.
4. Review the Google results for matching Xing `social-profile`s; open the most likely.
5. Pivot: full profile detail may need a (sock-puppet) Xing login; corroborate role/employer against LinkedIn and company sources.

## Inputs → Outputs
- **In:** `name`, job title, `employer-org`, location/keywords
- **Out:** Xing `social-profile`s and visible `employer-org`/role detail (via Google)
- **Empty/negative result looks like:** few/no Google hits — the subject may have a locked-down or unindexed Xing profile, or none; try LinkedIn and name variants.

## Gotchas & OpSec
- Relies on Google's (partial) index of public Xing pages — it won't reach login-only profile detail.
- Xing membership is DACH-concentrated; for other regions LinkedIn is the better target.
- OpSec: passive to build/search; opening a profile on Xing may require login and leave a footprint — sock puppet only.

## Overlaps ("do both")
- Part of the recruitin.net X-ray family alongside `[[google-to-search-profiles-on-dribbble]]`; pair with `[[the-dots]]` and LinkedIn searches to triangulate a professional identity.

## Trust & verifiability
`trust: community` — a dependable dork generator; the trust caveat is Google's incomplete Xing coverage, not the tool. Confirm role/employer on the actual profile and a second professional source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-to-search-profiles-on-xing |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
