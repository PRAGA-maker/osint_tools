---
id: cross-reference-multiple-media-against-each-other-and-known-locations-to-bound-the-search
name: Cross-reference multiple media against each other and known locations to bound the search
description: Use when When you have one confirmed location and another piece of media to geolocate from the same subject.
type: pattern
summary: Treat each confirmed location as a constraint that bounds the search for the next one. After geolocating the video to a specific building/lighting structure, the team searched for the photoshoot car-wash specifically in areas near that confirmed location and in areas listed on the MP BOLO, rather than searching the whole world. Locations from a subject's media tend to cluster geographically; use already-solved media to shrink the candidate area for unsolved media.
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- geolocation
- image
pivotTo:
- geolocation
- address
platforms:
- google
steps:
- Record every confirmed location and every location listed on the BOLO.
- When geolocating new media, restrict candidate-area searches to the vicinity of confirmed/BOLO locations first.
- Expand outward only if the bounded search fails.
- Note geographic clustering of the subject's media as a movement/area signal.
signals:
- The unsolved media's location turns up near an already-confirmed location
- BOLO-listed areas overlap with the bounded search and produce a hit
pitfalls:
- The subject may have traveled far; don't ignore evidence that breaks the cluster assumption
- Over-tight bounding can cause you to miss the true location
toolsUsed:
- Google Maps
- Google Street View
tags:
- geo-clustering
- search-bounding
- cross-reference
- bolo
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: '''began searching for car-washes in areas relevant to locations listed from the MP BOLO and areas in the vicinity of the previously found location from video 1.'''
trust: community
source: osinti4l-mvo-writeup
---

# Cross-reference multiple media against each other and known locations to bound the search

> Treat each confirmed location as a constraint that bounds the search for the next one. After geolocating the video to a specific building/lighting structure, the team searched for the photoshoot car-wash specifically in areas near that confirmed location and in areas listed on the MP BOLO, rather than searching the whole world. Locations from a subject's media tend to cluster geographically; use already-solved media to shrink the candidate area for unsolved media.

**When to use:** When you have one confirmed location and another piece of media to geolocate from the same subject.

## Steps
- Record every confirmed location and every location listed on the BOLO.
- When geolocating new media, restrict candidate-area searches to the vicinity of confirmed/BOLO locations first.
- Expand outward only if the bounded search fails.
- Note geographic clustering of the subject's media as a movement/area signal.

## Signals it's working
- The unsolved media's location turns up near an already-confirmed location
- BOLO-listed areas overlap with the bounded search and produce a hit

## Pitfalls
- The subject may have traveled far; don't ignore evidence that breaks the cluster assumption
- Over-tight bounding can cause you to miss the true location

**Tools:** Google Maps, Google Street View

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
