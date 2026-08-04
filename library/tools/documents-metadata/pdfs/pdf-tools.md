---
id: pdf-tools
name: PDF Tools (Didier Stevens)
description: Use when you have a PDF and want to dissect its structure — returns objects, embedded scripts/files, and `metadata-exif`-style creator/producer fields, plus malicious-object detection.
url: https://blog.didierstevens.com/programs/pdf-tools/
category: documents-metadata
path:
- documents-metadata
- pdfs
bestFor: Command-line dissection of a PDF's internal structure — objects, streams, embedded JavaScript/files, and document metadata.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (pdfid.py, pdf-parser.py) from Didier Stevens; Python, no account.
opsec: passive
opsecNote: Fully local, offline analysis — the tools parse a file you already hold and make no network calls, leaking nothing about you or the target. Analyse a copy in an isolated environment, since PDFs can carry active/malicious content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Written by Didier Stevens, a highly reputable security researcher; these are the de-facto standard PDF forensic tools, widely used and inspectable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- xorsearch-and-xorstrings
aliases:
- pdfid
- pdf-parser
- Didier Stevens PDF tools
tags:
- pdf
- file-forensics
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# PDF Tools (Didier Stevens)

> The standard forensic toolkit for taking a PDF apart — `pdfid.py` triages it, `pdf-parser.py` walks its objects — exposing the metadata, embedded files and scripts that a viewer hides.

## When to use
You have a PDF as evidence or as a lead and need what's *inside* it: the author/creator/producer metadata (which app and often which user/organisation made it), creation/modification timestamps, embedded files or images, and any hidden or active content (JavaScript, launch actions) that signals tampering or malware. This is the go-to when a PDF's provenance or safety matters.

## How to use it (`bestInteractionPattern`: cli)
1. Download `pdfid.py` and `pdf-parser.py` from https://blog.didierstevens.com/programs/pdf-tools/ (Python).
2. Triage: `python pdfid.py file.pdf` — counts risky keywords (`/JS`, `/JavaScript`, `/OpenAction`, `/Launch`, `/EmbeddedFile`) and shows the object landscape.
3. Dissect: `python pdf-parser.py file.pdf` — walk objects/streams; use `-o`/`-s`/`--search` to pull the `/Info` dictionary (Author, Creator, Producer, dates) and extract embedded streams/files.
4. Analyse suspicious objects in isolation; extract embedded content for separate examination.
5. Pivot: Author/Producer/software strings feed `name`/tool attribution; embedded files feed further metadata analysis (e.g. images through an EXIF tool).

## Inputs → Outputs
- **In:** a local PDF file (no selector — you supply the file)
- **Out:** `metadata-exif` (the PDF's document metadata: author, creator/producer app, timestamps) plus object/structure detail and embedded-content extraction
- **Empty/negative result looks like:** a sparse `/Info` dictionary and no risky keywords — many PDFs are cleanly generated and carry little identifying metadata; absence isn't tampering.

## Gotchas & OpSec
- PDF metadata is editable and often reflects the *last* tool that saved the file (e.g. a print-to-PDF driver), not the original author — treat as a lead.
- PDFs can be actively malicious; analyse copies in a sandbox/VM and never "open" a suspect file to inspect it.
- These are analysis tools, not sanitisers — extracting an object doesn't neutralise the file.

## Overlaps ("do both")
- Pairs with string/XOR tools like [[xorsearch-and-xorstrings]] for obfuscated content, and with image-EXIF tools for any images you extract from the PDF.

## Trust & verifiability
`trust: trusted` — authored by a leading security researcher and long the standard for PDF forensics; output reflects the file's actual bytes, so findings are directly verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pdf-tools |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
