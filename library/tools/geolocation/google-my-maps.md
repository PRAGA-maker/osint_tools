---
id: google-my-maps
name: Google My Maps
description: Use when you have multiple `geolocation`/`address` points and want to plot, annotate, and visually correlate them on a shared custom map.
url: https://www.google.com/maps/about/mymaps
category: geolocation
path:
- geolocation
bestFor: Building a custom annotated map to plot and correlate location leads in a case.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free with any Google account.
opsec: passive
opsecNote: A workspace/visualization tool — it does not query the target. Maps are private by default; do not share a case map with a public/anyone-with-link setting.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product, stable and widely used for OSINT geospatial casework.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Google My Maps

> Google's free custom-map builder for plotting, layering, and annotating your own location leads on top of Google Maps.

## When to use
You have collected several `geolocation`/`address` leads — last-known location, friends' homes, sightings, ATM/transit points — and need to see them together to find a pattern, travel corridor, or cluster. My Maps is the canvas you drop those pins on; it does not find new data, it organizes what you have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL, sign in to a Google research account, and click "Create a new map."
2. Add points by searching an `address`/place or pasting `geolocation` coordinates; organize them into layers (e.g., "sightings," "associates," "transit").
3. Annotate each pin with date/source notes and color-code by lead type. Import a CSV/KML of bulk points if you have one.
4. Read the map for spatial patterns; pivot promising pins into [[instant-google-street-view]] or [[here-maps]] for ground-level context.

## Inputs → Outputs
- **In:** `geolocation`, `address` (manually entered or CSV/KML imported)
- **Out:** an annotated `geolocation` map layer you can analyze and export (KML/KMZ)
- **Empty/negative result looks like:** an empty canvas — this tool produces nothing on its own; value depends entirely on the leads you plot.

## Gotchas & OpSec
- Human-in-the-loop: Google account login required.
- Default sharing is private — keep it that way; an accidental "anyone with link" exposes the whole investigation.
- OpSec: passive — purely a visualization workspace; nothing is sent to or about the target.

## Overlaps ("do both")
- Pairs with [[gpsvisualizer]] — GPSVisualizer is stronger for converting/cleaning raw coordinate files before you import them into My Maps for analysis.

## Trust & verifiability
`trust: trusted` — a first-party Google service; reliable and standard for casework mapping.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-my-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
