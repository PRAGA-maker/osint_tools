---
id: cryo-tools
name: CryO Tools
description: Use when an investigation involves snow/ice/glacier terrain — returns open-source scientific software for modelling and analysing the cryosphere.
url: https://cryo-tools.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding open-source software to analyse glaciers, snow, ice, and other cryosphere data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open source; a directory pointing to open-source scientific tools (OGGM, COSIPY, OSARIS, etc.).
opsec: passive
opsecNote: Passive — a public directory of scientific software; no target interaction. Any geospatial analysis you run is on public satellite/climate datasets, not on a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A curated hub of established, peer-used cryospheric-science software; the listed tools come from academic/research communities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- CryoTools
- cryo-tools.org
tags:
- bellingcat-toolkit
- environment-wildlife
- cryosphere
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# CryO Tools

> A curated directory of open-source scientific software for the cryosphere — glaciers, snow, sea ice — for the rare investigation that hinges on ice/snow terrain analysis.

## When to use
A niche geospatial resource: when an investigation involves glaciated or snow/ice regions — verifying imagery of a polar/alpine location, modelling glacier change, or interpreting cryosphere satellite data — CryO Tools points you to the specialist software (e.g. OGGM for glacier modelling, COSIPY for snow/energy balance, OSARIS for InSAR) that general mapping tools don't cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cryo-tools.org/ and browse the catalogue of tools by function.
2. Pick the tool matching your task (glacier modelling, SAR processing, snow cover, etc.).
3. Follow through to that tool's own repo/docs; most are Python and self-installed.
4. Run the analysis on public satellite/climate datasets for your `geolocation` of interest.
5. Pivot: the geospatial output corroborates or dates imagery tied to a location.

## Inputs → Outputs
- **In:** `geolocation` (an ice/snow region to analyse) — plus the relevant public dataset
- **Out:** processed cryosphere/geospatial results for that `geolocation`
- **Empty/negative result looks like:** a listed tool being unmaintained or requiring data you can't access — check each tool's repo for current status.

## Gotchas & OpSec
- Highly specialised and scientific — steep learning curve, not a point-and-click OSINT tool.
- It's a directory: the real work happens in the individual tools it links, each with its own dependencies and data requirements.
- Very narrow applicability — only relevant when a case genuinely turns on cryosphere terrain.

## Overlaps ("do both")
- Pairs with general satellite-imagery and mapping platforms — mainstream tools handle the base imagery, while CryO Tools adds the ice/snow-specific analysis those tools lack.

## Trust & verifiability
`trust: trusted` — curates established, research-community software; outputs are scientific and reproducible, though only as good as the input datasets and your configuration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cryo-tools |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
