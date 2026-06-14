---
id: wayback-imagery
name: Wayback Imagery
description: Use when you need to see how a location's satellite imagery looked on specific past dates — to detect change, date a structure, or match an undated photo to an imagery era.
url: https://livingatlas.arcgis.com/wayback/
category: geolocation
path:
- geolocation
bestFor: Browsing dated archives of Esri World Imagery to detect change and narrow when a scene was photographed.
input: Location and imagery version selection
output: Historical basemap snapshots by release date
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free to browse via the web app; programmatic tiles available through Esri.
opsec: passive
opsecNote: Browsing archived satellite tiles; no contact with the target. Esri sees your queries like any web service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Esri Living Atlas "World Imagery Wayback" — authoritative, versioned satellite imagery archive maintained by Esri.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- view-in-google-earth
- travel-by-drone
aliases:
- World Imagery Wayback
- Esri Wayback
tags:
- satellite-imagery
- change-detection
- chronolocation
source: arf-seed
lastVerified: ''
enrichment: full
---

# Wayback Imagery

> Esri's "World Imagery Wayback" — a versioned archive of the global satellite basemap that lets you step through dated releases of the same spot.

## When to use
You have a `geolocation` and need its imagery history: did a structure/vehicle/tent/road exist on a given date, when did something appear or disappear, or which imagery era matches an undated photo. Stepping through dated releases gives change-detection that a single current satellite view can't — directly useful for narrowing when a missing-persons scene was active and for dating ground features.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://livingatlas.arcgis.com/wayback/.
2. Zoom/pan to the location (or paste coordinates).
3. The sidebar lists imagery releases whose pixels changed for that view; each is tagged with a capture/release date. Click through them to compare.
4. Toggle releases on/off and use the date list to bracket when a feature first appeared or vanished.
5. Pivot: take a dated finding into the case timeline; cross-check with Google Earth's historical imagery via [[view-in-google-earth]], or get low-altitude context from [[travel-by-drone]].

## Inputs → Outputs
- **In:** `geolocation` (map view / coordinates).
- **Out:** dated satellite snapshots and the list of capture dates for that spot (refines `geolocation`; helps date imagery → supports `metadata-exif` reasoning).
- **Empty/negative result looks like:** few or no distinct releases for a remote area (low revisit/update frequency), or cloud-obscured captures — coverage and cadence vary by region.

## Gotchas & OpSec
- "Release date" is when Esri published that imagery, which can lag the actual capture date — note the distinction.
- Update frequency is far higher over cities than over rural/remote areas; sparse archives are normal in the latter.
- No login or captcha; passive. Esri logs requests like any web service — use ordinary OpSec hygiene, but there is no target interaction.

## Overlaps ("do both")
- Use **with** Google Earth's historical imagery ([[view-in-google-earth]]); the two archives have different capture dates, so one often shows a date the other misses.

## Trust & verifiability
`trust: trusted` — first-party Esri product; imagery is authoritative and each layer is explicitly versioned and dated for verifiability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-imagery |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
