---
id: toolsley-analyze-file-format-online
name: 'Toolsley: File Identifier'
description: Use when you have a file of unknown/mismatched type and want its true format — reads the binary signature in-browser and returns the actual file type regardless of extension.
url: https://www.toolsley.com/file.html
category: documents-metadata
path:
- documents-metadata
bestFor: Confirming a file's real format from its magic bytes when the extension is missing, wrong, or suspicious.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, no account; runs entirely in the browser.
opsec: passive
opsecNote: Processing happens locally in your browser via JavaScript — the file is NOT uploaded to a server — so it's safe for sensitive evidence. Still, work from a copy to preserve the original's hash/metadata.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small independent utility (Toolsley) that applies file-signature detection (the classic `file`/magic-number approach) client-side; identification is heuristic but standard and easy to corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Toolsley file identifier
- toolsley.com/file
tags:
- Files
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Toolsley: File Identifier

> A drag-and-drop, in-browser "what actually *is* this file?" — it reads the binary signature (magic bytes) and tells you the true format, ignoring a misleading or missing extension.

## When to use
You have a file whose extension is absent, wrong, or deliberately disguised (a `.jpg` that's really an archive, a nameless attachment, a blob pulled from a dump) and you need its real type before you can open or analyse it correctly. Because everything runs locally, it's safe to use on sensitive material without uploading it anywhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.toolsley.com/file.html.
2. Drag the file onto the page (or click to select) — processing stays in your browser.
3. Read the identified format/type.
4. Route the file to the right analyser: e.g. a PDF to [[pdf-tools]], an image to an EXIF tool, an audio file to [[mutagen]].
5. Pivot: knowing the true type prevents mis-analysis and can itself be a signal (a disguised file suggests intent).

## Inputs → Outputs
- **In:** a local file (no selector — you supply the file)
- **Out:** the file's true format/type (`document-id`-level identification of the artefact)
- **Empty/negative result looks like:** an "unknown"/generic result for files with no recognisable signature (plain text, custom/proprietary formats, encrypted blobs) — inconclusive, not wrong.

## Gotchas & OpSec
- Signature detection identifies the *container/format*, not the trustworthiness of contents — a correctly-identified PDF can still be malicious.
- Local-only processing is a privacy win, but always analyse a copy so the original's hash and metadata stay intact for evidence.
- For anything decisive, corroborate with a second identifier (e.g. the `file` command or a hex-header check).

## Overlaps ("do both")
- The triage step before format-specific analysis — pair with [[pdf-tools]] (PDFs), [[mutagen]] (audio), and image-EXIF tools; this decides which of them to use.

## Trust & verifiability
`trust: community` — an independent utility using the standard magic-byte method; identification is easily verified against a known-good reference or the `file` utility.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toolsley-analyze-file-format-online |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
