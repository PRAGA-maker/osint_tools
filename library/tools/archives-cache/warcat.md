---
id: warcat
name: Warcat
description: Use when you have a `.warc` web-archive file and want to list, extract, or verify its contents — returns the individual captured pages, resources, and metadata inside.
url: https://github.com/chfoo/warcat
category: archives-cache
path:
- archives-cache
bestFor: Listing and unpacking WARC (Web ARChive) files locally so you can inspect archived captures record by record.
selectorsIn:
- document-id
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python, MIT); install with pip.
opsec: passive
opsecNote: Runs entirely offline on files you already hold — nothing is sent to any network or target when listing/extracting. The one caveat is provenance: extracted resources may embed original URLs and timestamps, so handle them as sensitive evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source utility by chfoo on GitHub, moderately maintained; the author now also offers a faster Rust rewrite (warcat-rs). Widely used in the web-archiving community.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- warcat-rs
tags:
- Archives
- Tools for working with WARC (WebARChive) files
- warc
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Warcat

> A simple command-line tool and Python library for handling WARC files — treat a web archive like a tar/zip: list what's inside, extract it, verify it, split or join it.

## When to use
You have obtained a WARC file — from Wayback Machine exports, a `wget --warc` capture, ArchiveBox, or Conifer/Webrecorder — and need to look inside without a full archive-replay server. Warcat lets you enumerate every captured URL/resource and extract specific pages, so you can recover a since-deleted profile page, image, or document that a WARC preserved. This is the step after you've captured or downloaded an archive and want to mine its records.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install warcat` (or clone the repo and `python3 setup.py install` for the latest).
2. List the archive's contents: `warcat list capture.warc.gz` — shows every record (URLs, response headers, resource types).
3. Extract everything: `warcat extract capture.warc.gz --output-dir ./out` — unpacks captured resources to disk as files.
4. Verify integrity: `warcat verify capture.warc.gz` — checks digests and WARC conformance so you know the capture is intact and untampered.
5. Manage large archives: `warcat split` / `warcat concat` to break apart or join WARCs (it can partially extract gzipped members without loading the whole file).
6. Pivot: extracted HTML/images → run through metadata and face/image tools; captured URLs → feed further archive or live lookups.

## Inputs → Outputs
- **In:** a local `.warc` / `.warc.gz` file (`document-id`)
- **Out:** listed records, extracted page/resource files, embedded `metadata-exif` and capture timestamps, verification result
- **Empty/negative result looks like:** `list` returns few/no records, or `verify` reports errors — the WARC is empty, truncated, or corrupt; re-obtain the capture.

## Gotchas & OpSec
- It handles the archive, not the live web — you must already have the WARC; Warcat won't fetch or crawl.
- The Python project is only lightly maintained; for very large or malformed archives the newer Rust rewrite `warcat-rs` is faster and stricter.
- Fully offline and passive — the OpSec concern is chain-of-custody: extracted resources carry original URLs/timestamps, so preserve them as evidence.

## Overlaps ("do both")
- Complements Wayback/archive lookups: use those to find and download a capture, then Warcat to open and extract the WARC they produce.

## Trust & verifiability
`trust: community` — an established open-source tool in the web-archiving ecosystem; its `verify` command lets you independently confirm a WARC's digests, so provenance is checkable rather than taken on faith.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | warcat |
| category | archives-cache |
| selectorsIn → selectorsOut | document-id → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
