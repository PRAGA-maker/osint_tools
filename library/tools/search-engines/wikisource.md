---
id: wikisource
name: Wikisource
description: Use when you have a name and want it located in historical/public-domain documents — returns document mentions, dates and associate/place context.
url: https://wikisource.org
category: search-engines
path:
- search-engines
bestFor: Full-text searching public-domain and freely-licensed source documents (historical records, gazettes, court/legislative texts) for a person or place.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Fully free and open; Creative Commons content, no account needed to read or search.
opsec: passive
opsecNote: Reading and searching are passive; no query about your target leaves as a lookup against a third-party people-database. Wikimedia logs IPs of edits, not of reads; searching does not touch the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Wikimedia Foundation; a curated transcription of original source documents, though transcription errors are possible and content is community-maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wikisource.org
- Wikimedia Wikisource
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Wikisource

> Wikimedia's free digital library of transcribed source documents — searched in OSINT to place a name inside historical records, gazettes, and official texts.

## When to use
You have a `name` (often a historical, genealogical, or long-cold-case subject) and want to find them in primary-source documents: government gazettes, census and immigration texts, court and legislative records, old newspapers, letters, and out-of-copyright books. It shines for pre-internet identity work where a person surfaces only in scanned/transcribed paper records, and for corroborating an address, relative, or event mentioned in an older document.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wikisource.org (multilingual hub) or the relevant language edition (e.g. en.wikisource.org).
2. Enter the `name` (quote exact phrases; try surname-first and historical spelling variants) in the search box.
3. Open matching document pages; use in-page find to locate the name in context — note the document's date, place, and any co-named people.
4. Pivot: an `associate` or `address` in a record feeds relationship/location research; the document title/date bounds a timeline; follow the source citation to the original archive for verification.

## Inputs → Outputs
- **In:** `name` (person or place)
- **Out:** `name` in-context, `associate` (co-named people), `address`/place references, plus the document's date and provenance
- **Empty/negative result looks like:** no page contains the name — either the person never appears in a transcribed public-domain source or the relevant document isn't yet on Wikisource; try national archives or genealogy sites instead.

## Gotchas & OpSec
- Human-in-the-loop: none for reading; you don't need an account.
- OpSec: fully passive — nothing about the subject is submitted to a data broker.
- Coverage is uneven: it holds only what volunteers have transcribed and only public-domain / freely-licensed works, so recent people are essentially absent. Transcriptions can contain OCR/typo errors — verify against the linked scan.

## Overlaps ("do both")
- Pairs with `[[wikipedia]]`-style reference lookups and dedicated genealogy/archive tools — Wikisource gives the *primary* document text where an encyclopedia only summarizes it.

## Trust & verifiability
`trust: trusted` — Wikimedia-operated and citation-backed to original sources, so claims are traceable; the caveat is community transcription (possible errors) rather than data-broker fabrication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikisource |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
