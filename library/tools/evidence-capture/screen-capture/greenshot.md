---
id: greenshot
name: Greenshot
description: Use when you need to capture and annotate on-screen evidence — an open-source screenshot tool that produces annotated PNG/JPG images of a region, window, or page.
url: https://getgreenshot.org/
category: evidence-capture
path:
- evidence-capture
- screen-capture
bestFor: Quickly capturing, annotating (highlight/blur/arrow), and saving screenshots of web pages or app windows for case documentation.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open source on Windows (a paid Greenshot exists on macOS); no account. Runs entirely locally.
opsec: passive
opsecNote: Captures only your own local screen — nothing is transmitted and the target is never contacted, so it's fully passive. For evidentiary integrity, capture visible URL/timestamp in-frame and preserve the original file; annotations should be on copies, not the master.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established open-source screenshot utility with public source; widely used and safe to run locally.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- getgreenshot
tags:
- evidence-capture
- screenshot
- documentation
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Greenshot

> A free, open-source screenshot tool for capturing and annotating on-screen evidence — the workhorse for documenting what you find before it changes or disappears.

## When to use
You've found something online (a profile, post, listing, page) and need to preserve it as visual evidence: a timestamped, annotated screenshot for your case file. Because online content is edited and deleted, capturing it immediately is core OSINT hygiene. Greenshot lets you grab a region, window, or scrolling page and mark it up (highlight the relevant detail, blur unrelated PII) locally, without any cloud upload.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Greenshot from https://getgreenshot.org/ (Windows) and let it run in the tray.
2. Trigger a capture (PrtSc / hotkey) and choose region, window, or full/scrolling capture.
3. In the editor, annotate: arrows/highlights to mark the key detail, blur to redact unrelated personal data.
4. Save the ORIGINAL unedited capture first (as the master), then export annotated copies (PNG/JPG); keep the visible URL and a clock/timestamp in-frame where possible.
5. Pivot: file the capture with its source URL and capture time; pair with a full-page archive so you have both a fixed image and a live archived copy.

## Inputs → Outputs
- **In:** a screen region / window / page you want to preserve
- **Out:** annotated PNG/JPG image files (local) carrying capture `metadata-exif` (time, dimensions)
- **Empty/negative result looks like:** n/a — it's a capture tool, not a search; the only "failure" is a missed capture (content changed before you saved it), which is why you capture early.

## Gotchas & OpSec
- Windows-native (the macOS build is a separate paid app) — confirm platform before relying on it.
- Evidentiary care: keep the unedited original as the master and annotate copies; note capture time and source URL separately since a screenshot alone is easily disputed.
- A static image doesn't prove a live page — pair with a timestamped web-archive capture for stronger provenance.
- OpSec: fully passive/local; nothing leaves your machine.

## Overlaps ("do both")
- Pairs with web-archiving tools — Greenshot fixes an annotated visual snapshot; an archive service preserves the live, verifiable page behind it.

## Trust & verifiability
`trust: trusted` — a mature open-source utility with public source, safe to run locally. It captures faithfully; robust evidence still depends on your process (originals preserved, source URL and timestamp recorded).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greenshot |
| category | evidence-capture |
| selectorsIn → selectorsOut | — → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
