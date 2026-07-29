---
id: library-genesis
name: Library Genesis
description: Use when you have an author `name` or a title and want to find/read the books or academic papers behind it — returns document metadata and `document-id`s (ISBN/DOI) plus downloadable full text.
url: https://libgen.fun
category: search-engines
path:
- search-engines
bestFor: Locating and reading books and academic articles by title, author, ISBN, or DOI, including paywalled material.
selectorsIn:
- name
- document-id
selectorsOut:
- document-id
- name
status: degraded
pricing: free
costNote: Free to search and download; no account. Availability is unstable — the project runs across rotating mirror domains and individual mirrors go up and down.
opsec: active
opsecNote: Library Genesis is a shadow library and legally contested in many jurisdictions; accessing it can be logged by your ISP and downloads may carry legal/copyright risk. Use a VPN/sock-puppet connection and treat any downloaded file as untrusted (scan before opening).
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous, mirror-hosted shadow library with no accountable operator; catalog metadata is community-uploaded and files can be mislabeled or tampered with.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- LibGen
- Libgen
- Library Genesis
tags:
- Search engines
- Filesharing Search Engines
- academic-search
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Library Genesis

> A shadow library and search engine for books and academic articles — useful for reading a subject's authored work or paywalled source material, with real legal caveats.

## When to use
You have an author `name`, a book title, an ISBN, or a DOI (`document-id`) tied to a subject — an academic they cite, a self-published author you are profiling, a paper referenced in a case file — and you want the actual text, not just a citation. Library Genesis lets you search that catalog and pull the full document when a legitimate library or publisher paywall blocks you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Reach a working mirror. `libgen.fun` is one entry point, but mirrors rotate; if it is down, search for a current Library Genesis mirror.
2. Enter the query — title, author `name`, ISBN, or DOI — and pick the correct object type (books vs. scientific articles) if the mirror separates them.
3. Read the results table: each row shows title, author, year, publisher, size, format, and a `document-id` (ISBN/DOI). Match on those fields to confirm you have the right edition.
4. Download via one of the mirror links (a CAPTCHA or intermediary click page is common).
5. Pivot: an author `name` or DOI here can confirm authorship claims elsewhere; the document's own metadata (dedication, acknowledgements, affiliation) can yield further leads.

## Inputs → Outputs
- **In:** author `name`, title, ISBN, or DOI (`document-id`)
- **Out:** matching catalog entries with `document-id`s, author `name`s, and downloadable full text
- **Empty/negative result looks like:** no rows returned on a mirror — this may mean the item is genuinely absent *or* that this mirror's index is stale; try another mirror before concluding it does not exist.

## Gotchas & OpSec
- Human-in-the-loop: expect CAPTCHAs and intermediary download pages; mirrors change frequently, so a dead link is normal.
- OpSec: this is **active** and legally sensitive — access is a copyright-infringement concern in many countries and can be logged. Use a VPN/sock-puppet and never on infrastructure that ties back to you or a client.
- Files are community-uploaded: metadata can be wrong and binaries can be malicious. Scan downloads; do not trust them as pristine evidence.

## Overlaps ("do both")
- Use alongside legitimate academic search (Google Scholar, publisher sites, PubMed) to *confirm* a work exists and who authored it, then fall back to Library Genesis only when you need the full text and no lawful copy is reachable.

## Trust & verifiability
`trust: unverified` — no accountable operator, rotating anonymous mirrors, and user-supplied metadata mean neither availability nor file integrity can be relied on; corroborate any citation against an authoritative catalog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | library-genesis |
| category | search-engines |
| selectorsIn → selectorsOut | name, document-id → document-id, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
