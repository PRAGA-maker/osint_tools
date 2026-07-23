---
id: annotely
name: Annotely
description: Use when you need to annotate a screenshot for a report — add arrows/highlights to mark evidence or blur personal data before sharing — an evidence-presentation and redaction aid.
url: https://annotely.com/editor
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Quickly annotating and redacting screenshots — arrows, highlights, and blurring of personal data — for investigation reports.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to use in-browser for core annotation; advanced/pro features may sit behind a paid plan.
opsec: passive
opsecNote: A browser-based image editor for YOUR screenshots. For genuine redaction, prefer blur/pixelate over a solid box you might misplace, and verify the exported image no longer contains the sensitive detail — never assume an overlay removed underlying data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small third-party web image-annotation service; fine for non-sensitive markup, but avoid uploading case-critical originals to any third party.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- annotely.com
tags:
- screenshot-annotation
- redaction
- reporting
source: cyb-detective
lastVerified: '2026-07-23'
---

# Annotely

> A simple in-browser screenshot annotator: drop arrows and highlights to point at evidence, and blur personal data before a screenshot leaves your hands.

## When to use
This is reporting/OPSEC tooling, not a data source. Use it when you have a screenshot — a profile, a post, a record — and need to (a) mark up the relevant detail with arrows/highlights for a report, or (b) redact personal data (faces, names, numbers) before sharing the image with a colleague, tip line, or public appeal. It smooths the "capture → annotate/redact → hand off" step of an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://annotely.com/editor and load your screenshot.
2. Add arrows/highlights to draw attention to the evidence.
3. Blur or pixelate any personal data that must not be shared.
4. Export the edited image and double-check the export: confirm the redacted detail is truly gone from the saved file.
5. Use in reports, appeals, or handoffs — keep an unedited original archived separately for your own records.

## Inputs → Outputs
- **In:** your own screenshot/image (no subject selector)
- **Out:** an annotated/redacted image for sharing
- **Empty/negative result looks like:** not applicable — output is whatever you produce.

## Gotchas & OpSec
- Redaction is only real if the underlying pixels are destroyed: blur/pixelate the region and verify the export, rather than trusting an overlay that a viewer might reverse or that you might place slightly off.
- Don't upload a case-critical original to a third-party site; work from a copy, and mind that anything uploaded leaves your device.
- OpSec: **passive** — it edits your images; nothing about the subject is queried.

## Overlaps ("do both")
- Pairs with dedicated redaction tools and local image editors — Annotely is fast for markup; for high-stakes redaction, use a tool that flattens and strips metadata, and verify the result.

## Trust & verifiability
`trust: unverified` — a convenient small web utility; suitable for non-sensitive markup, but for anything sensitive prefer a local editor and always verify the exported image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | annotely |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
