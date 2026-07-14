---
id: names-directory
name: Names Directory
description: Use when you have a first `name` or surname and want to discover which forenames/surnames commonly pair with it (to generate candidate full names) — returns associated name combinations with frequency counts.
url: https://namesdir.com/
category: username
path:
- username
- username-search-engines
bestFor: Generating plausible full-name variants by finding forename↔surname pairings and their frequency.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free public name database; no account or payment required.
opsec: passive
opsecNote: Queries a static, pre-crawled public name database; no contact with any target and nothing is sent to anyone. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2007) third-party aggregator of publicly-crawled name pairings; useful for generating leads, not an authoritative identity source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- namesdir.com
- names directory
tags:
- name-variants
- reference
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Names Directory

> A reverse name-pairing database: given a surname, list the forenames it commonly appears with (and vice versa), with frequency counts — a lead generator for candidate full names.

## When to use
You have only a partial `name` — a surname, or a first name — and want to expand it into plausible full-name candidates before running people-search or username tools. Names Directory catalogues forename↔surname pairings crawled from public sources with counts, so you can see which combinations actually occur and how common they are. Useful for prioritising which "John Smith"-style variants to chase, or for guessing a subject's likely surname/forename when you only have one half.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://namesdir.com/.
2. Enter a surname (to list associated forenames) or a first name (to list associated surnames); or browse the alphabetical directories.
3. Read the returned pairings and their frequency counts — higher counts = more common real-world combinations.
4. Pivot: feed the ranked candidate full `name`s into people-search, social, and username tools; use rarity (low counts) to identify distinctive names worth prioritising.

## Inputs → Outputs
- **In:** `name` (a single forename or surname)
- **Out:** associated forename/surname pairings (candidate full `name`s) with frequency counts
- **Empty/negative result looks like:** few or no pairings — the name may be rare, non-Latin-script, or capped (common names like "Smith"/"Jack" are limited to ~1,000 records). Absence of a pairing is not proof it doesn't exist.

## Gotchas & OpSec
- This is a **statistical/aggregation** tool — it suggests which names co-occur in public data, not that any specific person has that name. Treat outputs as hypotheses to test.
- Common names are capped at 1,000 records, so the list is illustrative, not exhaustive.
- OpSec: fully passive; a static database read with no target contact.

## Overlaps ("do both")
- Feeds people-search and username-enumeration tools — do both: this generates the candidate names, those tools test whether a real person/account matches.

## Trust & verifiability
`trust: community` — a third-party crawl of public name data; good for generating leads, but every candidate name must be confirmed against a real identity source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | names-directory |
| category | username |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
