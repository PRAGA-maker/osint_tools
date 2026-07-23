---
id: audacity
name: Audacity
description: Use when you have an audio file/recording and want to analyze it — returns spectrogram/waveform views, isolated sounds, and clues to location, edits, or background events.
url: https://www.audacityteam.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Free desktop audio forensics — spectrogram analysis, cleanup, and isolating background sounds in a recording.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL); cross-platform desktop application, no account.
opsec: passive
opsecNote: "Audacity runs offline on your machine, so analyzing a recording you already hold touches no one and leaks nothing — passive. Standard evidence hygiene applies: work on a copy, keep the original untouched for chain of custody, and note recent Audacity builds have had telemetry/privacy discussions — use the official build and review its privacy settings."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-established open-source audio editor (now under Muse Group); a general audio tool, so forensic conclusions depend on your analysis, not the tool asserting anything.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Audacity audio editor
- audacityteam.org
tags:
- toddington
- curated-directory
- audio-forensics
- useful-websites-tools-documents
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Audacity

> A free, open-source audio editor investigators use for lightweight audio forensics — reading spectrograms, cleaning noise, and isolating background sounds that can reveal where or when a recording was made.

## When to use
You have an audio file — a voicemail, a video's audio track, a leaked recording, a ransom/proof-of-life clip — and want to analyze it: view the spectrogram to spot edits/splices, reduce noise to make speech intelligible, or isolate background sounds (traffic, PA announcements, mains hum, bells) that hint at `geolocation` or timing. General forensic tooling, so low direct missing-persons relevance, though audio can carry strong locational clues.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Audacity from https://www.audacityteam.org/ and import a **copy** of the audio (keep the original pristine).
2. Switch the track to **Spectrogram** view to inspect frequency content — abrupt discontinuities can indicate cuts/splices.
3. Use Noise Reduction, EQ, and amplification to bring up faint speech or background events.
4. Isolate and identify background sounds (announcements, sirens, music) that localize the recording; note mains hum (50/60 Hz) as a region hint.
5. Export processed clips and annotated spectrograms as findings; document every transformation for reproducibility.

## Inputs → Outputs
- **In:** an audio file/recording
- **Out:** spectrogram/waveform analysis, cleaned audio, isolated background sounds → clues to `geolocation`/timing/editing
- **Empty/negative result looks like:** no distinguishing sounds and a clean spectrogram — the recording may be too degraded, too short, or genuinely featureless; that's a limit of the audio, not proof of anything.

## Gotchas & OpSec
- It's an editor, not an authenticator — it helps you *observe* edits and sounds; conclusions are your interpretation and should be corroborated.
- Aggressive noise reduction introduces artifacts that can be mistaken for edits — process conservatively and keep the raw copy.
- Log every step; forensic value depends on a reproducible, documented workflow.

## Overlaps ("do both")
- Complements metadata tools (which read a media file's `metadata-exif`/container info) — Audacity analyzes the *content* of the audio, metadata tools analyze the *file*; run both on a suspect recording.

## Trust & verifiability
`trust: trusted` — a mature, transparent open-source tool; because it only reveals what's in the audio, verifiability comes from documenting your processing steps so another analyst can reproduce the same spectrogram and conclusions.
