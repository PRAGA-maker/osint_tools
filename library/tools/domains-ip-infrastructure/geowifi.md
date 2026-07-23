---
id: geowifi
name: geowifi
description: Use when you have a WiFi `mac-address` (BSSID) or SSID and want to geolocate it — queries Wigle, Apple, Google, Mylnikov and more to return the access point's `geolocation`.
url: https://github.com/GONZOsint/geowifi
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning a WiFi BSSID/SSID into a physical location from public geolocation databases.
selectorsIn:
- mac-address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source (GONZOsint). Some backends (Wigle, Google, Combain) need your own free API keys/credentials; others (Apple, Mylnikov) work without.
opsec: passive
opsecNote: You query third-party WiFi-location databases, not the target's network — you never touch the access point itself, so it's low-footprint. Queries and any API keys are attributable to you; use sock-puppet API accounts and a VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-regarded open-source geolocation tool by GONZOsint; results are only as accurate/current as the public wardriving databases behind it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- GONZOsint/geowifi
- GeoWiFi
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
- wifi
- geolocation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- deepfaceui-github-com
---

# geowifi

> WiFi-to-map lookup: feed it a BSSID or SSID and it pulls the access point's coordinates from the big public wardriving databases at once.

## When to use
You have a WiFi `mac-address` (BSSID) — from a photo's metadata, a device log, a network scan, or a leaked config — or a distinctive SSID, and you want the physical `geolocation` of that access point. Because wardriving projects (Wigle et al.) map millions of APs to coordinates, a BSSID often resolves to a precise location, which can place a device or person at an address. High-value for tying a network name/MAC back to a place.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/GONZOsint/geowifi && pip install -r requirements.txt` (or run the Docker image).
2. Add any API keys you have (Wigle, Google, Combain) to the config to widen coverage; Apple/Mylnikov work key-free.
3. Search by BSSID: `python3 geowifi.py -s bssid 00:11:22:33:44:55`, or by SSID: `python3 geowifi.py -s ssid "MyNetwork"`.
4. Read the aggregated hits; export JSON or view the plotted HTML map.
5. Pivot: a resolved coordinate feeds mapping/street-view and address lookups; a matched SSID at multiple points can trace movement.

## Inputs → Outputs
- **In:** a WiFi `mac-address` (BSSID) or SSID (optionally an approximate `geolocation` to disambiguate)
- **Out:** the access point's `geolocation` (coordinates) from one or more databases, on a map/JSON
- **Empty/negative result looks like:** no hits — the BSSID was never wardriven, or the SSID is too common (many false coordinates); a blank BSSID result means "not in these databases", not "doesn't exist".

## Gotchas & OpSec
- SSID searches are noisy — common names (e.g. "linksys") return many unrelated APs; BSSID is far more precise.
- Coverage/accuracy depend on the databases; Wigle needs a (free) account, and results can be stale as APs move.
- OpSec: passive — you query databases, not the AP — but use sock-puppet API accounts and a VPN.

## Overlaps ("do both")
- Complements EXIF/metadata analysis — extract a BSSID or geotag from a photo first, then use geowifi to resolve any captured BSSID to coordinates for cross-confirmation.

## Trust & verifiability
`trust: community` — a popular, auditable open-source tool; the coordinates come from public wardriving datasets, so accuracy hinges on those sources and should be corroborated with a second location signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geowifi |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | mac-address, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
