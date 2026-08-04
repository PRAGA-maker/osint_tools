---
id: intellyweave
name: IntellyWeave
description: Use when you have a pile of documents (`document-id`, PDFs/DOCX) and want AI-driven entity extraction and link analysis — returns names, organisations, locations and relationship/geospatial graphs with confidence-scored hypotheses.
url: https://github.com/vericle/intellyweave
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning document dumps into extracted entities, relationship graphs and geospatial views for investigation.
selectorsIn:
- document-id
- name
selectorsOut:
- name
- employer-org
- geolocation
- associate
status: live
pricing: free
costNote: Free and open-source (BSD-3-Clause). Self-hosted; requires an LLM API key (OpenAI/Anthropic/Google) or a local Ollama model.
opsec: passive
opsecNote: Runs locally on your own documents, so it doesn't touch any external target — but if you configure a cloud LLM, your document contents are sent to that provider for processing. Use a local Ollama model to keep sensitive case material fully offline.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: docker
trust: community
trustNote: Active beta community project (vericle, ~70 stars); AI extraction can hallucinate, so treat entities/hypotheses as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- intelly-weave
tags:
- document-analysis
- entity-extraction
- link-analysis
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# IntellyWeave

> A self-hosted, AI-powered platform that ingests documents and extracts entities, maps relationships, plots geolocations and proposes confidence-scored investigative hypotheses.

## When to use
You have a corpus of documents tied to a case (`document-id`s, PDFs, DOCX, reports, dumps) and want to turn that "document chaos" into structured intelligence: who and what is named, how entities connect, where events happened, and what hypotheses the evidence supports. Best for the analysis stage after you've collected material, not for live collection.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo; start the local vector DB with Docker (`docker compose up` for Weaviate) and the FastAPI backend (Python 3.12).
2. Configure an LLM key (OpenAI/Anthropic/Google) or point it at a local Ollama model for offline use; `elysia start`.
3. Upload documents (PDF/DOCX/TXT/Markdown) — GLiNER extracts persons, orgs, locations, dates, events, laws, cryptonyms.
4. Explore the outputs: relationship graphs, 3D geospatial map (Mapbox), and the two-agent (Quartermaster/Case Officer) hypothesis workflow.
5. Ask natural-language questions and review confidence-scored answers; pivot on extracted `name`/`employer-org`/`geolocation` into other tools.

## Inputs → Outputs
- **In:** documents (`document-id`, PDF/DOCX/TXT/MD) and natural-language questions.
- **Out:** extracted `name`s, `employer-org`s, `associate` links, `geolocation`s, relationship/network graphs, and hypothesis assessments with confidence scores.
- **Empty/negative result looks like:** few or no entities extracted — scanned/low-text documents (OCR first) or genuinely sparse material.

## Gotchas & OpSec
- Human-in-the-loop: needs an LLM key or local model; **AI extraction can hallucinate entities and links** — verify against the source document before acting.
- Cloud LLMs send your documents off-box; use local Ollama for sensitive cases.
- Beta software with a small user base; expect setup friction and rough edges.

## Overlaps ("do both")
- Analysis-side counterpart to collection tools — feed it the documents/reports gathered by tools like `[[recon-ng]]` or `[[reconftw]]`, and use its graph to organise what broad sweeps like `[[e4gl30s1nt]]` surface.

## Trust & verifiability
`trust: community` — an active but early-stage project using LLM extraction; every entity, link and hypothesis is a machine-generated lead that must be confirmed against the underlying document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intellyweave |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id, name → name, employer-org, geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (api-key) |
