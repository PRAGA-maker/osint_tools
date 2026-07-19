---
id: snapmap-archiver
name: snapmap-archiver
description: Use when you have a `geolocation` (or a Snap Map URL) and want to bulk-download all public Snapchat Snap Map posts from that spot — returns media plus `metadata-exif`-style location/time JSON.
url: https://pypi.org/project/snapmap-archiver/
category: social-networks
path:
- social-networks
bestFor: Downloading and archiving every public Snap Map post from a specific location and radius, with per-snap coordinates and timestamps.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free and open source (GPLv3+); installed from PyPI with pip. No account or API key needed — it uses Snapchat's public Snap Map endpoint.
opsec: passive
opsecNote: You pull from Snapchat's public map API without logging in, so nothing ties the query to the target. Still run from a sock-puppet IP; scraping many tiles quickly can rate-limit or flag your address. Archive fast — public Snaps expire, and once gone they cannot be re-fetched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Community-maintained open-source tool (author "king-millez") on PyPI/GitHub; not affiliated with Snap. Verify the source before running and pin a known version.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- snapmap_archiver
tags:
- snapchat
- snapmap
- geolocation
- Social Media
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# snapmap-archiver

> A CLI/Python tool that scrapes and archives every public Snapchat Snap Map post from a set of coordinates, with location and timestamp metadata.

## When to use
You have a `geolocation` (last-known location of a subject, an incident scene, an event) and want to see and preserve what people posted publicly to the Snap Map there. Because Snaps are ephemeral, this is a capture-before-it-disappears tool: pull the media now, geolocate/timeline it later. Useful when a missing person's last movements may be visible in bystander Snaps at a known place.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install snapmap-archiver` (needs Python 3.10+).
2. Run against a coordinate pair, choosing an output directory:
   `snapmap-archiver -o ./snaps -l="45.4215,-75.6972"`
3. Tune the pull with optional flags: search `--radius` (metres), `--zoom-depth`, and a time window to narrow results; pass multiple `-l` locations or a `-f` input file of URLs/IDs for several spots at once.
4. Read the output: media files land in the output dir, and an optional JSON export lists each snap's coordinates and posting time.
5. Pivot: feed the media into reverse-image/face tools and the JSON coordinates into a mapping/timeline; corroborate a sighting against `[[bellingcat-openstreetmap-search]]` or other geolocation.

## Inputs → Outputs
- **In:** `geolocation` (lat,long), Snap Map URL, or Snap ID
- **Out:** downloaded Snap media + JSON with per-snap `geolocation` and timestamp (`metadata-exif`-style)
- **Empty/negative result looks like:** zero files / empty JSON — no public Snaps were posted in that radius/time window (or they have already expired), not proof no one was there.

## Gotchas & OpSec
- Snaps are ephemeral — anything not archived while live is gone; there is no backfill.
- Only public Snap Map submissions are visible; private stories are not exposed.
- OpSec: passive and login-free, but scraping many tiles fast can rate-limit your IP — throttle and use a sock-puppet.
- It depends on Snap's undocumented endpoint; if Snap changes it, the tool can break until updated.

## Overlaps ("do both")
- Pairs with `[[bellingcat-openstreetmap-search]]` — snapmap-archiver captures who posted from a place; the OSM tool helps confirm and describe the place itself.

## Trust & verifiability
`trust: community` — an independent open-source scraper, not an official Snap product. The media it returns is authentic public Snap content, but the tool's continued function depends on volunteer upkeep; review the code and pin a version.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapmap-archiver |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
