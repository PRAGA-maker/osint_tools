---
id: metadetective
name: MetaDetective
description: Use when you have a `domain` or a set of documents/images and want to harvest their metadata for author names, usernames, software, and hostnames — returns `name`, `username`, and `metadata-exif` leads.
url: https://github.com/franckferman/MetaDetective
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scraping a website's public documents and extracting their metadata (authors, usernames, GPS, internal hostnames) for OSINT.
selectorsIn:
- domain
selectorsOut:
- name
- username
- metadata-exif
status: live
pricing: free
costNote: Open source (AGPL-3.0); free. Depends on exiftool being installed.
opsec: active
opsecNote: The metadata parsing is passive, but the web-scraping/download mode fetches files directly from the target's site — that traffic hits their server and can appear in their logs. Use `--scan` (preview) or a sock-puppet IP/proxy when you don't want to touch the target directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source OSINT/pentest tool by franckferman, positioned as a modern Metagoofil replacement; community-maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- MetaDetective
- Metagoofil replacement
tags:
- Domain/IP/Links
- metadata-extraction
- document-osint
source: cyb-detective
lastVerified: '2026-07-23'
---

# MetaDetective

> A metadata-harvesting CLI: point it at a directory of files or a website, and it extracts document/image metadata — author and editor names, software versions, GPS, internal hostnames, serial numbers — for OSINT.

## When to use
You have a `domain` (an organisation or person's website) or a batch of files and want the leakage hidden in their metadata: the real `name` of a document's author or last editor, network `username`s, internal hostnames and paths, software fingerprints, and GPS/EXIF from images. It automates the classic Metagoofil workflow — discover public files on a site, download them, and mine their metadata for people and infrastructure clues.

## How to use it (`bestInteractionPattern`: cli)
1. Install exiftool, then get MetaDetective (`pip install MetaDetective`, the single script via curl, Docker, or git clone).
2. Local files: run it against a directory to extract metadata from documents/images you already have.
3. Website: point it at a URL with a crawl depth; use `--scan` to preview discoverable files, or let it download and analyse them.
4. Read the report (HTML/TXT/JSON): authors/editors (`name`), usernames, hostnames, software, GPS coordinates.
5. Pivot: author/editor `name`s and `username`s feed people/username search; internal hostnames feed infrastructure mapping; image GPS feeds geolocation.

## Inputs → Outputs
- **In:** `domain`/URL (or local files/directory)
- **Out:** `name` (document authors/editors), `username`, `metadata-exif` (GPS, camera, software, hostnames)
- **Empty/negative result looks like:** files found but stripped of metadata (increasingly common as tools sanitise on export), or no downloadable files discovered — clean metadata means nothing leaked, not that the tool failed.

## Gotchas & OpSec
- OpSec: **active** in scrape/download mode — you fetch files straight from the target's server; prefer preview/`--scan` or route through a proxy when discretion matters.
- Metadata can be stale or spoofed; an author name in an old PDF may be a template's original creator, not your subject.
- OpSec of findings: internal hostnames/usernames are sensitive; handle responsibly.

## Overlaps ("do both")
- Pairs with EXIF viewers like `[[exif-app]]` and document-search dorks — MetaDetective automates discovery-plus-extraction at scale; a single-image EXIF tool is better for one file examined by hand.

## Trust & verifiability
`trust: community` — a solid open-source tool; corroborate any extracted `name`/`username` against another source, since metadata authorship is easily misleading.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metadetective |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, username, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
