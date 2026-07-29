---
id: cute-pdf-writer-program
name: Cute PDF Writer Program
description: Use when you need to turn a web page, record, or on-screen exhibit into a fixed PDF for the case file — a virtual printer that outputs a `document-id` (PDF) exhibit.
url: http://www.cutepdf.com/Products/CutePDF/writer.asp
category: documents-metadata
path:
- documents-metadata
bestFor: Printing any viewable page or document to a stable PDF exhibit on Windows.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: CutePDF Writer (basic PDF creation) is free; CutePDF Pro (editing, forms, security) is paid.
opsec: passive
opsecNote: Runs entirely locally as a Windows print driver — it sends nothing to a network and reveals nothing about a target. It captures whatever is on screen, so scrub your own username/paths from headers before filing the output as an exhibit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Long-standing third-party Windows utility (Acro Software); free version bundles/prompts for a converter dependency (Ghostscript). Vet the installer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- CutePDF Writer
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- evidence-capture
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Cute PDF Writer Program

> A free Windows virtual-printer that "prints" any viewable page to PDF — handy for freezing web pages and records into stable exhibits for the case file.

## When to use
You are looking at something on a Windows machine — a web record, a report, a chat view — and need a fixed, shareable PDF copy for evidence, from an app that offers no native export. CutePDF appears as a printer; anything printable becomes a PDF. It produces exhibits, not intelligence about a subject.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install CutePDF Writer (and its Ghostscript-based converter when prompted) on Windows.
2. In any application, choose **Print** and select **CutePDF Writer** as the printer.
3. Print; save the resulting PDF to your evidence folder with a descriptive, dated filename.
4. Hash the PDF and log the capture time/source URL in your evidence register.
5. No pivot — the output is a preserved `document-id` exhibit.

## Inputs → Outputs
- **In:** none as a selector — whatever page/document you print
- **Out:** `document-id` (a PDF exhibit)
- **Empty/negative result looks like:** a blank or partial PDF if the source app renders poorly to print — verify the PDF matches what you saw before relying on it.

## Gotchas & OpSec
- Prefer a proper web-archiving tool (which records URL, timestamp, and full DOM) for web evidence; a printed PDF is a weaker capture that omits provenance.
- Free version historically bundles/prompts for extra software — decline unwanted add-ons and vet the installer.
- OpSec: **passive** and fully local; nothing leaves the machine.

## Overlaps ("do both")
- Pairs with a timestamped web-archive/screenshot tool for provenance-rich captures; use CutePDF only when native export is unavailable.

## Trust & verifiability
`trust: unverified` — third-party utility. The PDF is only as trustworthy as your capture discipline; record source and time so the exhibit is defensible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cute-pdf-writer-program |
| category | documents-metadata |
| selectorsIn → selectorsOut |  → document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
