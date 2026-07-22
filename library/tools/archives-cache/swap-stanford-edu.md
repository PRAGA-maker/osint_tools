---
id: swap-stanford-edu
name: Stanford Web Archive Portal (SWAP)
description: Use when a site has changed or vanished and you want an archived copy — returns Stanford-preserved snapshots of selected websites by URL.
url: https://swap.stanford.edu/
category: archives-cache
path:
- archives-cache
bestFor: Retrieving archived snapshots of websites collected and preserved by Stanford University Libraries.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open access to a Stanford Libraries web-archive collection; no account required.
opsec: passive
opsecNote: Passive retrieval of archived pages from Stanford's servers; you request a URL, not a person, so nothing subject-specific is disclosed and the live target site is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party academic web archive (Stanford Libraries, via Archive-It); snapshots are faithful captures, but the collection is curated/selective rather than comprehensive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- stanford-large-network-dataset-collection
- highwire-free-online-full-text-articles
- palladio
- regular-expression-analyzer
aliases:
- SWAP
- Stanford Web Archive Portal
- Stanford Wayback
tags:
- Archives
- web-archive
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Stanford Web Archive Portal (SWAP)

> Stanford Libraries' web-archive access point — a curated Wayback-style collection for recovering snapshots of selected sites that have since changed or disappeared.

## When to use
A website relevant to your investigation has been edited, taken down, or gone dark, and you want a preserved version. SWAP provides access to sites Stanford's subject specialists selected and crawled (via Archive-It), so it is strongest for topics Stanford collects — academic, government, cultural, and organisational web content — and can hold captures the general Wayback Machine missed or that were curated more deeply. Use it to recover a `domain`'s old pages: removed bios, deleted staff lists, prior contact details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://swap.stanford.edu/ (collections live under `/was/`).
2. Look up the target `domain`/URL, or browse the relevant curated collection.
3. Open an archived capture and read the preserved page for content that is gone from the live site — names, contacts, affiliations, dates.
4. Note the capture timestamp to date the information.
5. Pivot: recovered names/contacts feed people- and email-OSINT; compare against a live copy to see what changed and when.

## Inputs → Outputs
- **In:** `domain` / URL to recover
- **Out:** archived snapshot(s) of that `domain` with historical content and capture dates
- **Empty/negative result looks like:** the URL isn't in Stanford's collection — expected, since SWAP is selective, not a whole-web archive. Absence here does not mean no archive exists; fall back to the Internet Archive Wayback Machine.

## Gotchas & OpSec
- Curated and selective: coverage is limited to what Stanford chose to crawl, so many sites won't be present.
- Captures are point-in-time; a page may be archived only at certain dates, missing the version you need.

## Overlaps ("do both")
- Pairs with the Internet Archive Wayback Machine and archive.today — run all three, since each captured different sites at different times; SWAP may hold a curated capture the others lack, and vice versa.

## Trust & verifiability
`trust: trusted` — a first-party academic web archive, so snapshots are faithful captures; the only caveat is selectivity, meaning gaps in coverage rather than doubts about authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | swap-stanford-edu |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
