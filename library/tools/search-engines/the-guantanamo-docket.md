---
id: the-guantanamo-docket
name: The Guantanamo Docket
description: Use when you have a `name` of a Guantanamo Bay detainee and want their case file — returns a profile plus government documents (status reviews, transfer records).
url: https://www.nytimes.com/interactive/projects/guantanamo
category: search-engines
path:
- search-engines
bestFor: Looking up any acknowledged Guantanamo Bay detainee and reading the government documents and profile compiled for their case.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- dob
status: live
pricing: free
costNote: Free to access on The New York Times; this interactive project sits outside the paywall. No account required to search or read the documents.
opsec: passive
opsecNote: You browse a published journalistic database; no subject is contacted and nothing ties the query to you. Fully passive — the records are already public government documents curated by the NYT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by The New York Times from official Pentagon/government documents (Combatant Status Review and Administrative Review Board files); a well-sourced, periodically updated project.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- new-york-times
aliases:
- Guantanamo Docket
- Guantánamo Docket
tags:
- toddington
- curated-directory
- specialty-search
- detainees
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# The Guantanamo Docket

> A free, searchable New York Times database of every acknowledged Guantanamo Bay detainee — each with a profile and the underlying government documents.

## When to use
You have the `name` (or an approximate spelling/transliteration) of someone held at Guantanamo Bay since 2002 and want their consolidated record: a short profile, key dates, and the primary government documents (Combatant Status Review Board and Administrative Review Board files, transfer/release records). It's a specialised people-lookup for this specific population — useful when tracing an individual's detention history, status, or fate, and for sourcing primary documents behind a claim.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nytimes.com/interactive/projects/guantanamo.
2. Search by detainee `name` or browse the list (by country, status, etc.).
3. Open a detainee's page: read the profile, key dates (capture/transfer/release), and their status.
4. Follow the linked government documents (`document-id`s) for the primary records behind the profile.
5. Pivot: transliterated names/aliases and dates feed broader searches; the primary documents corroborate or source a claim elsewhere.

## Inputs → Outputs
- **In:** detainee `name` (or country/status browse)
- **Out:** detainee profile, key dates/`dob` where known, and primary government `document-id`s
- **Empty/negative result looks like:** no match — the person isn't among the Pentagon-acknowledged detainees covered, or the name's transliteration differs; try alternate spellings before concluding absence.

## Gotchas & OpSec
- Narrow scope: only acknowledged Guantanamo detainees — irrelevant outside this population.
- Names are transliterated from Arabic/other scripts; spellings vary widely, so search multiple variants.
- It reflects documented status as of its last update; very recent developments may lag.
- OpSec: fully passive reading of a public journalistic database.

## Overlaps ("do both")
- Sits alongside `[[new-york-times]]` reporting — the docket provides the structured records and documents; NYT articles add narrative context around a case.

## Trust & verifiability
`trust: trusted` — a New York Times project built directly on official government documents, with the source files linked. Reliable and primary-sourced; still read the underlying documents rather than relying on the summary profile alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-guantanamo-docket |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, document-id, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
