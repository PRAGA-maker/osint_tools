---
id: radware-live-cyber-threat-map
name: Radware Live Cyber Threat Map
description: Use when you want an at-a-glance global picture of live cyber-attack activity by region and type — returns aggregate attack visualisation (not per-target lookup).
url: https://livethreatmap.radware.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Situational-awareness visualisation of ongoing attack volumes/types worldwide.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public visualisation by Radware; no account.
opsec: passive
opsecNote: Passive — you view an aggregate dashboard; no subject is involved and you enter no target data. It reflects Radware's own sensor network, not the whole internet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Vendor (Radware) marketing/awareness dashboard drawn from Radware's telemetry; illustrative rather than an investigative data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Radware threat map
tags:
- live-cyber-threat-maps
- threat-intel
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Radware Live Cyber Threat Map

> A live global visualisation of cyber-attack activity — attack types, top targeted/attacking regions — drawn from Radware's sensor telemetry.

## When to use
You want quick situational awareness of current large-scale attack trends (which attack types are active, which regions are seeing volume) rather than an answer about a specific person, IP or domain. Like other vendor "threat maps," it is a high-level dashboard: good for context and briefings, not for investigating an individual selector. Missing-persons relevance is minimal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://livethreatmap.radware.com/.
2. Watch the animated globe/feed: attack types, top source and destination countries, and category breakdowns.
3. Read it as an aggregate trend indicator — you cannot enter or look up a specific IP/domain here.
4. For actual per-target intelligence, move to a queryable service (WHOIS/DNS, Shodan, threat-intel exchanges).

## Inputs → Outputs
- **In:** none (a passive dashboard — no selector entry)
- **Out:** aggregate attack visualisation — categories, source/destination regions, volume trends
- **Empty/negative result looks like:** a quiet map/low counts during a lull; there is no "lookup," so this never returns a result for a specific target.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing you do is tied to a subject.
- It's a vendor awareness/marketing tool from Radware's own sensors — treat figures as illustrative of Radware's visibility, not a complete or neutral measure of global attacks.

## Overlaps ("do both")
- Similar in kind to `[[ibm-x-force-exchange-current-malicious-activity]]` and other live threat maps — all are situational dashboards; use a queryable intel platform when you need to investigate a specific indicator.

## Trust & verifiability
`trust: community` — a reputable vendor's public dashboard, but it's an aggregate visualisation, not verifiable per-target data; don't cite it as evidence about any specific host or person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radware-live-cyber-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
