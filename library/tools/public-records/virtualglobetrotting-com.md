---
id: virtualglobetrotting-com
name: VirtualGlobetrotting.com
description: Use when you have a `name` or place and want user-submitted satellite/street-view locations — returns pinpointed `address`es/coordinates for celebrity homes, landmarks, and notable sites.
url: https://virtualglobetrotting.com/
category: public-records
path:
- public-records
bestFor: Finding the exact map location (satellite + street view) of a named person's home or a notable place that the community has already geolocated.
selectorsIn:
- name
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to browse and search; free account only needed to submit your own locations.
opsec: passive
opsecNote: You browse a third-party community site — nothing is sent to the person whose location is pinned. The imagery is standard Google/Bing map data, so viewing it does not alert anyone; still, treat located home addresses as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: User-generated database — locations are crowd-submitted and voted on, not authoritative. A "celebrity home" pin may be wrong, outdated, or a former residence; corroborate before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- virtual-globe-trotting
aliases:
- Virtual Globetrotting
tags:
- property
- geolocation
- satellite-imagery
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# VirtualGlobetrotting.com

> A crowd-sourced atlas of interesting map locations — celebrity homes, landmarks, military sites, filming locations — each pinned to satellite/street-view imagery and searchable by name.

## When to use
You have a `name` (often a public figure) or a place and want a specific map location the community has already found and pinned. For a well-known person, someone may have submitted their house with exact coordinates and imagery — instantly giving you an `address`/`geolocation` to corroborate against property and people-search records. Also useful for identifying a landmark or notable site from a description, or reverse-checking whether an address matches a claimed "celebrity home."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://virtualglobetrotting.com/ and search by the person's `name`, a place name, or a category (celebrity homes, landmarks, etc.).
2. Open a matching entry — it shows the pinned location on Google/Bing satellite (and often Street View) with coordinates and a description.
3. Note the coordinates/address and read the comments/votes, which often debate accuracy or note "former home."
4. Cross-check the pin against property records, mapping tools, and Street View to confirm it's current and correct.
5. Pivot: a confirmed `address`/`geolocation` → property/parcel records, neighbor and people search, and further map analysis.

## Inputs → Outputs
- **In:** `name` (person/place) or `address`/category
- **Out:** pinned `address`/`geolocation`, satellite & street-view imagery, community notes
- **Empty/negative result looks like:** no entries for the name/place — no one has submitted it; absence tells you nothing about where the person actually lives.

## Gotchas & OpSec
- Crowd-sourced and unverified: pins can be wrong, guessed, or former addresses — always corroborate with authoritative records before acting.
- Coverage skews to celebrities, landmarks, and oddities; ordinary private individuals are rarely present.
- Passive to view (standard map imagery), but a located home is sensitive personal data — handle accordingly.

## Overlaps ("do both")
- Pairs with `[[virtual-globe-trotting]]` and mapping/property tools — use this to get a candidate location, then authoritative records and live Street View to verify it's current.

## Trust & verifiability
`trust: unverified` — an entirely user-generated, vote-driven database with no editorial verification; treat every pin as a lead to confirm against primary property/mapping sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | virtualglobetrotting-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
