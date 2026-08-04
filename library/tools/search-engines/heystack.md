---
id: heystack
name: HeyStacks
description: Use when you have a topic/keyword and want publicly-shared Google Docs, Sheets, and Slides about it — returns community-curated public documents filterable by tag and date.
url: https://heystacks.com/
category: search-engines
path:
- search-engines
bestFor: Discovering public Google Docs/Sheets/Slides on a topic that normal search often misses.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to browse and search the community collection; no account needed to read.
opsec: passive
opsecNote: You browse HeyStacks' own index of shared documents — passive and non-alerting. Opening a linked Google Doc fetches it from Google; anonymous viewing is fine, but don't open sensitive docs while signed into a real Google account (your view can appear to the doc owner).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated directory of user-submitted public documents; coverage is whatever members have added, so it's a supplement, not a comprehensive index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- HeyStacks
- heystacks.com
tags:
- google-docs
- public-documents
- document-search
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# HeyStacks

> A curated directory of public Google Docs, Sheets, and Slides — surfacing shared documents on a topic that a normal web search tends to bury.

## When to use
You have a topic, keyword, or `name` and want *documents* people have shared publicly on Google Drive — guides, comparison sheets, trackers, decks. Public Google Docs are a rich, under-searched OSINT surface (people over-share and forget the "anyone with the link" setting). HeyStacks is a community-curated way in; pair it with `site:docs.google.com` dorking for broader reach. Reach for it when you want reference material or leaked/over-shared docs on a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://heystacks.com/ and search your keyword, or browse by tag (technology, gaming, music, etc.).
2. Sort by Best/Hot/New and filter by topic group and creation date.
3. Open a listed `document-id` (the public Google Doc/Sheet/Slides).
4. Read/preserve it; note any author or contact info the doc exposes.
5. Pivot: for broader coverage, run `site:docs.google.com "<term>"` (and Sheets/Slides equivalents) in a search engine; a doc's author can be a new `name` lead.

## Inputs → Outputs
- **In:** `name`/topic/keyword
- **Out:** `document-id` (public Google Docs/Sheets/Slides)
- **Empty/negative result looks like:** few/no results — the community hasn't added docs on that topic; it's a curated set, so fall back to Google `site:` dorks before concluding nothing is shared.

## Gotchas & OpSec
- Curated and community-built — not exhaustive; treat as one entry point, not the whole of public-Drive content.
- OpSec: opening a doc while signed into a real Google account can reveal your view to the owner; view anonymously.
- Documents are user-shared and unverified; corroborate any factual claim inside them.

## Overlaps ("do both")
- Complements Google `site:docs.google.com` dorking and general document search: HeyStacks gives a curated, browsable set; dorks give raw reach — do both when hunting for over-shared or leaked Drive documents.

## Trust & verifiability
`trust: community` — a curated community directory; the documents themselves are user-generated, so use it to *find* material and verify the content independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | heystack |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
