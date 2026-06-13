---
id: exif-and-chronolocation
name: pivot-exif-and-chronolocation
description: Use when you have an original image file — pull embedded EXIF for an exact GPS/timestamp, and when EXIF is gone, derive WHEN a photo was taken from shadows, light, and seasonal cues.
type: technique
phase: pivot
pivotFrom: [image, metadata-exif]
pivotTo: [geolocation, address, dob]
platforms: [reddit, telegram, discord]
summary: An original photo file can carry EXIF — GPS coordinates, a precise timestamp, the camera/device — handing you location and time for free. But most social platforms RE-ENCODE uploads and strip EXIF, so the absence of metadata on a downloaded image tells you nothing. When EXIF is gone, chronolocation recovers the WHEN from the pixels: sun/shadow angle for time-of-day, foliage and snow for season, visible events or signage for a date range. Time pins are as valuable as place pins for building a timeline.
missingPersonsRelevance: high
whenToUse: You have an image file (ideally an original, not a platform-downloaded copy) and need when/where it was taken.
steps:
  - Get the most original copy possible — a file from a direct send, a download link, or a less-processing platform keeps EXIF that Instagram/Facebook would have stripped.
  - Extract metadata — read EXIF/IPTC/XMP for GPS, timestamp, device, and software; a hit gives you geolocation + time directly.
  - Don't trust absence — a stripped image is NOT evidence the photo had no metadata; the platform removed it (see `[[antipattern-trusting-stripped-metadata]]`).
  - Chronolocate when EXIF is gone — shadow direction/length for time-of-day and latitude, foliage/snow/daylight for season, visible signage/events for a date range.
  - Cross-check the timestamp against the timeline — a metadata time can be wrong (timezone, fake) so corroborate it.
signals:
  - EXIF GPS lands on a plausible location that an independent clue also supports — two-source convergence.
  - Shadow-derived time-of-day matches a posted caption or an independent timeline entry.
pitfalls:
  - Assuming "no EXIF" means "no data" — platform re-encoding strips it; the pixels still hold time/place signal.
  - Trusting a timestamp blindly — device clocks, timezones, and deliberate edits make EXIF times fallible.
  - Geotag spoofing / staleness — an embedded GPS can be set or copied; treat it as a strong candidate, not proof.
toolsUsed: [exiftool, jeffrey-exif-viewer, suncalc, google-earth]
evidence: []
trust: trusted
relatedStrategies: [pivot-image-to-geolocation, antipattern-trusting-stripped-metadata, pattern-timeline-anchoring, pattern-reverse-image-everything]
tags: [image, metadata, chronolocation, geoint]
source: ""
---

# Image → EXIF & chronolocation (when/where a photo was taken)

## The move
Two complementary reads of a single file. **EXIF** (if present) gives you exact GPS and timestamp for free. **Chronolocation** recovers the *when* from the pixels when the metadata is gone — and it usually is gone, because platforms re-encode uploads.

## EXIF: the free win that's often already deleted
An original photo can embed GPS coordinates, a precise capture time, the device model, and editing software. Pull it with a metadata reader and you may get location and time in one shot. The catch: **Instagram, Facebook, X, and most platforms strip EXIF on upload by re-encoding the image.** So the version you scraped off a feed almost never has it. The way to *keep* EXIF is to get a more original copy — a direct file send, an original-quality download, or a platform/app that preserves metadata (some chat apps "send as file" do).

## Absence proves nothing
This is the key discipline: an image with no EXIF is *not* evidence the photo never had any. The platform removed it. Concluding "no metadata, dead end" is `[[antipattern-trusting-stripped-metadata]]`. The pixels remain a rich source.

## Chronolocation: read the time from the frame
When EXIF is gone, derive the *when*:
- **Sun and shadows** — shadow direction gives orientation; shadow length with a known date narrows time-of-day and latitude. This is the time-side of `[[pivot-image-to-geolocation]]`.
- **Season** — foliage state, snow, daylight length, what people are wearing.
- **Hard date anchors** — a dated sign, a concert/event, a newspaper, construction state visible in street-view history.

## Verify the time too
A timestamp can be wrong — a misset clock, a timezone offset, or a deliberate edit. Corroborate any time pin against the timeline (`[[pattern-timeline-anchoring]]`) before you build on it. Same for an embedded GPS: strong candidate, not proof, because geotags can be spoofed or stale.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| pivot | image, metadata-exif → geolocation, address, dob |
| platforms | reddit, telegram, discord |
| MP relevance | high |
| tools | exiftool, jeffrey-exif-viewer, suncalc, google-earth |
