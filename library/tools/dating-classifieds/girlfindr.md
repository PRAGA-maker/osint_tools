---
id: girlfindr
name: GirlFindr
description: Use when you have a `name`/`username` or traits and want a subject's OnlyFans presence — returns matching creator `social-profile`s linking to official pages.
url: https://girlfindr.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding OnlyFans creator profiles by keyword, location, or category.
selectorsIn:
- name
- username
- geolocation
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search without an account; monetised via affiliate links to creators' OnlyFans pages.
opsec: passive
opsecNote: Passive keyword search against the site's index — the creator is never contacted. Adult-content platform; use a puppet browser and handle any subject's identity, consent, and legal context with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator unaffiliated with OnlyFans; index completeness is unknown and listings are affiliate-driven, so results are leads, not confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlysearch-co
- secretfans
aliases:
- girlfindr.com
tags:
- onlyfans
- creator-search
- adult
source: osintambition-social
lastVerified: '2026-07-28'
enrichment: full
---

# GirlFindr

> A third-party OnlyFans discovery engine — indexes public creator profiles by category, location, and keyword and links out to their official pages.

## When to use
You suspect a subject has an OnlyFans account and want to locate it from a `name`, `username`, or location/attribute filters. OnlyFans has no public search, so external indexes like GirlFindr are one of the few routes to a creator profile that can corroborate identity, location, or online activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://girlfindr.com/ in a puppet browser (no account needed).
2. Search by keyword/`name`/`username`, or browse by location/category; filter by country, attributes, age range.
3. Open a matching listing; it links to the creator's official OnlyFans page for confirmation.
4. Pivot: take the confirmed OnlyFans `username` and run username-enumeration and cross-platform tools to link other accounts.

## Inputs → Outputs
- **In:** `name`, `username`, or `geolocation` (via filters)
- **Out:** OnlyFans creator `social-profile`s (handle, description, link to official page)
- **Empty/negative result looks like:** no listings or only loosely-related creators — the index is partial, so absence never proves the subject has no account; a match is a claim until verified on OnlyFans.

## Gotchas & OpSec
- Not affiliated with OnlyFans; coverage is incomplete and listings are affiliate-driven (bias toward creators who convert).
- Adult-content context — be careful with privacy, consent, legality, and misidentification; corroborate before concluding.
- Descriptions/attributes are self-reported marketing text, unverified.

## Overlaps ("do both")
- Pairs with [[onlysearch-co]] and [[secretfans]] — the OnlyFans indexes have different coverage, so search all three, then verify any handle on OnlyFans and across platforms.

## Trust & verifiability
`trust: unverified` — an independent affiliate-driven aggregator with no disclosed methodology; use hits strictly as leads and confirm the person via an independent selector.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | girlfindr |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, geolocation → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
