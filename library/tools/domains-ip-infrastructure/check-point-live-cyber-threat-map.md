---
id: check-point-live-cyber-threat-map
name: Check Point Live Cyber Threat Map
description: Use when you want situational awareness of live global attack activity (source/target countries, attack types) — returns a real-time threat visualization, not a per-subject lookup.
url: https://threatmap.checkpoint.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A live wall-map view of ongoing cyberattacks by country and attack type, for context/briefing rather than investigating a specific subject.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public dashboard operated by Check Point; no account required.
opsec: passive
opsecNote: A read-only visualization served from Check Point's ThreatCloud telemetry. You submit no subject data and reveal nothing about a target; the only thing logged is your own visit to Check Point.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Check Point Software (a major security vendor) and fed by its ThreatCloud sensor network — authoritative as an aggregate telemetry display, though it is not a lookup source for individual IPs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fortinet-threat-map
- fireeye-cyber-threat-map
aliases:
- Check Point ThreatMap
- ThreatCloud live map
tags:
- live-cyber-threat-maps
- threat-intelligence
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Check Point Live Cyber Threat Map

> Check Point's ThreatCloud rendered as a live attack globe — aggregate cyber-threat situational awareness, not a tool you feed a selector into.

## When to use
You want a real-time, at-a-glance picture of where attacks are originating and landing right now — top attacked/attacking countries, attack types, daily counts — for a briefing, a demo, or context on current threat weather. It is **not** an investigative lookup: you cannot enter an IP, domain, or name and get a report back. If you have a specific `ip-address` to check, use a reputation/enrichment tool instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://threatmap.checkpoint.com/ in any browser.
2. Watch the animated arcs — each represents a detected attack between a source and target country drawn from Check Point's ThreatCloud sensors.
3. Read the side panels: "Top Targeted Countries," "Top Attack Types," and the live/malware/phishing counters.
4. Use it for context only; to act on a specific indicator, pivot to a queryable source.
5. Pivot: for a real IP/domain investigation feed `[[shodan]]` or a passive-DNS/reputation tool; keep this map as background situational awareness.

## Inputs → Outputs
- **In:** none — there is no search box; it is a display.
- **Out:** none per-subject; only an aggregate real-time visualization (country-level attack flows, attack-type tallies).
- **Empty/negative result looks like:** a static or blank globe means the feed/JS failed to load — refresh, or use another vendor map like `[[fortinet-threat-map]]`.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you disclose nothing about any target. Treat the map itself with care in reporting: the arcs are illustrative marketing-grade telemetry, not precise geolocation of individual attackers, and country attribution is coarse.
- Do not mistake this for an indicator-enrichment tool; it answers "what's the global threat weather," not "is this IP malicious."

## Overlaps ("do both")
- Pairs with `[[fortinet-threat-map]]` and `[[fireeye-cyber-threat-map]]` — different vendors' sensor networks give slightly different pictures; compare them for a fuller situational read.

## Trust & verifiability
`trust: trusted` — first-party Check Point property backed by its ThreatCloud sensor network. Reliable as an aggregate telemetry display; not a citable source for any single IP or actor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-point-live-cyber-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
