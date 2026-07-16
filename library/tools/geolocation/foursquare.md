---
id: foursquare
name: Foursquare
description: Use when you have a `geolocation`/`address` or a venue and want place details, photos, and user tips — returns venue `geolocation`, `address`, and associated user activity.
url: https://foursquare.com
category: geolocation
path:
- geolocation
bestFor: Enriching a place/venue with precise coordinates, photos, tips, and (where public) the users who engaged with it.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
- social-profile
status: live
pricing: freemium
costNote: Browsing venue pages, photos, and tips is free. Programmatic/bulk access via the Foursquare Places API is a paid developer product with a free tier.
opsec: passive
opsecNote: Reading public venue pages and tips is passive. If you engage (check in, comment, follow) via a logged-in account you leave traces and may notify others — browse read-only, and use a sock-puppet account if you must log in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established location-technology company; venue/place data is well-maintained. Personal check-in data is now largely in its Swarm app and much less public than it once was.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Foursquare City Guide
- Swarm
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- foursquare-business-search
- foursquare-time-machine
---

# Foursquare

> A global places database with user tips and photos — pin a venue to exact coordinates, mine its photos/tips, and surface the users who reviewed it.

## When to use
You have a place tied to your subject — a venue named in a post, an `address`, or approximate `geolocation` — and you want to enrich it: exact coordinates, an address, opening context, user-uploaded photos, and tips whose authors (`social-profile`) may include or connect to your subject. Also useful to identify a location from a photo's visible venue, or to build a picture of places a subject frequents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://foursquare.com and search the venue name, `address`, or area (or navigate the map to a `geolocation`).
2. Open the venue page: read the precise coordinates/address, category, photos, and user tips.
3. Note the tip/photo authors — their `social-profile`s are pivotable, and repeated authors can indicate regulars.
4. Cross-reference a subject's known usernames against tip authors on venues they'd plausibly visit.
5. Pivot: coordinates feed mapping tools; venue photos feed reverse-image/geolocation verification; tip-author profiles feed username OSINT.

## Inputs → Outputs
- **In:** venue name, `address`, or `geolocation`
- **Out:** venue `geolocation` + `address`, category, photos, and user tips with `social-profile` authors
- **Empty/negative result looks like:** venue not found or thin (no photos/tips) — common for private residences and low-traffic places. Personal, real-time check-in feeds are mostly gone from the public web (moved into Swarm), so do not expect a live "who's here now" list.

## Gotchas & OpSec
- The rich per-user check-in history that made Foursquare an OSINT classic is largely deprecated/private now; treat it primarily as a places+tips source.
- Venue data can be user-edited and occasionally wrong or duplicated; confirm coordinates against a map.
- Bulk/structured pulls need the paid Places API, not the website.

## Overlaps ("do both")
- Pairs with `[[google-maps]]`/`[[instagram]]` location pages — each surfaces different photos and reviewers for the same place, so cross-check venues across all three.

## Trust & verifiability
`trust: trusted` — a reputable location-data company; venue/place data is reliable, though user tips are self-published and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foursquare |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address, social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
