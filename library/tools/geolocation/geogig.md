---
id: geogig
name: GeoGig
description: Use when you need to version, branch, and merge large geospatial datasets like Git for GIS — a data-engineering tool, not a lookup.
url: http://geogig.org
category: geolocation
path:
- geolocation
bestFor: Distributed version control (Git-style) for geospatial vector data; for managing GIS datasets, not finding people.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Open-source (LocationTech/Eclipse); free but project activity has slowed.
opsec: passive
opsecNote: Operates on your own geospatial repositories locally; no target interaction.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: GeoGig is a real open-source LocationTech project for versioning geospatial data; it is infrastructure for GIS teams, with little direct missing-persons use.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- GeoGit
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# GeoGig

> An open-source, Git-style distributed version control system for geospatial vector data — lets teams branch, merge, and track history on large GIS datasets.

## When to use
Only when you are managing geospatial datasets as a data pipeline — versioning edits to a shapefile/feature collection, syncing collaborators, auditing who changed a feature. It does not take a name, image, or coordinate and return an answer; it is GIS infrastructure, so its direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: cli)
1. Install GeoGig (JVM-based) from geogig.org and add it to your PATH.
2. `geogig init` a repository, then `geogig import` vector data (PostGIS, shapefile, GeoJSON).
3. Use `geogig add` / `commit` / `branch` / `merge` like Git to version dataset changes.
4. Export or sync to a working GIS as needed.
5. Pivot: actual map/imagery analysis happens in `[[esri]]` or `[[google-earth-pro]]`; GeoGig only stewards the data layer.

## Inputs → Outputs
- **In:** geospatial datasets (`geolocation` feature collections).
- **Out:** versioned/merged `geolocation` datasets with history.
- **Empty/negative result looks like:** N/A as a lookup — this manages data, it does not search for subjects.

## Gotchas & OpSec
- Human-in-the-loop: yes — you author and review commits/merges manually.
- Project maintenance has slowed; check current build/compatibility before relying on it (`status: degraded`).
- OpSec: passive; runs locally on your own data.

## Overlaps ("do both")
- Use alongside `[[esri]]` (GIS analysis) — GeoGig is the version-control backstore, not a viewer.

## Trust & verifiability
`trust: community` — legitimate open-source LocationTech project, but it is GIS plumbing with low direct relevance to person-finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geogig |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
