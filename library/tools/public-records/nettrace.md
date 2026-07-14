---
id: nettrace
name: Net-Trace
description: Use when you have a `name` and an Australian (or AU/UK/US/NZ) subject and want the right free public-record source — returns a curated directory of searches yielding `name`, `dob`, `document-id` and licensing/registry records.
url: https://www.nettrace.com.au/resource/search/people
category: public-records
path:
- public-records
bestFor: Finding the correct free people-search and public-record databases for Australia (and other countries) from one long-running curated directory.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- address
status: live
pricing: free
costNote: The directory is free (operating since 1998); the government/registry databases it links to are largely free, though some certificate copies may charge.
opsec: passive
opsecNote: Net-Trace is a link directory — searches run on the destination government/registry sites, which see your IP/query. Use a sock-puppet browser; the subject is not notified.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established (since 1998) curated directory of free people-search and public-record links, Australia-focused with international coverage; result quality is that of each linked destination.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- court-records-directory
aliases:
- nettrace.com.au
- Net-Trace people search
tags:
- court
- inmate
- people-search
- australia
- directory
- public-records
source: metaosint
lastVerified: '2026-07-13'
enrichment: full
---

# Net-Trace

> A long-running curated directory of free people-search and public-record sources — the Australia-centric counterpart to a US records directory, with international links too.

## When to use
You have a `name` and an Australian subject (or one in the UK/US/NZ) and want the authoritative *free* source — births/deaths/marriages registries, criminal-history checks, professional-licensing directories, lawyer directories, military records — rather than a paid aggregator. Net-Trace routes you to the right official database for the jurisdiction and record type, where you then run the actual search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nettrace.com.au/resource/search/people.
2. Browse to the relevant country and record category (people search, licensing, BDM, criminal, etc.).
3. Follow the curated link to the destination database and search the `name` there.
4. Read the destination's output: names, `dob`, registration/licence `document-id`s, addresses.
5. Pivot: a licence/registration `document-id` and `dob` anchor identity; state BDM records feed family/associate mapping.

## Inputs → Outputs
- **In:** `name` + jurisdiction (you pick the right link)
- **Out:** links to official sources returning `name`, `dob`, `document-id`, `address`
- **Empty/negative result looks like:** the directory lists no source for that record type in that jurisdiction, or the destination returns no match — Net-Trace only points; it holds no records itself.

## Gotchas & OpSec
- Human-in-the-loop: you choose the jurisdiction and interpret each destination's results; directory links can go stale over 20+ years — expect the occasional dead link.
- Strongest for Australia; international sections are thinner and overlap with dedicated country tools.
- OpSec: passive; the directory collects nothing about the subject.

## Overlaps ("do both")
- Pairs with `[[court-records-directory]]` (US-focused) — use Net-Trace for Australian/AU-Pacific sources and the US directory for American jurisdictions.

## Trust & verifiability
`trust: community` — a respected long-standing curator linking to official sources; verifiability is inherited from each destination, so confirm findings on the source database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nettrace |
