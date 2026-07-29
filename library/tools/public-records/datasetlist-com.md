---
id: datasetlist-com
name: Dataset List
description: Use when you need a public machine-learning dataset (faces, images, text, audio) to build or benchmark a recognition/analysis model — returns a categorized directory of datasets with licenses.
url: https://www.datasetlist.com/
category: public-records
path:
- public-records
bestFor: Finding public ML datasets (computer vision, NLP, audio, medical) by category, with licensing and source links.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free to browse; datasets it links carry their own licenses (some non-commercial/research-only).
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about a subject. It's a tooling/reference resource, not a query against a person; respect each dataset's license and any privacy constraints when you use one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained directory of ML datasets; useful as an index, but its listings appear to have last been actively updated around 2020–2021, so treat currency as partial.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- datasetlist
- Dataset List
tags:
- dataset-directory
- machine-learning
- tooling-resource
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Dataset List

> A categorized directory of public machine-learning datasets — the resource for sourcing training/benchmark data when you're building your own recognition or analysis tooling.

## When to use
This is tooling infrastructure, not a person-finder. Reach for it when your investigation needs a *capability* you must build or benchmark — a face-recognition baseline, an image classifier, a language/audio model — and you need public datasets (with clear licensing) to train or test on. It indexes datasets across computer vision, NLP, audio, medical, and other domains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open datasetlist.com and browse by category (CV, NLP, Audio, Medical, etc.) or year.
2. Open a dataset entry for its description, size, license, source link, and associated paper.
3. Check the license (some are research/non-commercial only) before downloading.
4. Follow the source link to obtain the data.
5. Pivot: the dataset feeds your model-building; the resulting model then processes your actual evidence.

## Inputs → Outputs
- **In:** the type of data capability you need (no subject selector)
- **Out:** a shortlist of public datasets with licenses/sources — feeds tool-building, not direct investigation
- **Empty/negative result looks like:** no dataset for a niche need, or stale entries/dead links — cross-check Kaggle, HuggingFace, or UCI, which the site also links.

## Gotchas & OpSec
- **Not an investigative lookup** — it returns datasets, not intelligence about a subject; wrong tool if you're trying to identify a person.
- Apparent staleness (last big updates ~2020–2021): verify a dataset is still hosted, and prefer current hubs (HuggingFace/Kaggle) for recent releases.
- **License-gate:** honor each dataset's terms and any embedded-privacy constraints (e.g. face datasets).

## Overlaps ("do both")
- Complements the live model hubs (Kaggle, HuggingFace, UCI) it links — use this as a curated index and those for current, downloadable data.

## Trust & verifiability
`trust: community` — a helpful community index whose currency is partial; treat it as a starting map and verify individual dataset links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datasetlist-com |
