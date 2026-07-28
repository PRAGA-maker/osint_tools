---
id: pixplot
name: PixPlot
description: Use when you have a large `image` collection and want an ML-driven interactive map clustering visually-similar images — surfaces patterns, duplicates, and outliers for triage.
url: https://github.com/YaleDHLab/pix-plot
category: image-video-face
path:
- image-video-face
bestFor: Visualizing and clustering thousands of images by visual similarity to spot patterns, near-duplicates, and outliers.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (Yale DHLab); runs locally in Python, benefits from a GPU on large sets.
opsec: passive
opsecNote: Runs entirely locally on images you already hold — nothing uploads and nothing touches a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Academic open-source tool from Yale's Digital Humanities Lab, listed in Bellingcat's toolkit; a visualization aid, not an identification oracle.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- PixPlot
- pix-plot
tags:
- bellingcat-toolkit
- misc
- image-analysis
- clustering
- machine-learning
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# PixPlot

> Throw thousands of images at it and get back a zoomable map where visually-similar pictures cluster together — so patterns and oddballs jump out instead of hiding in a folder.

## When to use
You've amassed a large `image` set — scraped from a profile/site, pulled from a case, or a dumped gallery — and eyeballing them one by one is hopeless. PixPlot uses a neural network to embed each image and lays them out so similar images sit together, letting you spot themes, near-duplicates, and outliers (the one image that doesn't belong is often the interesting one).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install pixplot` (or clone `https://github.com/YaleDHLab/pix-plot`); it needs Python and works far faster with a GPU on big sets.
2. Point it at a folder of images: `pixplot --images "path/to/*.jpg"`.
3. It processes the set and generates a local WebGL visualization; open the produced site in your browser.
4. Explore the map — pan/zoom into clusters, inspect outliers, and identify duplicates or recurring scenes.
5. Pivot: an outlier or a tight cluster tells you which images to pull for reverse-image search, EXIF ([[exif-viewer-addons-mozilla-org]]), or manual review.

## Inputs → Outputs
- **In:** a local `image` collection (a folder of images)
- **Out:** an interactive similarity map — visual clusters, near-duplicates, and outliers
- **Empty/negative result looks like:** a formless blob with no clear clusters — the set may be too small or too visually uniform for structure to emerge; it's a triage aid, not a verdict.

## Gotchas & OpSec
- It clusters by **visual similarity**, not identity — it does not recognize people or tell you who's who; it points you at what to look at.
- Large sets need real compute (GPU strongly helps); processing can be slow on a laptop.
- OpSec: fully local; safe for sensitive image sets.

## Overlaps ("do both")
- Feeds a targeted workflow: cluster with PixPlot, then run standout images through reverse-image search and [[exif-viewer-addons-mozilla-org]] for metadata/GPS.

## Trust & verifiability
`trust: community` — a reputable academic tool; it organizes images faithfully but makes no claims about content, so every lead it surfaces still needs independent verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pixplot |
| category | image-video-face |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
