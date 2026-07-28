---
id: kaspersky-cyberthreat-live-map
name: Kaspersky Cyberthreat live Map
description: Use when you want a live global picture of malware/attack detections by country — returns real-time threat-telemetry visualization, situational context rather than per-subject data.
url: https://cybermap.kaspersky.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A live, visual global map of cyberthreat detections (by type and country) for situational awareness.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public visualization; no account.
opsec: passive
opsecNote: You view an aggregate telemetry map on Kaspersky's site — no target is queried and nothing you enter reaches a subject. Standard third-party site logging; be aware it is a vendor marketing/telemetry product.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: First-party Kaspersky visualization of their own detection telemetry; representative of what their products see, not an independent or complete measure of global threats.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cybermap
- kaspersky-tdsskiller-anti-rootkit-tool
aliases:
- Kaspersky Cybermap
- cybermap.kaspersky.com
tags:
- live-cyber-threat-maps
- threat-intelligence
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Kaspersky Cyberthreat live Map

> A real-time global visualization of Kaspersky's threat detections — eye-catching situational context on where and what kinds of attacks are being seen, not a lookup on any person or IP.

## When to use
Low-relevance, context-only. Reach for it when you want a quick, visual sense of global cyberthreat activity — which countries and detection types (on-access, on-demand, web, mail, network, vulnerability scans) are lighting up right now — as background for a threat-landscape briefing or a report visual. It shows aggregate telemetry; you cannot query a specific `ip-address`, person, or incident.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cybermap.kaspersky.com/.
2. Spin the globe or select a country to see its detection statistics and rankings.
3. Toggle the detection-type layers to see the mix of threat categories.
4. Use it for situational/illustrative context — then go to actual threat-intel feeds for anything you need to act on.

## Inputs → Outputs
- **In:** none (you browse by country/threat type — not a personal selector)
- **Out:** aggregate real-time threat-detection visualization (no personal selectors)
- **Empty/negative result looks like:** not applicable in the lookup sense — it always shows a live aggregate; a quiet country simply reflects fewer Kaspersky detections there, not a queryable "no result."

## Gotchas & OpSec
- It reflects **Kaspersky's own product telemetry**, not the whole internet — it's representative, not authoritative or complete, and is partly a marketing showcase.
- No drill-down to individual IPs/incidents; it's a picture, not a data source you can pivot from.
- OpSec: **passive**, nothing reaches any subject.

## Overlaps ("do both")
- For anything actionable, use real threat-intelligence feeds and IP-reputation tools instead: this map is for situational framing, while those give queryable, per-indicator data.

## Trust & verifiability
`trust: community` — a first-party vendor visualization of Kaspersky's detection data. Fine as an illustrative overview; don't cite it as a neutral or complete measure of global threat activity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kaspersky-cyberthreat-live-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
