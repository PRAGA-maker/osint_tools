---
id: spaces-down
name: Spaces Down
description: Use when you have an X/Twitter Spaces link or a host `username` and want the audio for review — returns a downloadable MP3 recording of the Space (a `social-profile` audio artifact).
url: https://spacesdown.com/
category: social-networks
path:
- social-networks
bestFor: Downloading X/Twitter Spaces audio as MP3 for offline review and evidence preservation.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier ~5 downloads/day with MP3 conversion and basic search; paid tiers add volume and formats (WAV/FLAC).
opsec: passive
opsecNote: You submit a public Space URL to a third-party service; the host is not notified, but SpacesDown sees which Space you pulled. Downloading captures a public broadcast — passive toward the subject. Do the request from a sock-puppet browser and store the audio locally as evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party capture/archive service (claims 148k+ Spaces); convenient but unofficial — verify audio integrity and provenance for anything evidential.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SpacesDown
- Twitter Spaces downloader
tags:
- social-media
- twitter
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Spaces Down

> A third-party recorder/downloader for X (Twitter) Spaces — turns an ephemeral live audio room into a saved MP3 you can review and preserve.

## When to use
A subject hosted or spoke in an X Space and you need the audio: to review what was said, transcribe it, voice-compare a speaker, or preserve it before the host deletes the recording. Spaces are audio-only and often disappear; SpacesDown captures them (including a searchable back-catalogue of past Spaces) as downloadable files.

## How to use it (`bestInteractionPattern`: web-manual)
1. On X.com, find the Space and copy its URL (address bar or the share button).
2. Open https://spacesdown.com/ and paste the link into the download field; submit.
3. Wait for processing (a long Space takes a few minutes) and download the MP3 (or WAV/FLAC on paid tiers).
4. Or use its search to locate a past Space by host/keyword if you don't have the direct link.
5. Pivot: run the audio through a transcription tool, then mine the transcript for `name`, `associate`, place and event details; the host handle confirms a `social-profile`.

## Inputs → Outputs
- **In:** an X Space URL (or host `username` via the site's search)
- **Out:** a downloadable MP3/audio recording tied to that `social-profile`
- **Empty/negative result looks like:** "Space not found / not available" — the Space was never recorded, was deleted before capture, or the link is malformed; not every live Space is retrievable after it ends.

## Gotchas & OpSec
- Free tier caps daily downloads; large/old Spaces may be missing if never captured.
- Provenance matters for evidence: note the Space URL, host, and capture time, since this is an unofficial re-host.
- OpSec: passive toward the subject; the third-party service logs your pulls, so use a sock puppet.

## Overlaps ("do both")
- Pairs with X profile/timeline tooling and a transcription/voice tool — SpacesDown gets the audio, profile tools place it in the subject's account context, and transcription turns it into searchable text.

## Trust & verifiability
`trust: community` — a useful unofficial archive; treat downloaded audio as needing provenance verification, and cross-check claims made in a Space against other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spaces-down |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
