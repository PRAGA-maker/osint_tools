---
id: australian-bureau-of-statistics
name: Australian Bureau of Statistics
description: Use when you have an Australian place or demographic question and want official census/population data — returns area statistics that frame a location, not individual records.
url: https://www.abs.gov.au/
category: search-engines
path:
- search-engines
bestFor: Official Australian census, population and demographic statistics to contextualize a location or area.
selectorsIn:
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official government statistics; no account or payment. Census tables and datasets are openly downloadable.
opsec: passive
opsecNote: Anonymous browsing of published aggregate statistics. No login, nothing written, no subject notification. This is population-level data, not personal records, so there is no individual to alert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Australia's official national statistical agency; the data is authoritative aggregate census/survey data, deliberately non-identifying at the individual level.
missingPersonsRelevance: low
coverage:
- au
auth: none
api: true
localInstall: false
registration: false
aliases:
- ABS
- abs.gov.au
tags:
- toddington
- curated-directory
- specialty-search
- statistics
- australia
source: toddington-resources
lastVerified: '2026-07-19'
---

# Australian Bureau of Statistics

> Australia's official statistics agency — census, population and demographic data for framing an Australian place, not for looking up a person.

## When to use
Your case has an Australian geographic angle and you need context around an area rather than an individual: who lives in a suburb (age/occupation/ancestry/language mix from the census), population and dwelling counts, socio-economic indicators. ABS QuickStats and Census tables let you characterize a location — useful for understanding a subject's community, assessing whether a claimed address profile is plausible, or scoping a search area. It is aggregate, privacy-protected data: it will never return a named individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.abs.gov.au/ and use Census "QuickStats" for a suburb/area, or browse Statistics by topic.
2. Enter a place name or postcode to pull that area's demographic profile.
3. Read the tables (population, age, occupation, ancestry, language, dwellings); download data or use the API for bulk work.
4. Pivot: the area profile contextualizes an `address`/`geolocation` and can corroborate or challenge assumptions about where/how a subject lived.

## Inputs → Outputs
- **In:** an Australian `address`/place/postcode
- **Out:** aggregate demographic/`geolocation` context for that area (population, age, occupation, ancestry, language, housing)
- **Empty/negative result looks like:** no area match for a mistyped place, or suppressed cells in very small areas (ABS masks small counts to protect privacy) — never an individual record.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Aggregate only — this contextualizes a place, it does not identify people; don't over-read small-area numbers (they're perturbed for privacy).
- Census is periodic (every 5 years) — data reflects the last census, not this moment.

## Overlaps ("do both")
- Pairs with Australian electoral/registry and property tools — this frames the area demographically, those (where lawful) reach individual-level records.

## Trust & verifiability
`trust: trusted` — the authoritative national statistical agency; data is reliable at the aggregate level and intentionally non-identifying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australian-bureau-of-statistics |
| category | search-engines |
| selectorsIn → selectorsOut | address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
