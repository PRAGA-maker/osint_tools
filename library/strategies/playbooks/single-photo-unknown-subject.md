---
id: single-photo-unknown-subject
name: playbook-single-photo-unknown-subject
description: Use when you have one image and no identity — an ordered sequence that wrings location, face, and metadata out of a single photo to bootstrap an identity from nothing.
type: playbook
phase: triage
pivotFrom: [image]
pivotTo: [face, geolocation, name, social-profile, any]
platforms: [any]
summary: One photo, no name, no handle — the classic CTF "who and where is this?" An image is the densest possible single seed, carrying three independent pivots at once: reverse-search the whole frame for a source, face-search the person, and read the pixels and any surviving EXIF for place and time. The ordered move is cheapest-first (reverse image), then parallel face and geolocation, with each new selector feeding the next. The discipline that holds it together is treating every face/place hit as a candidate until two signals converge.
missingPersonsRelevance: high
whenToUse: You hold a single image and have no confirmed identity selectors to start from.
steps:
  - Reverse-image the whole frame first — cheapest move; may hand you a source, profile, or location directly (`[[pattern-reverse-image-everything]]`).
  - Crop and re-search distinctive regions — a sign, a logo, the face alone — full-frame and crop return different results.
  - Run face search in parallel — isolate a clean face and query multiple engines; every return is a candidate (`[[pivot-image-to-face]]`).
  - Geolocate the background in parallel — read signs, architecture, terrain, sun; confirm geometry on street-view (`[[pivot-image-to-geolocation]]`).
  - Pull EXIF / chronolocate — extract any surviving metadata; if stripped, derive time from shadows/season (`[[pivot-exif-and-chronolocation]]`).
  - Converge and verify — combine the face, place, and time into one candidate identity; promote only when independent signals agree (`[[phase-verification]]`).
signals:
  - Two of {face hit, location, source} independently point at the same person/place — convergence that bootstraps an identity.
  - A reverse-image source profile matches the face-search return — mutual confirmation.
pitfalls:
  - Acting on a single face hit as identity — facial similarity is not identity; require a second signal (`[[antipattern-forcing-the-match]]`).
  - Concluding "no EXIF, no data" — the platform stripped it; the pixels still hold place and time (`[[antipattern-trusting-stripped-metadata]]`).
  - Geolocating or face-searching an image that's actually stock/reposted — reverse search first to catch that.
toolsUsed: [yandex-images, google-lens, pimeyes, exiftool, google-earth]
evidence: []
trust: trusted
relatedStrategies: [pattern-reverse-image-everything, pivot-image-to-face, pivot-image-to-geolocation, pivot-exif-and-chronolocation, phase-verification]
tags: [playbook, image, ctf, bootstrap, high-yield]
source: ""
---

# Playbook: Single photo, unknown subject

## When this applies
You have **one image** and no confirmed identity — no name, no handle, no email. The classic CTF prompt: "who is this and where was it taken?" The good news is that an image is the **densest single seed there is**: a single photo carries three independent pivots — a source, a face, and a place/time — so even from nothing you usually have three shots at a break.

## The ordered sequence (cheapest first, then parallel)
1. **Reverse-image the whole frame.** Seconds of work, highest cheap-yield. It can return the original source, a profile, or the location outright — and it tells you immediately if the image is **stock or a repost** (in which case it's not your subject and you've saved a lot of wasted geolocation). `[[pattern-reverse-image-everything]]`.
2. **Crop and re-search.** Isolate distinctive regions — a sign, a logo, the face alone — and search each. Full-frame and crop are different queries and hit different indexes.
3. **Face search (in parallel).** Isolate a clean, frontal face and run it through multiple engines. Every return is a **candidate**, not the person. `[[pivot-image-to-face]]`.
4. **Geolocate the background (in parallel).** Read text/signs, architecture, terrain, and sun; confirm by matching geometry in satellite/street-view. `[[pivot-image-to-geolocation]]`.
5. **EXIF / chronolocation.** Extract any surviving metadata for a free GPS/timestamp; if it's been stripped (usually), derive the *when* from shadows and season. **Absence of EXIF is not absence of data.** `[[pivot-exif-and-chronolocation]]`.

## Converge to bootstrap an identity
The power of the single-photo case is **convergence**: a face hit that lands on a profile, whose posts geolocate to the same place your background analysis found, is three independent signals agreeing — and that's how you build an identity from a blank start. Combine face + place + time + source into one candidate, and promote it only when independent signals agree. `[[phase-verification]]`.

## The two cardinal mistakes
- **Acting on a single face hit as identity.** Similarity is not identity; one engine return is a lead, not a person. `[[antipattern-forcing-the-match]]` does the most damage here, where you have nothing else to check it against.
- **"No EXIF, dead end."** The platform stripped it; the pixels are still full of signal. `[[antipattern-trusting-stripped-metadata]]`.

---
## Metadata
| field | value |
|---|---|
| type | playbook |
| phase | triage → pivot → verification |
| MP relevance | high |
| tools | yandex-images, google-lens, pimeyes, exiftool, google-earth |
