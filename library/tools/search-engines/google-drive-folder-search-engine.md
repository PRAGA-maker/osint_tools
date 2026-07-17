---
id: google-drive-folder-search-engine
name: Google Drive Folder Search Engine
description: Use when you have a `name`, `username`, or keyword and want publicly shared Google Drive files/folders mentioning it — returns documents, `metadata-exif`, and leaked-file leads.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:nwzqlcysx_w
category: search-engines
path:
- search-engines
bestFor: Finding public/misconfigured Google Drive documents, spreadsheets and folders indexed by Google, by keyword or name.
selectorsIn:
- name
- username
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account needed to search.
opsec: passive
opsecNote: This is a Google search over already-public Drive content — passive, with no contact to any file owner. Opening a returned file is a normal Google Drive view; use a sock-puppet Google session if you don't want the access tied to you (owners of link-shared files can't see viewers, but be cautious with sign-in-required files).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine scoped to drive.google.com; results depend on the CSE config and Google's index, which can drift over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Drive CSE
- public Drive search
tags: []
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Google Drive Folder Search Engine

> A Google Custom Search Engine scoped to `drive.google.com` — surfaces public and inadvertently-shared Drive documents, folders and spreadsheets that mainstream search buries.

## When to use
You have a `name`, `username`, org, project codename, email fragment, or any distinctive keyword and want documents a subject or their circle uploaded to Google Drive and shared publicly (or "anyone with the link", once that link got indexed). People routinely over-share rosters, contact sheets, itineraries, and photo folders — a rich source of `document-id`s, embedded `metadata-exif`, and named associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL.
2. Search a distinctive term — full name in quotes, an email/username, an organisation, or a project name.
3. Scan results (Docs, Sheets, PDFs, Slides, and folder listings hosted on Drive).
4. Open promising files in a sock-puppet Google session; check document properties/EXIF and shared-folder siblings.
5. Pivot: names/emails inside a doc feed people- and email-search; images feed reverse-image and EXIF tools; a folder often exposes many more files than the one you found.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** `document-id` (public Drive files/folders), `metadata-exif` (authors, timestamps, GPS in embedded images), plus names/contacts inside the documents.
- **Empty/negative result looks like:** no hits — nothing matching is publicly indexed (most Drive content is private); try alternate spellings, an email, or Google dorks (`site:drive.google.com "term"`).

## Gotchas & OpSec
- Coverage is limited to what Google has indexed and the CSE's configuration; it is not a live crawl of all Drive — treat misses as "not indexed", not "doesn't exist".
- Some results require sign-in; use a persona account, never your real one.
- Ethics/OpSec: only inadvertently-public files appear, but handle personal data responsibly and lawfully.

## Overlaps ("do both")
- Complements general search-engine dorking (`site:drive.google.com`) and other document-search CSEs — the CSE is convenient; manual dorks let you tune the query and combine hosts.

## Trust & verifiability
`trust: community` — a user-built CSE over Google's index; results are real Google hits but scope is defined by an unknown third party, so corroborate the file's authenticity before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-drive-folder-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
