---
id: wikishire-united-kingdom
name: Wikishire (UK & Ireland gazetteer)
description: Use when you have a British/Irish place name and want to resolve it geographically — returns county, coordinates, and local geographic context.
url: http://wikishire.co.uk/wiki/Main_Page
category: search-engines
path:
- search-engines
bestFor: Resolving and disambiguating British and Irish place names to their historic county, location, and geography.
selectorsIn:
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free, openly editable MediaWiki gazetteer; no account needed to read.
opsec: passive
opsecNote: Read-only reference lookup with no per-subject query; ordinary web browsing. No login or footprint concerns beyond standard logging.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced MediaWiki gazetteer (~36k articles) organised by historic counties; community-edited, so treat details as reference-grade, not authoritative.
missingPersonsRelevance: medium
coverage:
- gb
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wikishire
- wikishire.co.uk
tags:
- toddington
- curated-directory
- specialty-search
- gazetteer
- geography
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Wikishire (UK & Ireland gazetteer)

> A crowdsourced gazetteer of Britain and Ireland organised by historic county — the tool for turning an obscure village, hamlet, or place name into a location and geographic context.

## When to use
You have an `address` fragment or place name from Britain or Ireland — a village, parish, estate, or historic place — that a generic map does not cleanly resolve, and you need to know which county it sits in, roughly where, and what surrounds it. Because Wikishire is organised by traditional counties and includes an interactive map plus KML/postcode resources, it is useful for disambiguating same-named places and grounding a UK/Irish `geolocation` lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://wikishire.co.uk/wiki/Main_Page.
2. Search the place name in the wiki search box, or browse via the county lists or the interactive map of the British Isles.
3. Read the article for the historic county, location description, nearby settlements, and any coordinates or map links.
4. Use the site's GIS resources (KML files, postcode lookup) to convert the place into precise `geolocation`.
5. Pivot: the resolved county/coordinates narrow searches on UK electoral, property, and public-records tools; nearby-settlement context helps interpret a witness or last-seen location.

## Inputs → Outputs
- **In:** `address` / place name (UK or Ireland)
- **Out:** `geolocation` (county, area, coordinates/KML), local geographic `address` context
- **Empty/negative result looks like:** no article for the place — the name may be too minor, misspelled, or outside GB/Ireland. Try an alternate spelling or a national mapping source before concluding it does not exist.

## Gotchas & OpSec
- Coverage is Britain and Ireland only, and organised by historic (not modern administrative) counties, which can differ from postal counties.
- Being community-edited, coordinates and details are reference-grade; verify a precise location against Ordnance Survey / an authoritative map before acting on it.

## Overlaps ("do both")
- Pairs with national mapping and postcode tools — Wikishire disambiguates and gives historic-county context, while OS/postcode services give the authoritative modern coordinates.

## Trust & verifiability
`trust: community` — a genuine crowdsourced gazetteer useful for orientation and disambiguation; because anyone can edit it, confirm exact coordinates with an authoritative geographic source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikishire-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
