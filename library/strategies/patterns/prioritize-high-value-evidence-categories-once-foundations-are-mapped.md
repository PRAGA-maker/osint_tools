---
id: prioritize-high-value-evidence-categories-once-foundations-are-mapped
name: Prioritize high-value evidence categories once foundations are mapped
description: Use when After you have the basic network mapped and need to decide where to spend remaining time.
type: pattern
summary: Not all findings are worth the same. Day-Last-Seen photos/CCTV, recent location/geolocation, and phone history carry far more value than basic friend/employment facts. The winning move is to build the foundational network map quickly (friends, family, accounts) and then deliberately pivot toward high-value lifestyle, location, and last-seen evidence rather than continuing to grind low-value connection flags. Quality and recency beat raw volume of trivial facts once the basics are covered.
missingPersonsRelevance: high
phase: triage
pivotFrom:
- social-profile
- associate
pivotTo:
- geolocation
- image
- phone
- physical-description
platforms:
- facebook
- instagram
- tiktok
steps:
- 'Quickly capture foundational flags: close friends, family, known accounts.'
- Once network value diminishes, deliberately pivot to high-value categories.
- Hunt Day-Last-Seen photos/CCTV and recent geolocation (highest points).
- Document phone models/numbers and recent activity.
- Extract lifestyle/physical descriptors (tattoos, vehicles, substance-use indicators) from photos.
signals:
- You are still finding new flags but each is low value
- A recent post or photo carries location or last-seen significance
pitfalls:
- Grinding low-point friend flags after the network is mapped
- Skipping CCTV/official photos assuming law enforcement already has them
tags:
- scoring
- prioritization
- day-last-seen
- high-value
evidence:
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Day-Last-Seen photos/CCTV 500 pts, phone history 450 pts; prioritize quality over quantity; do not assume LE already has public evidence
- type: writeup
  url: https://jack.bio/blog/tracelabs
  note: Timeline advancement +700 points per pre-disappearance geolocated post
trust: community
source: searchparty-writeups
---

# Prioritize high-value evidence categories once foundations are mapped

> Not all findings are worth the same. Day-Last-Seen photos/CCTV, recent location/geolocation, and phone history carry far more value than basic friend/employment facts. The winning move is to build the foundational network map quickly (friends, family, accounts) and then deliberately pivot toward high-value lifestyle, location, and last-seen evidence rather than continuing to grind low-value connection flags. Quality and recency beat raw volume of trivial facts once the basics are covered.

**When to use:** After you have the basic network mapped and need to decide where to spend remaining time.

## Steps
- Quickly capture foundational flags: close friends, family, known accounts.
- Once network value diminishes, deliberately pivot to high-value categories.
- Hunt Day-Last-Seen photos/CCTV and recent geolocation (highest points).
- Document phone models/numbers and recent activity.
- Extract lifestyle/physical descriptors (tattoos, vehicles, substance-use indicators) from photos.

## Signals it's working
- You are still finding new flags but each is low value
- A recent post or photo carries location or last-seen significance

## Pitfalls
- Grinding low-point friend flags after the network is mapped
- Skipping CCTV/official photos assuming law enforcement already has them

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
