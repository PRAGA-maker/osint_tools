---
id: bitdefender-threat-map
name: Bitdefender Threat Map
description: Use when you want live situational awareness of global cyberattacks — an interactive real-time map of attacks, infections and spam by country.
url: https://threatmap.bitdefender.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A real-time visualization of worldwide attack/infection/spam activity and source→target country flows for situational awareness.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to view; no account required.
opsec: passive
opsecNote: A public dashboard of aggregated telemetry — you watch it, you query no target. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Bitdefender from its own detection telemetry; it's a promotional/situational dashboard, not a queryable intelligence source about a specific target.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- threatmap.bitdefender.com
tags:
- threat-map
- situational-awareness
- cyberattacks
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- bitdefender-antivirus
---

# Bitdefender Threat Map

> A live, interactive world map of cyberattacks, infections and spam drawn from Bitdefender's detection telemetry — situational awareness, not a targeted lookup.

## When to use
You want a real-time, big-picture view of where attacks and infections are being detected globally right now — for a briefing visual, general situational awareness, or to sanity-check that a spike in activity is broad rather than targeted. It does not let you look up a specific `ip-address`, person, or organisation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://threatmap.bitdefender.com/.
2. Watch the live feed: entries show time, attack type, source country and target country, with a legend for attacks/infections/spam.
3. Use the map/locations controls to focus on regions of interest.
4. Read it as an aggregate trend indicator, not evidence about any individual actor.
5. For actual indicators/targeted intel, move to a threat-intel platform or IOC feed.

## Inputs → Outputs
- **In:** none (it's a live dashboard)
- **Out:** aggregate attack/infection/spam activity by type and country flow
- **Empty/negative result looks like:** not applicable — it always streams aggregate data; it simply cannot answer a query about a specific target.

## Gotchas & OpSec
- Situational-awareness/marketing dashboard — no per-target lookup, no attribution you can act on.
- Reflects only Bitdefender's own telemetry, so it's a partial view of global activity.
- OpSec: fully passive.

## Overlaps ("do both")
- Overlaps with other vendors' live threat maps (Kaspersky, Checkpoint) for a fuller picture — but for real investigation use IOC feeds and threat-intel platforms, not the maps.

## Trust & verifiability
`trust: trusted` — genuine first-party telemetry from Bitdefender, but it's an aggregate visualization; don't derive target-specific conclusions from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitdefender-threat-map |
