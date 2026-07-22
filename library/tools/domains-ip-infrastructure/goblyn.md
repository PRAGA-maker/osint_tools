---
id: goblyn
name: Goblyn
description: Use when you have a `domain` and want the metadata inside its exposed files — enumerates directories/files and extracts EXIF/document `metadata-exif`.
url: https://github.com/loseys/Goblyn
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Discovering files left in a website's open directories and pulling their document/image metadata (authors, software, timestamps) for leads.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- name
status: live
pricing: free
costNote: Free and open-source (GPL-3.0). Requires exiftool installed alongside it.
opsec: active
opsecNote: It actively crawls the target site's directories and downloads files — this generates traffic in the target's server logs. Only run against sites you're authorised to assess; use attributable-safe infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small open-source GPL-3.0 project (single v0.1 release, 2021); functional but only lightly maintained — verify it still installs cleanly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- loseys/Goblyn
tags:
- Domain/IP/Links
- metadata-extraction
- file-enumeration
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- oblivion
---

# Goblyn

> A Python CLI that finds files in a website's open directories and rips their metadata via exiftool — a directory-buster crossed with a metadata scraper.

## When to use
You have a `domain` and suspect its web server exposes documents/images with revealing metadata (author names, editing software, GPS/EXIF, internal paths). Goblyn enumerates likely directories, grabs files of chosen types (pdf, docx, png, …), and extracts their `metadata-exif` — useful for turning an organisation's own published files into people/leads.

## How to use it (`bestInteractionPattern`: cli)
1. Install Python 3.9+, `exiftool` (`sudo apt install exiftool`), then `sudo python3 setup.py install` from the repo.
2. Run against the target: `sudo goblyn -t <URL> -wl <wordlist> --file-types=pdf,docx,png`.
3. It discovers accessible directories, downloads matching files, and runs exiftool over them.
4. Read the extracted metadata for author `name`s, creation software, timestamps and embedded GPS — each is a lead.
5. Pivot: an author name feeds people-search; embedded GPS feeds geolocation.

## Inputs → Outputs
- **In:** target `domain`/URL (+ optional wordlist and file-type filter)
- **Out:** `metadata-exif` (authors/`name`, software, timestamps, GPS) from discovered files
- **Empty/negative result looks like:** no directories/files found or metadata stripped — a well-configured site or scrubbed files; not a tool failure.

## Gotchas & OpSec
- **Active:** crawling and downloading generates logged traffic on the target — authorised targets only.
- Metadata is frequently stripped by CMSs; absence isn't proof, and present metadata can be stale/misleading.
- Lightly maintained (2021 release) — check it still installs on your system.

## Overlaps ("do both")
- Overlaps with metadata-extraction tools like FOCA/metagoofil and directory brute-forcers — Goblyn combines the discovery and extraction steps in one CLI.

## Trust & verifiability
`trust: community` — auditable GPL-3.0 code, but small and lightly maintained; extracted metadata is authoritative to the file but should be corroborated before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goblyn |
