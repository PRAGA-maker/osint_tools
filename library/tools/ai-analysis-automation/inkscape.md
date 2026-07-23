---
id: inkscape
name: Inkscape
description: Use when you need to edit, trace, measure, or annotate images/vectors during analysis — a free vector-graphics editor useful for image forensics and evidence markup.
url: https://inkscape.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free vector editing/tracing/annotation of imagery for analysis and evidence presentation.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL); cross-platform desktop app. No account.
opsec: passive
opsecNote: Runs entirely offline on your machine — fully passive, nothing leaves your host. Ideal for handling case imagery you don't want uploaded to any web tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Mature, widely-used open-source vector editor; reputable and offline, so no data-handling risk beyond your own machine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Inkscape vector editor
tags:
- ai-analysis-automation
- image
- vector
- annotation
- forensics
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Inkscape

> A free, offline vector-graphics editor — investigator plumbing for tracing, measuring, annotating, and cleaning up imagery during analysis and reporting.

## When to use
Not a data source — reach for it when analysis needs image work you'd rather not do in a web tool: overlaying and aligning a photo against a map/satellite image for geolocation, tracing outlines to compare shapes, measuring angles/proportions, enhancing or isolating detail, redacting sensitive parts, and producing clean annotated exhibits for a report. All offline, so sensitive `image`s never leave your machine.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Inkscape for your OS from https://inkscape.org and install.
2. Import the `image`; use layers to overlay a reference (map/satellite) and adjust opacity/transform to align.
3. Trace, measure (with the measure tool), annotate, or redact as the analysis needs.
4. Export the annotated result (PNG/PDF/SVG) for your report. Pivot: alignments feed geolocation conclusions; annotated exhibits document findings.

## Inputs → Outputs
- **In:** an `image` (or blank canvas) to edit/annotate
- **Out:** an edited/annotated/traced image or exhibit (no selector output — it's a tool, not a lookup)
- **Empty/negative result looks like:** n/a — success is the edited/annotated artifact you produce.

## Gotchas & OpSec
- It's an editor, not an analyzer — it doesn't extract metadata or detect manipulation; pair with forensic tools for that.
- Editing evidence imagery: keep the original untouched and document your annotations, so the exhibit is defensible.
- Learning curve for precise overlay/measurement work.

## Overlaps ("do both")
- Complements EXIF/forensic tools and mapping — Inkscape does the visual overlay/annotation; metadata and satellite tools (`[[copernicus-browser-formerly-sentinel-hub-playground-eo-browser]]`) supply the reference data you align against.

## Trust & verifiability
`trust: trusted` — a mature, reputable open-source tool that runs offline; there's no data-handling risk, and outputs are exactly what you create.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inkscape |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
