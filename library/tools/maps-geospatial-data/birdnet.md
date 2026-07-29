---
id: birdnet
name: BirdNET
description: Use when you have audio (e.g. from a subject's video) with birdsong and want to narrow location — identifies bird species from sound and maps where that species is observed, yielding `geolocation` context.
url: https://birdnet.cornell.edu/map
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying bird species from audio and using their observed range to constrain where a recording was made.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free academic/conservation project from Cornell; the analyzer and observation map are free to use.
opsec: passive
opsecNote: You analyze audio you already hold against Cornell's model/observation data — nothing is sent to or about the subject. If you upload the subject's audio to BirdNET's servers, be mindful that clip is transmitted to a third party; strip identifying metadata first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Cornell University's K. Lisa Yang Center for Conservation Bioacoustics with Chemnitz University of Technology; a serious, peer-reviewed scientific project.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- cornell-legal-information-institute-united-states
- lexcraft-cornell-university-legal-wiki-canada
aliases:
- BirdNet
tags:
- bellingcat-toolkit
- environment-wildlife
- audio-geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# BirdNET

> Cornell's birdsong AI as a geolocation aid: identify the species in a recording, then use its observed range to narrow where the audio was captured.

## When to use
You are geolocating a video or audio clip (from a subject's post, a hostage/missing-person recording, a scene) and there is audible birdsong. Identifying the species — and checking where BirdNET observations of it cluster — can rule regions in or out or corroborate a claimed location. It is a corroboration layer for chrono/geolocation, not a person-finder. Combine with visual and vegetation cues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Isolate a clean segment of birdsong from your clip.
2. Use the BirdNET analyzer (web/app) to identify the likely species from the audio.
3. Open https://birdnet.cornell.edu/map and view where that species' observations concentrate (anonymized detections, most-frequent-observation markers by region).
4. Cross-reference the species' range/seasonality with your candidate `geolocation` and time of year to test plausibility.
5. Pivot: combine with vegetation, architecture, sun-position, and language cues to tighten the location estimate.

## Inputs → Outputs
- **In:** audio clip containing birdsong (not a formal OSINT selector)
- **Out:** identified species and observation `geolocation` distribution
- **Empty/negative result looks like:** low-confidence species guesses or a species with near-global range — little geographic discrimination; treat as inconclusive, not as evidence of any location.

## Gotchas & OpSec
- Migratory and wide-ranging species constrain little; the technique works best with range-restricted species and clear audio.
- Model confidence varies with recording quality and overlapping sounds — a single ID is a hypothesis, not proof.
- Captive/urban birds and playback can mislead; corroborate with independent cues.

## Overlaps ("do both")
- Pairs with visual geolocation workflows (satellite/streetview matching, vegetation ID) — BirdNET adds an audio dimension that image-only geolocation misses.

## Trust & verifiability
`trust: trusted` — a peer-reviewed Cornell/Chemnitz scientific project; the model and observation data are credible, though any single identification should be confidence-checked and corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | birdnet |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
