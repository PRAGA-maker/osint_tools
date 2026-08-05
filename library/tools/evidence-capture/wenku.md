---
id: wenku
name: Wenku
description: Use when you have a Baidu Wenku document URL and want to download/capture the document without a Baidu account or paid credits — a document-downloader for evidence capture; returns the file and its metadata.
url: https://pypi.org/project/wenku/
category: evidence-capture
path:
- evidence-capture
bestFor: Downloading Baidu Wenku documents without registration for offline evidence capture.
selectorsIn:
- document-id
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source Python package on PyPI; you run it yourself (needs Python).
opsec: active
opsecNote: The downloader fetches the document from Baidu's servers, so Baidu sees the request in real time (active). Route it through a VPN/sock-puppet if the retrieval itself is sensitive, and analyse downloaded files in a sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: A small open-source PyPI tool; convenient but dependent on Baidu Wenku's current page structure, so it can break when Baidu changes their site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- baidu wenku downloader
tags:
- Downloaders
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Wenku

> A Python tool that downloads Baidu Wenku documents without an account — capture Chinese-language documents locked behind Baidu's registration/credit wall.

## When to use
Evidence capture on Chinese-language material. Baidu Wenku hosts a huge library of documents (reports, forms, presentations) that are awkward to save — often gated behind a Baidu login or paid credits. When a lead points to a Wenku `document-id`/URL, this tool pulls the document to disk so you can read, preserve, and analyse it (including any `metadata-exif`) offline.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install it: `pip install wenku` (in an isolated Python environment).
2. Provide the target Baidu Wenku document URL/ID to the tool.
3. It fetches and reconstructs the document into a local file.
4. Preserve the download as evidence (note the capture time/source) and inspect its metadata.
5. Pivot: the document's content/`metadata-exif` may reveal authors, orgs, or identifiers to chase further.

## Inputs → Outputs
- **In:** a Baidu Wenku `document-id`/URL
- **Out:** the downloaded document file and its `metadata-exif`
- **Empty/negative result looks like:** download fails/partial — Baidu changed their page structure, the doc is region-locked, or it requires interaction the tool can't do; try a manual capture.

## Gotchas & OpSec
- **Fragile:** it depends on Baidu Wenku's current layout and can break without notice.
- **Active retrieval:** Baidu sees the fetch; use a VPN/sock-puppet for sensitive pulls.
- Handle downloaded files in a sandbox and document your capture for evidentiary integrity.

## Overlaps ("do both")
- Pairs with general web-archiving/capture tools for preserving the source page, and with document-metadata analyzers for what you download.

## Trust & verifiability
`trust: community` — a small open-source downloader; the file it returns is authentic to Baidu's copy, but verify integrity and record provenance since the tool can silently fail on Baidu changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wenku |
| category | evidence-capture |
| selectorsIn → selectorsOut | document-id → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | active |
| human-in-loop | no |
