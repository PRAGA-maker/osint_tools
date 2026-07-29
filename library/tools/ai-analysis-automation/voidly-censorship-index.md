---
id: voidly-censorship-index
name: Voidly Censorship Index
description: Use when you have a country/`geolocation` and want to know which platforms are blocked and how heavily it censors — returns per-country censorship scores and blocked-service data.
url: https://voidly.ai/censorship-index
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Contextualising a subject's country by which apps/services are blocked, so you know why a person may be unreachable on a given platform.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Open access with free CSV/JSON exports and a public API under CC BY 4.0; no account required.
opsec: passive
opsecNote: You query Voidly's aggregated dataset, not the target or their country's infrastructure. Fully passive; nothing about your subject is transmitted. Route through your normal research setup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent research project (Voidly Research) aggregating OONI, CensoredPlanet, IODA and its own measurement network; methodology is published but not a first-party authority.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Global Censorship Index
- Voidly Atlas censorship
tags:
- threat-intelligence
- censorship
- geolocation-context
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Voidly Censorship Index

> A live, per-country internet-censorship ranking built from 38M+ network measurements — tells you what's blocked where.

## When to use
You have a subject's country or region (`geolocation`) and need to understand the connectivity environment: which platforms (Google, YouTube, Facebook, VPNs, messengers, news sites) are blocked, how severe the censorship is, and whether it's tightening. This explains *why* a person in a given country may be absent from, or using workarounds for, particular services — useful before concluding "no online footprint."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://voidly.ai/censorship-index.
2. Browse or search the country ranking; each country shows a severity score, a risk tier (Free → Severe), and a trend arrow (worsening/stable/improving).
3. Open a country profile to see its blocked-services list and linked incident evidence.
4. For bulk work, pull the free CSV/JSON export or hit the public API.
5. Pivot: a blocked-platform finding shapes which apps to check for a subject and whether to expect VPN/mirror usage.

## Inputs → Outputs
- **In:** `geolocation` (country/region)
- **Out:** censorship severity score, blocked-service list, trend, and evidence links (contextual `geolocation` intelligence)
- **Empty/negative result looks like:** a country tiered "Free" with no blocked services — treat as low-censorship context, not as proof a specific service is reachable at a specific moment.

## Gotchas & OpSec
- This is country-level context, not a per-user or per-IP reachability test — it won't tell you if one person's connection is filtered.
- Data refreshes every ~6 hours and reflects aggregated measurements; short-lived or regional blocks may lag.
- Community project: corroborate critical claims against the underlying OONI/CensoredPlanet sources it cites.

## Overlaps ("do both")
- Pair with live network-reachability and OONI Explorer checks — this gives the standing censorship picture; those confirm real-time blocking of a specific service.

## Trust & verifiability
`trust: community` — an independent research aggregation with a published methodology and cited upstream sources (OONI, CensoredPlanet, IODA); credible but not an official/first-party authority, so verify high-stakes claims against the primary datasets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voidly-censorship-index |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
