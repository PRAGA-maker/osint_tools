---
id: snapscraper
name: SnapScraper
description: Use when you have a `geolocation` (lat/long) and want public Snapchat media there — downloads Snap Map "Our Story" videos and their metadata for a coordinate box.
url: https://rhematt.github.io/Snap-Scraper/
category: social-networks
path:
- social-networks
bestFor: Bulk-downloading public Snap Map media (and metadata) for a set of coordinates — capturing eyewitness footage before it expires.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free/open-source CLI (MIT-style, github.com/rhematt/Snap-Scraper); no account. Currently ships as a macOS binary but is compilable.
opsec: passive
opsecNote: Pulls the same public Snap Map data the website serves — posters aren't notified and no login is used. Passive. It queries Snap's public endpoints for a coordinate area; run over a VPN if you want to avoid your IP hitting those endpoints repeatedly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source OSINT tool by rhematt; it automates access to Snapchat's public Snap Map media API, so data is authentic Snap content.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- snap-map
- snapchat
aliases:
- Snap-Scraper
- SnapScraper
tags:
- snapchat
- snap-map
- geolocation
- media-download
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# SnapScraper

> A CLI that downloads public Snap Map ("Our Story") videos and metadata for a set of coordinates — the automated, archivable counterpart to browsing the Snap Map by hand.

## When to use
You have a `geolocation` (latitude/longitude) tied to a case and want every public Snapchat Snap posted there — not just what you can eyeball on the Snap Map, but downloaded with metadata for evidence. Snaps are ephemeral, so grabbing them programmatically preserves potential eyewitness footage of a subject, vehicle, or scene at a place and time. This is a genuinely high-value geolocation-to-footage tool for time-and-place work.

## How to use it (`bestInteractionPattern`: cli)
1. Get the tool from https://rhematt.github.io/Snap-Scraper/ / github.com/rhematt/Snap-Scraper (macOS binary, or compile for your OS).
2. Obtain latitude/longitude for the location of interest from `[[snap-map]]` (map.snapchat.com).
3. Run SnapScraper with those coordinates; it queries the Snap Map for media in that area and lists results with metadata.
4. Save the links and download the media promptly — Snaps expire.
5. Pivot: downloaded footage → look for a subject, vehicles, plates, and geolocation cues; timestamps → build/verify a timeline; a poster handle → `[[snapchat]]` checks.

## Inputs → Outputs
- **In:** a `geolocation` (lat/long coordinate area)
- **Out:** downloadable public Snap Map videos (`image`/video) plus metadata and the `geolocation` they were posted
- **Empty/negative result looks like:** no media returned — no public Snaps were posted in that box in the available window; Snap Map content is recent and sparse in quiet areas.

## Gotchas & OpSec
- **Ephemeral data:** Snaps expire quickly — download immediately; there's no historical back-catalog.
- Relies on Snap's public Snap Map endpoints; if Snap changes them, the tool can break until updated (open-source, community-maintained).
- Ships primarily as a macOS binary — Windows/Linux users compile from source.
- Passive toward posters, but you're hitting Snap's servers repeatedly — a VPN is prudent for volume.

## Overlaps ("do both")
- Pairs with `[[snap-map]]` — use the web Snap Map to find the right coordinates and eyeball activity, then SnapScraper to bulk-download and preserve the media.
- Pairs with `[[snapchat]]` to follow up any identifiable poster/handle.

## Trust & verifiability
`trust: community` — an open-source tool automating Snapchat's own public Snap Map data, so the media is authentic Snap content. Verify what each clip actually shows against detail in the footage; the tool's reliability tracks Snap's API stability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapscraper |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
