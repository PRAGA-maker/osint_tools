---
id: wifispc-com
name: Wifispc.com
description: Use when you have a `geolocation`/`address` (venue, city, or coordinates) and want known public WiFi hotspots there — returns SSIDs, passwords, and mapped points that can corroborate or narrow a location.
url: https://wifispc.com/
category: geolocation
path:
- geolocation
bestFor: Finding community-submitted free WiFi hotspots (SSID + password) at a city, venue, or map point.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to search on the web and mobile apps; supported by ads. No account required to browse the map.
opsec: passive
opsecNote: You query WiFi Space's own database, not the target's infrastructure, so the subject is not alerted. Nothing you enter reaches the venue. Treat community-submitted SSIDs/passwords as unverified leads, and never actually connect to a target's network as part of an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced hotspot database; entries are user-submitted and unverified, so coverage and accuracy vary widely by region.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WiFi Space
- wifispc
tags:
- wifi
- hotspot-map
- geolocation
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Wifispc.com

> Crowd-sourced map of free public WiFi hotspots worldwide — search a place, see the networks (and often passwords) reported there.

## When to use
You have a `geolocation` or `address` — a café, hotel, airport, neighborhood, or city — and want to know what public WiFi networks have been reported at that spot. Useful for corroborating that a venue exists and is frequented, for spotting an SSID that matches a name/handle you're tracking, or as a soft geolocation aid when someone mentions connecting to a named network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wifispc.com/ and allow the map to load (grant location only if you want your own area centered — otherwise search manually).
2. Search by city, venue, or pan/zoom the map to your area of interest (`selectorsIn`).
3. Read the plotted points: each shows an SSID, sometimes a password, and the mapped location (`selectorsOut`).
4. Pivot: an unusual SSID (a personal/business name) can be cross-checked against usernames or business records; a cluster of hotspots confirms a venue is real and active.

## Inputs → Outputs
- **In:** `geolocation` / `address` (place, venue, or map coordinates)
- **Out:** WiFi hotspot points — SSID, optional password, `geolocation`
- **Empty/negative result looks like:** a bare map with no pins in the searched area — meaning no one has submitted a hotspot there, NOT that no WiFi exists.

## Gotchas & OpSec
- Human-in-the-loop: none required to browse.
- OpSec: passive — you're reading a public crowd database, so nothing reaches the target. Do not actually connect to any listed network during an investigation.
- Data is user-submitted and stale in many regions; treat any SSID/password match as a lead, not fact.

## Overlaps ("do both")
- Pairs with [[wigle-net]]-style BSSID/SSID geolocation databases when you have a network name to place — WiFi Space indexes free-hotspot listings, while WiGLE-type tools map by radio identifiers.

## Trust & verifiability
`trust: community` — the entire database is crowd-sourced and unverified; individual entries can be wrong, outdated, or promotional, so confirm any geolocation lead against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wifispc-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
