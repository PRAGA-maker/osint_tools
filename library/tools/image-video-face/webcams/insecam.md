---
id: insecam
name: Insecam
description: Use when you have a location/country and want to browse publicly accessible (often unsecured) IP cameras there — returns live webcam feeds with approximate geolocation.
url: https://insecam.org/
category: image-video-face
path:
- image-video-face
- webcams
bestFor: Browsing an index of internet-exposed IP cameras by country, city, or coordinates.
input: Country/city filter, map area, or camera tag
output: Live/recent camera feeds with approximate location and device metadata
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- geolocation
- ip-address
status: live
pricing: free
costNote: Free; ad-supported.
opsec: passive
opsecNote: You only view third-party feeds; you do not contact the subject. Note the legal/ethical sensitivity — these are often unsecured private cameras. Use a VPN; do not interact with or attempt to access camera controls.
humanInLoop: true
humanInLoopReason:
- manual-review
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running public directory of cameras left on default/no credentials. Feeds are real but the site is legally/ethically gray; treat purely as a viewing index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- webcams
- cctv
source: arf-seed
lastVerified: ''
enrichment: full
---

# Insecam

> A public directory of internet-exposed IP cameras, browsable by country/city/map — a way to see a live or recent view of a place.

## When to use
You have a `geolocation`/`address` (a city, neighborhood, or coordinates) tied to a missing-person timeline and want to check whether a publicly indexed camera overlooks that area — e.g., a street, parking lot, or storefront a subject may have passed. Use only for situational/scene context, never to surveil a private individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://insecam.org/ and filter by country, then city, or use the map/coordinate view.
2. Open candidate feeds and check the on-screen scene against your location of interest; note the listed city and approximate coordinates.
3. Capture a frame/timestamp if a feed shows a relevant area.
4. Pivot: a confirmed camera location feeds your geolocation timeline; the listed area can corroborate or refine an `address`.

## Inputs → Outputs
- **In:** `geolocation` / `address` (place filter)
- **Out:** `image`/live `image` frames, approximate `geolocation`, sometimes `ip-address`/device info
- **Empty/negative result looks like:** no cameras indexed for the area, or feeds that are offline/relocated — coverage is sparse and shifts as cameras are secured.

## Gotchas & OpSec
- Legal/ethical gate: these are largely unsecured private cameras. Viewing the index is passive, but do not log in, change settings, or use feeds to surveil an individual; jurisdictions vary.
- Listed locations are approximate (geo-IP), often wrong by miles; verify scene contents independently.
- OpSec: passive toward subjects; use a VPN and avoid any interaction with the device.

## Overlaps ("do both")
- Pairs with general camera/IoT discovery (Shodan-style) when you have an `ip-address` rather than a place.

## Trust & verifiability
`trust: community` — a well-known but legally gray public index. Feeds are genuine; locations are unreliable and must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insecam |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review, legal-gate) |
