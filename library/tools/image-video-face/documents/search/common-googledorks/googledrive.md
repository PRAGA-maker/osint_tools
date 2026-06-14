---
id: googledrive
name: GoogleDrive
description: Use when you want to find publicly shared Google Drive files/folders mentioning a name, email, or org — a Google dork (site:drive.google.com) returning indexed link-shared content.
url: https://www.google.com/?q=site:drive.google.com+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Finding publicly shared/indexed Google Drive files and folders that mention a search term.
input: Google dork query site:drive.google.com + <searchterm>
output: Public Drive folders and files (PDFs, sheets, slides, images) mentioning the term
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- name
- email
- phone
- address
- associate
- document-id
status: live
pricing: free
costNote: Free; just a Google search query.
opsec: passive
opsecNote: Keyword query against Google's index; the target is not contacted. Opening a found file requests it from Google (logged by Google).
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Standard, well-documented Google dork; reliability depends on Google's current index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- googledocs
aliases:
- 'dork: site:drive.google.com'
tags:
- google-dork
source: arf-seed
lastVerified: ''
enrichment: full
---

# GoogleDrive

> A Google dork (`site:drive.google.com`) for surfacing publicly shared or accidentally indexed Drive folders and files tied to your subject.

## When to use
You have a `name`, `email`, or `employer-org` and want to find link-shared Drive content — open folders, PDFs, scanned documents, photo dumps, spreadsheets — that someone published as "anyone with the link" and Google indexed. Open folders in particular can expose a trove of files (photos with EXIF, contact lists, scans).

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run: `site:drive.google.com "Jane Doe"` (replace the term; fills the URL's `<searchterm>` slot).
2. Narrow with identifiers or org names; add file-type words ("roster", "resume", "scan") to focus.
3. Scan results, open folders/files, and harvest contact data and embedded photos (`selectorsOut`); note any `document-id` for citing.
4. Pivot found images into `[[google-images]]` reverse search and emails/phones into people-search; run the same dork on `[[googledocs]]`.

## Inputs → Outputs
- **In:** `name`, `email`, `employer-org`
- **Out:** `name`, `email`, `phone`, `address`, `associate`, `document-id`
- **Empty/negative result looks like:** no results or only generic public templates — the subject's Drive content is private/unindexed; vary terms and try `[[googledocs]]`.

## Gotchas & OpSec
- Only finds link-shared *and* indexed content; the vast majority of Drive files are private and invisible to this dork.
- Open folders can be large and disorganized; download/screenshot quickly because access can be revoked or de-indexed.
- OpSec: passive. Opening files is logged by Google; owners usually can't see link viewers unless they added tracking. Use a clean account for sensitive work.

## Overlaps ("do both")
- Pairs with `[[googledocs]]` (Docs-specific) — run both against the same subject to cover documents and file/folder shares.

## Trust & verifiability
`trust: trusted` — standard, reproducible Google dork; the technique is reliable but specific hits depend on Google's volatile index, so archive findings promptly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | googledrive |
| category | image-video-face |
| selectorsIn → selectorsOut | name, email, employer-org → name, email, phone, address, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
