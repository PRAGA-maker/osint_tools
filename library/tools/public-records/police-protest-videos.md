---
id: police-protest-videos
name: Police Protest Videos (ProPublica)
description: Use when you have a US `geolocation`/date around the 2020 protests and want documented incident footage — returns geolocated videos of police-protester encounters as `geolocation`/event leads.
url: https://projects.propublica.org/protest-police-videos/
category: public-records
path:
- public-records
bestFor: Browsing ProPublica's map/catalogue of verified videos of police-protester incidents during the 2020 George Floyd protests, by place and date.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public ProPublica news project; no account or payment.
opsec: passive
opsecNote: Passive — you browse a published journalistic dataset, no target interaction and no subject-alerting. The videos depict identifiable people at protests; handle any identification downstream carefully and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published and curated by ProPublica, a respected investigative newsroom; videos were collected and reviewed, though it is a fixed 2020-era dataset, not a live feed.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- parler-capitol-videos
- the-nypd-files
- credibly-accused
- nonprofit-explorer
- nursing-home-inspect
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
aliases:
- ProPublica protest police videos
tags:
- propublica
- video-evidence
- protests
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Police Protest Videos (ProPublica)

> ProPublica's curated, geolocated catalogue of videos documenting police-protester encounters during the 2020 US protests — a searchable evidence layer tied to place and date.

## When to use
You are investigating an incident, person, or timeline connected to the summer-2020 US protests and want documented footage: which encounters were captured, where, and when. Useful for placing an event at a `geolocation`/date, finding video that may show a subject, or corroborating an account. It is a fixed historical dataset, not a live protest tracker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/protest-police-videos/.
2. Browse the map/list; filter/zoom to the city or area of interest.
3. Select an entry to view the video and its metadata (location, date, description).
4. Note the place/time and any identifying detail in the footage.
5. Pivot: a confirmed `geolocation`+date → local news archives and other footage; a visible person/vehicle → image and vehicle tools; cross-reference with related ProPublica datasets for the same event.

## Inputs → Outputs
- **In:** a US `geolocation` and/or date window (2020 protest period)
- **Out:** geolocated incident videos with location/date context (`geolocation`)
- **Empty/negative result looks like:** no entries for your area/date — the dataset covers documented 2020 incidents only, so gaps are expected; it won't have anything outside that scope.

## Gotchas & OpSec
- **Temporal scope:** primarily the 2020 protest period — not current events.
- Footage shows identifiable individuals; any identification you build from it must be handled lawfully and cautiously.
- Curated but not exhaustive; absence of a video isn't evidence an incident didn't occur.

## Overlaps ("do both")
- Pairs with `[[parler-capitol-videos]]` (a comparable geolocated video archive for a different event) and local news archives — together they widen event-footage coverage across time and place.

## Trust & verifiability
`trust: trusted` — a ProPublica-curated dataset; the collection and review are credible, and each video is directly viewable, so you can verify content yourself, while remembering it is a fixed 2020 snapshot.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-protest-videos |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
