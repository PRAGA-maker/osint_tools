---
id: newspapermap
name: NewspaperMap
description: Use when you have a `geolocation` (a place a subject is tied to) and want the local newspapers covering it — returns links to those papers (10,000+ worldwide) plotted on a map, with translation.
url: https://newspapermap.com/
category: communities-forums
path:
- communities-forums
bestFor: Finding the local/regional newspapers for a place so you can search their archives for coverage of a person or event.
selectorsIn:
- geolocation
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to browse; no account. Translation is handled via an embedded translate feature.
opsec: passive
opsecNote: You browse a public map of newspaper links; nothing about your subject is disclosed. Fully passive. (Searching the papers themselves happens on their sites, with their own logging.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community map of newspaper locations; the map is a directory of links, so accuracy of any given paper's URL should be spot-checked but the concept is sound and still maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Newspaper Map
- newspapermap.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- newspaper-map
---

# NewspaperMap

> A world map of 10,000+ newspapers — find the local press for any place, then search it for coverage of your subject.

## When to use
You have a `geolocation` — the town/region where a person went missing, was last seen, lived, or grew up — and you want to know which local and regional newspapers cover that area. Local papers frequently carry the details national outlets skip: appeals, obituaries, court notices, community reports. NewspaperMap turns "where" into "which papers to read."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://newspapermap.com/ and navigate/zoom the map to the target area (or search a place/language).
2. Click the markers to get each newspaper's name, language, and website link.
3. Note the language; use the built-in translate option for non-native papers.
4. Go to each paper's site and search its archive for the subject's name, the event, or the location.
5. Pivot: coverage found there feeds a timeline; named local officials/witnesses become new `name`/`associate` leads.

## Inputs → Outputs
- **In:** `geolocation` (place/region)
- **Out:** links (`domain`s) to local/regional newspapers for that area, with language and map position
- **Empty/negative result looks like:** sparse markers for rural or under-covered regions, or a marker whose link is dead — the directory can lag; confirm the paper still exists before assuming no local press.

## Gotchas & OpSec
- Human-in-the-loop: none for the map; the papers themselves may have paywalls or their own search quirks.
- It's a *directory of links*, not a search engine — it points you to papers; you still run the name search on each one.
- Link rot: some listed papers have moved or closed; verify the outlet independently.

## Overlaps ("do both")
- Pairs with a news-archive search (e.g. Google News, a country's press archive) — NewspaperMap tells you *which* local papers exist for a place; an archive search then queries their content for your subject.

## Trust & verifiability
`trust: community` — a community-maintained directory that's still active and widely cited; treat individual links as leads to verify, and rely on the actual newspaper as the source of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newspapermap |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
