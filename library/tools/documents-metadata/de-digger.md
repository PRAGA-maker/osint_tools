---
id: de-digger
name: de digger
description: Use when you have a `name`, keyword, or filename and want publicly shared Google Drive files about a subject — returns links to exposed documents/files (`document-id`, `metadata-exif`).
url: https://www.dedigger.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Finding publicly shared Google Drive documents and files by keyword and file-type operators.
selectorsIn:
- name
- email
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free to use; runs as a specialized Google search front-end, no account required.
opsec: passive
opsecNote: It builds and runs Google queries — you are querying Google's index, not the target's Drive, so the subject is not alerted. Standard search hygiene (sock-puppet browser) applies; opening a found file is a separate, more active step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community OSINT utility that wraps Google dorking of Google Drive's public URL space; results come straight from Google, so accuracy tracks Google's index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- dedigger
- de-digger
tags:
- google-dorking
- document-search
- filesharing
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# de digger

> A search front-end that surfaces publicly shared Google Drive files — dork the Drive URL space by keyword, name, or file type to find documents people forgot were public.

## When to use
You have a `name`, project keyword, `email`, or expected filename tied to a subject and suspect there may be documents shared publicly on Google Drive (resumes, spreadsheets, scans, backups) that never appear in a normal search. de digger builds targeted Google queries against Drive's public URL space so those exposed files surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dedigger.com/.
2. Enter your terms, using the supported operators: quotes for exact phrases, `OR`, `intext:` for body text, and file-type filters (e.g. `*.rar`, `*.pdf`, `*.xlsx`).
3. Submit — it runs the composed query against Google's index of public Drive links.
4. Read the results: each hit is a publicly accessible Drive file/folder. Open only what you are authorized to view.
5. Pivot: a found document yields `metadata-exif` (author, timestamps), a `document-id`, and often names/emails inside that feed further lookups.

## Inputs → Outputs
- **In:** `name`, keyword, `email`, or filename (+ operators)
- **Out:** links to publicly shared Google Drive documents/files, with their embedded `metadata-exif`
- **Empty/negative result looks like:** no hits — either nothing tied to those terms is publicly shared on Drive, or Google has not indexed it; not proof no such file exists.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; you decide which files to open.
- OpSec: the *search* is passive (you query Google). *Opening* a file may hit the owner's Drive and, for some sharing settings, could be logged — open cautiously and only when authorized.
- You will surface files that were shared publicly by mistake; handle sensitive documents lawfully and per your engagement scope.
- Coverage is limited to what Google has indexed as public Drive content — private/link-only files that Google never crawled will not appear.

## Overlaps ("do both")
- Complements plain Google dorking and other public-document search tools: de digger specializes the query for the Google Drive namespace, so run it alongside general `site:` dorking to cover both Drive and the wider web.

## Trust & verifiability
`trust: community` — a thin, transparent wrapper over Google search operators; results are Google's, so they are as verifiable as any search hit — open the file to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | de-digger |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, email → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
