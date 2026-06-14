---
id: crowdmap
name: CrowdMap
description: Use when you want to aggregate and map crowdsourced incident/sighting reports — but note Crowdmap (Ushahidi's hosted platform) has been discontinued; treat as a legacy/unavailable tool.
url: https://crowdmap.com
category: geolocation
path:
- geolocation
bestFor: Crowdsourced incident mapping — historically Ushahidi's hosted version; now effectively retired.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- metadata
status: down
pricing: free
costNote: Was a free hosted service; the hosted Crowdmap product has been discontinued by Ushahidi.
opsec: passive
opsecNote: A crowdsourced mapping platform; viewing public maps was passive. The self-hosted Ushahidi platform is the surviving successor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdmap was the hosted SaaS edition of Ushahidi (a reputable crisis-mapping project). The hosted crowdmap.com service has been shut down/retired; verify before assuming availability.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Ushahidi Crowdmap
- crowdmap.com
tags:
- geospatial-research-and-mapping-tools
- crowdsourced-mapping
- crisis-mapping
source: awesome-osint
lastVerified: ''
enrichment: full
---

# CrowdMap

> The hosted (SaaS) edition of Ushahidi's crowdsourced incident-mapping platform — it let people submit geotagged reports that aggregate onto a shared map. The hosted crowdmap.com service has since been **discontinued**.

## When to use
Conceptually, when you want to collect and plot many geotagged `address`/`geolocation` reports (sightings, tips, incidents) onto one map. In practice, the hosted Crowdmap is **retired**, so this entry is mainly historical: if you encounter an old Crowdmap deployment URL referenced in a case, this explains what it was. For active crowdsourced mapping today, use the self-hosted **Ushahidi** platform instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. First check whether https://crowdmap.com still resolves to a working service — expect that it does not (the hosted product was sunset).
2. If you are viewing an archived/legacy deployment, read the submitted reports plotted on its map (each carries a location and timestamp).
3. For new work, stand up Ushahidi (self-hosted) rather than relying on Crowdmap.
4. Pivot: treat any plotted report as an unverified tip — corroborate each `geolocation` independently.

## Inputs → Outputs
- **In:** `geolocation` / `address` (report locations submitted by contributors)
- **Out:** `geolocation` + `metadata` (a map of crowdsourced reports with timestamps/notes)
- **Empty/negative result looks like:** the service does not load at all (the likely current state), or a deployment with no reports.

## Gotchas & OpSec
- **Discontinued:** do not assume crowdmap.com is live; treat `status: down` as the default and verify.
- Crowdsourced reports are unvetted — anyone could submit, so every point is a lead to verify, not a fact.
- OpSec: passive when viewing public maps; submitting reports could expose your account/IP — use sock infrastructure if you ever contribute.

## Overlaps ("do both")
- Superseded by **Ushahidi** (self-hosted) for active crowdsourced mapping; conceptually similar to any community sighting-map you'd build for a missing-persons campaign.

## Trust & verifiability
`trust: community` — built on the reputable Ushahidi crisis-mapping lineage, but the hosted service is retired. Confirm availability before relying on it, and treat all crowdsourced points as unverified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crowdmap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
