---
id: journal-seek
name: JournalSeek
description: Use when you have a journal name/abbreviation or ISSN and want to identify the publication and its scope/homepage — returns journal metadata, not article text.
url: http://journalseek.net
category: search-engines
path:
- search-engines
bestFor: Resolving an academic journal title/abbreviation/ISSN to its publisher, scope, and homepage.
selectorsIn:
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free directory; no account. Contains journal metadata only, not articles or abstracts.
opsec: passive
opsecNote: You look up a journal, not a person — fully passive. Nothing about your subject is submitted; safe to browse freely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing but lightly-maintained academic journal directory (~39,000 titles); useful as a lookup, freshness of individual entries not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- JournalSeek
- Genamics JournalSeek
tags:
- academic-resources-and-grey-literature
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# JournalSeek

> A free directory of ~39,000 academic journals — resolve a title, abbreviation, or ISSN to the journal's scope, publisher, and homepage.

## When to use
A **reference/disambiguation** tool for academic footprints. When a subject's trail runs through scholarly publishing — a CV, a cited paper, a byline, a cryptic journal abbreviation — JournalSeek turns that fragment into the actual publication: full title, aims/scope, subject category, ISSN, and the journal's `domain`/homepage. From there you can find editorial boards, author lists, and institutional affiliations. It holds no articles, so it's a signpost, not a source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://journalseek.net.
2. Search the journal by name/abbreviation, or browse its 23 subject categories; you can also match by ISSN.
3. Read the entry: full title, description (aims & scope), abbreviation, subject, ISSN, and homepage link.
4. Pivot: follow the journal `domain` to editorial boards / issue archives to locate the person's paper, co-authors, and affiliation.

## Inputs → Outputs
- **In:** journal `name` / abbreviation / ISSN
- **Out:** journal metadata + homepage `domain` (no article text)
- **Empty/negative result looks like:** no match — the journal may be too new, too obscure, or renamed; cross-check with a live index (publisher site or a scholarly database) before concluding it doesn't exist.

## Gotchas & OpSec
- **Directory only:** no abstracts, no full text — use it to *identify* a journal, then go to the publisher for content.
- Lightly maintained; some homepage links may be stale for defunct or merged journals.
- OpSec: **passive** — you query a journal directory, nothing about your subject leaves your browser.

## Overlaps ("do both")
- Complements full-text scholarly search: JournalSeek resolves *which* journal an abbreviation means; a database like a preprint/citation index or the publisher site is where you then read the actual paper and its author details.

## Trust & verifiability
`trust: community` — a real, established academic directory, but lightly curated; treat entries as a starting reference and confirm current details on the journal's own site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | journal-seek |
| category | search-engines |
| selectorsIn → selectorsOut | name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
