---
id: ph055a-osint-collection
name: Ph055a/OSINT_Collection
description: Use when you need more tools for a class of investigation and want a categorised, free-tools-only index to mine — returns pointers to other OSINT resources, not data on a person.
url: https://github.com/Ph055a/OSINT_Collection
category: search-engines
path:
- search-engines
bestFor: Browsing a large, category-organised GitHub index of free OSINT resources to discover new tooling.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free, open GitHub README. Note the repository was archived (read-only) in March 2025 — content is frozen, so some links will have rotted.
opsec: passive
opsecNote: Browsing a public GitHub README leaks nothing about your subject. Each linked tool carries its own OpSec profile — read that tool's own page before pointing it at a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-maintainer "awesome"-style list, now archived; a useful map of free tools but unmaintained, so entries are not vetted or kept current.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fbi-tools
- trace-labs-awesome-osint
- bellingcat-s-online-investigation-toolkit-2
- osint-framework-2
aliases:
- Ph055a/OSINT_Collection
- Ph055a OSINT Collection
tags:
- tool-collection
- awesome-list
- github
source: ultimate-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Ph055a/OSINT_Collection

> A large, category-organised GitHub "awesome list" of free OSINT resources — a frontier index to mine for tooling, now archived (frozen) but still a useful map.

## When to use
You have exhausted your current tools for a class of problem — people search, public records, geospatial, social media, image/video, financial/crypto, leaks/dark web — and want a curated menu of *free* resources for that category. This list groups hundreds of tools by investigation type, so you can scan the relevant section and pull candidates you don't already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/Ph055a/OSINT_Collection and use the README's table of contents to jump to a category (e.g. People, Public Records, Geospatial, Social Media, Images/Videos, Financial, Dark Web).
2. Scan the section and follow links to candidate tools.
3. Evaluate each destination on its own page — confirm it is still live, free, and safe before using it (the list is archived, so expect some dead links).
4. Pivot: fold useful finds into your own workflow; nothing here queries a subject directly.

## Inputs → Outputs
- **In:** none — you bring an investigation type, not a selector
- **Out:** none — pointers to other tools; no data about any person
- **Empty/negative result looks like:** the category has no relevant live entries, or links 404 — expected for an archived list; verify each destination and fall back to a currently-maintained index.

## Gotchas & OpSec
- Archived March 2025: read-only and no longer updated, so link rot and stale entries are guaranteed — treat it as a snapshot, not a current directory.
- Inclusion is not endorsement or vetting; assess each tool independently.
- OpSec: reading the list is passive; risk lives in the tools it points you to.

## Overlaps ("do both")
- One of several discovery indexes — cross-reference `[[fbi-tools]]`, `[[trace-labs-awesome-osint]]`, `[[bellingcat-s-online-investigation-toolkit-2]]`, and `[[osint-framework-2]]`; each curates a different (and more or less current) slice, so the union beats any single list.

## Trust & verifiability
`trust: community` — a single curator's frozen link collection; valuable as a map, but every destination needs independent verification, especially given the archive date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ph055a-osint-collection |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
