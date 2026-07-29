---
id: scirp
name: SCIRP
description: Use when you have an author `name` or research topic and want open-access papers published in SCIRP journals — returns document-id, employer-org, associate.
url: http://www.scirp.org
category: search-engines
path:
- search-engines
bestFor: Finding open-access papers and author affiliations across SCIRP's journal catalogue.
selectorsIn:
- name
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free to search and read full-text open-access papers; authors pay publication fees (this is an author-pays open-access publisher).
opsec: passive
opsecNote: Passive — searching a publisher's site; no contact with any subject and no query attributable to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: SCIRP is a large author-pays open-access publisher widely flagged as low-quality/"predatory"; use it to locate a subject's output and affiliation, not as evidence of research credibility.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Scientific Research Publishing
- scirp.org
tags:
- academic-resources-and-grey-literature
- academic
- open-access
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# SCIRP

> Scientific Research Publishing — a large open-access journal platform whose free full-text papers can surface a subject's publications, affiliation, and co-authors even when mainstream indexes don't.

## When to use
Your subject may have published academically and you have their `name` (or a topic tied to them). SCIRP hosts hundreds of open-access journals with freely readable full text, which exposes an author's **affiliation** (`employer-org`), **co-authors** (`associate`), and often a contact email. Because SCIRP publishes broadly and with light gatekeeping, it captures output from authors and institutions that selective databases skip — handy for building a fuller picture of someone's academic footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.scirp.org and use the site search (or browse Journals A–Z / subject categories).
2. Search the author name in quotes, or a topic keyword.
3. Open article records to read the free full text and the header block: affiliation, co-authors, corresponding-author email, and DOI.
4. Pivot: an affiliation feeds an institution lookup; co-authors feed further people-search; the DOI/email feed citation and email OSINT.

## Inputs → Outputs
- **In:** `name` (author) or research topic
- **Out:** `document-id` (papers), author `employer-org` (affiliation), co-author `associate` links, plus contact email in the paper
- **Empty/negative result looks like:** no hits, or hits for a same-named different author — verify the field/affiliation before attributing a paper to your subject.

## Gotchas & OpSec
- No login to search/read; fully open.
- **Quality caveat:** SCIRP is widely regarded as a predatory/low-rigour publisher — a paper here confirms someone *published*, not that the work is sound. Treat findings as identity/affiliation leads, not credibility signals.
- Passive — searching never touches the subject.

## Overlaps ("do both")
- Pairs with Google Scholar, ORCID, and `[[free-full-pdf]]` / `[[african-journal-online]]` — each indexes a different slice of the literature; SCIRP catches open-access output the selective indexes drop.

## Trust & verifiability
`trust: unverified` — the platform is genuine and its papers are real, but its editorial standards are poor; use it for who/where, and verify any factual claim against better sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scirp |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id, employer-org, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
