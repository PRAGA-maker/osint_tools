---
id: mine-photos-and-videos-for-context-and-embedded-clues
name: Mine photos and videos for context and embedded clues
description: Use when Whenever you have access to photos or videos posted by or featuring the subject.
type: technique
summary: 'TOFM frames media analysis around two questions: contextual knowledge (when was it created, who posted it, when was it shared, does the timing align with the content?) and information extraction (does the media reveal location, emotional state, associates, habits, or identifiable objects like license plates or badges?). In missing-persons cases the subject''s and associates'' photos/videos are often the single richest source of a recent timeline and a place.'
missingPersonsRelevance: high
phase: enrichment
pivotFrom:
- image
- social-profile
pivotTo:
- geolocation
- associate
- vehicle-plate
- employer-org
- metadata-exif
platforms:
- instagram
- tiktok
- facebook
steps:
- 'Establish the temporal frame: creation time vs. post time, and whether the content matches that timing.'
- Identify who posted it and who appears in it (associates).
- Scan for location indicators (signage, landmarks, architecture, weather/season).
- 'Scan for identifiable objects: license plates, ID/badges, uniforms, logos, store names.'
- Note behavioral/emotional cues that hint at state of mind or routine.
signals:
- A photo yields a readable sign, plate, badge, or landmark that ties to a place or organization
pitfalls:
- Conflating post date with the date the photo was actually taken
- Overlooking small background objects that carry the real clue
tags:
- media-analysis
- image-pivot
- timeline
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: TOFM media-analysis questions on temporal context and information extraction (location, associates, plates, badges).
trust: community
source: tofm
---

# Mine photos and videos for context and embedded clues

> TOFM frames media analysis around two questions: contextual knowledge (when was it created, who posted it, when was it shared, does the timing align with the content?) and information extraction (does the media reveal location, emotional state, associates, habits, or identifiable objects like license plates or badges?). In missing-persons cases the subject's and associates' photos/videos are often the single richest source of a recent timeline and a place.

**When to use:** Whenever you have access to photos or videos posted by or featuring the subject.

## Steps
- Establish the temporal frame: creation time vs. post time, and whether the content matches that timing.
- Identify who posted it and who appears in it (associates).
- Scan for location indicators (signage, landmarks, architecture, weather/season).
- Scan for identifiable objects: license plates, ID/badges, uniforms, logos, store names.
- Note behavioral/emotional cues that hint at state of mind or routine.

## Signals it's working
- A photo yields a readable sign, plate, badge, or landmark that ties to a place or organization

## Pitfalls
- Conflating post date with the date the photo was actually taken
- Overlooking small background objects that carry the real clue

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
