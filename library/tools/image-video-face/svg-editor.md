---
id: svg-editor
name: SVG Editor
description: Use when you have an SVG `image` and want to inspect, edit, annotate or redact it in-browser — returns a modified image/vector, useful for markup and evidence handling.
url: https://svg-edit.github.io/svgedit/
category: image-video-face
path:
- image-video-face
bestFor: In-browser inspecting, annotating and redacting of SVG/vector graphics without installing software.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open-source (runs entirely client-side in the browser); can also be self-hosted. No account, no upload to a server.
opsec: passive
opsecNote: Fully passive and offline-capable — SVGEdit is client-side JavaScript, so images you load are processed in your browser and not uploaded anywhere. This makes it safe for handling sensitive case imagery you don't want to send to a third-party service. Prefer a self-hosted/local copy for the most sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Mature open-source project (SVGEdit, 15+ years, active on GitHub); code is auditable and runs locally, so it is safe and predictable — it's a graphics editor, so its OSINT role is support/annotation, not discovery.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- SVGEdit
- svg-edit
tags:
- image-editing
- vector-graphics
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# SVG Editor

> A free, open-source, browser-based SVG/vector editor — a support tool for inspecting, annotating and redacting graphics locally, not a discovery tool.

## When to use
You have a vector `image` (an SVG map fragment, a logo, a diagram, a screenshot exported as SVG) and need to examine or modify it: annotate a scene, box/blur-out identifying details before sharing, extract embedded text/paths, or clean up a graphic for a report. Because SVGEdit runs entirely in your browser, it's a safe way to handle sensitive evidence imagery without uploading it to an online editor. It does not find information — it's the utility you use *after* you have an image.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://svg-edit.github.io/svgedit/ (or run a local/self-hosted copy for sensitive files).
2. Open your SVG (File → Open) or paste/import a graphic.
3. Inspect the layers/paths; use the shape, text and colour tools to annotate, highlight, or redact regions.
4. Export the result (File → Save/Export) as SVG or a raster image.
5. Pivot: any embedded text or coordinates you uncover in the SVG structure become new leads; a redacted copy is what you attach to shareable reports.

## Inputs → Outputs
- **In:** SVG/vector `image`
- **Out:** modified/annotated/redacted `image`
- **Empty/negative result looks like:** N/A — it's an editor, not a lookup; "nothing found" isn't a concept here. If a file won't open it's likely malformed or not actually SVG.

## Gotchas & OpSec
- It edits vector SVGs; complex raster photos are outside its purpose (use a raster editor for those).
- Redaction must remove underlying data, not just cover it — delete redacted paths/text, don't just draw a black box over them, or the original remains in the file.
- OpSec: **passive** and local — nothing leaves your browser, which is exactly why it suits sensitive imagery.

## Overlaps ("do both")
- Pair with EXIF/metadata viewers and reverse-image tools — those *extract intelligence* from an image; SVGEdit is where you then *annotate or safely redact* it for sharing.

## Trust & verifiability
`trust: community` — a mature, auditable open-source project that runs client-side. There's no data source to distrust; the only judgement call is your own redaction discipline before sharing edited files.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | svg-editor |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
