---
id: onlyfinder-com
name: onlyfinder.com
description: Use when you have a `username`, `name`, or `geolocation` and want to find a matching OnlyFans creator — returns creator profiles, handles, and an approximate-location map.
url: https://onlyfinder.com/map/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching for an OnlyFans creator by username/name, or browsing creators by approximate location on a map.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free search of the creator index; some features/deeper results are gated behind a paid tier.
opsec: passive
opsecNote: Searches a third-party index of public OnlyFans creator pages; you don't interact with the creator and they aren't notified. Passive. Given the sensitive/adult nature, keep queries in a sock-puppet browser and handle any findings with care for the subject's privacy and safety.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party search engine that indexes public OnlyFans profile data and self-reported creator locations; not affiliated with OnlyFans, and location data is approximate/self-declared.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlyfinder
- social-searcher
aliases:
- OnlyFinder
- onlyfinder map
tags:
- onlyfans
- OnlyFans Related Sites
- adult
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# onlyfinder.com

> A search engine for OnlyFans creators — look up a handle/name or browse a map of creators by their (self-declared, approximate) location.

## When to use
You suspect a subject has an OnlyFans presence and you have a `username`, `name`, or a rough `geolocation`. OnlyFinder indexes public OnlyFans creator pages so you can search for a matching creator or, via its map, see creators clustered by their stated location. In a missing-persons context this can surface an income source, an active online presence (a signal the person is alive/active), or contactable accounts — always handled with care given the adult and privacy-sensitive nature.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://onlyfinder.com/ (search) or /map/ (location browse), ideally in a sock-puppet browser.
2. Search by username or name; or open the map and zoom to a region to see creators who set that location.
3. Review candidate profiles — display name, handle, bio, and any linked socials.
4. Corroborate identity carefully: reused usernames/photos/bio text linking to known accounts, not location alone (locations are self-set and often false).
5. Pivot: a confirmed handle → cross-platform username search and `[[social-searcher]]`; linked socials → the person's wider footprint.

## Inputs → Outputs
- **In:** `username`, `name`, or approximate `geolocation`
- **Out:** OnlyFans creator `social-profile`(s), handle, bio, self-declared `geolocation`
- **Empty/negative result looks like:** no matching creator — the person has no OnlyFans (or a very private one), uses a different handle, or isn't indexed; a null is weak evidence, and map locations are unreliable.

## Gotchas & OpSec
- Locations are self-declared and frequently fake (creators mask their real city) — never treat the map pin as a real address.
- Adult/sensitive context: protect the subject's privacy, avoid engaging, and consider legal/ethical limits, especially in a welfare case.
- Freemium: some results/features need payment; the free tier may under-report.
- Identity confirmation must rest on corroborating signals (reused handle/photos/links), not a name or location match alone.

## Overlaps ("do both")
- Pairs with `[[social-searcher]]` and cross-platform username tools — confirm a handle here, then trace it across other networks.

## Trust & verifiability
`trust: community` — an unaffiliated third-party index of public OnlyFans data. Profile existence is checkable directly on OnlyFans; treat self-declared location and any inferred identity as leads needing corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlyfinder-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
