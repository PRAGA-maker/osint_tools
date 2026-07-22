---
id: visual-genome
name: Visual Genome
description: Use when you need a large annotated image dataset (objects, regions, relationships) to build or benchmark image-analysis tooling — returns bulk `image` corpus data, not per-target lookups.
url: https://visualgenome.org/
category: archives-cache
path:
- archives-cache
- public-datasets
bestFor: Sourcing a densely-annotated image corpus for training or evaluating scene-understanding / image-analysis models.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free for academic/research use; images and annotations are downloadable in bulk (JSON + image links), no payment.
opsec: passive
opsecNote: This is infrastructure, not a target lookup — you download a static research dataset. There is no interaction with any subject and nothing is disclosed about an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A well-known academic dataset (Stanford, Krishna et al.); reputable for research, but it is a fixed corpus of everyday web images with crowd-sourced annotations, not an investigative source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- VisualGenome
- Visual Genome dataset
tags:
- public-datasets
- image-analysis
- ml-training-data
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Visual Genome

> A large Stanford research dataset of ~100k images densely annotated with objects, regions, attributes and relationship graphs — tooling infrastructure for image analysis, not a per-person lookup.

## When to use
This is not a service you query with a subject's photo. Reach for it when the *investigation tooling* is the task: you are building, fine-tuning or benchmarking a scene-understanding / object-relationship model (e.g. to auto-describe images, detect objects, or reason over relationships in seized media) and need labelled training/eval data. Visual Genome supplies images plus structured annotations — objects, bounding-box regions, attributes, pairwise relationships, region descriptions and question-answer pairs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://visualgenome.org/ and go to the download/API section.
2. Pull the components you need: image URLs, region descriptions, objects, attributes, relationships, and scene graphs (distributed as JSON) — or use the documented API/data files.
3. Load into your ML/analysis pipeline as training or evaluation data.
4. Pivot: use the trained/benchmarked model on your actual case media; Visual Genome itself yields no subject data.

## Inputs → Outputs
- **In:** `image` (conceptually — you consume the corpus of images and their annotations)
- **Out:** none per-target — bulk annotated image data (objects, regions, relationship graphs) for model building
- **Empty/negative result looks like:** N/A as a lookup; the only "failure" is that a specific object class or scene type you need is under-represented in the fixed corpus.

## Gotchas & OpSec
- Not a search tool: you cannot look a person up here. Mislabelling it as a lookup wastes case time.
- Fixed academic corpus of ordinary web images; check the licence for your use and expect dataset bias.
- Fully passive — a static download, no target exposure.

## Overlaps ("do both")
- Pairs with other public image/vision datasets and with reverse-image and face-matching *services* — those do per-target lookups; this only trains/benchmarks the models behind them.

## Trust & verifiability
`trust: unverified` — a reputable, widely-cited academic dataset, but its annotations are crowd-sourced and its images are everyday web photos, so it is research infrastructure rather than an evidentiary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | visual-genome |
| category | archives-cache |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
