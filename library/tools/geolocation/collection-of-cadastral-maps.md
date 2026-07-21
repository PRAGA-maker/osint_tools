---
id: collection-of-cadastral-maps
name: Collection of cadastral maps
description: Use when you have an `address` or `geolocation` in a specific country and want the official land-registry/cadastral portal that maps parcels and ownership — returns a jumping-off link, not data directly.
url: https://cipher387.github.io/collection_of_cadastral_maps/
category: geolocation
path:
- geolocation
bestFor: Finding the right national cadastral/land-registry map portal for a given country before pivoting to property/owner lookups.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: degraded
pricing: freemium
costNote: The directory itself is free; individual country cadastres it links to vary — some are free, some flag "(r)" registration or "($)" paid access.
opsec: passive
opsecNote: Browsing the cipher387 index leaks nothing about your target. OpSec risk begins on the downstream cadastre — some national portals log searches or require login; treat each linked site on its own terms and use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained GitHub Pages index by cipher387 (cyb_detective), a well-known OSINT curator; carries a self-disclosed "no longer being updated" notice.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cipher387 cadastral maps
- cadastral maps directory
tags:
- Maps, Geolocation and Transport
- property-records
- cadastre
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Collection of cadastral maps

> A country-indexed directory pointing to official cadastral/land-registry map portals in ~41 countries — a router, not a database.

## When to use
You have an `address` or approximate `geolocation` in a particular country and want to inspect the official parcel map — boundaries, plot numbers, and sometimes registered owner — but you don't know which national cadastre to open. This index maps "country → cadastral portal" so you skip the guesswork and land on the authoritative source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/collection_of_cadastral_maps/.
2. Scroll to your target country (entries are alphabetical by nation).
3. Note the access flags: `(r)` means the linked cadastre needs registration, `($)` means it charges for full records.
4. Click through to the national portal and search by the parcel/address there.
5. Pivot: a parcel record can yield an owner `name` or a corroborating `address`; feed that to people-search or public-records tools.

## Inputs → Outputs
- **In:** `geolocation` / `address` (plus the country context)
- **Out:** a link to the relevant national cadastral map (which downstream may yield parcel `geolocation`, owner `address`/`name`)
- **Empty/negative result looks like:** the country simply isn't listed (only ~41 covered) — that's a gap in this index, not proof no cadastre exists. Fall back to the Worldwide OSINT Tools Map, which the page itself recommends.

## Gotchas & OpSec
- The maintainer flags the list as "no longer being updated," so some links may have moved — verify the destination is the current official cadastre before trusting it (`status: degraded` for that reason).
- Human-in-the-loop: none for the index; downstream cadastres may impose CAPTCHAs, logins, or fees.
- OpSec: passive at the index level; the real leakage risk lives on the national portal you click into.

## Overlaps ("do both")
- Pairs with broader geolocation map collections and property-record tools — this one only routes you to the correct cadastre; another tool does the actual parcel-to-owner resolution.

## Trust & verifiability
`trust: community` — curated by cipher387 (cyb_detective), a reputable OSINT list-maker, but it is a static community index with a stale-content warning; always confirm the linked cadastre is live and official.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | collection-of-cadastral-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
