---
id: docmind-ai
name: DocMind AI
description: Use when you have sensitive documents to query and want a local RAG chat over them with no cloud exposure — returns summaries, Q&A and extracted insights processed entirely offline.
url: https://github.com/BjornMelin/docmind-ai-llm
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Private, offline question-answering and summarisation over collected documents.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free/open-source (MIT); self-hosted. You supply a local LLM backend (Ollama, vLLM, LM Studio); optional GPU speeds it up.
opsec: passive
opsecNote: Passive and self-contained — the developers block remote LLM endpoints by default, so documents, embeddings and retrieval stay on your machine. Ideal for confidential case files. Only enable remote endpoints deliberately, and never for sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community single-author project; a Streamlit app wrapping local RAG. Output quality depends on the local model you attach.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ollama
aliases:
- docmind-ai-llm
tags:
- llm
- local-ai
- rag
- document-analysis
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# DocMind AI

> A self-hosted Streamlit app for private RAG over your documents — ask questions and get summaries/insights with a local LLM, nothing leaving your machine.

## When to use
You have collected documents (PDFs, Word files, spreadsheets, text) that are too sensitive for a hosted AI service and want to query them conversationally — summarise, extract entities, ask "who/where/when," build a timeline. DocMind runs a local retrieval pipeline plus a local LLM backend, so processing stays offline. It's an analysis layer over material you already hold; it produces no OSINT selectors itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Clone the repo; install Python 3.12+ and run `uv sync` for dependencies.
2. Stand up a local LLM backend separately — e.g. `[[ollama]]`, vLLM, or LM Studio — and point DocMind at it via environment variables.
3. Launch the UI: `streamlit run app.py`, then open it in your browser.
4. Upload documents; the app parses and indexes them (dense + sparse retrieval, optional knowledge graph), then answer questions in the chat.
5. Pivot: names/locations/dates it extracts become fresh selectors for the rest of the library — but verify them, as local models can hallucinate.

## Inputs → Outputs
- **In:** your own documents (PDF, Office, text) + questions (no OSINT selector)
- **Out:** summaries, Q&A answers, extracted insights; optional knowledge-graph and searchable-PDF export
- **Empty/negative result looks like:** vague or hallucinated answers when the documents don't contain the fact, or the local model is too small — treat outputs as leads to verify.

## Gotchas & OpSec
- Human-in-the-loop: none to operate, but you must run and secure the local LLM backend.
- OpSec: passive/offline — remote endpoints are blocked by default; keep them off for sensitive files.
- RAG answers are only as good as the retrieval + local model; always trace a claim back to the source document.

## Overlaps ("do both")
- Pairs directly with `[[ollama]]` (a common local backend) — Ollama runs the model, DocMind adds the document-retrieval/chat layer on top for querying files specifically.

## Trust & verifiability
`trust: unverified` — a small open-source project; the code is inspectable and runs locally, but answer accuracy depends on your model and retrieval config, so corroborate every extracted fact against the underlying document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | docmind-ai |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
