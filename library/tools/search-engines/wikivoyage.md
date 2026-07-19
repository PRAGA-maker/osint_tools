---
id: wikivoyage
name: Wikivoyage
description: Use when you have a place/`geolocation` and want ground-truth local context — returns a crowdsourced travel guide of districts, landmarks, transport and local detail.
url: https://www.wikivoyage.org
category: search-engines
path:
- search-engines
bestFor: Crowdsourced local knowledge about a place — neighborhoods, landmarks, transport, and on-the-ground detail useful for geolocation and planning.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free, ad-free Wikimedia project; no account needed to read.
opsec: passive
opsecNote: Reading a travel wiki is entirely passive and reveals nothing about your subject or investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A Wikimedia Foundation project with open editing and community moderation; reliable for general local context, though crowdsourced detail can be dated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- wikivoyage.org
tags:
- toddington
- curated-directory
- specialty-search
- travel
- local-context
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Wikivoyage

> The Wikimedia travel guide — a crowdsourced, ad-free source of local detail about places worldwide, useful for building ground-level context around a `geolocation`.

## When to use
You have a place tied to your case — a city, town, district, or region — and need to understand it the way a local or traveller would: how it's divided into neighborhoods, its landmarks and their names, transport hubs, common accommodation areas, and practical detail. Good background for geolocating imagery, planning where a person might go, or interpreting place references in a message. Its value is contextual, not person-specific (hence low MP relevance).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.wikivoyage.org and pick a language edition (English is largest).
2. Search for the city/region of interest.
3. Read the destination article: "Districts" for how the place is divided, "Get around" for transport, "See/Do" for landmarks, "Sleep/Eat" for hotel and dining clusters.
4. Note named landmarks, station names, and district boundaries — these translate place references and imagery cues into mappable locations.
5. Cross-reference the guide's landmark names against a map or Street View to pin an area.
6. Pivot: named landmarks/addresses → mapping and Street View geolocation; district context → narrowing where to search or which local records apply.

## Inputs → Outputs
- **In:** a `geolocation` (city/region/place)
- **Out:** local-context travel guide — districts, landmarks, transport, and sometimes specific `address`es of notable places
- **Empty/negative result looks like:** a stub article or no page for a small/obscure place — coverage is deep for tourist destinations and thin for minor localities. Fall back to Wikipedia or local sources.

## Gotchas & OpSec
- Travel-oriented and crowdsourced: great for orientation, but detail (prices, hours, transport) can be outdated and it won't cover residential minutiae.
- Not a locator: it gives context about a place, never data about an individual.
- OpSec: fully passive.

## Overlaps ("do both")
- Complements Wikipedia and mapping tools — Wikivoyage adds practical, district-level local knowledge that Wikipedia's encyclopedic article and a bare map don't convey.

## Trust & verifiability
`trust: trusted` — a moderated Wikimedia project reliable for general local context; treat specific, perishable details (hours, prices) as possibly stale and confirm against current sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikivoyage |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
