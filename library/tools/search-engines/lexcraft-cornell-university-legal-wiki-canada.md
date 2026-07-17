---
id: lexcraft-cornell-university-legal-wiki-canada
name: LexCraft (Cornell LII Wiki)
description: Use when you need to understand how a jurisdiction publishes its legal texts and citations — a reference wiki that documents legal-information publishing standards, not a person/records lookup.
url: https://www.law.cornell.edu/wiki/lexcraft
category: search-engines
path:
- search-engines
bestFor: Background reference on legal-citation formats, court URIs, and statute-numbering conventions when you are trying to locate or parse primary legal documents.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Fully free, public, no account. Maintained by Cornell Law School's Legal Information Institute.
opsec: passive
opsecNote: Static reference wiki hosted by Cornell; reading it reveals nothing about your subject and touches no target. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by Cornell Law School's Legal Information Institute, a respected academic legal-information publisher; content is a curated best-practices notebook, deliberately sparse in places.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cornell-legal-information-institute-united-states
- birdnet
aliases:
- LexCraft
- Cornell LII wiki
tags:
- toddington
- specialty-search
- legal-reference
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# LexCraft (Cornell LII Wiki)

> Cornell LII's wiki on *how* legal information is published electronically — a methods reference (citation formats, court URIs, statute numbering), not a searchable case or person database.

## When to use
This is a support resource, not a lookup tool. Reach for it when a legal-records lead has stalled on *format*: you have a citation you can't parse, need to know how a court structures its document URIs, or want the correct citation convention to search a primary-law database. It helps you turn a fuzzy reference into a precise `document-id` you can then look up in an actual court/statute repository.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.law.cornell.edu/wiki/lexcraft.
2. Browse the topic index — American legal citation, U.S. Code background, court URIs, citation-extraction tools, and publishing standards (Akoma Ntoso, MetaLex).
3. Use it to decode or construct the citation/identifier you need.
4. Take the corrected `document-id` / citation to a primary-source database to retrieve the actual document.
5. Pivot: correctly formatted citation → `[[cornell-legal-information-institute-united-states]]` (Wex/LII) or the relevant court's public records system.

## Inputs → Outputs
- **In:** `name` of a legal concept/citation format (conceptual, not a person)
- **Out:** guidance that yields a well-formed `document-id` / citation for downstream lookup
- **Empty/negative result looks like:** the page notes its own material is "sparse" — many topics are stubs. If a topic isn't covered, fall back to the main LII/Wex encyclopedia.

## Gotchas & OpSec
- Not an investigative lookup — it returns no data about people. Miscategorizing it as a records search wastes time.
- Content is intentionally incomplete (a collaborative "shared notebook"); expect gaps.
- Fully passive and static.

## Overlaps ("do both")
- Pairs with `[[cornell-legal-information-institute-united-states]]` — LexCraft explains the publishing/citation mechanics; the main LII/Wex site is where you actually read the law once you know the citation.

## Trust & verifiability
`trust: trusted` — published by Cornell Law School's Legal Information Institute, an authoritative academic source. Reliable as reference; just remember it is documentation, not data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lexcraft-cornell-university-legal-wiki-canada |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
