---
id: snradar
name: SnRadar
description: Use when you have a geolocation (or a VK profile) and want to find VKontakte photos taken near that point — returns social-profile links and geotagged image leads.
url: https://snradar.azurewebsites.net/
category: social-networks
path:
- social-networks
bestFor: Map-based search for geotagged VKontakte photos around a location.
selectorsIn:
- geolocation
- username
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free web tool. No account required; it queries VK's public photo data through VK's API.
opsec: passive
opsecNote: Searches VK's public geotagged-photo index; it does not visit the target's profile or notify anyone. Runs on a free Azure host that frequently sleeps — a passive lookup, but treat the third-party host as untrusted with your query terms.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing community VK-OSINT utility referenced by OSINTCurio.us and Russian-speaking OSINT lists. Hobbyist-run on free Azure hosting, so uptime is unreliable and it may break when VK changes its API.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osintdashboard-azurewebsites-net
- sn-radar-vk-photo-search
aliases:
- Snradar
- SN Radar
tags:
- vk
- russia
- geolocation
- photo-search
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# SnRadar

> Map-driven VKontakte photo search — draw an area on a map and it surfaces geotagged VK photos taken there, a classic Russian-speaking geo-OSINT pivot.

## When to use
You have a `geolocation` (a place a subject was, a home/work address, an incident site) and want to see who has posted VK photos from that spot — or you have a VK `username` and want to place their photos on a map. VKontakte's huge, historically geotag-rich photo base makes this a strong tool for tying a person to a location and discovering associates who posted nearby at the same time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://snradar.azurewebsites.net/ (allow a few seconds — the free Azure host often cold-starts).
2. Navigate/zoom the map to your area of interest and define a search radius/box.
3. Optionally set a date range to bound the photos to a relevant window.
4. Run the search: it returns geotagged VK photos in that area, each linking back to the poster's VK profile (`social-profile`).
5. Pivot: click through to the VK profiles, then run VK-specific tooling; cross-reference the sibling `[[sn-radar-vk-photo-search]]` for the same data through a different front-end.

## Inputs → Outputs
- **In:** `geolocation` (map area + optional date range), or a VK `username`.
- **Out:** `social-profile` (VK profile links) and `image` (geotagged photo leads) for the selected area/time.
- **Empty/negative result looks like:** no pins in the box — either no one geotagged VK photos there, VK has since stripped the geodata, or the tool's API access is throttled/broken. Empty is common now that VK exposes far fewer geotags than it once did.

## Gotchas & OpSec
- Human-in-the-loop: the tool depends on VK's API and free Azure hosting, so expect cold-start delays, rate-limiting, and occasional outages — retry rather than assuming the target has no photos.
- OpSec: **passive** — it queries VK's public photo index, not the target's profile, and sends no notification. Your query terms do pass through a third-party hobbyist host; keep sensitive specifics minimal.
- Geotag coverage has declined sharply as VK tightened privacy, so historical photos are your best hits; recent activity may be invisible.

## Overlaps ("do both")
- Pairs with `[[sn-radar-vk-photo-search]]` and `[[osintdashboard-azurewebsites-net]]` — same VK geo-photo data surfaced through sibling interfaces; if one host is asleep or broken, the other may still return results.

## Trust & verifiability
`trust: community` — a well-known but hobbyist-maintained VK-OSINT utility (referenced by OSINTCurio.us and CIS OSINT lists). Marked `status: degraded` because it runs on free hosting and rides VK's shifting API; verify any hit by opening the underlying VK photo/profile directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snradar |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
