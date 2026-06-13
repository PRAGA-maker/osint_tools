---
id: confirm-a-geolocation-by-matching-multiple-incidental-micro-features-in-street-view
name: Confirm a geolocation by matching multiple incidental micro-features in Street View
description: Use when After you have a candidate location, to confirm the exact spot and produce report-grade evidence.
type: pattern
summary: 'A single matching landmark is a candidate, not proof. The team confirmed the exact filming spot by corroborating several incidental, hard-to-fake details visible in both the media and Google Street View: a matching padlock and storage area, matching lighting fixtures, and a Chevron gas-station sign in the same relative position. For the photoshoot image they similarly matched a cleaning station, nearby building satellite-dish/window positions, and a fence-line. Stack independent micro-features to pin a location down to the exact camera position and to make the conclusion defensible.'
missingPersonsRelevance: high
phase: verification
pivotFrom:
- image
- geolocation
pivotTo:
- geolocation
- address
platforms:
- google
steps:
- 'List every incidental, fixed detail in the media: padlocks, storage areas, fixtures, signage, fence-lines, satellite dishes, window arrangements.'
- Open Google Street View / satellite at the candidate location.
- Match each incidental detail one-by-one between media and Street View, noting relative positions.
- Require multiple independent matches before declaring confirmation.
- Screenshot side-by-side comparisons for the report.
signals:
- Multiple unrelated micro-features line up between the image and Street View
- Relative positions (left/right of a sign, fence orientation) match, pinning camera position
pitfalls:
- 'Confirmation bias: forcing a match on one detail while ignoring contradicting ones'
- Street View imagery may be outdated; account for changed signage/construction
toolsUsed:
- Google Street View
- Google Maps
tags:
- geolocation
- corroboration
- street-view
- micro-features
- verification
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Confirmed via 'matching padlock and storage area, matching lighting, and a Chevron gas station sign'; image 2 via 'cleaning station, nearby building satellite dish/window positions, and matching fence-line.'
trust: community
source: osinti4l-mvo-writeup
---

# Confirm a geolocation by matching multiple incidental micro-features in Street View

> A single matching landmark is a candidate, not proof. The team confirmed the exact filming spot by corroborating several incidental, hard-to-fake details visible in both the media and Google Street View: a matching padlock and storage area, matching lighting fixtures, and a Chevron gas-station sign in the same relative position. For the photoshoot image they similarly matched a cleaning station, nearby building satellite-dish/window positions, and a fence-line. Stack independent micro-features to pin a location down to the exact camera position and to make the conclusion defensible.

**When to use:** After you have a candidate location, to confirm the exact spot and produce report-grade evidence.

## Steps
- List every incidental, fixed detail in the media: padlocks, storage areas, fixtures, signage, fence-lines, satellite dishes, window arrangements.
- Open Google Street View / satellite at the candidate location.
- Match each incidental detail one-by-one between media and Street View, noting relative positions.
- Require multiple independent matches before declaring confirmation.
- Screenshot side-by-side comparisons for the report.

## Signals it's working
- Multiple unrelated micro-features line up between the image and Street View
- Relative positions (left/right of a sign, fence orientation) match, pinning camera position

## Pitfalls
- Confirmation bias: forcing a match on one detail while ignoring contradicting ones
- Street View imagery may be outdated; account for changed signage/construction

**Tools:** Google Street View, Google Maps

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
