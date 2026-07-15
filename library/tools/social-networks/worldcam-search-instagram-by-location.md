---
id: worldcam-search-instagram-by-location
name: Worldcam - Search Instagram by location
description: Use when you have a `geolocation`/`address` and want to see public Instagram photos taken there — returns images, poster usernames and social-profile links (largely defunct since Instagram removed its location API).
url: http://worldc.am
category: social-networks
path:
- social-networks
bestFor: Historically, surfacing public Instagram posts geotagged to a specific place or venue.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- social-profile
- username
- geolocation
status: down
pricing: free
costNote: Was free with no login; built on the (now-deprecated) public Instagram, Foursquare and Geonames APIs.
opsec: passive
opsecNote: Querying a third-party web front end for a location does not touch the target's account, so it is passive against the subject. You do, however, disclose the location/venue of interest to whoever operates worldc.am; use a sock-puppet browser/IP if the location itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party mashup by "Act Normal"; depended entirely on Instagram's public location API, which Instagram shut down. No first-party guarantees and no recent evidence of a working index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Worldcam
- worldc.am
tags:
- instagram
- geolocation
- location-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Worldcam - Search Instagram by location

> A 2012-era mashup that mapped public Instagram photos to a place — powerful in concept for geolocation OSINT, but broken since Instagram killed its location API.

## When to use
You have a `geolocation` or `address` (a venue, street, or landmark the subject was last associated with) and want to see who was publicly posting Instagram photos *from that spot*. In its working days this let you pivot from "where" to "which accounts" — a strong lead-generator for missing-persons work where the last known location is known but the people around it are not.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://worldc.am in a clean/sock-puppet browser.
2. Search for the place — historically by venue/place name (it resolved place names via Foursquare/Geonames), e.g. `worldc.am/ps/<postcode or place>`.
3. Read the output: a grid of recent public Instagram photos tagged to that location, each linking to the poster's `username`/profile and the exact geotag.
4. Pivot: a poster `username` feeds username OSINT ([[namecheck]]-style checks) and the image feeds reverse-image / face tools.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a place or venue name)
- **Out:** `image`, poster `username` / `social-profile`, `geolocation`
- **Empty/negative result looks like:** a blank grid, a 503/timeout, or the site failing to load at all — which is now the expected state. Do **not** read an empty result as "nobody posted there"; the underlying Instagram location feed is simply no longer available to the tool.

## Gotchas & OpSec
- **Almost certainly defunct.** Instagram removed the public location endpoint this tool relied on (its Platform API was deprecated 2018–2020). At verification the site returned HTTP 503 and all corroborating write-ups date to 2012. Treat `status: down`; confirm live before relying on it.
- OpSec: passive against the subject, but you reveal the searched location to the site operator.
- Even when it worked, coverage was limited to *public* geotagged posts — most modern Instagram posts strip or omit location.

## Overlaps ("do both")
- Pairs with a working location-based Instagram/social search and with reverse-image tools — if Worldcam is down, treat it as a reminder to try current geolocation-search alternatives rather than a dead end.

## Trust & verifiability
`trust: unverified` — a hobbyist third-party mashup with no first-party data guarantees, wholly dependent on an API Instagram has since removed. Any result it does return should be corroborated directly on the poster's live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldcam-search-instagram-by-location |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, address → image, social-profile, username, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
