---
id: ancestor-hunt
name: Ancestor Hunt
description: Use when you have a `name` and want a curated directory of free genealogy/public-record collections (births, deaths, marriages, obituaries, newspapers, criminal records) to search — returns name, dob, associate leads.
url: http://ancestorhunt.com
category: public-records
path:
- public-records
bestFor: A curated hub of free genealogy and vital-record links to research a person's family history.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: The core is a free, ad-supported directory of links and research guides (some optional paid video/research guides and an ad-free subscription exist). The linked record collections have their own separate pricing.
opsec: passive
opsecNote: Reading link directories and following them to public-record archives is passive — no contact with any living subject. Use a clean browser; some destination archives may require their own accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-regarded, long-running genealogy resource (The Ancestor Hunt, by Kenneth R Marks) curating 275k+ links to legitimate free collections; it's a signpost, so accuracy depends on the destination archives, not this site.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- The Ancestor Hunt
- theancestorhunt.com
tags:
- genealogy
- family
- vital-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Ancestor Hunt

> A curated, ad-free hub (The Ancestor Hunt) that points you to hundreds of thousands of *free* genealogy and vital-record collections — the fast way to find which archive holds the record you need.

## When to use
You have a `name` and want to research family history or vital records — births, deaths, marriages, obituaries, historical newspapers, even criminal records — but don't know which free archive to use. Ancestor Hunt is a directory/signpost: it doesn't hold records itself, it curates and links the free collections and teaches how to search them. Best for building out family links (`associate`), confirming a `dob`/death date, and finding obituaries that name relatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the site (ancestorhunt.com / theancestorhunt.com).
2. Pick the record type or state you need (e.g. Obituaries, Birth/Marriage/Death, Newspapers, Criminal Records) from its guides/link lists.
3. Follow the curated links to the actual free archives and run your `name` search there.
4. Use its Quick Reference Guides for search technique on tricky collections (e.g. newspaper archives).
5. Pivot: obituaries yield relatives' names (`associate`) and dates (`dob`); vital records confirm identity anchors that feed people-search and other public-record tools.

## Inputs → Outputs
- **In:** `name` (plus place/date context)
- **Out:** links to collections that return `name`, `dob`/death dates, `associate` (family members), obituaries
- **Empty/negative result looks like:** the directory has no link for your specific locality/record type, or the destination archive returns nothing — the latter is the real negative; Ancestor Hunt itself just routes you.

## Gotchas & OpSec
- It's a directory, not a search engine — the actual records (and their coverage/quality) live on the linked archives.
- Strongest for US/North American genealogy and historical newspapers; thinner elsewhere.
- OpSec: passive; destination archives may need their own logins.

## Overlaps ("do both")
- Pairs with [[familysearch-org]]-style archives and obituary/newspaper databases it links to — Ancestor Hunt finds the right collection; those hold the records.

## Trust & verifiability
`trust: trusted` — a reputable, long-maintained genealogy resource curating legitimate free collections; the routing is reliable, but verify each fact against the primary record it links to.
