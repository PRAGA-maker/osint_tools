---
id: google-patent-search
name: Google Patents
description: Use when you have an inventor `name` or `employer-org` and want their patents — returns patent `document-id`s, co-inventor `associate`s and assignee `employer-org`s.
url: https://patents.google.com/
category: public-records
path:
- public-records
- patent-records
bestFor: Searching worldwide patents and applications by inventor name, assignee, keyword or number.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- associate
- employer-org
status: live
pricing: free
costNote: Free to search full patent text and PDFs across many national offices; no account.
opsec: passive
opsecNote: You search Google's public patent index; the inventor/company is not contacted. Google logs your query as usual — use a clean browser for sensitive research, but the patent data itself is public record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official patent-office data (USPTO, EPO, WIPO and many more); the underlying grants/applications are authoritative public records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Patents
- patents.google.com
tags:
- patent-records
- inventor-search
- public-records
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Google Patents

> A free full-text search over worldwide patents — turn an inventor's `name` or a company (`employer-org`) into the patents they filed, their co-inventors, and the companies they assigned rights to.

## When to use
You have a `name` you suspect is an inventor, or a company, and want the patent trail. Patents publicly list inventor names, their city/country at filing, co-inventors (`associate`s), and the assignee `employer-org`. This ties a technical person to employers, collaborators and a timeline of work — useful for professional-background verification, disambiguation, and mapping a person's affiliations. Coverage spans USPTO, EPO, WIPO and dozens of national offices.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://patents.google.com/.
2. Search the inventor `name` (use the `inventor:` filter), a company (`assignee:`), a keyword, CPC class, or a patent number.
3. Open a result: read inventors (with filing-time locations), assignee, priority/filing dates, and cited/citing patents (the patent "family").
4. Use filters (date, jurisdiction, status) to narrow; download the PDF for the full document.
5. Pivot: feed co-inventor `name`s into people search, the assignee `employer-org` into company registries, and the inventor's filing-time city into location work.

## Inputs → Outputs
- **In:** `name` (inventor) or `employer-org` (assignee)
- **Out:** patent `document-id`s, co-inventor `associate` names, assignee `employer-org`, filing dates and locations
- **Empty/negative result looks like:** no patents — the person never filed (most people don't), filed under a name variant, or the assignee holds patents under a subsidiary. Try name variants and the company name before concluding.

## Gotchas & OpSec
- OpSec: **passive** — public patent records; nothing reaches the subject.
- Inventor addresses are as-of-filing and may be years old; treat as historical.
- Common names collide; confirm with co-inventors, assignee or technical field before attributing.

## Overlaps ("do both")
- Pairs with `[[canadian-intellectual-property-office]]` and national patent offices (Espacenet, USPTO) — Google Patents is the broad aggregator; national databases give authoritative status/legal detail.

## Trust & verifiability
`trust: trusted` — indexes official patent-office data; each hit links to the authoritative published patent, so findings are directly verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-patent-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
