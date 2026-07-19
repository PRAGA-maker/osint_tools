---
id: wikicrimes
name: WikiCrimes
description: Use when you have a `geolocation`/area and want crowdsourced crime reports mapped there — returns location-tagged incident points and density, mainly for Brazil/Latin America.
url: http://wikicrimes.org/main.html
category: search-engines
path:
- search-engines
bestFor: Browsing a crowdsourced, user-reported crime map for an area — individual incidents plus crime density, with strongest coverage in Brazil.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free to browse; a free account is needed only to submit reports. Note the site is aging and intermittently unavailable — verify it loads before relying on it.
opsec: passive
opsecNote: Browsing the public map is passive and reveals nothing about your subject. If you register to report, that account is attributable — use a sock-puppet, and note reports are user-generated and may be unreliable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An academic crowdsourced-crime project (originated by Vasco Furtado, Univ. of Fortaleza). Data is public-submitted and unvetted; incidents are rated by user credibility, not official confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wiki Crimes
tags:
- toddington
- curated-directory
- specialty-search
- crime-map
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# WikiCrimes

> A crowdsourced, wiki-style crime map where the public reports incidents by location — useful as area context, strongest in Brazil, but user-generated and aging.

## When to use
You have an `address` or `geolocation` and want a rough, community-reported picture of crime activity around it — density hot-spots and individual incidents that neighbours have logged. This is background/context for an area (e.g. assessing where a subject was last seen), not an authoritative record. Its coverage is heavily concentrated in Brazil and Latin America, so relevance drops sharply elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://wikicrimes.org/main.html (confirm it loads — the site is intermittently down).
2. Navigate the map to your area of interest, or search a locality.
3. Read the pins and density overlay: each report shows an incident type, location, and a user-assigned credibility rating; comments may add detail.
4. Weight everything against the credibility rating and remember reports are unverified crowd input.
5. Pivot: use hot-spot areas as leads for official crime data or local news, not as confirmed facts.

## Inputs → Outputs
- **In:** `geolocation` / `address` / locality
- **Out:** location-tagged crowd-reported incidents + crime-density view (`geolocation` context)
- **Empty/negative result looks like:** an empty map for your area — almost always means no one reported there (very common outside Brazil), not that the area is crime-free.

## Gotchas & OpSec
- Status is degraded: the site is old and frequently unavailable; treat access as unreliable.
- Data is entirely user-submitted and unverified — credibility ratings are the only quality signal; do not treat any pin as fact.
- Geographic bias: near-complete outside Brazil/Latin America.
- OpSec: passive to browse; registering to report is attributable.

## Overlaps ("do both")
- Complements official/local crime-data sources — WikiCrimes gives crowd context, which should be corroborated against authoritative records or news for the same area.

## Trust & verifiability
`trust: unverified` — an academic crowdsourcing experiment with unvetted, user-generated data and unreliable uptime. Use only as a lead source and confirm anything important elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikicrimes |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
