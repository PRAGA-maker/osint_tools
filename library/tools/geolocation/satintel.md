---
id: satintel
name: SatIntel
description: Use when you need satellite reconnaissance (orbital/TLE data, satellite tracking) rather than ground geolocation of a person.
url: https://github.com/ANG13T/SatIntel
category: geolocation
path:
- geolocation
bestFor: Open-source CLI for satellite OSINT — pulling orbital element (TLE) data and tracking/identifying satellites.
selectorsIn: [metadata]
selectorsOut: [geolocation, metadata]
status: live
pricing: free
opsec: passive
opsecNote: Queries public satellite catalogs from your machine; reveals nothing about a missing person, only your own catalog lookups.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source GitHub project by ANG13T; legitimate satellite-recon tooling but a niche space-OSINT use case, not person geolocation.
missingPersonsRelevance: low
coverage: [global]
auth: api-key
api: false
localInstall: true
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# SatIntel

> An open-source command-line tool for satellite reconnaissance — retrieving orbital (TLE) data and tracking/identifying satellites.

## When to use
This is satellite OSINT, not ground geolocation of a person. Reach for it when the investigative question is about a spacecraft: pulling Two-Line Element (TLE) orbital data, identifying or tracking a satellite, or enriching `metadata` about space assets. For locating a missing person on the ground it is not the right tool — use ground-imagery tools instead.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo from GitHub and install per its README (Python-based CLI).
2. Provide any required API credentials (e.g. an N2YO/space-data API key) as noted in the docs.
3. Run the CLI with a satellite identifier to fetch TLE/orbital `metadata` and tracking output.
4. Read the `geolocation`/`metadata` (sub-satellite point, pass predictions). Pivot: not a person-locator — return to ground tools like `[[sentinel-hub]]` for imagery.

## Inputs → Outputs
- **In:** `metadata` (a satellite name/NORAD ID)
- **Out:** orbital `metadata` (TLE, pass predictions) and sub-satellite `geolocation`
- **Empty/negative result looks like:** lookup fails — usually a missing/invalid API key or an unknown satellite ID.

## Gotchas & OpSec
- Human-in-the-loop: likely needs an API key for the underlying space-data service.
- OpSec: passive and local; queries public satellite catalogs, leaks nothing about a target.
- Niche use case — clearly off-path for typical missing-persons geolocation, hence low MP relevance.

## Overlaps ("do both")
- Does not overlap with ground-geolocation tools; complementary only if a case genuinely involves satellite assets.

## Trust & verifiability
`trust: community` — a legitimate open-source project on GitHub by ANG13T. The code is inspectable; relevance to missing-persons work is low.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | satintel |
| category | geolocation |
| selectorsIn → selectorsOut | metadata → geolocation, metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes |
