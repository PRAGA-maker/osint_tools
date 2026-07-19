---
id: arxiv-org
name: arXiv.org
description: Use when you have a `name` (a researcher/academic) and want their preprints and research footprint — returns papers, co-authors, affiliations, and dates from the open-access preprint archive.
url: https://arxiv.org/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Finding a person's scientific preprints and mapping their co-authors, institutions, and research timeline.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Fully free and open-access; no account needed to search or read. Submitting papers requires endorsement, but reading/searching does not.
opsec: passive
opsecNote: You search a public academic archive; nothing about your subject is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Cornell University; the primary open-access preprint server for physics, math, CS, and related fields — an authoritative, curated (moderated) archive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- arXiv
- arxiv.org
tags:
- academic
- preprints
- research
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# arXiv.org

> Cornell's open-access preprint archive — a person's scientific papers, co-authors, and institutional affiliations, freely searchable.

## When to use
You have a `name` you believe belongs to a researcher, academic, engineer, or student in the sciences, and you want to map their published footprint: what they work on, who they publish with, where they've been affiliated, and when. Co-authors become `associate` leads, listed affiliations become `employer-org`/location leads, and submission dates anchor a timeline — all useful for building out an academic subject's network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://arxiv.org/ and use the search (or the author-search / `au:` field) for the person's name.
2. Filter by field/date to disambiguate common names; open a paper to see the full author list and affiliations.
3. Follow the author's listing to enumerate their other papers and recurring co-authors.
4. Note the arXiv API is available for structured/bulk queries if you're enumerating many authors.
5. Pivot: co-authors → people-search; affiliations → institution/employer records; a paper title → Google Scholar for citations and a fuller publication list.

## Inputs → Outputs
- **In:** `name` (researcher)
- **Out:** preprints with co-authors (`associate`), affiliations (`employer-org`), submission dates
- **Empty/negative result looks like:** no hits means the person likely doesn't publish in arXiv's fields (it's strong in physics/math/CS, weak in biology/medicine/humanities) — try Google Scholar, PubMed, or SSRN before concluding they've published nothing.

## Gotchas & OpSec
- Human-in-the-loop: none.
- **Name ambiguity:** common names collide; confirm identity via field, co-authors, and affiliation before attributing a paper to your subject.
- Coverage is field-skewed — arXiv is not comprehensive for life sciences, medicine, or non-STEM work; absence here is not absence everywhere.

## Overlaps ("do both")
- Pairs with Google Scholar and `[[pubmed]]`-style databases — arXiv gives the open preprint + affiliation; Scholar adds citations and journal versions, and PubMed covers the biomedical papers arXiv misses.

## Trust & verifiability
`trust: trusted` — a Cornell-operated, moderated open-access archive; papers and author metadata are authoritative, though author *identity* (which "J. Smith") still needs disambiguation by you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arxiv-org |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
