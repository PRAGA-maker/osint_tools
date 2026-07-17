---
id: cyclocane
name: Cyclocane
description: Use when a photo/event references a storm or you need to know what tropical cyclone was active at a place and time — returns current and recent hurricane/cyclone tracks and details for cross-checking a timeline.
url: https://cyclocane.com
category: geolocation
path:
- geolocation
bestFor: Checking which tropical storm/hurricane was active in a region to corroborate a photo or event date.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, independently run tracker aggregating official NHC/JTWC data; donations optional, no paywall.
opsec: passive
opsecNote: You browse a public weather map; no target is contacted. Fully passive. Use a VPN only for general hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent aggregator presenting data from official agencies (US National Hurricane Center, Joint Typhoon Warning Center); the source data is authoritative, the site is a convenient viewer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cyclocane.com
- cyclone hurricane tracker
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Cyclocane

> A live cyclone-and-hurricane tracker aggregating official NHC/JTWC data — useful in OSINT for tying weather to a place and time when a storm appears in evidence.

## When to use
A photo, post, or account mentions or shows a tropical storm — flooding, wind damage, a named hurricane, evacuation — and you need to confirm which cyclone was active, where, and when. Cyclocane shows current active storms and their tracks/intensity, and links to the official forecasts. Matching a claimed storm to the real historical track corroborates (or breaks) a timeline and can support geolocation of a weather-driven scene. It's a narrow corroboration tool, hence low direct person-finding relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cyclocane.com and view the map of currently active systems, or use the site's archive/named-storm pages for a specific storm.
2. Click a storm for its track, current position, wind speed, and forecast cone (sourced from NHC/JTWC).
3. Match the storm's name/location/date against what the evidence claims or shows.
4. For historical events, follow through to the official agency's archive (NHC/JTWC) for authoritative past-track data — cyclocane emphasizes current/recent activity.
5. Pivot: a confirmed storm + location narrows a photo's date and region; the region feeds other geolocation checks.

## Inputs → Outputs
- **In:** a region/`geolocation` and an approximate time, plus a claimed/observed storm
- **Out:** the matching cyclone's track, intensity, and dates (`geolocation`) for corroboration
- **Empty/negative result looks like:** no active/relevant storm for that area/time — either the claim is wrong, the timing is off, or the storm predates the site's live view (use the official NHC/JTWC archives for older events).

## Gotchas & OpSec
- Strongest for **current and recent** systems; for older historical storms go to the official NHC/JTWC best-track archives, which are the authoritative record.
- It's a convenience viewer, not the source of record — cite the official agency data for a report.
- OpSec: **passive** — public map browsing, no target contact.

## Overlaps ("do both")
- Pairs with historical weather-archive tools and the official NHC/JTWC databases — cyclocane for a quick current-storm read, the archives for authoritative past tracks used in geolocation/timeline work.

## Trust & verifiability
`trust: community` — an independent site, but it surfaces official NHC/JTWC data, so the underlying facts are authoritative; confirm decisive details against the source agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyclocane |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
