---
id: antennasearch
name: AntennaSearch
description: Use when you have a US address or coordinates near where a person was last seen and want to identify nearby cell towers/antennas and their owners to anchor mobile-coverage or device-location reasoning.
url: https://www.antennasearch.com/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Mapping cell towers and antennas (with owner/registration data) around a US location.
selectorsIn: [address, geolocation]
selectorsOut: [geolocation, employer-org]
status: live
pricing: free
costNote: Free public search; the underlying tower data derives from FCC ASR/registration records.
opsec: passive
opsecNote: You only query a public US tower database; no contact with the target or their devices. Nothing about your query reaches the person of interest.
humanInLoop: true
humanInLoopReason: [captcha]
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent US tower/antenna lookup site that surfaces FCC Antenna Structure Registration and licensing data; not an official government source, so cross-check against the FCC directly.
missingPersonsRelevance: medium
coverage: [us]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [cellmapper-net, celltowermaps-com, beacondb]
aliases: []
tags: [cell-tower, fcc, antenna]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# AntennaSearch

> A free US-only database of cell towers and antennas, searchable by address, that returns each structure's location, owner, and registration details.

## When to use
You have an `address` or `geolocation` (e.g. a last-known location, a photo background, a ping area) inside the United States and want to know what mobile infrastructure is physically nearby — which towers exist, who owns them, and what registration/frequency data is on file. Useful for sanity-checking a claimed cell-tower hit, identifying a structure visible in a photo, or building a map of carriers serving a search area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.antennasearch.com/.
2. Enter a US street `address` (or as close as you can get) in the search box and submit; you may be asked to confirm/disambiguate the address.
3. Review the two result sets it returns for the radius around that point: **existing structures** (registered towers) and **processing/pending** applications.
4. Click a structure to read its detail page — `geolocation` (lat/long), owner/`employer-org`, structure height, and the FCC registration (ASR) number.
5. Pivot: take the ASR number to the FCC ASR registration site to confirm owner and licensees; feed coordinates into `[[cellmapper-net]]` or `[[celltowermaps-com]]` to map carrier-specific coverage.

## Inputs -> Outputs
- **In:** `address`, `geolocation`
- **Out:** `geolocation` (tower coordinates/height), `employer-org` (tower owner/operator), registration IDs
- **Empty/negative result looks like:** no structures listed for the radius (rural/unregistered area), or only "processing" applications with no built towers. A non-US address returns nothing.

## Gotchas & OpSec
- Human-in-the-loop: address geocoding/CAPTCHA-style confirmation may interrupt automation; do it manually.
- US-only — do not use outside the United States.
- Owner names reflect the tower/structure owner, not necessarily the carrier transmitting from it; a single tower commonly hosts multiple carriers (co-location). Don't infer a specific carrier from ownership alone.
- This is a third-party mirror/index of FCC data, not the FCC itself; treat registration details as a lead and confirm against the official ASR database before relying on them.

## Overlaps ("do both")
- Pairs with `[[cellmapper-net]]` and `[[celltowermaps-com]]` because AntennaSearch gives ownership/registration while those map carrier coverage and cell IDs.
- Pairs with `[[beacondb]]` when you also have a BSSID/cell ID rather than just an address.

## Trust & verifiability
`trust: community` — independent, established US tower-lookup service that republishes FCC Antenna Structure Registration data. Reliable as a pointer, but verify any owner/registration claim against the FCC ASR system directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | antennasearch |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
