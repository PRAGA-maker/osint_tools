---
id: metawarc
name: metawarc
description: Use when you have a WARC web-archive file and want the metadata inside it — returns embedded document metadata (authors, software, timestamps) from archived files.
url: https://github.com/datacoon/metawarc
category: archives-cache
path:
- archives-cache
bestFor: Extracting document/file metadata (author names, software, dates) from every file bundled inside a WARC web archive.
selectorsIn:
- domain
selectorsOut:
- name
- metadata-exif
- employer-org
status: live
pricing: free
costNote: Free and open source; install via pip. No account.
opsec: passive
opsecNote: Runs entirely locally against a WARC file you already have — no network calls to any target, nothing leaks. Fully passive; the analysis happens on your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source utility from the datacoon project; it reads standard WARC/embedded-file metadata, so results are as reliable as the archived files' own metadata.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- datacoon metawarc
tags:
- Archives
- warc
- metadata
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# metawarc

> A CLI that cracks open a WARC web-archive and harvests the metadata from every file inside it — a way to pull author names, software, and timestamps out of an archived site.

## When to use
You have a WARC file — a crawl of a target's website (from `wget --warc`, ArchiveBox, a Wayback export, etc.) — and want the hidden metadata in the documents it contains: PDF/Office author and organisation fields, image `metadata-exif`, creation software and timestamps. This is how you turn an archived site into identity leads: the "About Us" PDF or a leaked spreadsheet often carries a real author `name` and `employer-org` in its metadata that the visible page never shows.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install metawarc` (review the repo first).
2. Point it at a WARC file: use its commands to list the archive's structure and dump metadata from all contained files.
3. Read the extracted metadata — author, organisation, software, dates, EXIF — across every archived document/image.
4. Pivot: an author name/org feeds people- and company-search; EXIF geolocation feeds location work; software/timestamps help fingerprint who built the site.

## Inputs → Outputs
- **In:** a WARC file (typically a crawl of a `domain`)
- **Out:** `name` (document authors), `metadata-exif`, `employer-org` from embedded files
- **Empty/negative result looks like:** the WARC contains no metadata-bearing files, or authors scrubbed the metadata — you get empty fields, which means nothing was embedded, not that no author exists.

## Gotchas & OpSec
- You need the WARC first — metawarc analyses, it doesn't crawl; pair it with a crawler/archiver to produce the input.
- Metadata can be forged or auto-populated (e.g. a shared "admin" account) — treat authorship as a strong lead, not proof.
- OpSec: fully local and passive; the target sees nothing.

## Overlaps ("do both")
- Sits downstream of web crawlers/archivers and alongside EXIF tools — crawl a site to WARC, then run metawarc to strip identity metadata the live pages hide.

## Trust & verifiability
`trust: community` — an open-source utility reading standard file metadata; reproducible and inspectable, bounded only by what the archived files actually embed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metawarc |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → name, metadata-exif, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
