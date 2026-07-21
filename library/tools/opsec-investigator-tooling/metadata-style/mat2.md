---
id: mat2
name: MAT2
description: Use when you have a file with embedded `metadata-exif` (a photo, PDF or document) and want to strip that metadata before sharing — returns a cleaned copy with the `metadata-exif` removed.
url: https://0xacab.org/jvoisin/mat2
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- metadata-style
bestFor: Locally stripping EXIF/metadata from files before you publish or share them, to avoid leaking your own operational data.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (LGPL); install from Debian/most distros (`apt install mat2`), pip, or the GitLab repo.
opsec: passive
opsecNote: Runs entirely offline on your own machine — nothing is uploaded. This is a defensive investigator-hygiene tool: run it on any file you are about to publish so you don't leak your camera model, GPS, author name, or software fingerprints. It does NOT contact the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Julien Voisin and packaged in Debian and Tails; widely used and open-source, so its behaviour is auditable — but verify you have an up-to-date version since format support changes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Metadata Anonymisation Toolkit 2
- mat2 metadata remover
tags:
- opsec
- metadata
- exif
- anonymisation
- cli
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# MAT2

> The Metadata Anonymisation Toolkit — a local, offline scrubber that strips EXIF and document metadata from your files before you share them.

## When to use
This is an OpSec tool for *you*, the investigator, not a lookup on a subject. Any file you are about to publish, attach to a report, or hand to a source can carry hidden `metadata-exif`: a photo's GPS coordinates and camera serial, a PDF's author name and editing software, a DOCX's revision history. MAT2 removes that. Run it before sharing screenshots, evidence exports, or documents so you don't accidentally leak your identity, location, or tooling. (Conversely, remember the *reverse* lesson: a subject's files may carry the same metadata — extract, don't strip, those with an EXIF reader.)

## How to use it (`bestInteractionPattern`: cli)
1. Install: `apt install mat2` (Debian/Ubuntu/Tails), `pip install mat2`, or clone https://0xacab.org/jvoisin/mat2.
2. Inspect what metadata a file holds: `mat2 --show file.jpg`.
3. Clean it: `mat2 file.jpg` — this writes `file.cleaned.jpg` alongside the original, leaving the source untouched.
4. Verify the copy: `mat2 --show file.cleaned.jpg` should report no (or minimal) remaining metadata.
5. Share only the `.cleaned.` copy. It also exposes a Python library (`import libmat2`) for batch/automated pipelines.

## Inputs → Outputs
- **In:** a file carrying `metadata-exif` (JPEG/PNG, PDF, DOCX/ODT, MP3/FLAC, and more)
- **Out:** a cleaned copy of the file with `metadata-exif` stripped (original preserved)
- **Empty/negative result looks like:** `--show` reporting "No metadata found" (already clean), or an "unsupported format" message — meaning MAT2 can't guarantee cleaning that type, so handle it manually.

## Gotchas & OpSec
- Human-in-the-loop: none; it's fully scriptable.
- OpSec: passive and offline — the safe way to sanitise files. The failure mode is forgetting to run it, then publishing a photo with GPS intact.
- Cleaning is format-dependent and best-effort; MAT2 can't strip metadata from formats it doesn't support, and some containers hide data it won't touch. Re-check sensitive files with an independent EXIF reader.

## Overlaps ("do both")
- The mirror image of EXIF/metadata *extraction* tooling: those read a subject's hidden metadata as intelligence, while MAT2 removes yours before you share. Use extraction on their files, MAT2 on yours.

## Trust & verifiability
`trust: community` — open-source and shipped in privacy-focused distributions like Tails; its logic is auditable, but keep it updated because new file formats and metadata fields appear over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mat2 |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
