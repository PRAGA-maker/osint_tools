---
id: geolocate-a-video-by-freeze-framing-a-single-identifying-landmark-e-g-a-casino-sign
name: Geolocate a video by freeze-framing a single identifying landmark (e.g., a casino sign)
description: Use when When you have video of the MP and need to establish where it was filmed.
type: technique
summary: Even a roughly one-second frame in a video can carry a location-defining landmark. The team found a frame where the camera faded out on a background building with a 'casino' sign, used Google search + Google Maps to identify the building, then walked Google Street View to find the nearby lighting structure the subject stood in front of. Step through video frame-by-frame looking for any unique, searchable signage or structure; one good frame can anchor the entire scene.
missingPersonsRelevance: high
phase: enrichment
pivotFrom:
- image
- metadata-exif
pivotTo:
- geolocation
- address
platforms:
- facebook
- youtube
steps:
- Scrub the video frame-by-frame, including transitions/fades, for any signage, business name, or distinctive structure.
- Capture the clearest frame of the landmark (e.g., a named business sign).
- Use Google search + Google Maps to identify the named landmark and its candidate locations.
- Switch to Google Street View around that landmark to find the exact foreground structure the subject was at.
- Confirm with multiple corroborating details rather than the sign alone.
signals:
- A single frame reveals a named/searchable landmark
- Street View reproduces the foreground structure near the identified landmark
pitfalls:
- Stopping at the named landmark without confirming the exact micro-location
- Chain businesses (same sign in many cities) require additional disambiguating details
toolsUsed:
- Google Search
- Google Maps
- Google Street View
tags:
- geolocation
- video-analysis
- frame-by-frame
- street-view
- landmark
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: '''An approximate one second frame... building in the background with a casino sign atop... allowed us to locate the building via Google searches, Google Maps, and Google Street View.'''
trust: community
source: osinti4l-mvo-writeup
---

# Geolocate a video by freeze-framing a single identifying landmark (e.g., a casino sign)

> Even a roughly one-second frame in a video can carry a location-defining landmark. The team found a frame where the camera faded out on a background building with a 'casino' sign, used Google search + Google Maps to identify the building, then walked Google Street View to find the nearby lighting structure the subject stood in front of. Step through video frame-by-frame looking for any unique, searchable signage or structure; one good frame can anchor the entire scene.

**When to use:** When you have video of the MP and need to establish where it was filmed.

## Steps
- Scrub the video frame-by-frame, including transitions/fades, for any signage, business name, or distinctive structure.
- Capture the clearest frame of the landmark (e.g., a named business sign).
- Use Google search + Google Maps to identify the named landmark and its candidate locations.
- Switch to Google Street View around that landmark to find the exact foreground structure the subject was at.
- Confirm with multiple corroborating details rather than the sign alone.

## Signals it's working
- A single frame reveals a named/searchable landmark
- Street View reproduces the foreground structure near the identified landmark

## Pitfalls
- Stopping at the named landmark without confirming the exact micro-location
- Chain businesses (same sign in many cities) require additional disambiguating details

**Tools:** Google Search, Google Maps, Google Street View

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
