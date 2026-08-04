---
id: bunkerweb-live-cyber-attack-threat-map
name: BunkerWeb Live Cyber Attack Threat Map
description: Use when you want a live visual of attacks blocked across BunkerWeb WAF deployments worldwide — returns aggregate attack geography/categories, not per-selector lookups.
url: https://www.bunkerweb.io/threatmap
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Situational-awareness visual of live web-application-firewall blocks (origins, targets, attack categories) from the open-source BunkerWeb project.
selectorsIn: []
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free public map from the open-source BunkerWeb WAF project (Bunkerity). No account. The live feed intermittently shows "impossible to get data".
opsec: passive
opsecNote: Spectator view of aggregate WAF telemetry; you enter nothing about a target and leak nothing. Normal sock-puppet browsing hygiene applies to the vendor site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by the open-source BunkerWeb WAF project; feed is aggregate telemetry from participating deployments — illustrative, not evidentiary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- threatseye-live-cyber-threat-map
aliases:
- BunkerWeb Threatmap
- threatmap.bunkerweb.io
tags:
- live-cyber-threat-maps
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# BunkerWeb Live Cyber Attack Threat Map

> A live world map of web-application attacks blocked across BunkerWeb firewall deployments — situational-awareness eye-candy, not a per-target lookup.

## When to use
You want a quick global picture of live WAF-blocked attack traffic (top origins, top targeted locations, attack categories such as blacklist / country / DNSBL). It is contextual only; there is no way to query a specific `ip-address`, `domain`, or person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bunkerweb.io/threatmap (the old `threatmap.bunkerweb.io` host now 301-redirects here).
2. Read the live counters: daily attack count, ongoing attacks, top targeted locations, leading origins, primary categories.
3. If it shows "Impossible to get data for the moment", the aggregate feed is temporarily down — retry later.
4. Treat as ambient context only; for a real investigation, pivot to WHOIS / passive DNS / IP-reputation tools.

## Inputs → Outputs
- **In:** none
- **Out:** aggregate `geolocation` of attack origins/targets and category breakdown (illustrative)
- **Empty/negative result looks like:** a "cannot get data" banner (feed degraded) — not a result about your subject.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; no target data is disclosed.
- Status is `degraded`: the live feed has been observed erroring out — do not depend on it being populated.

## Overlaps ("do both")
- Overlaps with `[[threatseye-live-cyber-threat-map]]` — both are aggregate live attack-map visuals; either serves as a briefing graphic, and neither replaces a per-selector infrastructure lookup.

## Trust & verifiability
`trust: community` — an open-source-project awareness visual; useful as context, not as citable evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bunkerweb-live-cyber-attack-threat-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
