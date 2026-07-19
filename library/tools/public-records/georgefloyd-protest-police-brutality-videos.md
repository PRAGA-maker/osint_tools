---
id: georgefloyd-protest-police-brutality-videos
name: George Floyd Protest — Police Brutality Videos (archive)
description: Use when you have a `geolocation`/date from the 2020 George Floyd protests and want documented incident footage — returns a curated spreadsheet of videos with locations, dates and source links.
url: https://docs.google.com/spreadsheets/u/1/d/1YmZeSxpz52qT-10tkCjWOwOGkQqle7Wd1P7ZM1wMW0E/htmlview
category: public-records
path:
- public-records
bestFor: A crowdsourced, curated archive of police use-of-force videos from the 2020 George Floyd protests, indexed by city/date with source links.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- social-profile
- document-id
status: live
pricing: free
costNote: Free, publicly viewable Google Sheet; no account required to read.
opsec: passive
opsecNote: Reading a published spreadsheet is passive. The linked videos live on Twitter/X and other platforms — opening them is normal browsing, but use a sock-puppet session if you don't want views attributed to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known crowdsourced compilation (widely attributed to attorney T. Greg Doucette and collaborators) documenting 2020-protest incidents; entries are community-submitted, so corroborate each video and its stated location/date at the source.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Police brutality video spreadsheet 2020
- GeorgeFloyd protest videos
tags:
- protest
- video-evidence
- 2020-protests
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# George Floyd Protest — Police Brutality Videos (archive)

> A large crowdsourced spreadsheet cataloguing police use-of-force videos from the 2020 George Floyd protests, indexed by city and date with links to the original footage — a ready-made evidence archive for that period.

## When to use
You are investigating a specific incident, location, or person connected to the summer-2020 US protests and want documented footage. The sheet lets you filter by `geolocation` (city/state) and date to find videos of a particular event, which can help geolocate an incident, identify individuals or officers visible in footage, or corroborate a claim about what happened where and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the spreadsheet (Google Sheets, read-only) and scan the columns — typically date, city/state, description, and source links.
2. Filter/scroll to your city and date range to find relevant incidents.
3. Open the linked videos (many on Twitter/X) and analyse the footage for location cues, people, and timing.
4. Because entries are crowd-submitted, verify each video's stated location/date against the footage and independent reporting.
5. Pivot: on-screen detail feeds `geolocation`; visible individuals feed face/username OSINT; the source `social-profile`s (posters) are further leads.

## Inputs → Outputs
- **In:** `geolocation` (city/state) and/or date from the 2020 protests
- **Out:** curated incident videos with `geolocation`, source `social-profile` links, and `document-id`-style row references
- **Empty/negative result looks like:** no entry for your city/date — the archive is broad but not exhaustive, and it is a static historical record (not updated for later events). Absence is not evidence nothing occurred.

## Gotchas & OpSec
- Static, historical (2020) archive — not a live feed and not comprehensive.
- Crowd-submitted metadata can be wrong; confirm each video's location/date at the source.
- Some linked videos may be deleted; use archive.org/Wayback for dead links.
- Handle footage of identifiable people responsibly.

## Overlaps ("do both")
- Pairs with reverse-video/keyframe search and social-media archiving — this indexes the incidents, while those verify a video's provenance and preserve it before links rot.

## Trust & verifiability
`trust: community` — a reputable, widely cited crowdsourced compilation, but each row is only as reliable as its submitted source; treat it as an index of leads to verify, not as adjudicated fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | georgefloyd-protest-police-brutality-videos |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → geolocation, social-profile, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
