---
id: pdfx
name: PDFx
description: Use when you have a PDF and want its metadata plus every referenced link — returns document metadata, extracted text, and URLs/DOIs/arXiv IDs.
url: https://github.com/metachris/pdfx
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling metadata, text, and all embedded/referenced links out of a PDF from the command line.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
- domain
status: degraded
pricing: free
costNote: Free and open source (Apache 2.0). Repository archived June 2023 — still installable and working, but unmaintained.
opsec: passive
opsecNote: Metadata/text/link extraction runs locally with no network calls. The optional "download referenced PDFs / check broken links" mode DOES reach out to those URLs — skip it if you don't want to touch the referenced hosts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source utility by metachris; auditable source, but the repo is archived/unmaintained since 2023.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- pdfx
tags:
- pdf
- metadata-extraction
- documents
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# PDFx

> One command turns a PDF into its metadata, its text, and a list of every URL/DOI/arXiv reference inside it.

## When to use
You have a PDF (a report, leaked document, resume, brochure) and want to (a) read its `metadata-exif` — author, creator/producer software, creation/mod dates — and (b) harvest every link it references. The metadata can reveal who/what tool produced a document; the referenced `domain`s/URLs open new investigative threads. Document-triage tool; missing-persons value is low and indirect (a document tied to a subject may leak an author name or linked sites).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install pdfx`.
2. Run against a local or online PDF:
   ```
   pdfx document.pdf              # metadata + references to stdout
   pdfx document.pdf -j           # JSON output
   pdfx https://site/report.pdf   # works on remote PDFs
   ```
3. Read the output: document metadata block, then extracted references (URLs, DOIs, arXiv IDs). Add `-t` to also dump text.
4. Pivot: the creator/producer metadata suggests the authoring software/environment; referenced `domain`s go to WHOIS/passive-DNS; use `-c` (check links) cautiously — it fetches each URL.

## Inputs → Outputs
- **In:** a PDF file/URL (its embedded `metadata-exif`)
- **Out:** document `metadata-exif` (author, producer, dates), extracted text, referenced `domain`s/URLs/DOIs
- **Empty/negative result looks like:** empty metadata and no references — common for scrubbed or image-only/scanned PDFs (no text layer, no embedded links); OCR won't recover metadata that was never set.

## Gotchas & OpSec
- Repo is archived (2023) — it still works but won't get fixes; very unusual/newer PDFs may parse imperfectly.
- Scanned/flattened PDFs yield little (no text or link layer).
- OpSec: extraction is local/passive; the link-check/download mode is active (it contacts referenced hosts) — avoid it for sensitive targets.

## Overlaps ("do both")
- Pairs with EXIF/metadata tools (e.g. ExifTool) for deeper metadata and with IOC/link extractors — PDFx is convenient for the metadata+references combo, ExifTool for exhaustive metadata across formats.

## Trust & verifiability
`trust: community` — auditable Apache-2.0 code, though unmaintained; treat extracted metadata as author-supplied (spoofable) and verify referenced links independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pdfx |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
