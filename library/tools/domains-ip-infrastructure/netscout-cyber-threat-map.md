---
id: netscout-cyber-threat-map
name: NETSCOUT Cyber Threat Map
description: Use when you want a live global picture of DDoS/attack activity by region and type — returns aggregate attack visualisation (not per-target lookup).
url: https://horizon.netscout.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Situational-awareness visualisation of worldwide DDoS/attack trends.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public visualisation (NETSCOUT Cyber Threat Horizon); no account for the map.
opsec: passive
opsecNote: Passive — you view an aggregate dashboard; no subject is involved and you enter no target data. It reflects NETSCOUT/ATLAS sensor telemetry, not the whole internet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Vendor (NETSCOUT) awareness dashboard drawn from its ATLAS DDoS telemetry; illustrative rather than an investigative per-target source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- radware-live-cyber-threat-map
- ibm-x-force-exchange-current-malicious-activity
aliases:
- NETSCOUT Cyber Threat Horizon
- horizon.netscout.com
tags:
- live-cyber-threat-maps
- ddos
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# NETSCOUT Cyber Threat Map

> A live global visualisation of DDoS/attack activity from NETSCOUT's ATLAS sensor network — a situational dashboard, not a queryable lookup.

## When to use
You want quick situational awareness of large-scale DDoS/attack trends — which regions and attack types are active — rather than intelligence on a specific person, IP or domain. Like other vendor threat maps it's a high-level, illustrative dashboard; there's no per-selector query here. Missing-persons relevance is minimal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://horizon.netscout.com/.
2. Explore the map/feed: attack types, source/destination regions, volumes and trends over time.
3. Read it as an aggregate indicator; you cannot enter or look up a specific IP/domain.
4. For per-target intelligence, use a queryable service (WHOIS/DNS, Shodan, threat-intel exchanges).

## Inputs → Outputs
- **In:** none (a passive dashboard — no selector entry)
- **Out:** aggregate DDoS/attack visualisation — types, regions, volume trends
- **Empty/negative result looks like:** a quiet map during a lull; there is no "lookup," so it never returns a result for a specific target.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing ties to a subject.
- It's a vendor awareness tool from NETSCOUT's own ATLAS sensors — treat figures as illustrative of their visibility, not a complete or neutral global measure.

## Overlaps ("do both")
- Same class as `[[radware-live-cyber-threat-map]]` and `[[ibm-x-force-exchange-current-malicious-activity]]` — all situational dashboards; use a queryable intel platform when you need to investigate a specific indicator.

## Trust & verifiability
`trust: community` — a reputable vendor's public dashboard, but an aggregate visualisation, not verifiable per-target data; don't cite it as evidence about any specific host or person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netscout-cyber-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
