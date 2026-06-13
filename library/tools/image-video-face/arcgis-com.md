---
id: arcgis-com
name: arcgis.com
description: Use when you have a place/area and want to plot geotagged public social media (Flickr, YouTube, Twitter, webcams) on a map to find imagery from a location.
url: http://www.arcgis.com/apps/PublicInformation/index.html
category: image-video-face
path:
- image-video-face
bestFor: Esri "Public Information Map" template that overlays geotagged social media (Flickr photos, YouTube videos, tweets, webcams) on a map by location.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- social-profile
- geolocation
status: degraded
pricing: free
costNote: The base map app is free to view; configuring your own instance needs a (free or paid) ArcGIS account. The default index.html template instance often loads empty and must be configured with a search location/feeds.
opsec: passive
opsecNote: Pulls from public social-media APIs by location; you do not contact the subject. Older social feed integrations (Twitter, Flickr API tiers) may be broken, so coverage is unreliable.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Esri/ArcGIS is a major, reputable GIS vendor. This specific legacy Public Information Map template is dated and its social feeds are degraded, but the platform itself is authoritative.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ArcGIS Public Information Map
- Esri Public Information Map
tags:
- flickr
- Flickr & Similar Linked Sites
- social-media-mapping
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# arcgis.com (Public Information Map)

> Esri's configurable map template that plots geotagged public social media — Flickr, YouTube, tweets, webcams — over a base map so you can pull imagery from a specific place.

## When to use
You have a `geolocation` / `address` (a missing person's last-known area, an incident site) and want to see geotagged `image`s and `social-profile` posts that originated from that spot — e.g. Flickr photos or YouTube clips tagged near the location, which may show the person, vehicles, or scene context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.arcgis.com/apps/PublicInformation/index.html. The default instance loads as a template — set a search location.
2. Pan/zoom to your area of interest and enable the social-media layers (Flickr, YouTube, etc.) in the app config.
3. Click clustered markers to view the geotagged media and the originating account.
4. Pivot: open the source post/account for the full media and the poster's `social-profile`; reverse-image any photo of interest.

## Inputs → Outputs
- **In:** `geolocation` / `address` (the area to map)
- **Out:** `image` (geotagged photos/videos), `social-profile` (posters), confirmed `geolocation`
- **Empty/negative result looks like:** no markers in the area — either nothing was geotagged there or the legacy social feeds are no longer returning data (likely, given the template's age).

## Gotchas & OpSec
- Degraded: this is an old Esri template; several upstream social APIs (Twitter, older Flickr tiers) have changed or closed, so layers frequently return nothing. Treat absence of data as inconclusive.
- Human-in-the-loop: you must configure the location/layers and manually inspect markers.
- OpSec: passive — you query public APIs by geography, never the subject.

## Trust & verifiability
`trust: trusted` — Esri/ArcGIS is an industry-standard GIS provider, but this specific legacy app is dated and its feeds are unreliable. Confirm any geotag against the source post and corroborate with a current social-media-by-location tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arcgis-com |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → image, social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual review) |
