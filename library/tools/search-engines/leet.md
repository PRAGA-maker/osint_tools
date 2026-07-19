---
id: leet
name: L33Tech Open Directory Search (ODS)
description: Use when you have a filename/keyword and want files exposed on open web directories — returns links to publicly-listed files and directory indexes.
url: https://sites.google.com/view/l33tech/tools/ods
category: search-engines
path:
- search-engines
bestFor: Finding documents/media exposed in open ("index of /") web directories by keyword or filename via a curated multi-directory search.
selectorsIn:
- name
selectorsOut:
- document-id
status: degraded
pricing: free
costNote: Free Google-Sites-hosted search front end (a Programmable/Custom Search over 1,200+ open directories); no account.
opsec: passive
opsecNote: Searching runs on Google's index (passive). Actually downloading a file contacts the hosting server directly, which can log your IP — fetch found files through a sock-puppet/VPN if the source is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist Google Sites tool (copyright 2016–2021), so it may be aging/partly stale; the underlying custom search still leverages Google, but maintenance appears intermittent.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- L33Tech ODS
- Open Directory Search
tags:
- open-directory
- file-search
- custom-search-engine
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# L33Tech Open Directory Search (ODS)

> A search front end that scopes Google across 1,200+ open web directories — the "index of /" listings where documents, media, and dumps sit publicly exposed and un-indexed by normal search.

## When to use
You're hunting for a specific file or a subject's leaked/exposed documents that live in open directory listings rather than on normal web pages — a `name` on a document, a distinctive filename, a leaked archive. Open directories often expose files (PDFs, spreadsheets, backups, media) that were never meant to be found, and a directory-scoped search surfaces them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sites.google.com/view/l33tech/tools/ods and use the ODS search.
2. Enter a filename, a subject's name, or a distinctive keyword.
3. Review results — links into open directory indexes and the files they list.
4. Pivot: open the directory index to see sibling files (often a whole leaked folder); download suspect files through a VPN; a document's metadata (`metadata-exif`) may reveal author/dates.

## Inputs → Outputs
- **In:** `name`, filename, or keyword
- **Out:** links to exposed files / open directory indexes (`document-id`-style hits)
- **Empty/negative result looks like:** no results — the file isn't in an indexed open directory, or the tool's curated index is stale; try manual `intitle:"index of"` Google dorks as a fallback.

## Gotchas & OpSec
- The tool is aging (2016–2021 footer) and may be partly stale — supplement with your own open-directory dorks.
- Downloading a file contacts the host directly; that reveals your IP unless you use a VPN/sock-puppet.
- Exposed ≠ authentic — verify any document before trusting it.

## Overlaps ("do both")
- Complements manual Google `intitle:"index of"` dorking and other file/document search engines — run both, since curated indexes and live dorks surface different directories.

## Trust & verifiability
`trust: unverified` — a hobbyist front end of uncertain upkeep; the files it finds are real web resources, but confirm the tool still returns fresh results and verify each file at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leet |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
