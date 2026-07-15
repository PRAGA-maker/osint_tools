---
id: midomi-music-search-engine
name: Midomi / SoundHound Music Search
description: Use when you have an audio clip, hum, or song playing in a subject's video and want to identify the track — returns song title/artist metadata (a minor corroboration/timeline aid).
url: http://www.midomi.com
category: image-video-face
path:
- image-video-face
bestFor: Identifying a song from a recording, hum, or sung snippet (music ID), now delivered via SoundHound.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free music-identification service; the midomi.com brand now redirects to SoundHound (music.soundhound.com), which offers free song detection via web and mobile apps.
opsec: passive
opsecNote: You submit an audio sample to SoundHound's recognition service — nothing about your subject is queried, only the audio you provide. Standard privacy caveats of uploading audio to a third party apply.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Midomi is now part of SoundHound Inc., an established music-recognition company (Houndify technology); the recognition result is reliable, though this is a niche OSINT use.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Midomi
- SoundHound
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- audio
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Midomi / SoundHound Music Search

> A "hum/sing/record to identify" music-recognition search — the Midomi brand now redirects to SoundHound.

## When to use
This is a niche, corroborating tool. Reach for it when a subject's video or audio clip contains music you cannot name — identifying the track can add small context (an event, a scene, a cultural/linguistic hint) or help align a clip to a timeline (e.g., a song only released after a certain date). It does **not** identify people; it identifies songs. Do not over-rely on it — it is a supporting detail, not a primary lead, despite its inherited "high" relevance tag.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to midomi.com (redirects to SoundHound's music service) or use the SoundHound app.
2. Provide the audio: play the clip near your microphone, hum/sing the melody, or let the app listen to the music in the subject's video.
3. Read the match: song title, artist, album, and links to lyrics/streaming.
4. Pivot: a release date bounds a timeline; lyrics language/region can hint at the subject's cultural context.

## Inputs → Outputs
- **In:** an audio sample (recording, hum, or sung melody) — not a standard OSINT selector
- **Out:** song `metadata` (title, artist, album, release date, lyrics link)
- **Empty/negative result looks like:** "no match" — common for obscure, remixed, live, or non-commercial audio, or when the clip is too noisy/short.

## Gotchas & OpSec
- Recognises **commercial music only** — original speech, ambient sound, or unreleased audio won't match.
- Short or noisy clips fail often; isolate a clean segment of the music.
- OpSec: passive; you upload only the audio sample you choose.

## Overlaps ("do both")
- Complements video-frame geolocation and EXIF analysis — the music is one more contextual signal alongside visual and metadata cues. Cross-check a match with Shazam if SoundHound fails.

## Trust & verifiability
`trust: community` — recognition is powered by SoundHound, a reputable engine, so a positive match is reliable; the OSINT value, however, is marginal and contextual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | midomi-music-search-engine |
| category | image-video-face |
| selectorsIn → selectorsOut | (none) → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
