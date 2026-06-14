---
id: google-maps-update-alerts
name: Google Maps Update Alerts
description: Use when you have a `geolocation`/`address` of interest and want to be notified when Google's satellite/aerial imagery of that spot refreshes.
url: https://followyourworld.appspot.com/
category: geolocation
path:
- geolocation
bestFor: Getting email alerts when Google updates satellite imagery for a watched location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free; requires a Google account.
opsec: passive
opsecNote: You only register a location to watch; the target is never contacted. Alerts arrive to your Google account, so use a research account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legacy Google "Follow Your World" project on appspot.com; long unmaintained and may be defunct. Verify it still loads before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- historic-aerials
- land-viewer
aliases:
- Follow Your World
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Maps Update Alerts

> Google's legacy "Follow Your World" service that emails you when Google Maps/Earth imagery for a pinned location is refreshed.

## When to use
You have a specific `geolocation` or `address` (a last-known residence, a campsite, a property tied to a missing person) and you want to know the moment Google publishes newer satellite/aerial imagery of it — so you can re-check for changes like a moved vehicle, new structures, or disturbed ground. Passive monitoring; it does not search for people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and sign in with a Google research account (not your personal one).
2. Pick a location on the map and confirm the watch point.
3. Wait — Google emails the account when imagery for that area updates.
4. Pivot: when an alert fires, re-examine the spot in [[historic-aerials]] or [[land-viewer]] and compare against the prior capture.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a pinned spot)
- **Out:** an email notification keyed to that `geolocation` when imagery refreshes
- **Empty/negative result looks like:** no email for months (updates are infrequent), or the appspot page failing to load (service may be retired).

## Gotchas & OpSec
- Human-in-the-loop: Google account login required.
- This is a very old appspot.com project; it may be dead. Treat absence of alerts as inconclusive, not "no change."
- OpSec: passive — registering a watch point reveals nothing to the target. Keep alerts in a dedicated account.

## Overlaps ("do both")
- Pairs with [[historic-aerials]] and [[land-viewer]] — those let you pull the actual time-series imagery once an alert tells you something changed.

## Trust & verifiability
`trust: unverified` — a Google-run but effectively abandoned utility; confirm it still functions before depending on it for a live case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-maps-update-alerts |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
