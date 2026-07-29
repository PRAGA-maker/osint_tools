---
id: dictation-online-dictation-tool
name: Dictation.io
description: Use when you have audio/video and want a quick free browser transcription to text — a speech-to-text utility for turning spoken evidence into searchable notes.
url: https://dictation.io
category: documents-metadata
path:
- documents-metadata
bestFor: Fast, free, in-browser speech-to-text for transcribing spoken content into searchable notes.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free browser tool (uses the Web Speech API); no account.
opsec: passive
opsecNote: Transcription happens via the browser's built-in speech engine — which, in Chrome, sends captured audio to Google's speech service for recognition. Do not feed it sensitive/confidential audio you can't send to a third party; for that, use a local/offline transcriber (e.g. Whisper) instead.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small free web utility wrapping the browser's Web Speech API; accuracy and language support are the browser's, not a dedicated engine's, so transcripts need proofing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- dictation.io
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- transcription
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Dictation.io

> A free in-browser speech-to-text pad — a quick way to turn spoken evidence (a played-back clip, an interview) into searchable, quotable text.

## When to use
You have audio or video evidence — a voicemail, a livestream, a recorded call, a foreign-language clip — and want a fast, free transcript to search, quote, or translate, without installing anything. It's a convenience utility, not an investigative data source: it produces text from speech, and the investigative value is in what you then do with that text.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open dictation.io in Chrome (best Web Speech API support) and pick the spoken language.
2. Click start and play the audio into the microphone (route system audio to the mic input for cleaner capture than a room mic).
3. Watch the live transcript build; it also supports voice commands for punctuation.
4. Proofread against the audio, then save/copy the text.
5. Pivot: names, places, and handles spoken in the clip become new selectors for search.

## Inputs → Outputs
- **In:** live speech / played-back audio (no data selector)
- **Out:** a text transcript (feeds keyword search, translation, quoting) — no direct selector output
- **Empty/negative result looks like:** garbled or empty text — usually poor audio routing, background noise, or an unsupported accent/language; re-run with cleaner input.

## Gotchas & OpSec
- **Third-party recognition:** Chrome's Web Speech API sends audio to Google — never transcribe confidential material here; use an offline tool (Whisper) for sensitive audio.
- Accuracy is browser-grade and degrades on noise, overlap, and accents — always proof against the source before quoting.
- Real-time only (mic capture); for a large media file, a dedicated file-based transcriber is faster and more accurate.

## Overlaps ("do both")
- An easy first pass; for accuracy, volume, or privacy, prefer a local Whisper-based transcriber and use this only for a quick, non-sensitive gist.

## Trust & verifiability
`trust: unverified` — a lightweight utility over the browser's speech engine; fine for rough transcripts, but treat every transcript as draft until proofed against the audio.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dictation-online-dictation-tool |
