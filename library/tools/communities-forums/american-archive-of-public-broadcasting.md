---
id: american-archive-of-public-broadcasting
name: American Archive of Public Broadcasting
description: Use when you have a `name`, place, topic, or date and want to find historic US public radio/TV footage — returns archived programs that may show a person, place, or event.
url: https://americanarchive.org
category: communities-forums
path:
- communities-forums
bestFor: Locating decades-old public-media appearances or coverage of a person, place, or event across 200+ US stations.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- geolocation
- image
status: live
pricing: free
costNote: Free to search and stream; a Library of Congress + GBH collaboration. Some items are viewable only on-location, but metadata and many recordings are online.
opsec: passive
opsecNote: A public digital archive — searching and streaming touches only the archive, never any subject. Standard request logging applies to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Library of Congress and GBH (Boston public media); provenance and station attribution are documented, making it a citable primary source.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AAPB
tags:
- tv-radio
- media-archive
- historical
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# American Archive of Public Broadcasting

> A Library-of-Congress + GBH archive of historic US public radio and television — a searchable well of decades-old footage in which a person, place, or event may appear.

## When to use
You are researching someone's or somewhere's past and suspect there is public-media coverage: a local news segment, an interview, a documentary, a call-in show. AAPB indexes programs from 200+ public stations, so a `name`, a town (`geolocation`), a topic, or an era can surface archival audio/video that puts a face, voice, or location on record — useful for biographical background, historical missing-persons context, or verifying a claimed appearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://americanarchive.org and use the search (or **Advanced Search**).
2. Query a `name`, place, station, topic, or date range. Refine by media type (radio/television), station, and era.
3. Open a result: read the program metadata (date, station, description, participants) and stream the recording where available.
4. Extract leads: a person seen/named on air, a location shown, an associated organization — and capture a still `image` or timestamp as evidence.
5. Pivot: feed a confirmed `name`/affiliation into people-search and news archives; use the program date to anchor a timeline.

## Inputs → Outputs
- **In:** `name`, `geolocation`, topic, or date
- **Out:** archived programs (with dates, stations, descriptions) potentially yielding `name`, `geolocation`, `image`
- **Empty/negative result looks like:** no matching programs — many recordings are undigitized or access-restricted to on-site, so absence online is not absence from the collection; note the item may exist but be unavailable remotely.

## Gotchas & OpSec
- Human-in-the-loop: none, but some items are marked "available at the Library of Congress / GBH only" — you'll see the metadata but not stream it remotely.
- OpSec: **passive** — a public archive; nothing reaches any subject.
- Coverage is US public broadcasting and historically weighted; it will not have commercial-network or very recent material.

## Overlaps ("do both")
- Pairs with commercial news/TV archives and general search — AAPB covers *public* media specifically, so run it alongside broader archives to avoid missing a public-station segment that never aired commercially.

## Trust & verifiability
`trust: trusted` — Library of Congress and GBH stewardship with documented station provenance; recordings are citable primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | american-archive-of-public-broadcasting |
