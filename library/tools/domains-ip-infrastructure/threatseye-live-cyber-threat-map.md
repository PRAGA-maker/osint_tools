---
id: threatseye-live-cyber-threat-map
name: ThreatsEye | Live Cyber Threat Map
description: Use when you want an at-a-glance live visualisation of global cyber-attack activity by origin/target geography — returns aggregate attack flows, not lookups on a specific selector.
url: https://threatseye.io/threats-map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Ambient situational awareness of worldwide attack traffic; a briefing/demo visual, not an investigative lookup.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: free
costNote: The public map is free to view; no account needed. ThreatsEye's deeper threat-intel products are commercial.
opsec: passive
opsecNote: Purely a spectator view of aggregate data — you enter nothing about a target, so it leaks nothing. Standard sock-puppet browsing hygiene still applies to the vendor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Vendor-run marketing/awareness visual (ThreatsEye); the underlying feed is aggregate and unverifiable, so treat it as illustrative rather than evidentiary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ThreatsEye Threat Map
tags:
- live-cyber-threat-maps
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# ThreatsEye | Live Cyber Threat Map

> A live world map of aggregate cyber-attack activity — good for a situational-awareness glance, not for investigating a person or a single IP.

## When to use
You want a quick visual of where attack traffic is originating and landing right now, e.g. for a briefing slide or to sanity-check whether a region is seeing elevated activity. It is decorative/contextual: it does not let you query a specific `ip-address`, `domain`, or person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://threatseye.io/threats-map.
2. Watch the animated flows between origin and destination geographies; hover for the aggregate counters (top origins, top targets, attack categories).
3. Use it only as ambient context — there is no input box to enter a target selector.
4. To actually investigate an IP or domain, pivot to a real lookup tool (WHOIS, passive DNS, IP reputation).

## Inputs → Outputs
- **In:** none
- **Out:** aggregate `geolocation` of attack origins/targets (illustrative)
- **Empty/negative result looks like:** the map shows generic global activity regardless of your case — that is expected; it is never "about" your subject.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; you disclose nothing about a target.
- Do not treat the flows as evidence — threat-map feeds are aggregated, sampled and vendor-curated for visual effect.

## Overlaps ("do both")
- Overlaps with `[[bunkerweb-live-cyber-attack-threat-map]]` — both are live attack-map visuals; neither is a per-selector lookup, so pick one for a briefing rather than running both.

## Trust & verifiability
`trust: community` — a vendor awareness visual; useful as context, not as a source you would cite in an investigation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threatseye-live-cyber-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
