---
id: confirm-geolocation-with-a-stack-of-independent-micro-features-not-one-match
name: Confirm geolocation with a stack of independent micro-features, not one match
description: Use when Whenever you are about to assert an exact coordinate or address from imagery.
type: technique
summary: Across both the video and the image geolocations, the team never declared a location on a single match. They stacked independent corroborating micro-features in Street View - matching padlock and storage area, lighting structure, Chevron sign for the video; cleaning station, satellite-dish/window positions, and fence-line alignment for the car-wash. Requiring several unrelated physical details to all line up at one coordinate dramatically lowers false-positive geolocations, which matters because a confidently wrong location wastes searcher resources and damages report credibility.
missingPersonsRelevance: high
phase: verification
pivotFrom:
- geolocation
- image
pivotTo:
- geolocation
- address
platforms:
- google
steps:
- Identify 3+ fixed, independent features in the source image/video (signage, fences, fixtures, structures).
- Locate the candidate spot in Street View / satellite.
- Verify each feature matches in position and detail.
- Only assert the location if the independent features all align; otherwise widen the candidate set.
signals:
- Three or more unrelated fixed features all match at one coordinate
pitfalls:
- Anchoring on one feature (a single sign) and ignoring contradicting details
- Mistaking a chain-store generic layout for a unique location match
toolsUsed:
- Google Street View
- Google Maps
tags:
- geolocation
- verification
- false-positive-control
- street-view
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Both geolocations confirmed by stacking multiple independent fixed features
trust: community
source: osinti4l-user
---

# Confirm geolocation with a stack of independent micro-features, not one match

> Across both the video and the image geolocations, the team never declared a location on a single match. They stacked independent corroborating micro-features in Street View - matching padlock and storage area, lighting structure, Chevron sign for the video; cleaning station, satellite-dish/window positions, and fence-line alignment for the car-wash. Requiring several unrelated physical details to all line up at one coordinate dramatically lowers false-positive geolocations, which matters because a confidently wrong location wastes searcher resources and damages report credibility.

**When to use:** Whenever you are about to assert an exact coordinate or address from imagery.

## Steps
- Identify 3+ fixed, independent features in the source image/video (signage, fences, fixtures, structures).
- Locate the candidate spot in Street View / satellite.
- Verify each feature matches in position and detail.
- Only assert the location if the independent features all align; otherwise widen the candidate set.

## Signals it's working
- Three or more unrelated fixed features all match at one coordinate

## Pitfalls
- Anchoring on one feature (a single sign) and ignoring contradicting details
- Mistaking a chain-store generic layout for a unique location match

**Tools:** Google Street View, Google Maps

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
