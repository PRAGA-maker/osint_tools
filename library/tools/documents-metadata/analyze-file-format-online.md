---
id: analyze-file-format-online
name: Analyze file format online
description: Use when you have a file of unknown or mislabelled type and want its true format plus basic metadata — returns detected format(s) from binary signatures and file details.
url: https://www.aconvert.com/analyze.html
category: documents-metadata
path:
- documents-metadata
bestFor: Identifying a file's real format (by binary signature) and reading basic metadata online.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free web tool (aconvert.com); upload a file or supply a URL. No account.
opsec: passive
opsecNote: You upload the file to a third-party server for analysis — do NOT submit sensitive/evidential files here; use a local tool (`file`, TrID, exiftool) for anything confidential. Reading the result is otherwise passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A general file-conversion site's analyzer; convenient for quick format ID, but a third-party upload with no security guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- aconvert analyze
tags:
- documents-metadata
- file-format
- metadata
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Analyze file format online

> A quick online file-type analyzer — read a file's binary signature to reveal its true (and nested) format, plus basic metadata, without installing anything.

## When to use
You have a file whose extension is missing, wrong, or suspicious and you want to know what it actually is — identified from its binary signature rather than its name. It flags nested formats (e.g. a `.docx` recognised as both DOCX and ZIP) and surfaces basic metadata (image geometry, video bitrate, audio sample rate) when present.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aconvert.com/analyze.html.
2. Upload the file locally or paste a URL, then click "Analyze Now!" (mind the upload OpSec note).
3. Read the results: detected format(s), signature, and available `metadata-exif`-style details.
4. Pivot: a mismatched extension vs. true type is itself a finding (disguised file); the metadata feeds further document/image analysis.

## Inputs → Outputs
- **In:** a file (upload or URL) — no personal selector
- **Out:** detected file format(s) and basic `metadata-exif` details
- **Empty/negative result looks like:** an unrecognised/ambiguous signature — the format isn't in its database, or the file is corrupt/encrypted; fall back to a local tool.

## Gotchas & OpSec
- Uploading to a third-party site — never submit confidential/evidential files; use local `file`/TrID/exiftool for those.
- It identifies format and basic metadata, not full forensic metadata — use exiftool for depth.
- No guarantees on how uploads are retained.

## Overlaps ("do both")
- Complements local tools (`file`, TrID, exiftool) and `[[pywhat]]` — this is the quick no-install check; drop to local tools for sensitive files or complete metadata.

## Trust & verifiability
`trust: unverified` — a handy third-party analyzer; confirm important results (especially disguised-file findings) with a trusted local tool before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analyze-file-format-online |
| category | documents-metadata |
| selectorsIn → selectorsOut |  → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
