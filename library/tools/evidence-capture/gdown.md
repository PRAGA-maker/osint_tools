---
id: gdown
name: Gdown
description: Use when you have a Google Drive share link or file ID and want to reliably download the file (including large ones and whole folders) for evidence — returns the saved file.
url: https://github.com/wkentaro/gdown
category: evidence-capture
path:
- evidence-capture
bestFor: Downloading public Google Drive files and folders from the command line when curl/wget hit the virus-scan interstitial.
selectorsIn:
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (MIT); a single pip package.
opsec: passive
opsecNote: Downloading a public Drive file is passive to the owner, but the request comes from your IP and Google may log it against the file's access stats — use a sock-puppet Google session / VPS if the download itself should not be attributable to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source utility (wkentaro) with a large PyPI footprint; code is auditable and behaviour is easy to verify against a known file.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- gdown pip
- google drive downloader
tags:
- Downloaders
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Gdown

> A small Python CLI that pulls public Google Drive files and folders, skipping the "can't scan for viruses" confirmation page that breaks plain curl/wget on large downloads.

## When to use
An investigative lead points you to a public Google Drive link — a shared document, dataset, image archive or folder — and you need a clean, complete local copy for evidence preservation. Gdown handles the large-file virus-scan interstitial, resumes interrupted transfers, and can recurse an entire shared folder, which the browser and generic downloaders struggle with.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install gdown` (Python 3.10+; or `uv tool install gdown`).
2. Download by URL: `gdown "https://drive.google.com/uc?id=FILE_ID"`.
3. Or by file ID: `gdown FILE_ID`.
4. Save to a chosen path: `gdown URL -O evidence/report.pdf`; resume a cut-off transfer with `--continue`.
5. Whole folder: `gdown FOLDER_URL --folder`.
6. Pivot: hash the saved file (sha256) for your evidence log, then run it through metadata/EXIF or document tooling.

## Inputs → Outputs
- **In:** a Google Drive share URL or `document-id` (file/folder ID)
- **Out:** the file(s) saved to local disk
- **Empty/negative result looks like:** a private or permission-restricted file errors with a permission/redirect-to-login message rather than downloading — that means the link is not public, not that gdown is broken.

## Gotchas & OpSec
- Only works on files shared as "anyone with the link"; private files need the owner's access and gdown will not bypass permissions.
- Very large folders can rate-limit; rerun with `--continue`.
- OpSec: passive to the owner, but the download originates from your IP — use a disposable Google session/VPS when the retrieval itself must be deniable, and always hash the file on arrival for chain-of-custody.

## Overlaps ("do both")
- Complements general web-capture/archiving tools: those snapshot pages, while gdown retrieves the actual binary artifacts behind Drive links intact for forensic hashing.

## Trust & verifiability
`trust: community` — open-source and heavily used; correctness is trivially verifiable by hashing a downloaded file against a known-good copy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gdown |
