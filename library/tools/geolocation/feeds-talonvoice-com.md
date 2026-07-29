---
id: feeds-talonvoice-com
name: Talon Voice Radio Scanner Feeds
description: Use when you have a `geolocation`/city and want live text of public-safety radio traffic there — returns searchable transcriptions of scanner audio with playback.
url: https://feeds.talonvoice.com/
category: geolocation
path:
- geolocation
bestFor: Reading real-time speech-to-text transcriptions of US police/emergency scanner feeds by city.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free to read; donation-funded project. Coverage is limited to whatever feeds are actively transcribed at the time.
opsec: passive
opsecNote: You read a public web page of already-public radio traffic; you do not transmit or contact anyone, and monitoring is passive. Note that in some jurisdictions retaining or republishing public-safety audio has legal nuance — handle transcripts accordingly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent open-source project that ingests live scanner audio and transcribes it via speech recognition. Transcripts are machine-generated and community-corrected, so treat wording as approximate.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- broadcastify
aliases:
- Talon Voice scanner feeds
- feeds.talonvoice.com
tags:
- scanner
- public-safety
- radio
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Talon Voice Radio Scanner Feeds

> Live public-safety radio, turned into searchable text — it ingests scanner audio, splits on voice activity, and pushes speech-to-text transcriptions to per-city web feeds.

## When to use
You have a `geolocation` (a US city/area) and want situational awareness of what emergency services are broadcasting there right now, in readable text rather than raw audio. Relevant to time-sensitive cases — a recent incident, a search, a disappearance in a covered area — where police/fire/EMS radio chatter may reference locations, vehicles, or persons. Text form lets you scan and keyword-search far faster than listening.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://feeds.talonvoice.com/.
2. Pick an available city/agency feed (only actively transcribed feeds are listed; the roster changes).
3. Read the streaming transcript; each segment has a play button so you can verify the machine transcription against the source audio.
4. Keyword-scan for street names, cross-streets, vehicle descriptions, or names; use the audio playback to confirm anything you'll act on.
5. Pivot: a broadcast street/cross-street feeds mapping and geolocation; a vehicle or plate mention feeds vehicle-lookup tools. Corroborate with a live audio source before relying on it.

## Inputs → Outputs
- **In:** `geolocation` (city/area with a live feed)
- **Out:** timestamped text transcriptions of radio traffic, with references to locations/`geolocation`, incidents, and sometimes descriptions
- **Empty/negative result looks like:** the page shows only inactive feeds, or a feed is silent — no active transcription for that area at that moment; fall back to a live-audio scanner aggregator.

## Gotchas & OpSec
- Transcripts are **machine-generated** — names, plates, and addresses are frequently mis-heard. Always confirm against the linked audio before treating a detail as fact.
- Feed availability is patchy and donation-dependent; a city covered today may drop tomorrow (hence status: degraded). Many US agencies also encrypt their radio, so coverage is uneven.
- Public-safety audio handling has legal/ethical constraints in some places; do not republish and be mindful of privacy.

## Overlaps ("do both")
- Pairs with `[[broadcastify]]` — Broadcastify is the large live-audio scanner aggregator; Talon Voice adds machine transcription on top of a subset of feeds. Use Talon Voice to keyword-scan quickly, Broadcastify for authoritative live audio and broader coverage.

## Trust & verifiability
`trust: community` — a genuine, functioning open-source project, but transcription accuracy is limited and coverage is volatile. Treat every transcript as a lead to verify via the audio, not as a record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | feeds-talonvoice-com |
