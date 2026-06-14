---
id: environmental-investigation-agency
name: Environmental Investigation Agency
description: Use when researching environmental-crime investigations, reports, or geographic case context — not a person-search or coordinate tool.
url: https://eia-international.org
category: geolocation
path:
- geolocation
bestFor: Reference NGO publishing investigative reports on environmental crime; tangential to person-finding.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public website and reports.
opsec: passive
opsecNote: Reading a public NGO website only; no contact with any target and no person lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: EIA is a real, reputable environmental NGO, but it is an advocacy/investigations organisation, not an OSINT geolocation utility. Categorisation here appears to be a harvest artifact; low direct relevance to missing-persons work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- EIA
- EIA International
tags:
- geolocation
source: metaosint
lastVerified: ''
enrichment: full
---

# Environmental Investigation Agency

> The Environmental Investigation Agency (EIA) is an international NGO that investigates and campaigns against environmental crime — a reference/reporting body, not a geolocation or people-search tool.

## When to use
Reach for this only when case context is genuinely environmental — e.g. background on wildlife-trafficking, illegal logging, or pollution networks that intersect a missing-persons scenario in a specific region. It does not take a coordinate or an image and return a location, despite its `geolocation` category tag.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://eia-international.org.
2. Browse or search the Reports/Investigations sections for the relevant region or topic.
3. Read published findings; cite the report, not the homepage.
4. Pivot: actual geolocation work should go to `[[google-earth-pro]]`, `[[earthexplorer]]`, or `[[geonames]]`.

## Inputs → Outputs
- **In:** a region or environmental-crime topic (loosely `geolocation` context).
- **Out:** investigative narrative and regional context — not structured `geolocation` coordinates.
- **Empty/negative result looks like:** no report matches your region/topic, which is the common case for individual missing-persons work.

## Gotchas & OpSec
- Human-in-the-loop: none; static public site.
- This is categorised under geolocation by the harvest source, but it is an NGO, not a tool. Do not expect lookup functionality.
- OpSec: passive; reading public reports only.

## Overlaps ("do both")
- For real geospatial tasks use `[[earthexplorer]]` or `[[google-earth-pro]]`; EIA only supplies narrative context.

## Trust & verifiability
`trust: unverified` — EIA itself is a credible NGO, but its inclusion as a geolocation OSINT tool is unverified and likely a harvesting artifact; relevance to missing-persons is low.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | environmental-investigation-agency |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
