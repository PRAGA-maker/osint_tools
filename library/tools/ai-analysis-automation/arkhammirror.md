---
id: arkhammirror
name: ArkhamMirror
description: Use when you have a pile of documents to analyze and want structured intelligence — returns extracted entities (`name`, `associate`), timelines, and link graphs.
url: https://github.com/mantisfury/ArkhamMirror
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Local-first, AI-assisted analysis of document sets — entity extraction, timelines, and network graphs.
selectorsIn:
- document-id
selectorsOut:
- name
- associate
- geolocation
status: live
pricing: free
costNote: Free and open source; self-hosted via Docker/local install (your own compute; optional local or API LLM).
opsec: passive
opsecNote: Explicitly local-first and air-gap capable — documents stay on your machine and nothing is exported unless you choose to. If you wire it to a cloud LLM API, your document text goes to that provider; keep it fully local for sensitive material.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Actively-maintained open-source project (also branded "SHATTERED"); a capable community tool but not an accredited forensics product — verify its AI-derived findings.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SHATTERED
- mantisfury/ArkhamMirror
tags:
- other-tools
- document-analysis
- entity-extraction
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# ArkhamMirror

> A local-first, AI-assisted investigation platform — feed it documents and it extracts entities, builds timelines, and visualizes the network between people, places, and events.

## When to use
You have a corpus of documents — leaked files, court records, PDFs, images, DOCX — and need to turn them into structured intelligence: who is named, how they connect, what happened when, and where the contradictions are. ArkhamMirror is built for exactly this "make sense of a document dump" phase, keeping everything on your own machine.

## How to use it (`bestInteractionPattern`: docker)
1. Clone https://github.com/mantisfury/ArkhamMirror and deploy via Docker (Python 3.10+, React, PostgreSQL under the hood).
2. Ingest documents (PDF/image/DOCX and more); let it run entity extraction, media forensics, and temporal analysis.
3. Explore the graph (multiple layout modes), run semantic/keyword search, and use the competing-hypotheses framework to structure the analysis.
4. Manually review AI outputs — treat extracted entities/links as leads, confirm against the source documents.
5. Pivot: extracted `name`s/`associate`s feed people-search and social tooling; extracted `geolocation`s/dates anchor a timeline.

## Inputs → Outputs
- **In:** documents (`document-id`-level material: PDFs, images, DOCX)
- **Out:** extracted `name`s, `associate` links (network graph), `geolocation`s, timelines, contradiction flags
- **Empty/negative result looks like:** sparse graphs / few entities from low-text or heavily-scanned docs — OCR/quality limits extraction; verify manually before concluding "nothing there."

## Gotchas & OpSec
- AI-assisted extraction can hallucinate or mis-link — every entity/relationship is a lead to confirm against the primary document, not a fact.
- Self-hosting means you own the compute and updates; keep it patched.
- If you connect a cloud LLM, document text leaves your machine — use a local model for sensitive/air-gapped work.
- Requires some technical setup (Docker/DB) versus a hosted tool.

## Overlaps ("do both")
- Pairs with people-search and link-analysis tools — ArkhamMirror surfaces entities and connections from the documents, while people-search enriches each named person and dedicated graph tools deepen the network view.

## Trust & verifiability
`trust: community` — a capable, actively-maintained open-source project, but its AI-derived outputs are not evidence on their own; verifiability rests on tracing every finding back to the source document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arkhammirror |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id → name, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (manual-review) |
