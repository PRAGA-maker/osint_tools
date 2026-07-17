---
id: global-terriorism-database
name: Global Terrorism Database (GTD)
description: Use when you have a `geolocation`/date/group and want documented terrorist-incident records — returns incident `geolocation`, dates, actors, and sourced details.
url: https://twitter.com/cyb_detective/status/1578772549919559681
category: geolocation
path:
- geolocation
bestFor: Researching documented terrorist incidents worldwide (1970–2020) by location, date, group, or attack type, with sourced per-incident detail and statistics.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to search and to download for non-commercial/academic use after a free registration; some access tiers/commercial use are restricted.
opsec: passive
opsecNote: Querying an academic incident database is passive — no target is contacted. Registration ties downloads to an email; use a research/persona email if you prefer separation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by START at the University of Maryland; a widely-cited, methodologically documented academic dataset (coverage ends 2020).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- GTD
- START Global Terrorism Database
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Global Terrorism Database (GTD)

> START's open academic database of 200,000+ terrorist incidents worldwide (1970–2020) — searchable by place, date, group, and attack type, with sourced detail on each event.

## When to use
You have a `geolocation`, a date range, a group/actor, or an incident type and want authoritative, sourced records of terrorist attacks: where and when they occurred, who was responsible, weapons/targets, and casualty figures. In an investigation this contextualises a location's conflict history or connects a person/place to a documented event. (The recorded URL is a cyb_detective reference post; the database itself is hosted by START/University of Maryland — search there.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the GTD (START / University of Maryland: start.umd.edu/gtd, online search at gtd.terrorismdata.org).
2. Use the advanced search: filter by country/region, date range, perpetrator group, target type, and attack type.
3. Open an incident for its full record — date, precise `geolocation`, summary, actors, casualties, and the sources cited.
4. Register (free) to download the full dataset for offline/statistical analysis.
5. Pivot: an incident's location/date anchors a timeline; a named group feeds further conflict-OSINT; cited sources lead to primary reporting.

## Inputs → Outputs
- **In:** `geolocation` (country/region), date, group, or attack type
- **Out:** incident records — `geolocation`, dates, perpetrators, targets, casualties, and source citations; plus aggregate statistics.
- **Empty/negative result looks like:** no matching incidents for the filter, or events after 2020 missing (coverage ends 2020) — use a more recent conflict dataset for post-2020 events.

## Gotchas & OpSec
- Temporal cutoff: the GTD ends at 2020 — it is not a source for recent events.
- Definitional scope: inclusion follows START's specific "terrorism" criteria; some politically-violent events are excluded by design — read the codebook.
- Human-in-the-loop: full data download requires a free registration.
- OpSec: passive academic query; registration links downloads to an email.

## Overlaps ("do both")
- Complements ACLED and news-archive tools — GTD gives structured, sourced historical terrorism records; ACLED/news cover broader and more recent political violence.

## Trust & verifiability
`trust: trusted` — a peer-recognised academic dataset from START (University of Maryland) with a published methodology and per-incident source citations you can trace to primary reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-terriorism-database |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (registration) |
