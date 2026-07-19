---
id: internet-archive
name: Internet Archive
description: Use when you have a `name`, `username`, or topic keyword and want to full-text search the Internet Archive's collections — books, TV News, audio, software, and captured web media — returns archived documents and media (document-id) that may name or depict the subject.
url: https://archive.org/
category: search-engines
path:
- search-engines
bestFor: Full-text and media search across the Internet Archive's collections (texts, TV News Archive, audio, software, video) — distinct from single-URL Wayback snapshots.
selectorsIn:
- name
- username
- domain
selectorsOut:
- document-id
- social-profile
status: live
pricing: free
costNote: Free non-profit library; no account needed to search or view. A free account only adds uploads and "Save Page Now" captures.
opsec: passive
opsecNote: You search archive.org's own index, not the subject or any live site they control, so nothing reaches the target. The Archive logs your IP; a VPN is prudent for heavy scraping but a sock puppet is unnecessary.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive, a long-established non-profit digital library; captures and scanned items are authentic, though anyone may upload community items, so treat uploader-supplied metadata with normal skepticism.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- archive-org
- wayback-machine
- internet-archive-videos
- internet-archive-open-source-videos
- tv-closed-caption-search
- parler-archives
- snitch-list
- the-twitter-stream-grab
- wayback-machine-2
- web-archive-org
- web-archive-org-2
aliases:
- archive.org search
- Internet Archive library
tags:
- speciality-search-engines
- archives
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Internet Archive

> The Internet Archive's full-text and media search across books, TV News, audio, software, and video — use this to *find* material that mentions a subject, as opposed to the Wayback Machine, which *retrieves* snapshots of a URL you already have.

## When to use
You have a `name`, an old `username`/handle, an organisation, or a topic and want to see whether the subject appears anywhere in the Archive's scanned and captured holdings: a digitised local newspaper or yearbook, a TV News Archive clip whose closed captions name them, an uploaded home video, a defunct forum's archived page, or old shareware/software credited to them. It is strongest for people or events with a paper/broadcast trail that has left the live web but survives in a digitised collection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://archive.org/ and use the top search box.
2. Search a `name` in quotes for a phrase match; broaden or narrow with the left-rail facets (Media Type: Texts / Movies / Audio / Software; Year; Collection).
3. For broadcast mentions, search the **TV News Archive** (`https://archive.org/details/tv`) — it indexes closed captions, so a spoken `name` becomes searchable.
4. Open a hit and read/watch it; note the item identifier (the `document-id` in the URL) and uploader/collection for provenance.
5. Programmatic option: the Archive exposes an advanced-search API (`https://archive.org/advancedsearch.php?q=...&output=json`) for bulk queries.
6. Pivot: an archived page or profile feeds [[archive-org]] / [[wayback-machine]] for that exact URL's history, or a named clip/document feeds people- and social-search tools.

## Inputs → Outputs
- **In:** `name`, `username`, `domain`, or topic keyword
- **Out:** `document-id` (archived texts/media/software items), and sometimes an archived `social-profile` page
- **Empty/negative result looks like:** zero results, or only generic/unrelated items — the subject simply may not be in any digitised collection; absence here is not evidence of anything.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; uploads/Save-Page-Now need a free login.
- OpSec: fully **passive** — searching the index never touches the subject.
- Community uploads carry uploader-supplied titles/metadata that can be wrong or mislabelled; verify the actual content, not just the item title.
- This is the *search/library* face of archive.org; for the history of one specific page use the Wayback tools instead — don't conflate the two.

## Overlaps ("do both")
- Pairs with [[archive-org]] and [[wayback-machine]] — those retrieve time-stamped snapshots of a known URL, while this searches the Archive's whole corpus to surface material you didn't know existed.
- Pairs with [[tv-closed-caption-search]] for deeper caption-level querying of broadcast mentions.

## Trust & verifiability
`trust: trusted` — the Internet Archive is a reputable non-profit; scanned/captured items are authentic and each carries a stable identifier and provenance, though community-uploaded items warrant the usual check of the content itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internet-archive |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → document-id, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
