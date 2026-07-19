---
id: worldwide-detention-centres-map
name: Worldwide Detention Centres Map
description: Use when you have a `geolocation`/country and want to identify immigration detention facilities there — returns facility locations, status and type for trafficking/missing-migrant work.
url: https://www.globaldetentionproject.org/detention-centres/map-view
category: geolocation
path:
- geolocation
bestFor: Locating immigration detention centres worldwide by country/region, with operational status and facility type — relevant to missing migrants, refugees and trafficking cases.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public research resource from the Global Detention Project (a non-profit); no account or payment required.
opsec: passive
opsecNote: Browsing published research data is fully passive — you are reading a public NGO database, not touching any target infrastructure. No sock puppet strictly needed, though normal separation hygiene is good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Global Detention Project, an established Geneva-based research non-profit that documents immigration detention; data is sourced and cited in country profiles.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Global Detention Project map
- GDP detention centres map
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- migration
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Worldwide Detention Centres Map

> The Global Detention Project's interactive map of immigration detention facilities worldwide — a starting point when a missing person may be held, detained, or processed in the migration system.

## When to use
You are investigating a missing migrant, refugee, asylum-seeker, or possible trafficking victim and need to know which immigration detention facilities exist in a given `geolocation` (country or region), whether they are in use, and what type they are. It reframes a "where could they be held?" question into a concrete, mappable set of facilities to check against.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.globaldetentionproject.org/detention-centres/map-view.
2. Navigate the map (or switch to list view) and filter by region/country, operational status ("In use" / "Closed"), and facility type (administrative, ad hoc, criminal, unknown).
3. Select a facility to read its details and follow through to the country profile for sourced context (legal framework, conditions, reports).
4. Cross-reference facility names and locations with local records, NGO contacts, or official detention registries.
5. Pivot: a candidate facility gives you `address`/`geolocation` leads and named institutions to contact or search further.

## Inputs → Outputs
- **In:** `geolocation` (country/region of interest)
- **Out:** facility `geolocation`/`address`, operational status, facility type, and links to sourced country profiles
- **Empty/negative result looks like:** a country with no mapped facilities, or facilities marked "Closed". Absence in the database does not prove no detention occurs — GDP coverage is broad but not exhaustive.

## Gotchas & OpSec
- The map documents *known, researched* facilities; informal or undisclosed holding sites will not appear.
- Status and details reflect the GDP's last research cycle for that country — check the country profile's dating.
- OpSec: passive public research; nothing here alerts a target.

## Overlaps ("do both")
- Pairs with country-specific official detainee-locator systems and refugee/migration NGO resources — this gives the global map and sourced context, while national systems (where they exist) can confirm an individual's presence.

## Trust & verifiability
`trust: trusted` — the Global Detention Project is a recognised research non-profit whose entries are documented and cited; treat it as an authoritative directory of *researched* facilities, while remembering coverage gaps for undisclosed sites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldwide-detention-centres-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
