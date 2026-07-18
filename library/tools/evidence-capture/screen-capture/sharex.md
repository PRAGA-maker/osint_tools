---
id: sharex
name: ShareX
description: Use when you need to capture on-screen OSINT evidence — full page, region, or screen recording — with OCR and annotation; returns PNG/GIF/MP4 files plus extracted text.
url: https://getsharex.com/
category: evidence-capture
path:
- evidence-capture
- screen-capture
bestFor: Free, powerful Windows screen capture and recording with scrolling capture, OCR and annotation for documenting findings.
selectorsIn:
- social-profile
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open source (18+ years of development); no ads, no account. Windows only.
opsec: passive
opsecNote: Local capture of what your own screen already shows — no requests are sent to the target. Two cautions: (1) ShareX can auto-upload captures to cloud destinations, so disable/verify the "After capture" upload tasks before shooting sensitive material; (2) recordings can embed your own UI (usernames, tabs, notifications) — frame carefully and crop.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Widely used, long-lived open-source project (MIT-style licence, public GitHub and changelog); the code is auditable and the tool is purely local unless you configure uploads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- full-page-screen-capture-chrome-extension
aliases:
- ShareX screen capture
- getsharex
tags:
- evidence-capture
- screenshot
- screen-recording
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# ShareX

> A free, open-source Windows capture powerhouse — region/window/full-screen shots, scrolling capture, screen recording, OCR and annotation, all local by default.

## When to use
You need to **preserve** something you're viewing during an investigation: a profile before it's deleted, a video call frame, a map, a document. ShareX goes beyond a plain screenshot — scrolling capture grabs long pages, screen recording captures dynamic content (video, scrolling feeds) to MP4/GIF, OCR pulls text out of images, and the built-in editor lets you annotate/redact before filing. It runs entirely on your machine, so captures stay under your control.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install ShareX from https://getsharex.com/ (Windows: setup, portable, Store, or Steam build).
2. **Before capturing sensitive material, open Task settings → "After capture tasks" and turn OFF any auto-upload** so captures save locally only.
3. Pick a capture method: region, window, full screen, **scrolling capture** (for long pages), or **screen recording** (video/GIF).
4. Use the editor to annotate, highlight, or redact; use **OCR** ("Capture → Text capture (OCR)") to extract text from an image.
5. Save locally; log the source URL and capture time alongside the file — the image itself carries no trustworthy timestamp.
6. Pivot: file the capture in your evidence log; pair with a public archive for independent provenance.

## Inputs → Outputs
- **In:** whatever is on your screen — a `social-profile`, `domain`/site, video, document
- **Out:** PNG/JPG/GIF/MP4 capture files (`metadata-exif`-bearing) plus OCR-extracted text
- **Empty/negative result looks like:** DRM-protected video or hardware-overlay content may capture black frames; scrolling capture can misalign on dynamic pages — review the output.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must set up capture/upload preferences first.
- OpSec: **passive** and local — nothing goes to the target. The real risk is ShareX's optional cloud-upload destinations; confirm they're off for sensitive work.
- Windows-only. On macOS/Linux use a native equivalent.
- Captures aren't forensically timestamped on their own — pair with an archive service if the record must stand as evidence.

## Overlaps ("do both")
- Complements `[[full-page-screen-capture-chrome-extension]]` — the browser extension is a one-click full-page grab; ShareX adds screen recording, OCR and annotation for richer evidence, and works outside the browser.

## Trust & verifiability
`trust: community` — a mature, auditable open-source project that operates locally; trustworthy as a capture tool, but remember it documents *what you rendered*, not an independently verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sharex |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, domain → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
