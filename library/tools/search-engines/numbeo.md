---
id: numbeo
name: Numbeo
description: Use when you have a `geolocation` (city/country) and want crowd-sourced living-conditions data for it — returns cost-of-living, crime, healthcare and quality-of-life context as `geolocation` intelligence.
url: http://www.numbeo.com/common/
category: search-engines
path:
- search-engines
bestFor: Getting a quick, city-level read on cost of living, crime perception, healthcare and quality of life for a location tied to a case.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse; user-contributed database with optional paid data/API products for businesses. No account needed to read.
opsec: passive
opsecNote: You look up a place, not a person; nothing about a subject is submitted and no one is alerted. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The world's largest crowd-sourced cost-of-living database; figures are user-contributed estimates, useful for context and comparison rather than precise fact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- numbeo.com
tags:
- toddington
- curated-directory
- specialty-search
- cost-of-living
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Numbeo

> The largest crowd-sourced database of living-conditions data — cost of living, crime perception, healthcare, traffic and pollution — indexed by city and country.

## When to use
You have a `geolocation` — a city or country connected to a case — and want quick context about what life there is like: how expensive it is, the perceived crime level, healthcare quality, and general quality-of-life indices. It is background/context intelligence for understanding a location, not a way to find or identify a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.numbeo.com/ .
2. Search for a city (or country) and open its page.
3. Browse the sections: cost of living, property prices, crime, health care, traffic, pollution and quality-of-life indices; use the compare feature to contrast two cities.
4. Read the output: crowd-sourced index values and estimates for the `geolocation`.
5. Pivot: use the crime/cost picture to inform assumptions about a location; combine with mapping and local-news tools for a fuller picture.

## Inputs → Outputs
- **In:** `geolocation` (city / country)
- **Out:** `geolocation` context (cost-of-living, crime, healthcare, quality-of-life indices)
- **Empty/negative result looks like:** small or rarely-visited cities may have thin or no data (few contributors) — treat sparse pages as low-confidence.

## Gotchas & OpSec
- Data is user-contributed and self-selected, so figures are indicative estimates, not official statistics — good for comparison, not for precise claims.
- Crime numbers reflect resident *perception*, not police records; use official crime data where accuracy matters.
- OpSec: passive; you query a place, never a person.

## Overlaps ("do both")
- Complements official statistics portals and mapping tools: Numbeo gives a fast crowd-sourced snapshot, which you then verify against authoritative local sources.

## Trust & verifiability
`trust: community` — a large crowd-sourced dataset. Reliable as a comparative overview; individual figures should be corroborated against official sources before being treated as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numbeo |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
