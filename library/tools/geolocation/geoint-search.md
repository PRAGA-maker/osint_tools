---
id: geoint-search
name: GeoINT Search
description: Use when you have a place name/`geolocation` clue and want to search a curated set of geospatial/OSINT sources at once — returns geolocation references via a Google Programmable Search Engine.
url: https://cse.google.com/cse?cx=015328649639895072395:sbv3zyxzmji#gsc.tab=0
category: geolocation
path:
- geolocation
bestFor: Querying a pre-scoped Google Custom Search Engine focused on geolocation/GEOINT resources for place identification and imagery leads.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free hosted Google Programmable Search Engine; no account required.
opsec: passive
opsecNote: Queries hit Google's Programmable Search infrastructure like a normal Google search — passive toward any target. Use a sock-puppet Google session/IP if you want the query untied to you; Google logs the search.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured GEOINT-themed Google CSE; its exact source list is not visible and coverage depends on the unknown creator's scope, which may drift over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GEOINT CSE
tags:
- google-cse
- geolocation
- geoint
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# GeoINT Search

> A hosted Google Programmable Search Engine scoped toward geospatial/GEOINT resources — one query hits a curated slice of mapping, imagery and location sources instead of the whole web.

## When to use
You are geolocating a photo or resolving a place and have a `geolocation`/`address` clue — a place name, landmark, coordinates, or descriptive detail — and want to search across a curated set of GEOINT-oriented sites (mapping tools, imagery archives, place databases) in one shot rather than querying each individually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE: https://cse.google.com/cse?cx=015328649639895072395:sbv3zyxzmji#gsc.tab=0
2. Enter your location clue — a place name, landmark, feature description, or partial address.
3. Review results, which lean toward geospatial/GEOINT sources; open promising hits for maps, imagery, or place records.
4. Refine with additional distinctive terms visible in your reference photo (signage text, business names, unusual features).
5. Pivot: a candidate location feeds satellite/street-view confirmation and mapping tools for a definitive `geolocation`.

## Inputs → Outputs
- **In:** `geolocation`/`address` clue (place name, landmark, coordinates, description)
- **Out:** `geolocation` references and `image`/map leads from the CSE's scoped GEOINT sources
- **Empty/negative result looks like:** no relevant hits — the clue isn't covered by this CSE's scope, not that the place is unfindable. Fall back to full-web and dedicated mapping tools.

## Gotchas & OpSec
- The site list behind the CSE is opaque and may change silently; a null result is never authoritative.
- Google may present a CAPTCHA on repeated queries — solve it manually.
- OpSec: passive, but tied to your Google session — use a sock puppet if attribution matters.

## Overlaps ("do both")
- Pairs with dedicated satellite/street-view and reverse-image geolocation tools — this surfaces candidate sources broadly, while those confirm the exact spot.

## Trust & verifiability
`trust: community` — a genuine Google search product configured by an unknown third party; the Google index is reliable, but the GEOINT scope selection cannot be independently verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoint-search |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
