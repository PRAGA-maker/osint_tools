---
id: hcl-threat-map
name: HCL Threat Map
description: Use when you want a live, region/industry-filtered dashboard of recent deep/dark-web cyberattack activity — returns aggregated threat trends, not per-target lookups.
url: https://www.hcltech.com/hcl-threat-map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Situational awareness of current attack types and hotspots by region and sector; not an indicator lookup.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public marketing dashboard from HCLTech; no account required.
opsec: passive
opsecNote: You only view an aggregate dashboard — you submit no target selector, so nothing about your investigation leaves your browser except a normal page load to HCLTech. Safe to browse.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by HCLTech (a large IT-services vendor) as a marketing/awareness visualization; aggregate, non-attributable data with no methodology disclosure.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- HCLTech Threat Map
- HCL cyber threat map
tags:
- live-cyber-threat-maps
- dashboard
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# HCL Threat Map

> A live "pretty map" of the last 30 days of deep/dark-web cyberattack activity, filterable by region, threat type, and industry — context, not a per-target tool.

## When to use
You want a quick sense of the *current* threat climate — which attack types (phishing, DDoS, data leaks, compromised accounts, malware, fraud, hacktivism, web attacks) are spiking, in which regions (Americas / EMEA / APAC) and which of ~15 sectors. It is background/situational-awareness reading. It does **not** accept an IP, domain, or any subject selector, so it is not part of an enrichment pivot chain for a specific person or asset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hcltech.com/hcl-threat-map.
2. Use the region toggle (Americas / EMEA / APAC) and the "See by Industries" view.
3. Adjust the Threat Index / threat-type filters to focus on a category.
4. Read the trend for the last 30 days — treat it as directional context, not attributable evidence about any organization.

## Inputs → Outputs
- **In:** none (no selector submitted — you filter, you don't query)
- **Out:** aggregate threat trends by region / type / industry (situational context only)
- **Empty/negative result looks like:** the interactive widget fails to load (a vendor marketing page can go stale) — there is no "no result," only "dashboard up" or "dashboard down."

## Gotchas & OpSec
- This is a **vendor marketing visualization**: no disclosed methodology, no drill-down to indicators, no attribution. Do not cite it as evidence in a report.
- Not selector-driven — it will not tell you anything about a specific IP, domain, or person.
- OpSec: **passive** and safe — nothing about your target is transmitted.

## Overlaps ("do both")
- Stands alone as awareness context; for actual infrastructure lookups on a specific `domain`/`ip-address`, use the investigative tools elsewhere in this category rather than a threat-map dashboard.

## Trust & verifiability
`trust: community` — a real, live dashboard from a reputable vendor, but it is promotional and non-attributable; useful for orientation, not for evidentiary claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hcl-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
