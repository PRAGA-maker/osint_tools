---
id: library-of-congress-ask-a-librarian
name: 'Library of Congress: Ask a Librarian'
description: Use when you have a hard-to-source research question about a `name`, place or `document-id` and want expert help locating records — returns librarian-sourced leads to documents and collections.
url: http://www.loc.gov/rr/askalib
category: people-search
path:
- people-search
bestFor: Getting a Library of Congress reference librarian to point you to obscure records, historical documents, or collections you can't locate yourself.
selectorsIn:
- name
- document-id
selectorsOut:
- document-id
- name
status: live
pricing: free
costNote: Free public reference service from the U.S. Library of Congress. No account or payment; you submit a question and a librarian replies by email.
opsec: passive
opsecNote: You email a research question to LoC staff — do not include operational detail, real target identities you want kept private, or anything you wouldn't want logged by a federal institution. Frame questions as generic research and use a sock-puppet email.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official U.S. Library of Congress reference service staffed by professional librarians — authoritative for pointing to genuine collections and records.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- library-of-congress-united-states
- newspaper-navigator
- usa-telephone-directory-collection
- webarchive-loc-gov
aliases:
- Ask a Librarian LOC
- loc.gov Ask a Librarian
tags:
- expert-search
- reference-service
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Library of Congress: Ask a Librarian

> A free expert-research channel: when a record exists but you can't find it, LoC reference librarians will point you to the right collection, catalogue, or historical document.

## When to use
You have a research dead-end — a `name` tied to obscure historical records, an old publication or `document-id` you can't locate, a genealogy or place-history question — and the answer likely lives in a specialised archive rather than the open web. Ask a Librarian routes your question to subject-specialist LoC staff who know which finding aids, directories, newspaper archives, or collections hold the answer. It's a way to reach records that aren't directly searchable, not an instant lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.loc.gov/rr/askalib and pick the reading room / subject area that fits your question (e.g. Local History & Genealogy, Newspapers, Manuscripts).
2. Submit a focused research question via the web form — describe what you're trying to locate and what you've already tried.
3. A librarian replies by email with pointers: specific collections, catalogue records, digitised items, or how/where to access physical holdings.
4. Pivot: follow their leads into `[[library-of-congress-united-states]]`, `[[newspaper-navigator]]`, `[[usa-telephone-directory-collection]]`, or the referenced archive.

## Inputs → Outputs
- **In:** a research question referencing a `name`, place, or `document-id`
- **Out:** librarian-sourced leads — collection/catalogue references, `document-id`s, access paths (`name`s of holdings/finding aids)
- **Empty/negative result looks like:** a reply saying the material is outside LoC's scope or not held/known — a genuine dead end for that record, or a redirect to another institution.

## Gotchas & OpSec
- Human-in-the-loop: a **person** answers, on library timescales (days), not a database — this is for hard sourcing questions, not bulk lookups.
- It points to records; it does not do the investigation for you, and librarians won't run background checks or provide private data.
- OpSec: your question is read by federal staff and logged — keep it a generic research query, avoid revealing sensitive target detail, and use a sock-puppet email.

## Overlaps ("do both")
- Pair with `[[library-of-congress-united-states]]` and `[[newspaper-navigator]]` — search the digitised collections yourself first, then use Ask a Librarian for the pieces the self-serve tools can't surface.

## Trust & verifiability
`trust: trusted` — it's the official Library of Congress reference service; the leads are authoritative, though they're pointers to sources you must then consult, not verified answers in themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | library-of-congress-ask-a-librarian |
| category | people-search |
| selectorsIn → selectorsOut | name, document-id → document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
