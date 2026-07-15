---
id: onedrive
name: OneDrive (Google dork)
description: Use when you have a `name`/keyword and want publicly shared Microsoft OneDrive files or folders indexed by Google — returns document-id, name, metadata-exif.
url: https://www.google.com/search?safe=off&q=site:onedrive.live.com+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Surfacing accidentally-public OneDrive documents, photos and folders tied to a name, employer or keyword via a Google site: dork.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
- metadata-exif
status: live
pricing: free
costNote: Uses free Google web search; no account or payment.
opsec: passive
opsecNote: This is an ordinary Google query against Google's index — you never touch the target's OneDrive, so nothing is logged on their side and no owner is alerted. Heavy dorking can trigger a Google CAPTCHA against your IP; use a clean browser and pace queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A search technique, not a maintained tool — effectiveness depends entirely on what Google has indexed. Most OneDrive share links carry noindex hints, so coverage is thin and results skew to older or misconfigured shares.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- site:onedrive.live.com dork
- OneDrive Google dork
tags:
- google-dork
- documents
- cloud-storage
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# OneDrive (Google dork)

> A Google `site:onedrive.live.com` dork for finding publicly shared OneDrive files, photos and folders that a subject or their organisation left exposed to search engines.

## When to use
You have a `name`, `employer-org`, project name or other keyword and want to check whether any OneDrive content tied to it has been shared publicly and indexed by Google — leaked spreadsheets, photo folders, planning docs. Cloud-storage misconfiguration is a recurring source of accidental disclosure; this dork is the cheapest way to test for it.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run `site:onedrive.live.com <searchterm>` (replace `<searchterm>` with the name/employer/keyword). Try `site:1drv.ms <term>` too — OneDrive's short-link host.
2. Add operators to sharpen: quote exact names, add `filetype:` hints via the linked file names, or combine with an organisation name.
3. Open indexed results and assess: a shared file's title/preview may reveal the owner, and downloaded images may carry `metadata-exif` (camera, GPS, timestamps).
4. Pivot: an author name feeds people-search; EXIF GPS feeds geolocation; a shared folder may enumerate further documents.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or keyword
- **Out:** links to publicly shared OneDrive `document-id`s/files, owner `name` hints, `metadata-exif` from any downloaded media
- **Empty/negative result looks like:** no Google hits — expected in most cases, because OneDrive share pages are usually not indexed; absence here is NOT proof nothing is shared, just that Google hasn't indexed it.

## Gotchas & OpSec
- Low hit rate by design: OneDrive discourages indexing, so this catches only misconfigured/older public shares — treat a null result as inconclusive.
- Combine with the equivalent dorks for Google Drive, Dropbox and Box; each cloud leaks differently.
- OpSec: passive; it's just a Google search, but pace it to avoid CAPTCHAs.

## Overlaps ("do both")
- Run alongside the same dork against other cloud hosts (Google Drive, Dropbox) — coverage barely overlaps, so a subject's leak may only appear on one.

## Trust & verifiability
`trust: unverified` — a technique rather than a product; any file found is real, but the method's yield depends on Google's index and must be corroborated (confirm the owner, don't assume from a filename).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onedrive |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org → document-id, name, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
