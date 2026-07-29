---
id: free-full-pdf
name: Free Full PDF
description: Use when you have a subject's `name` or a research topic and want free full-text scientific PDFs they authored — returns document-id, employer-org, associate.
url: http://www.freefullpdf.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding free full-text academic PDFs by author name or topic.
selectorsIn:
- name
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free full-text scientific PDF search; optional free registration only for community/sharing features.
opsec: passive
opsecNote: Passive — a search over indexed scholarly PDFs; you never contact the subject. Downloading a paper touches the hosting journal/repository, not the author.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party academic PDF aggregator (a curated scholarly custom-search front end); verify each hit against the original publisher, since aggregators can surface stale or mislabelled copies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- FreeFullPDF
- freefullpdf.com
tags:
- document-and-slides-search
- academic
- papers
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Free Full PDF

> A free search front end aimed at surfacing full-text scientific PDFs across disciplines — useful for pulling the papers, theses, and posters a subject has authored.

## When to use
Your subject is an academic, researcher, clinician, or student, and you have their `name` (or a topic tied to them). Free Full PDF searches scholarly PDFs and returns downloadable papers — which expose an author's **affiliation** (`employer-org`), **co-authors** (`associate`), funding, dates, and often contact details in the paper header. Use it to confirm a person's field/institution and to enumerate their collaborators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.freefullpdf.com and enter the author's name (in quotes for an exact match) or a topic keyword.
2. Browse the returned list of full-text PDF hits across its indexed disciplines (life sciences, engineering, social sciences, etc.).
3. Open promising PDFs and read the header/first page for affiliation, co-authors, corresponding-author email, and dates.
4. Registration is optional and only unlocks sharing/community features — searching and reading do not require an account.
5. Pivot: an affiliation feeds an institution directory lookup; co-author names feed further people-search; a corresponding-author email feeds email-OSINT.

## Inputs → Outputs
- **In:** `name` (author) or research topic
- **Out:** `document-id` (papers/PDFs), author `employer-org` (affiliation), co-author `associate` links, plus dates and often a contact email inside the PDF
- **Empty/negative result looks like:** no PDF hits, or hits for a same-named different person — common with common names, so cross-check the field/affiliation before attributing a paper to your subject.

## Gotchas & OpSec
- No login required to search; no CAPTCHA in normal use.
- Passive — searching and downloading never touch the subject.
- As an **aggregator**, it can surface stale, pre-print, or mislabelled copies; always confirm authorship and version against the original publisher (DOI/journal).

## Overlaps ("do both")
- Pairs with mainstream scholarly search (Google Scholar / ORCID / institutional repositories) — run both, since each indexes a different slice of the literature and this one is tuned toward freely downloadable full text.

## Trust & verifiability
`trust: community` — a third-party scholarly aggregator with no formal editorial control; treat each result as a lead and verify the paper and its authorship at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-full-pdf |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
