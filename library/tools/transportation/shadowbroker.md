---
id: shadowbroker
name: Shadowbroker
description: Use when you have a `geolocation` / area of interest and want a self-hosted map fusing 60+ live OSINT feeds (aircraft, ships, satellites, fires, conflict, comms) plus a built-in recon toolkit — returns geolocated activity and infrastructure leads.
url: https://github.com/BigBodyCobain/Shadowbroker
category: transportation
path:
- transportation
bestFor: Multi-domain geospatial situational awareness from 60+ open feeds in one self-hosted dashboard.
selectorsIn:
- geolocation
- ip-address
selectorsOut:
- geolocation
- ip-address
status: live
pricing: freemium
costNote: Free and open-source (AGPL-3.0), self-hosted via Docker. Optional paid APIs (Shodan, Sentinel Hub, Global Fishing Watch) add layers; your keys stay local.
opsec: passive
opsecNote: Self-hosted, and it proxies sensitive recon queries server-side so your API keys aren't exposed in the browser. Aggregating public feeds is passive, but the recon toolkit (IP geolocation, DNS, WHOIS, BGP) and any Shodan queries disclose the selectors you look up to those upstream services — use dedicated research keys.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Popular community project (BigBodyCobain); broad-scope aggregator, so verify any single feed's data at its source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- shadow-broker
tags:
- geoint
- aggregator
- aviation
- satellite
source: gh-topic-osint-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Shadowbroker

> A self-hosted, decentralized OSINT dashboard that fuses 60+ real-time public feeds — flights, ships, satellites, seismic, fires, conflict, CCTV, comms — onto one map with 40+ toggleable layers and a built-in recon toolkit.

## When to use
You have a `geolocation` / region of interest and want broad, multi-domain situational awareness — what's flying, sailing, burning, or being reported there right now — plus quick infrastructure lookups, all in one place. It's GEOINT/situational, not person-lookup, so its missing-persons value is indirect (e.g. contextualising a location or narrowing a search area).

## How to use it (`bestInteractionPattern`: docker)
1. Self-host with Docker: `git clone https://github.com/BigBodyCobain/Shadowbroker && cd Shadowbroker && docker compose pull && docker compose up -d`, then open `http://localhost:3000`.
2. (Optional) Add API keys (Shodan, Sentinel Hub, Global Fishing Watch) in `.env` to enable those layers; keys stay local and recon queries are proxied server-side.
3. Navigate to your area of interest and toggle the relevant layers (OpenSky flights, AIS ships, CelesTrak satellites, USGS quakes, NASA FIRMS fires, GDELT geopolitics, etc.).
4. Use the recon toolkit (IP geolocation, DNS, WHOIS, BGP, sanctions lookup) and region dossiers for detail; build entity relationship graphs.
5. Pivot: geolocated activity and looked-up `ip-address`/infrastructure feed dedicated trackers and enrichment tools.

## Inputs → Outputs
- **In:** `geolocation` / area of interest, or an `ip-address`/host for the recon toolkit.
- **Out:** geolocated multi-feed activity, region dossiers, and recon results (`ip-address` geolocation, DNS/WHOIS/BGP) with entity graphs.
- **Empty/negative result looks like:** sparse layers over an area — low real activity or a feed with poor coverage there; check each layer's source.

## Gotchas & OpSec
- Broad but shallow per-feed: it aggregates, so confirm any specific track/detection at the authoritative source (OpenSky, AIS provider, USGS, etc.).
- Some layers require your own (free or paid) API keys; without them those layers stay dark.
- Self-host it; the recon toolkit makes real queries, so use research keys and a controlled IP.

## Overlaps ("do both")
- Overlaps focused maritime/airspace tooling like `[[phantom-tide]]` — Shadowbroker is the wide multi-domain map, Phantom Tide is deeper convergence scoring for sea/air; cross-check flagged activity between them.

## Trust & verifiability
`trust: community` — a popular community aggregator; its strength is breadth of open feeds, but because it re-serves other people's data, verifiability rests on tracing each layer back to its named upstream source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadowbroker |
| category | transportation |
| selectorsIn → selectorsOut | geolocation, ip-address → geolocation, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
