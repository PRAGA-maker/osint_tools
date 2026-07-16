---
id: geomacfinder
name: GeoMacFinder
description: Use when you have a Wi-Fi access point `mac-address` (BSSID) and want its physical location via a Telegram bot — returns an approximate `geolocation`.
url: https://t.me/geomacbot
category: messaging
path:
- messaging
bestFor: Geolocating a Wi-Fi access point from its MAC/BSSID by querying wardriving databases through a Telegram bot.
selectorsIn:
- mac-address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free basic BSSID lookups; higher volume or richer results may be credit-gated inside the bot.
opsec: passive
opsecNote: You query a MAC address against a wardriving database, not the target's device or network, so it does not touch the subject. The bot operator logs your queries — run from a sock-puppet Telegram account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous Telegram bot fronting Wi-Fi geolocation databases (e.g. WiGLE-style datasets); coverage and accuracy are unverified and depend on prior wardriving of that AP.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- geomacbot
- Geo Mac Finder
tags:
- telegram
- wifi-geolocation
- mac-address
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# GeoMacFinder

> A Telegram bot that maps a Wi-Fi BSSID to a physical location — turn a MAC address pulled from a photo, router, or device log into a point on the map.

## When to use
You have a Wi-Fi access point `mac-address` (BSSID) — from a subject's router, a network name/BSSID captured in an image or device, or a leaked connection log — and you want to place it geographically. A hit can pin a home, workplace, or last-known location for a missing person when the AP has been seen by wardriving projects.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open https://t.me/geomacbot and press Start.
2. Send the BSSID (`mac-address`, colon- or dash-separated).
3. Read the reply: if the AP is in the wardriving dataset, the bot returns approximate coordinates (`geolocation`) and sometimes a nearby `address`.
4. Pivot: drop the coordinates into a map, then cross-check with imagery/street-view; combine multiple nearby BSSIDs to triangulate.

## Inputs → Outputs
- **In:** `mac-address` (Wi-Fi BSSID)
- **Out:** approximate `geolocation` (lat/long), sometimes a nearby `address`
- **Empty/negative result looks like:** "not found" — the access point has never been logged by the underlying wardriving database (common for indoor/rural or recently-installed APs); absence is not proof of anything.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account-login; use a sock puppet.
- Only works if the BSSID was previously observed by wardrivers; coverage is patchy and skewed to urban areas.
- A single BSSID gives an approximate point; positions can be stale if the router moved. Corroborate before treating a location as current.

## Overlaps ("do both")
- Pairs with WiGLE-style Wi-Fi geolocation databases — cross-check any coordinate across a second source, since datasets differ in coverage.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram front-end over third-party wardriving data; the coordinate is only as good (and as current) as the last time someone drove past that AP.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geomacfinder |
| category | messaging |
| selectorsIn → selectorsOut | mac-address → geolocation, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
