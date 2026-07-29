---
id: fdupes
name: fdupes
description: Use when you have a large set of downloaded images/files and want to find byte-for-byte duplicates locally — a CLI de-duplicator for cleaning evidence sets.
url: https://github.com/adrianlopezroche/fdupes
category: image-video-face
path:
- image-video-face
bestFor: Finding and removing exact-duplicate files in a scraped/downloaded evidence collection.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open source; install from your package manager (`apt/brew install fdupes`).
opsec: passive
opsecNote: Runs entirely offline on your own machine against local files — nothing is uploaded and no target is contacted. The only consideration is handling the evidence files themselves securely (encrypted volume, careful with `-d` delete).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-established open-source utility (adrianlopezroche/fdupes) widely packaged across Linux distros; it compares file content (size then MD5 then byte-by-byte), so matches are exact and reliable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- fdupes cli
tags:
- bellingcat-toolkit
- misc
- deduplication
- file-triage
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# fdupes

> A command-line exact-duplicate finder — collapse a bloated image/evidence folder down to unique files before you analyze them.

## When to use
You've scraped or bulk-downloaded a large set of images or documents (a profile's whole media tab, a forum thread, a dump) and need to strip byte-for-byte duplicates so you review each unique artifact once. It is a triage/hygiene step ahead of visual analysis, hashing against known sets, or EXIF work — not a matcher of *similar* images (it finds exact copies only).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `sudo apt install fdupes` (or `brew install fdupes`).
2. Scan recursively: `fdupes -r ./evidence` lists duplicate groups.
3. Review/act: `fdupes -rSn ./evidence` shows sizes; `-d` prompts to delete extras (keep a backup first), or `-rf` prints only the redundant copies for scripting.
4. Pivot: the de-duplicated unique set feeds reverse-image search, EXIF/metadata extraction, and perceptual-hash tools.

## Inputs → Outputs
- **In:** a local directory of `image`s/files
- **Out:** grouped exact duplicates → a de-duplicated unique `image`/file set
- **Empty/negative result looks like:** no duplicate groups reported — every file is already unique (or files differ by even one byte, e.g. re-encoded copies, which fdupes treats as distinct).

## Gotchas & OpSec
- **Exact-match only:** re-saved, resized, or re-compressed near-duplicates have different bytes and won't be caught — use a perceptual-hash tool (e.g. dupeGuru/`imagehash`) for visually-similar dedup.
- `-d` deletes files — always work on a copy and confirm selections before purging evidence.
- **Passive/offline**: no network, no target contact.

## Overlaps ("do both")
- Precedes perceptual-similarity and reverse-image tools: fdupes removes exact copies cheaply; a perceptual-hash tool then catches the near-duplicates it can't.

## Trust & verifiability
`trust: community` — a mature, widely-packaged open-source utility; its content-based comparison makes reported duplicates definitionally exact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fdupes |
