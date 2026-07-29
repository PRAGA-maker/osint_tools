---
id: vincos-it
name: World Map of Social Networks (Vincos)
description: Use when you have a `geolocation`/country and want to know which social network dominates there — returns a country-by-country map of the leading social platforms.
url: http://vincos.it/world-map-of-social-networks
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Deciding which social platform to search for a subject based on what's dominant in their country.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free public infographic/analysis by Vincenzo Cosenza; no account. Updated periodically (not real-time).
opsec: passive
opsecNote: A published map you read — you submit no subject data, so it's fully passive. It informs *where* to look next; the actual (still passive) searching happens on the platforms it points you to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known, long-running analyst project (Vincenzo Cosenza) built on Alexa/SimilarWeb traffic data; credible directional signal, but periodic and traffic-estimate-based.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Vincos World Map of Social Networks
- vincos.it
tags:
- social-media
- geolocation
- reference
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# World Map of Social Networks (Vincos)

> A periodically-updated map of which social network leads in each country — the strategic layer that tells you *which platform* to search for a subject in a given place.

## When to use
You know a subject's country/region (`geolocation`) and need to prioritize where to look for their social presence. Global instinct says Facebook/Instagram/X, but this map shows the exceptions — VK across Russian-speaking regions, WeChat/Tencent in China, and other regional leaders — so you search the platform your subject is actually likely to use, not just the Western defaults. It's orientation, not a lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://vincos.it/world-map-of-social-networks.
2. Read the current edition; find the subject's country and its dominant (and second-place) network.
3. Prioritize your social sweep toward that platform's search/enumeration tools.
4. Check the edition date — it's periodic, so treat a very recent shift with caution.
5. Pivot: the identified platform sets which platform-specific OSINT tool you reach for next.

## Inputs → Outputs
- **In:** `geolocation` (country/region)
- **Out:** the leading (and runner-up) social network(s) for that country — a search-prioritization signal
- **Empty/negative result looks like:** the map is directional, not exhaustive — a "dominant" network doesn't mean your subject uses it; treat it as a probability nudge, not proof.

## Gotchas & OpSec
- **Periodic and traffic-based** — editions lag real shifts and rest on traffic estimates (Alexa/SimilarWeb); don't over-trust a single data point.
- Country-level generalization hides sub-populations (diaspora, niche communities) — still check mainstream platforms too.
- OpSec: **passive** — reading a map reveals nothing about your target.

## Overlaps ("do both")
- Feeds your platform-specific tooling: once Vincos suggests, say, VK for a Russian nexus, pivot to the relevant VK/username tools. Use it before a social sweep to allocate effort sensibly.

## Trust & verifiability
`trust: community` — a credible, long-running analyst project; directionally reliable but based on periodic traffic estimates, so confirm actual presence on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vincos-it |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | geolocation →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
