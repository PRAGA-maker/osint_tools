---
id: parler-capitol-videos
name: Parler Capitol Videos
description: Use when you have a time or `geolocation` at the US Capitol on Jan 6, 2021 and want ProPublica's archive of geolocated, timestamped Parler videos — returns geolocation, image and face leads.
url: https://projects.propublica.org/parler-capitol-videos/
category: public-records
path:
- public-records
bestFor: Browsing ProPublica's map/timeline of 500+ geolocated, timestamped Parler videos from the Jan 6 Capitol attack.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
- face
status: live
pricing: free
costNote: Free public ProPublica project. No account required.
opsec: passive
opsecNote: Fully passive — an archived public dataset hosted by ProPublica. Viewing it touches only ProPublica's servers and reveals nothing about your interest to any subject. The footage itself was public Parler content, preserved for the record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated and published by ProPublica, a reputable investigative newsroom; videos are geolocated/timestamped and sourced from the public Parler upload.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- credibly-accused
- nonprofit-explorer
- nursing-home-inspect
- police-protest-videos
- the-nypd-files
aliases:
- ProPublica Parler Capitol Videos
- What Parler Saw
tags:
- january-6
- video-archive
- geolocated
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Parler Capitol Videos

> ProPublica's preserved archive of 500+ Parler videos from January 6, 2021 — each placed on a map and timeline of the US Capitol attack, browsable by location and time.

## When to use
You're researching the January 6, 2021 Capitol attack and want primary-source video tied to a specific `geolocation` and moment: what was happening at a given spot on the Capitol grounds at a given time. The videos show scenes, crowds, and faces, making the archive useful for event reconstruction, identifying who was where and when, and corroborating other footage. It is a fixed historical dataset, not a live feed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/parler-capitol-videos/.
2. Use the map to pick a `geolocation` on/around the Capitol, or the timeline to pick a moment.
3. Play the geolocated, timestamped videos for that spot/time; note the exact location and timestamp shown.
4. Cross-reference scenes/faces with other Jan 6 footage archives.
5. Pivot: an identified location+time → build a movement timeline; a `face`/scene → compare against other public footage and databases (e.g. `[[police-protest-videos]]`).

## Inputs → Outputs
- **In:** a `geolocation` (Capitol area) and/or a time on Jan 6, 2021
- **Out:** geolocated, timestamped videos (`geolocation` + `image`/`face` content) of that place and moment
- **Empty/negative result looks like:** no videos for a spot/time — no preserved Parler upload covers it, not that nothing happened there; the archive is a sample, not exhaustive.

## Gotchas & OpSec
- Fixed to Jan 6, 2021 and to what was captured/preserved — coverage is partial in space and time.
- Geolocation/timestamps are ProPublica's best determination from the source metadata — treat as strong but not infallible.
- OpSec: fully passive archived public data.

## Overlaps ("do both")
- Sits alongside `[[police-protest-videos]]` and other Jan 6 footage collections — combine archives to cover moments/angles any single one misses.

## Trust & verifiability
`trust: trusted` — published by ProPublica with geolocation/timestamps from the source data; a reputable, well-documented archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | parler-capitol-videos |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → geolocation, image, face |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
