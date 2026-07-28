---
id: unogs-com
name: Unogs.com
description: Use when you need to know which countries a Netflix title streams in — returns per-country catalog availability (a region-verification aid, not person data).
url: http://unogs.com/
category: communities-forums
path:
- communities-forums
bestFor: Checking the Netflix global catalog — which titles are available in which countries.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web search; a paid uNoGS API is offered via RapidAPI for developers.
opsec: passive
opsecNote: Passive lookup against uNoGS's own scraped catalog — no target interaction. It concerns content availability by region, not individuals, so effectively no personal-privacy exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An unofficial, community-maintained scrape of Netflix's catalog; coverage is acknowledged as incomplete (Netflix anti-scraping), so treat availability data as indicative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- uNoGS
- unofficial Netflix Global Search
tags:
- Movies
- Netflix
- streaming-availability
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Unogs.com

> The unofficial Netflix Global Search — a searchable, community-maintained index of which Netflix titles stream in which countries.

## When to use
A niche corroboration tool: when a claim or piece of content hinges on Netflix regional availability — verifying whether someone could plausibly have watched a title in a stated country, or checking which regions carry a title referenced in an investigation — uNoGS maps the catalog by country. It is a content/region tool, not a people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://unogs.com/ and use the advanced search.
2. Search a title and/or filter by country, genre, year, rating.
3. Read the per-country availability for each title (`geolocation` of where it streams).
4. For automation, use the uNoGS API via RapidAPI.
5. Pivot: a title's availability by region can weakly corroborate or challenge a claimed location/VPN behaviour.

## Inputs → Outputs
- **In:** none directly (a Netflix title or filter set)
- **Out:** per-country streaming availability (`geolocation`) for titles
- **Empty/negative result looks like:** a title showing as unavailable everywhere, or missing — often a scraper gap rather than true absence (the site admits incomplete coverage).

## Gotchas & OpSec
- Unofficial scrape — Netflix actively resists it, so the catalog is incomplete and can lag reality.
- Very narrow OSINT use; treat any regional inference as weak corroboration, never proof.
- Availability changes constantly as Netflix rotates licences.

## Overlaps ("do both")
- Pairs with VPN/IP-geolocation checks — uNoGS shows what's available where, while IP-geolocation shows where a connection appears to originate; together they test a region claim.

## Trust & verifiability
`trust: community` — a useful but unofficial, community-scraped dataset; verify anything important against Netflix directly, since coverage is admittedly partial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unogs-com |
| category | communities-forums |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
