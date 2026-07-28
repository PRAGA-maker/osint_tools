---
id: onlysearch-co
name: Onlysearch.co
description: Use when you have a `name`/`username` or physical traits and want to find a subject's OnlyFans presence — returns matching creator `social-profile`s.
url: https://onlysearch.co/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating OnlyFans creator profiles by keyword, location or physical description.
selectorsIn:
- username
- name
- geolocation
- physical-description
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search; the site monetises via paid promotion/placement for creators.
opsec: passive
opsecNote: Passive keyword search against the site's own index — you never contact the creator. Results and the platform are adult-content; keep queries in a puppet browser and be mindful of the sensitivity/legal context around any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party aggregator not affiliated with OnlyFans; index completeness and result accuracy are unverified, and paid placement can skew rankings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OnlySearch
- onlysearch.co
tags:
- adult-content
- creator-search
- social-search
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Onlysearch.co

> A third-party search engine for OnlyFans creators — find profiles by keyword, location, or physical attributes when a subject may have an adult-content presence.

## When to use
You suspect a subject maintains an OnlyFans account and want to locate it from a `username`, display `name`, `geolocation`, or `physical-description`. OnlyFans has no public search of its own, so an external index like OnlySearch is one of the few ways to surface a creator profile that then corroborates identity, location, or online activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlysearch.co/ in a puppet browser.
2. Enter a keyword/`username`/`name`, and narrow with filters — location (US state / country), gender, age range, body type, ethnicity, price, and "free"/"new" flags.
3. Browse the returned creator cards; open a match to read its public bio/handle.
4. Pivot: take the confirmed OnlyFans `username`/handle and run it through username-enumeration and cross-platform tools to link other accounts.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation`, `physical-description` (via filters)
- **Out:** OnlyFans creator `social-profile`s (handle, public bio, stated location)
- **Empty/negative result looks like:** no cards returned, or only loosely-related creators — absence does not prove the subject has no account, since the index is incomplete.

## Gotchas & OpSec
- Not affiliated with OnlyFans; coverage is partial and paid placement can push promoted creators to the top, so ranking ≠ relevance.
- Adult-content platform — handle with care regarding the subject's privacy, consent, and any legal constraints; never treat inferred identity as confirmed without corroboration.
- Self-reported bio fields (location, age) are unverified marketing text.

## Overlaps ("do both")
- Pairs with username-enumeration tools — OnlySearch surfaces the OnlyFans handle, and those tools test that handle across other platforms to build the wider profile.

## Trust & verifiability
`trust: unverified` — an independent aggregator with no disclosed methodology; use hits strictly as leads and confirm the person via an independent selector before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlysearch-co |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation, physical-description → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
