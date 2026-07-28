---
id: binvis
name: BinVis.io
description: Use when you have a file of unknown type/contents and want to visually spot its structure, embedded data or file-type regions — returns metadata-exif style structural clues.
url: https://binvis.io/
category: documents-metadata
path:
- documents-metadata
bestFor: Visually fingerprinting a binary/file to spot embedded files, encryption, padding or hidden data.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, browser-based; the analysis runs client-side in your browser.
opsec: passive
opsecNote: Processing is client-side, so the file isn't uploaded to a server — but confirm that before dropping in sensitive evidence, and prefer an offline copy of the tool for classified material. Analysing a file leaks nothing to its author.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source visualiser by a known security author (Aldo Cortesi); the technique (space-filling byte plots) is well documented.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- binvis
- binary visualiser
tags:
- file-analysis
- binary
- forensics
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# BinVis.io

> An interactive byte-visualiser: drop in a file and see its structure as a picture — a fast way to spot embedded files, encryption, or hidden regions before you dig in with hex tools.

## When to use
You have a file — an attachment, a recovered image, a suspicious download, something with a wrong/missing extension — and want a quick read on what it actually contains. BinVis renders the bytes as a space-filling colour map so that different content (text, compressed/encrypted data, executable code, padding, an appended second file) shows as visually distinct regions. Use it to triage a file's type and spot anomalies (steganography, appended archives, embedded images) before committing to deeper forensic tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://binvis.io/ and load your file (processing is client-side in the browser).
2. View the byte-plot: look for distinct blocks — high-entropy noise (compressed/encrypted), structured stripes (text/records), and abrupt boundaries (an appended or embedded file).
3. Switch colouring/curve modes to emphasise entropy or byte-class.
4. Note where a file's "real" content ends and extra data begins — a classic sign of a hidden appended payload.
5. Pivot: feed suspicious regions into a hex editor, `file`/binwalk, or an EXIF/metadata reader to extract the actual embedded content.

## Inputs → Outputs
- **In:** a file (any binary/document)
- **Out:** a structural visualisation revealing content regions, entropy, and anomalies (`metadata-exif`-style structural clues about what's inside)
- **Empty/negative result looks like:** a uniform plot with no boundaries — likely a single homogeneous content type and nothing hidden; not every file has secrets.

## Gotchas & OpSec
- OpSec: browser-side processing means no upload in normal use — but verify, and run an offline copy for truly sensitive files.
- It shows *structure*, not decoded content — it points you at anomalies; you still need hex/forensic tools to extract them.
- Reading the plot is a skill; high entropy can be legitimate compression, not necessarily encryption or hiding.

## Overlaps ("do both")
- Do both with a hex editor and binwalk/EXIF readers in `documents-metadata` — BinVis finds *where* something odd is; those extract *what* it is.

## Trust & verifiability
`trust: community` — an open-source tool from a recognised security author; the method is well documented and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | binvis |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
