---
id: voyant-tools-org
name: Voyant Tools
description: Use when you have a body of text or documents (`.txt`, `.docx`, `.pdf`, a pasted corpus) and want to surface the most frequent words, names and phrases — returns `name`/`associate` leads and term trends.
url: https://voyant-tools.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Fast frequency/keyword/context analysis of a document set to find recurring names and themes.
selectorsIn: []
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free and open-source (GPL). Hosted web version at voyant-tools.org, plus a downloadable desktop "VoyantServer" for offline/local use.
opsec: passive
opsecNote: The hosted version uploads your corpus to voyant-tools.org servers — do NOT paste sensitive/leaked documents into the public instance. For confidential material run the local VoyantServer instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running academic project (Stéphan Sinclair & Geoffrey Rockwell) widely used in the digital-humanities community; open source and inspectable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- Voyant
- voyant-tools.org
tags:
- Files
- text-analysis
- corpus
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Voyant Tools

> Web-based text-mining workbench: drop in a pile of documents and see the words, names and phrases that dominate them.

## When to use
You have a large body of text — a document dump, a set of PDFs/emails, transcripts, a scraped forum — and want to find which `name`s, entities and terms recur so you know where to dig. Voyant turns an unreadable corpus into word-frequency clouds, trend lines and keyword-in-context concordances, quickly exposing the most-mentioned people (`associate` candidates) and topics without reading every page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://voyant-tools.org and add your corpus: upload files, paste raw text, or point it at a URL.
2. The default dashboard loads:
   - **Cirrus** (word cloud) — hover a word for its count; the biggest words are the dominant terms/names.
   - **Trends** — how a term's frequency rises/falls across documents.
   - **Contexts / KWIC** — every occurrence of a term with its surrounding sentence.
3. Add a stop-word list to strip filler and set a minimum frequency so real names surface above noise.
4. Search a specific `name` to see where and how often it appears and who co-occurs with it.
5. Pivot: surfaced names feed people-search; co-occurring names feed relationship mapping. For confidential material, download and run the local VoyantServer instead of the public site.

## Inputs → Outputs
- **In:** a text corpus (uploaded documents, pasted text, or a URL)
- **Out:** word-frequency lists / clouds, term trend graphs, keyword-in-context concordances, most-frequent `name`/`associate` mentions
- **Empty/negative result looks like:** a flat cloud of only common stop-words — means the corpus is too small or you haven't filtered stop-words; add more text or a stop-word list.

## Gotchas & OpSec
- OpSec: the public instance stores your uploaded corpus on a third-party server — never paste sensitive, leaked, or PII-heavy documents there; use the local VoyantServer for those.
- It counts strings, not entities — "John Smith" and "J. Smith" are separate tokens; normalise names manually.
- Frequency ≠ importance; a rarely-named person can still be central. Use Voyant to prioritise, not to conclude.

## Overlaps ("do both")
- Pairs with an OCR step like `[[online-ocr-converter]]` — OCR turns scanned documents into machine-readable text, then Voyant mines that text for names and themes.

## Trust & verifiability
`trust: trusted` — a mature, open-source academic project widely taught in digital humanities; the analysis is transparent and reproducible, though it's a counting tool, not an entity-resolution engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voyant-tools-org |
| category | documents-metadata |
| selectorsIn → selectorsOut |  → name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
