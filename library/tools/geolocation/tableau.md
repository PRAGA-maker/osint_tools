---
id: tableau
name: Tableau
description: Use when you have a spreadsheet of geocoded points (sightings, addresses, ping data) and need to plot and explore them on an interactive map.
url: http://www.tableausoftware.com
category: geolocation
path:
- geolocation
bestFor: Mapping and visually analyzing your own structured geodata (address/coordinate tables) rather than looking up new facts.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Tableau Public is free (work is published publicly); Tableau Desktop/Cloud is a paid Salesforce product.
opsec: passive
opsecNote: A visualization platform, not a lookup — it does not contact the target. BUT Tableau Public dashboards are world-readable; never publish case data there.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Tableau is a mainstream commercial BI product (now Salesforce); reliable software, but it shows only the data you load.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- zeemaps
- worldmap-harvard
aliases:
- Tableau Public
- Tableau Desktop
tags:
- geospatial-research-and-mapping-tools
- data-visualization
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Tableau

> A mainstream business-intelligence platform used in OSINT to map and visually explore your own geocoded datasets — it analyzes data you bring, it does not discover it.

## When to use
You have already collected structured data with location columns — a list of `address`es, sighting coordinates, tower-ping rows, or financial transactions tagged by place — and you need to see the spatial/temporal pattern. Tableau plots those `geolocation`/`address` rows on a map and lets you filter by date or category to spot clusters and movement. It is not the tool for looking up a fact about an unknown person.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Get Tableau Public (free) or Tableau Desktop. Note `www.tableausoftware.com` redirects to tableau.com.
2. Connect a data source: CSV/Excel with latitude/longitude or recognizable address fields, or a database.
3. Drag geographic fields onto the canvas; Tableau auto-generates a map. Add date/category fields to filters and color.
4. Build a dashboard to slice the data (e.g. sightings over time, distance from last-known location).
5. Pivot: export findings or screenshots into the case file; for a quick shareable pin map instead, use [[zeemaps]].

## Inputs → Outputs
- **In:** your own table containing `geolocation` (lat/long) or `address` fields.
- **Out:** interactive maps/visualizations (refined `geolocation` insight; pattern detection).
- **Empty/negative result looks like:** Tableau can't geocode your address field (misspelled/ambiguous), so points fail to plot — fix the data, not the tool.

## Gotchas & OpSec
- Account login required for Desktop/Cloud; Tableau Public requires a free account.
- Critical OpSec: Tableau **Public** publishes every workbook to the open web. For sensitive missing-persons data use Desktop/Cloud with private storage, never Public.
- It is purely a viz layer — accuracy is entirely a function of the data you feed it.

## Overlaps ("do both")
- Pairs with [[zeemaps]] (faster, lighter web pin maps) and [[worldmap-harvard]] (academic GIS layers) depending on whether you need heavyweight analytics or a quick map.

## Trust & verifiability
`trust: trusted` — established commercial software from Salesforce; the platform is dependable, though all conclusions depend on the source data you import.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tableau |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes |
