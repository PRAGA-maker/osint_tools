---
id: secretfans
name: SecretFans
description: Use when you have a `name`/`username` or traits and want a subject's OnlyFans presence — returns matching creator `social-profile`s.
url: https://secretfans.net/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding OnlyFans creator profiles by keyword, niche, location, or popularity.
selectorsIn:
- name
- username
- geolocation
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free for searchers; creators can list free, with paid featured/top placement (so ranking is partly paid).
opsec: passive
opsecNote: Passive keyword search against the site's index — the creator is never contacted. Adult-content platform; use a puppet browser and handle any subject's identity/consent/legal context with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator not affiliated with OnlyFans; index completeness is unknown and paid placement skews rankings, so results are leads, not confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlysearch-co
aliases:
- secretfans.net
tags:
- onlyfans
- creator-search
- adult
source: osintambition-social
lastVerified: '2026-07-28'
enrichment: full
---

# SecretFans

> A third-party search engine for OnlyFans creators — filter by niche, price, location, and popularity to surface a profile when a subject may have an adult-content presence.

## When to use
You suspect a subject maintains an OnlyFans account and want to locate it from a `name`, `username`, or physical/location filters. OnlyFans has no public search, so an external index like SecretFans is one of the few routes to a creator profile that can corroborate identity, location, or online activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://secretfans.net/ in a puppet browser.
2. Search by keyword/`name`/`username`, and narrow with filters — niche, price, location (`geolocation`), content type, popularity.
3. Open a matching profile card; read the public bio/handle and linked creator page.
4. Pivot: take the confirmed OnlyFans `username` and run username-enumeration and cross-platform tools to link other accounts.

## Inputs → Outputs
- **In:** `name`, `username`, or `geolocation` (via filters)
- **Out:** OnlyFans creator `social-profile`s (handle, public bio, stated location)
- **Empty/negative result looks like:** no cards, or only loosely-related creators — the index is partial, so absence never proves the subject has no account; a match is a claim until verified on OnlyFans.

## Gotchas & OpSec
- Not affiliated with OnlyFans; coverage is incomplete and paid placement pushes promoted creators up — ranking ≠ relevance.
- Adult-content context — be careful with privacy, consent, legality, and the possibility of misidentification; corroborate before concluding.
- Bio fields (location, age) are self-reported marketing text, unverified.

## Overlaps ("do both")
- Pairs with [[onlysearch-co]] and username-enumeration tools — the two OnlyFans indexes have different coverage, so search both, then verify any handle across platforms.

## Trust & verifiability
`trust: unverified` — an independent aggregator with no disclosed methodology and paid-placement bias; use hits strictly as leads and confirm the person via an independent selector.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | secretfans |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, geolocation → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
