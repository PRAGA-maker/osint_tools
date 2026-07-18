---
id: 50-states
name: 50 States
description: Use when you have a US state or region and want a curated jump-off to that state's public-records, vital-records, and directory portals — returns links toward `address`/records sources, not data itself.
url: http://www.50states.com/
category: public-records
path:
- public-records
bestFor: A free reference hub of per-state facts plus directory links to white pages, public records, and vital records.
selectorsIn:
- geolocation
- name
selectorsOut:
- address
status: live
pricing: free
costNote: Fully free reference site, no account. It links out to third-party directories/records sites that may themselves charge.
opsec: passive
opsecNote: Reading state reference pages and clicking directory links is passive and reveals nothing about your target. Any actual lookup happens on the third-party site you follow to, where that site's own logging/opsec rules apply.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A general-interest educational reference site, not an investigative data source. Its value is orientation and outbound links; the linked directories vary widely in quality and freshness.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- 50states.com
tags:
- toddington
- curated-directory
- reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# 50 States

> A free US-state reference site whose OSINT value is its directory links out to public-records, vital-records, and white/yellow-pages portals — an orientation hub, not a data source.

## When to use
You are working a US case and need a fast, free jump-off to a specific state's records ecosystem, or you need contextual facts about a state (capital, abbreviations, county/area-code/zip layout) to disambiguate a location. Reach for it early to find *where* to look — the white-pages, public-records, and vital-records links per state — rather than expecting it to return person data directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.50states.com/ and pick the relevant state, or use the reference sections (area codes, zip codes, maps) to pin down a `geolocation`.
2. Follow the directory links — White Pages, Yellow Pages, Public Records, Vital Records — into the third-party services they point to.
3. Run the actual `name`/`address` lookup on the destination site, applying that site's own opsec.
4. Use the state facts (county boundaries, area codes, zip ranges) to disambiguate which jurisdiction's records to pursue.
5. Pivot: the linked public/vital-records portals are the real data step; this site just routes you to them.

## Inputs → Outputs
- **In:** `geolocation` (a US state/region) or a `name` you intend to look up downstream
- **Out:** `address` and records leads *indirectly* — via curated outbound links, plus state reference facts (area codes, zip codes, county maps)
- **Empty/negative result looks like:** the site never returns person records itself; a "dead end" is a stale/broken outbound link — follow a different linked directory instead.

## Gotchas & OpSec
- This is a reference/education site, not a search engine — do not expect it to resolve a name to an address on its own.
- Outbound links age; some point to defunct or paywalled directories. Treat them as suggestions to verify.
- Passive throughout; any attribution risk lives on the third-party site you click through to.

## Overlaps ("do both")
- A low-tech companion to the real engines in the [[public-records]] set — use 50 States to discover which state-level portal to hit, then a dedicated people-search/records tool to actually pull the data.

## Trust & verifiability
`trust: community` — a general-audience reference resource curated into Toddington's directory. Reliable for static state facts; treat its outbound records links as leads whose destinations you must independently verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 50-states |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, name → address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
