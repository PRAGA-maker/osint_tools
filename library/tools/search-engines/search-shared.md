---
id: search-shared
name: Search Shared
description: Use when you have a `name`/keyword and want files hosted on file-sharing sites — returns links to matching content across hosts like Mediafire/4shared, occasionally surfacing leaked documents.
url: https://www.searchshared.info
category: search-engines
path:
- search-engines
bestFor: Searching one-click file-hosting sites at once for files matching a name or keyword.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search; the linked file-hosts have their own free/paid download limits.
opsec: passive
opsecNote: Searching the index is passive, but the linked file-hosts and any download are on third-party (often sketchy) sites — use a sandbox/VM and VPN, never open unknown files on your working machine, and be mindful of legality.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator over one-click file lockers (Mediafire, 4shared, RapidGator, etc.); results are noisy, unvetted, and often piracy-oriented — treat with strong caution.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Search Shared
- searchshared.info
tags:
- toddington
- curated-directory
- specialty-search
- file-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Search Shared

> A metasearch over one-click file-hosting sites — a niche way to hunt for a document, dump or media file by name across hosts like Mediafire, 4shared and RapidGator.

## When to use
You have a `name`, filename, or distinctive keyword and want to check whether a related file (a leaked document, a resume, a photo set, a spreadsheet) has been uploaded to public one-click file-hosts. It aggregates several file lockers, so it can occasionally surface material that mainstream search engines don't index. This is a narrow, lower-tier source: most results are irrelevant or piracy-oriented, so it's a supplementary check, not a primary lead generator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchshared.info in a sandboxed browser/VM behind a VPN.
2. Search a distinctive filename, `name`, or keyword; pick a host/filter if offered.
3. Scan results for genuinely relevant files; verify the filename/host look plausible before opening anything.
4. Pivot: a relevant document (`document-id`) may contain names, contact details, or `metadata-exif`; extract and feed those into the appropriate tools — but analyse in isolation.

## Inputs → Outputs
- **In:** `name` / filename / keyword
- **Out:** links to matching files on third-party file-hosts (`document-id`)
- **Empty/negative result looks like:** no results or only junk/unrelated files — the common case; absence means nothing was indexed here, not that no such file exists.

## Gotchas & OpSec
- Human-in-the-loop: none to search, but downloading is on you — treat every file as hostile.
- **Safety:** results point to unvetted file lockers rife with malware and pirated content; only ever open files in a disposable VM/sandbox, and consider the legal implications before downloading.
- Signal is low and noisy; use it only after mainstream and dedicated leak sources come up empty.

## Overlaps ("do both")
- Pairs with dedicated document/leak-search and general search-engine `filetype:` queries — those are safer and higher-signal for finding a subject's documents; use Search Shared only as a last-resort supplementary sweep.

## Trust & verifiability
`trust: unverified` — an unvetted aggregator over sketchy file-hosts; nothing here is validated, so treat every hit as unconfirmed and potentially malicious until proven otherwise.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-shared |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
