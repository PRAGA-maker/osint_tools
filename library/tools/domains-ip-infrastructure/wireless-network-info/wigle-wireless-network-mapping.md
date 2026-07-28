---
id: wigle-wireless-network-mapping
name: 'WiGLE: Wireless Network Mapping'
description: Use when you have a Wi-Fi `mac-address` (BSSID) or SSID and want where it has been observed — returns geolocation, or list the networks seen at an address.
url: https://wigle.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- wireless-network-info
bestFor: Geolocating a Wi-Fi/cell network by BSSID/SSID, or enumerating wireless networks observed at a location, from crowd-sourced wardriving data.
selectorsIn:
- mac-address
- geolocation
selectorsOut:
- geolocation
- mac-address
status: live
pricing: freemium
costNote: Free to search with a registered account; volume/API use is rate-limited, and bulk access may require higher tiers.
opsec: passive
opsecNote: You query WiGLE's crowd-sourced archive, not any live network or device — the subject is not alerted. The query is tied to your WiGLE account, so use an appropriate account. Data is historical observations from volunteers, not real-time presence.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Large, long-running crowd-sourced wardriving database; coverage depends on where volunteers have driven, and observations can be dated.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- WiGLE
- wigle.net
tags:
- wardriving
- wifi
- bssid
- geolocation
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# WiGLE: Wireless Network Mapping

> A crowd-sourced map of hundreds of millions of Wi-Fi and cell networks — turn a BSSID or SSID into places it's been seen, or turn a location into the networks observed there.

## When to use
You have a Wi-Fi `mac-address` (BSSID, e.g. from a router in EXIF-adjacent data, a device log, or a photo of a network), or an unusual SSID, and want to know where WiGLE volunteers have observed it — a strong geolocation lead. Or you have an `address`/`geolocation` and want the networks seen there (e.g. to identify a home router's BSSID). It's a wardriving archive: powerful for device/location correlation, low direct person-finding value on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/log in at https://wigle.net/ (a free account is required to search).
2. Use **Search** → query by BSSID (MAC), SSID, or draw/enter a location on the map.
3. Read results:
   - By BSSID/SSID → the observed `geolocation`(s), first/last-seen dates, and encryption/type.
   - By location → the list of networks (`mac-address`/SSID) observed in that area.
4. Pivot: a BSSID's mapped location anchors a device to a place; an SSID unique to a person/business links appearances across locations.

## Inputs → Outputs
- **In:** `mac-address` (BSSID), SSID, or `geolocation`/area
- **Out:** observed `geolocation` (with dates), and network `mac-address`/SSID lists per area
- **Empty/negative result looks like:** "no results" — the network was never wardriven, is new, or is in an area with no volunteer coverage; absence is not proof it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: a free account/login is required, and queries are rate-limited.
- Data is **historical and volunteer-sourced** — coverage is uneven (dense in some cities, absent elsewhere) and observations can be years old; a BSSID may have since moved.
- Common/default SSIDs (e.g. "linksys") are useless for correlation; unique ones are gold.

## Overlaps ("do both")
- Do both with EXIF/metadata tools: a photo's metadata or an app leak can hand you a BSSID/SSID, which WiGLE then geolocates — neither tool does the other's job.

## Trust & verifiability
`trust: community` — a large, well-known crowd-sourced project. The observations are real but volunteer-collected and dated; treat a location hit as a strong lead to corroborate, not a live fix.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wigle-wireless-network-mapping |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | mac-address, geolocation → geolocation, mac-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
