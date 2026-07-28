---
id: agent-ransack
name: Agent Ransack
description: Use when you have a folder/drive of documents (a leak dump, downloaded records, disk image) and want fast full-text and filename search with regex — returns matching files.
url: https://www.mythicsoft.com/agentransack/
category: documents-metadata
path:
- documents-metadata
bestFor: Fast local full-text + filename searching across large document sets with regex and content preview.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free edition of Mythicsoft's FileLocator; the Pro version (FileLocator Pro) adds features but the free Agent Ransack covers core searching. Windows.
opsec: passive
opsecNote: Runs entirely locally on your own machine over your own files — nothing is sent anywhere, which is ideal for handling sensitive dumps offline. Keep such material on an encrypted, air-gapped or isolated workstation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established Windows tool from Mythicsoft; widely used and reputable for local file search.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- FileLocator
- Mythicsoft Agent Ransack
tags:
- file-search
- documents
- forensics
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Agent Ransack

> A fast Windows file-search tool: point it at a folder, drive or dump and it searches inside documents (full text) and filenames — with regex, boolean and content preview — locally and offline.

## When to use
You have a large local set of files — a leaked archive, a batch of downloaded records/PDFs, an exported mailbox, a mounted disk image — and need to find where a `name`, phone, email, keyword or pattern appears across thousands of documents. Agent Ransack indexes-free-searches content and filenames quickly, shows matching context, and supports regex, so it's the workhorse for triaging a document corpus offline. It finds files/passages; the intel is in what they contain.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Agent Ransack (Windows) from Mythicsoft.
2. Set the folder/drive to search and enter your term — plain text, boolean, or a regular expression.
3. Optionally filter by file type, size, date; run the search.
4. Review the hit list with in-context previews; open promising files.
5. Pivot: extract selectors from matches (names, emails, phones) and run found documents through an EXIF/metadata reader for authorship/GPS.

## Inputs → Outputs
- **In:** a search term / regex + a local folder or drive (often a `name` or keyword)
- **Out:** matching files with in-context previews (`document-id`-style file hits) to read and extract from
- **Empty/negative result looks like:** no matches — the term may be phrased differently, inside an unsupported/binary format, or in images (needs OCR first); broaden the query or pre-OCR scans.

## Gotchas & OpSec
- OpSec: local and offline — nothing leaves your machine, ideal for sensitive dumps; still keep such data on an isolated/encrypted workstation.
- Searches text layers, not images — OCR scanned PDFs/photos first, or you'll miss content.
- Windows-only; on macOS/Linux use ripgrep/`grep -r`/recoll for the equivalent.

## Overlaps ("do both")
- Do both with EXIF/metadata readers in `documents-metadata` — Agent Ransack finds the right files by content, those pull the authorship/software/GPS metadata inside them.

## Trust & verifiability
`trust: trusted` — a reputable, long-established Windows utility; it reports literal matches in your own files, so results are directly verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | agent-ransack |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
