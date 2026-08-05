---
id: overview
name: Overview
description: Use when you have a large `document-id` set (leaks, FOIA dumps, PDFs) and want to search, cluster and tag them at scale — returns entities like `name`/`email`/`address` buried across thousands of pages.
url: https://www.overviewdocs.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Investigative analysis of large document collections — full-text search, topic clustering and tagging across thousands of files.
selectorsIn:
- document-id
selectorsOut:
- name
- email
- address
status: live
pricing: free
costNote: Free and open-source (AGPL). The hosted overviewdocs.com now points to the self-hostable "overview-local" (Docker) release on GitHub; no per-seat cost.
opsec: passive
opsecNote: Self-host it (Docker) so sensitive documents never leave your control — do not upload leaked/PII-heavy material to a shared third-party instance. Run on an isolated analysis VM.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: trusted
trustNote: Built for investigative journalists (originated at the Associated Press / Knight Foundation ecosystem); open-source code is auditable and the project is well established in newsroom OSINT.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- Overview Docs
- overview-local
tags:
- document-analysis
- Tools collections/toolkits
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Overview

> An open-source document-mining platform for investigators: load thousands of pages, then full-text search, auto-cluster by topic, and tag your way to the names and facts hidden inside.

## When to use
You have a large `document-id` corpus — a leak, an FOIA/records release, seized PDFs, scanned files — and need to find the person-relevant needles (a `name`, `email`, `address`, phone, or relationship) without reading every page. Overview ingests the set, OCRs/indexes it, and lets you search and cluster to isolate the documents that matter.

## How to use it (`bestInteractionPattern`: docker)
1. Get the self-hosted release: clone `github.com/overview/overview-local` and start it with the provided Docker Compose (keeps documents local).
2. Create a document set and upload your files (PDFs, text, CSVs); Overview OCRs scans and builds a full-text index.
3. Explore: use full-text search for known selectors, browse the auto-generated topic tree, and apply tags to slice the corpus.
4. Pivot: export tagged subsets; feed extracted `name`/`email`/`address` values into people-search and email/phone tools.

## Inputs → Outputs
- **In:** `document-id` (a collection of documents/files)
- **Out:** `name`, `email`, `address` and other entities/leads found via search and clustering
- **Empty/negative result looks like:** a search that returns no documents means the selector doesn't appear in that corpus (or OCR missed it on a poor scan) — try variant spellings and check OCR quality before concluding it's absent.

## Gotchas & OpSec
- Human-in-the-loop: this is an analysis workbench — clustering and tagging are manual, judgement-driven work, not one-click answers.
- OpSec: prefer the local/Docker deployment for sensitive material; a shared instance exposes your documents to its operator.
- OCR quality gates everything — bad scans yield unsearchable text.

## Overlaps ("do both")
- Complements entity-extraction and link-analysis tools: Overview surfaces the relevant documents; a graph/NER tool turns the extracted names and relationships into a network.

## Trust & verifiability
`trust: trusted` — a mature, open-source tool built for and used by investigative journalists; the code is auditable and self-hostable, so you control both data and process.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | overview |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id → name, email, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (manual-review) |
