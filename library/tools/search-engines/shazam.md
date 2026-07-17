---
id: shazam
name: Shazam
description: Use when you have an audio/video clip and want to identify the music playing in it — returns the song title and artist, a chronolocation/context clue.
url: https://www.shazam.com
category: search-engines
path:
- search-engines
bestFor: Identifying an unknown song heard in a video or recording, as a context/timeline clue.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free app (iOS/Android) and free web/song pages. Owned by Apple; no account needed to identify a song.
opsec: passive
opsecNote: You are matching an audio fingerprint against Shazam's music database — nothing about the subject is transmitted and nobody is alerted. Analyse a downloaded copy of the media rather than streaming from the source if you want to avoid touching the target's page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Owned and operated by Apple; the audio-fingerprint match is authoritative for identifying commercially released music.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Apple Shazam
tags:
- toddington
- curated-directory
- specialty-search
- audio
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Shazam

> Apple's music-recognition service — point it at audio and it names the song; a small but real tool for squeezing context out of a video's soundtrack.

## When to use
A video or recording tied to your investigation has music playing and you want to identify it. Knowing the exact track can help: a song released on a certain date puts a floor under when the footage was made; radio/TV audio in the background can hint at region or station; and matching the same track across clips can link them. It won't identify a person, but it's a cheap corroboration/timeline lead when other clues are thin.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Get the audio playing where Shazam can hear it — play the clip on one device and run the Shazam app (iOS/Android) on another, or use the "listening" feature over a section with clear music.
2. Let it capture a few seconds; it returns the song title and artist.
3. Open the matched song page for release date, album, and (via linked services) the era/context.
4. Use the result as a clue: cross-check the release date against the footage's claimed timeline; note station/broadcast context if the audio is from radio/TV.

## Inputs → Outputs
- **In:** an audio/video clip containing music
- **Out:** song title + artist (and release/album context from the song page)
- **Empty/negative result looks like:** "No match found" — the audio is too noisy, too short, speech-only, live/unreleased, or not in Shazam's catalogue. A non-match doesn't mean the audio is unidentifiable; try a cleaner segment or a different recognizer.

## Gotchas & OpSec
- Needs reasonably clean, commercially-released music; heavy background noise, talking over the track, or obscure/local recordings often defeat it.
- Passive — it fingerprints audio locally against a catalogue; nothing about the subject is sent anywhere. Prefer analysing a saved copy of the media.
- It identifies the *song*, not the *event* — a track can appear in countless videos, so treat it as one weak signal, corroborated by other evidence.

## Overlaps ("do both")
- Do both with a second recognizer (e.g. Google's "what's this song" / SoundHound) when Shazam misses — different catalogues and matching engines catch different tracks — and with frame-level image geolocation, so audio and visual clues jointly constrain place and time.

## Trust & verifiability
`trust: trusted` — Apple-operated and authoritative for identifying released music; the limitation is coverage (obscure/live audio), not accuracy of the matches it does return.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shazam |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
