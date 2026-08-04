---
id: forensicdots-de
name: ForensicDots (Dotspotter)
description: Use when you have a scanned printed `document-id` and want to reveal the hidden printer tracking dots (Machine Identification Code) — returns the printer serial/timestamp fingerprint encoded on the page.
url: https://www.forensicdots.de/
category: documents-metadata
path:
- documents-metadata
bestFor: Detecting and reading the yellow Machine Identification Code dots that colour laser printers embed in printed pages.
selectorsIn:
- document-id
selectorsOut:
- device-id
- metadata-exif
status: live
pricing: free
costNote: Free web tool (Dotspotter); donation-supported (PayPal button), no account or payment required.
opsec: passive
opsecNote: You upload a scan to their server to analyse it, so the file leaves your machine — never submit a genuinely sensitive/case document to a third-party service; test the technique here, then analyse real evidence with an offline tool. Nothing is sent to the document's author.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Runs by the EFF/academic-documented MIC decoding method; community-maintained project, results should be corroborated with the EFF's own dot-decoding guidance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Dotspotter
- forensicdots
- Machine Identification Code decoder
tags:
- printer-forensics
- yellow-dots
- machine-identification-code
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ForensicDots (Dotspotter)

> Reveals the near-invisible yellow tracking dots colour laser printers stamp on every page — the Machine Identification Code that encodes the printer's serial number and a timestamp.

## When to use
You have a scanned printed page (a leaked memo, a threatening letter, a forged document) and want to know *which printer produced it and when*. Most colour laser printers embed a hidden dot grid (MIC) carrying the device serial and a date/time stamp. Decoding it can tie a physical document to a specific printer (`device-id`) and time — a strong forensic pivot in a document-provenance investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Scan the printed page at **600 dpi, 24-bit colour**, saved as a JPG under 10 MB (photo-quality settings to preserve the faint dots).
2. Go to https://www.forensicdots.de/ and upload the scan to Dotspotter.
3. The tool highlights the detected yellow-dot pattern on the page.
4. Decode the grid (with the tool's/EFF's key) into the printer serial number and timestamp.
5. Pivot: the `device-id` (serial) can be matched against known devices; the timestamp corroborates or contradicts a claimed creation date.

## Inputs → Outputs
- **In:** `document-id` (a high-res colour scan of a printed page)
- **Out:** `device-id` (printer serial) and `metadata-exif`-style embedded timestamp
- **Empty/negative result looks like:** no dots detected — either the printer doesn't embed MIC (many mono/inkjet printers don't), the scan resolution/quality was too low, or the dots were stripped; re-scan at higher dpi before concluding absence.

## Gotchas & OpSec
- Scan quality is everything: below 600 dpi or with aggressive JPEG compression the dots vanish.
- OpSec: this is a third-party upload — don't submit truly sensitive originals; use it to learn/confirm the technique, then decode case evidence offline.
- Not all printers embed MIC, and patterns vary by manufacturer.

## Overlaps ("do both")
- Complements EXIF/document-metadata tools: those read digital metadata, while ForensicDots recovers a *physical-print* fingerprint the digital file never had — do both when a document exists in both scanned and native form.

## Trust & verifiability
`trust: community` — a community tool implementing the well-documented (EFF-published) MIC decoding method; verify any serial/timestamp reading against the EFF dot-decoding reference rather than trusting the tool blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensicdots-de |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → device-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
