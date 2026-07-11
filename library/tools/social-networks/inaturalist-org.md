---
id: inaturalist-org
name: iNaturalist
description: Use when you have a `username`/`name` on iNaturalist and want their nature observations — returns geotagged, time-stamped observation photos revealing places the person has physically been.
url: https://www.inaturalist.org/
category: social-networks
path:
- social-networks
bestFor: Mapping where and when a person has been, via their geotagged nature-observation photos.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
- image
status: live
pricing: free
costNote: Free citizen-science platform; no account needed to browse public observations and profiles.
opsec: passive
opsecNote: Browsing public observations is passive — the user is not notified. Note iNaturalist obscures coordinates for sensitive/threatened species and lets users obscure their own locations, so precise geodata isn't guaranteed. Use a sock-puppet if you ever create an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable, widely used citizen-science platform (California Academy of Sciences / National Geographic). Observation locations/timestamps are user-supplied but generally reliable, subject to deliberate obscuring.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- inaturalist.org
- iNaturalist
tags:
- gsocialmedia
- General Social Media Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# iNaturalist

> A global nature-observation network whose public profiles are an OSINT goldmine — each observation is a geotagged, time-stamped photo placing a person at a specific spot on a specific day.

## When to use
You have an iNaturalist `username` (or a `name` that might match one) and want a movement/location pattern: the platform's public observations carry precise coordinates and dates, so a subject's account effectively maps where they've physically been and when. Genuinely useful in missing-person and pattern-of-life work when the subject is a nature/birding/hiking enthusiast.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.inaturalist.org/ and search people for the `username`/`name`, or search observations.
2. Open the user's profile and their observations feed: each entry has a photo, species, date, and (usually) a map pin.
3. Plot the observations over time to reveal home range, regular spots, and travel; note the capture dates.
4. Watch for obscured locations (sensitive species or user-set privacy) where coordinates are generalised.
5. Pivot: recurring `geolocation`s narrow a home area; photos feed reverse-image/face tools; the profile links to other handles.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** public profile (`social-profile`), geotagged observation `image`s with precise `geolocation` and timestamps
- **Empty/negative result looks like:** no account or an account with no/obscured-location observations — the person may not use it, or has obscured their data; absence isn't proof of anything.

## Gotchas & OpSec
- Location obscuring: coordinates for threatened species and user-flagged observations are deliberately generalised — don't treat every pin as exact.
- Enthusiast-only: only useful if the subject actually uses the platform.
- OpSec: passive; browsing public data touches no subject. Use the API for bulk location analysis.

## Overlaps ("do both")
- Pairs with `[[mapillary-2]]` and mapping tools — iNaturalist supplies dated, geotagged points; street/satellite imagery confirms and enriches each location.

## Trust & verifiability
`trust: community` — a reputable citizen-science platform; observation geodata is generally reliable but user-supplied and sometimes intentionally obscured, so verify precise coordinates before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inaturalist-org |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
