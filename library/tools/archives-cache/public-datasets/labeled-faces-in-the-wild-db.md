---
id: labeled-faces-in-the-wild-db
name: Labeled Faces in the Wild (LFW)
description: Use when you need a labeled benchmark set of real-world `face` images to test, tune or baseline a face-recognition/verification pipeline — returns 13,233 named face photos of 5,749 people.
url: https://vis-www.cs.umass.edu/lfw/
category: archives-cache
path:
- archives-cache
- public-datasets
bestFor: A canonical labeled face dataset for benchmarking and validating face-recognition tools before you trust them on a case.
selectorsIn:
- face
selectorsOut:
- face
- name
status: live
pricing: free
costNote: Free academic download; no account or payment. Also bundled in scikit-learn, TensorFlow Datasets and similar libraries.
opsec: passive
opsecNote: Static academic dataset retrieval — no target interaction and nothing exposed. Note the images are real people (mostly public figures) scraped from news; handle in line with data-use norms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, widely cited benchmark maintained by University of Massachusetts researchers; the de-facto reference set for face-verification evaluation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- LFW
- Labeled Faces in the Wild
tags:
- face-dataset
- benchmark
- public-dataset
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Labeled Faces in the Wild (LFW)

> The reference face dataset — 13,233 web photos of 5,749 named people — used to benchmark and sanity-check face-recognition systems, not to search for an individual.

## When to use
You're evaluating or calibrating a face-recognition/verification tool and need ground-truth data: a standard, labeled set of "in the wild" faces (varied pose, lighting, resolution) with known identities and official train/test splits. Reach for LFW to measure how well an FR pipeline actually performs before you rely on it in an investigation — a reality check on the tooling, not a lookup of your subject. (The identities are mostly public figures from ~2007-era news, so it is a *benchmark*, not a live people index.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vis-www.cs.umass.edu/lfw/ and download the image set plus the pairs/splits files (or load it via `sklearn.datasets.fetch_lfw_people` / TensorFlow Datasets `lfw`).
2. Note the structure: 13,233 images, 5,749 people, 1,680 of them with ≥2 photos; faces were detected by the Viola-Jones detector at 250×250.
3. Run your face-recognition tool against the recommended 10-fold verification protocol (matched/mismatched pairs) to get a comparable accuracy figure.
4. Compare that number against published LFW baselines to judge whether the tool is trustworthy for real work.
5. Pivot: once a tool passes muster on LFW, apply it to actual case imagery — LFW itself is the yardstick, not the target data.

## Inputs → Outputs
- **In:** a `face`-recognition model/pipeline to evaluate (you supply the algorithm; LFW supplies the data)
- **Out:** labeled `face` images with person `name` labels and standardized evaluation splits/accuracy
- **Empty/negative result looks like:** N/A for search — it is a fixed dataset, not a query engine. It will *not* tell you who an unknown face is; a specific missing person is almost certainly not in it.

## Gotchas & OpSec
- **This is not a lookup tool.** You cannot submit an unknown photo and identify someone; LFW is a static benchmark of mostly-celebrity faces.
- The set is old and demographically skewed (a documented fairness limitation) — good FR scores on LFW don't guarantee good real-world, cross-demographic performance.
- OpSec: **passive** — a plain academic download.

## Overlaps ("do both")
- Pairs with actual face-search engines (PimEyes, FaceCheck-style tools) and detectors — use LFW to *validate* those tools, then use the tools themselves to *search* for a person.

## Trust & verifiability
`trust: trusted` — a canonical, heavily cited academic benchmark maintained by UMass. The labels are reliable; just remember its purpose is evaluation, and its age/composition limit how far its results generalize.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | labeled-faces-in-the-wild-db |
| category | archives-cache |
| selectorsIn → selectorsOut | face → face, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
