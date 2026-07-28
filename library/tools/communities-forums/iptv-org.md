---
id: iptv-org
name: iptv-org
description: Use when you have a country/region and want its publicly-listed IP TV channels and (sometimes) livestream links — returns geolocation-scoped media sources.
url: https://iptv-org.github.io/
category: communities-forums
path:
- communities-forums
bestFor: Finding publicly-available IPTV channels by country to monitor local/regional broadcasts.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; the channel database and M3U playlists are on GitHub, no account required.
opsec: passive
opsecNote: Browsing the channel list/API is passive. Opening a livestream connects you to the stream host (its IP sees you) — use a VPN if you don't want that host to log your IP. Only public/legal streams; don't use it to access pirated content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large community-maintained index of publicly available streams; links rot frequently and legality of individual streams varies by region — verify before relying on one.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- iptv-org
- iptv github
tags:
- tv
- media-monitoring
- livestream
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# iptv-org

> A big community-maintained index of publicly available IPTV channels across ~200 countries — a way to pull up local/regional TV to watch what a place is broadcasting.

## When to use
You want eyes (and ears) on live or listed broadcast media for a country or region — monitoring local news during a developing event, sampling regional programming, or finding a specific public channel's stream. iptv-org catalogs thousands of channels by country with metadata and, where available, livestream links and machine-readable playlists/API. It's a media-monitoring/context source tied to `geolocation`, not a person finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iptv-org.github.io/ and browse/filter channels by country (`geolocation`) or category.
2. Read the channel metadata (country, language, category); open a livestream link where provided.
3. For automation, pull the project's M3U playlists / JSON API from its GitHub to script channel selection.
4. Use a VPN when opening streams if you don't want the stream host to log your IP.
5. Pivot: use a monitored channel as an event-context feed alongside social and webcam sources for the same location.

## Inputs → Outputs
- **In:** a country/region (`geolocation`) or channel name
- **Out:** publicly-listed channels with metadata and (sometimes) livestream links — media context for that place. No person-level `selectorsOut`.
- **Empty/negative result looks like:** a channel with no working stream link, or thin coverage for a country — links rot constantly, so a dead stream is expected, not an error.

## Gotchas & OpSec
- OpSec: browsing is passive; opening a stream exposes your IP to the host — VPN if needed.
- Link rot is heavy and stream legality varies by jurisdiction; verify a stream is legitimate/public before using or citing it.
- It provides media, not identities — wrong tool for finding a person.

## Overlaps ("do both")
- Pairs with webcam directories (`[[city-webcams-com]]`) and social monitoring — IPTV gives broadcast context for a place, webcams give live scene, socials give the ground-level chatter.

## Trust & verifiability
`trust: community` — a large open-source community index; useful as a directory, but individual streams are third-party, volatile, and of varying legality — confirm each one you rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iptv-org |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
