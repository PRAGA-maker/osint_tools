---
id: wikipedia-list-of-online-mapping-programs-worldwide
name: Wikipedia — List of Online Map Services
description: Use when you have a `geolocation`/`address` in a specific country and want the right regional map/imagery service for it — routes you to local mapping tools.
url: https://en.wikipedia.org/wiki/List_of_online_map_services
category: geolocation
path:
- geolocation
bestFor: A maintained reference index of global and country-specific online map/imagery services, for picking the best mapping tool for a given region.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free Wikipedia reference article; the map services it lists have their own (often free) access terms.
opsec: passive
opsecNote: Reading a Wikipedia list is passive and leaks nothing. OpSec considerations belong to the destination map service you choose (e.g. don't sign into a personal account on an imagery site while working a case).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Community-maintained Wikipedia article; it is an index, so authority rests with the individual map services it points to.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- List of online map services
- online mapping programs worldwide
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Wikipedia — List of Online Map Services

> A maintained catalogue of map and imagery services — global platforms plus the country-specific tools that beat Google in their home region.

## When to use
You have a `geolocation` or `address` in a particular country and the mainstream platforms (Google/Apple Maps) give thin coverage there. This article lists the regional services that often have better local imagery, street-level, or address data — Yandex (Russia/CIS), Baidu (China), MapmyIndia (India), Kartverket (Norway), and so on — so you pick the right tool before chasing detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Wikipedia list.
2. Find the section for your target region (global services first, then per-country/regional).
3. Pick a service with strong coverage there and follow the link to it.
4. In that service, work your `geolocation`/`address`: verify a location, read local labels, or pull higher-resolution imagery than a global provider offers.
5. Pivot: corroborate a geolocation across two independent providers (e.g. Google + Yandex) to reduce false positives.

## Inputs → Outputs
- **In:** `geolocation` / `address` (and a target country)
- **Out:** the right regional mapping/imagery service to resolve or verify that `geolocation` / `address`
- **Empty/negative result looks like:** no listed service for an obscure territory — fall back to global OpenStreetMap/Google. The list itself is a directory; it never "fails to find a person," it just points you to tools.

## Gotchas & OpSec
- It is a reference index, not a search tool — you still do the mapping work in the destination service.
- Wikipedia lists can lag; a listed service may have changed access terms, and new regional tools may be missing.
- OpSec: reading the list is passive; apply OpSec at the map service you use.

## Overlaps ("do both")
- Pairs with reverse-image/geolocation engines (Yandex imagery, Google Lens) and with OpenStreetMap-based tools — this tells you *which* map to open; those do the actual place-matching.

## Trust & verifiability
`trust: trusted` — a stable, community-maintained Wikipedia index; verify each linked service's current coverage at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikipedia-list-of-online-mapping-programs-worldwide |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
