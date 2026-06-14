---
id: internet-archive-videos
name: Internet Archive Videos
description: Use when you need archived/historical video — old broadcasts, uploads, or footage of a place/person/event — returns hosted video items with metadata.
url: https://archive.org/details/movies
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Searching the Internet Archive's free video collections for archived footage, broadcasts, and user uploads.
input: Keyword, title, uploader, date, or place/event term
output: Hosted video items with descriptions, upload dates, and uploader metadata
selectorsIn:
- name
- geolocation
selectorsOut:
- image
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free, nonprofit. A (free) account is only needed to upload, not to view/search.
opsec: passive
opsecNote: Public nonprofit archive; searching and viewing are passive and not visible to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: archive.org is the Internet Archive, a long-established nonprofit digital library.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- video-search
- archive
source: arf-seed
lastVerified: ''
enrichment: full
---

# Internet Archive Videos

> The Internet Archive's free video library — a place to find archived broadcasts, old uploads, and footage that has disappeared elsewhere.

## When to use
You need historical or hard-to-find video: a local news segment about an event, an old upload that was deleted from YouTube, or footage of a `geolocation`/place relevant to a timeline. Useful for recovering content that subjects or media have since removed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://archive.org/details/movies (or the global search at archive.org) and search by keyword, `name`, place, or date.
2. Filter by collection (e.g., TV News Archive, community uploads), media type, and year.
3. Open an item to read its description, uploader, upload date, and any `metadata-exif`/source notes; play or download the file.
4. Pivot: a recovered clip can confirm a person's appearance/clothing, a date, or a `geolocation`; uploader names feed username/social lookups.

## Inputs → Outputs
- **In:** keyword / `name` / place / date
- **Out:** archived `image`/video item, item `metadata-exif`, `geolocation` clues in descriptions
- **Empty/negative result looks like:** no items or only unrelated public-domain films — the archive is broad but not exhaustive for personal/local content.

## Gotchas & OpSec
- Coverage is uneven: strong for TV news and public-domain media, sparse for personal uploads.
- Item metadata is contributor-supplied and can be wrong; verify dates/locations against the footage itself.
- OpSec: fully passive; no subject is notified.

## Overlaps ("do both")
- Pairs with the Wayback Machine (same org) to recover the web page that originally embedded a now-deleted video.

## Trust & verifiability
`trust: trusted` — operated by the Internet Archive nonprofit. Treat individual item descriptions as unverified contributor metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internet-archive-videos |
| category | image-video-face |
| selectorsIn → selectorsOut | name, geolocation → image, metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
