---
id: snap-map
name: Snap Map
description: Use when you have a `geolocation` (or a place/event) and want public Snapchat videos posted there — returns a map of geotagged public Snaps you can view by location and time.
url: https://map.snapchat.com/
category: social-networks
path:
- social-networks
bestFor: Finding public, geotagged Snapchat videos posted from a specific location — eyewitness footage of a place and time.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
- social-profile
status: live
pricing: free
costNote: Free; viewable in a web browser with no Snapchat account required.
opsec: passive
opsecNote: Browsing the public Snap Map is passive — you only view content users chose to submit publicly, and posters aren't told who watched. No login needed; use a clean browser. You're not interacting with any individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Snap Inc. (Snapchat); the Snaps are first-party user submissions to the public map, authoritative as to what was posted where.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- snapchat
- snapchat-com
aliases:
- Snapchat Map
- map.snapchat.com
tags:
- snapchat
- geolocation
- social-media
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Snap Map

> Snapchat's public map of geotagged Snaps — browse eyewitness video from any location and recent time window, straight from a web browser.

## When to use
You have a `geolocation` — a last-known location, an event, a neighborhood — and want to see public Snapchat videos posted from there. Snap Map aggregates Snaps users submitted to "Our Story," pinned to where they were taken, so you can look for footage that might show a subject, a vehicle, or the scene around a relevant time. Genuinely valuable in time-and-place investigations: it's crowd-sourced eyewitness video, viewable without an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.snapchat.com/ in a browser.
2. Navigate/zoom to the location of interest; heat spots indicate clusters of public Snaps.
3. Click a spot to play the geotagged public Snaps; note that Snaps are recent (roughly the last day or so) and vanish over time.
4. Look for a subject, clothing, vehicles, license plates, or background detail that geolocates/timestamps the scene.
5. Pivot: capture/screen-record relevant footage promptly (it expires); a visible person/vehicle → image and plate tools; a poster's handle → `[[snapchat]]` profile checks.

## Inputs → Outputs
- **In:** a `geolocation`/place (and implicitly a recent time window)
- **Out:** public geotagged Snap videos (`image`/video), the `geolocation` they were taken, sometimes the poster's `social-profile`
- **Empty/negative result looks like:** no Snaps at that spot — nobody posted publicly there recently, or the window has expired; a quiet area simply has no submissions (absence ≠ nothing happened).

## Gotchas & OpSec
- **Ephemeral:** public Snaps are recent and disappear — capture anything useful immediately; there's no historical archive to go back to.
- Only shows Snaps users chose to make public ("Our Story"); most Snapchat activity never appears here.
- Geotags are user/device-set and generally reliable, but treat any single Snap's location as corroborated only when detail in the video confirms it.
- Passive and account-free — safe to browse without exposure to the poster.

## Overlaps ("do both")
- Pairs with `[[snapchat]]` — Snap Map surfaces public footage from a place; the Snapchat app/profile side lets you check a specific handle you identify from it.

## Trust & verifiability
`trust: trusted` — first-party Snap Inc. platform. Content is authentic user-submitted video; verify the *meaning* of any clip (who/what/when) against detail visible in the footage itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snap-map |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation, image, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
