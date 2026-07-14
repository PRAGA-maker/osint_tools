---
id: court-records-search-directory
name: OnlineSearches Court Records Directory
description: Use when you have a name and a US jurisdiction and want the official court-record search for it — returns links to state/county court, docket and case-index searches.
url: http://publicrecords.onlinesearches.com/courts.htm
category: public-records
path:
- public-records
bestFor: Finding the correct official free US court/docket search site for a specific county or state.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: The directory and the official court searches it links to are free; OnlineSearches (Intelius-run) also upsells paid reports on the same pages — use the outbound official links.
opsec: passive
opsecNote: Browsing the directory is passive and alerts no one. Each outbound court search runs on a government site with its own logging. Avoid the Intelius-branded paid boxes if you want to stay off a broker's logs; VPN for sensitive names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial directory (Intelius-operated) that links to authoritative government court sites; the directory is a signpost, so trust the official portals it points to, not the aggregator.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches courts
- court records directory
- publicrecords.onlinesearches.com courts
tags:
- court
- inmate
- public-records-directory
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# OnlineSearches Court Records Directory

> The courts section of the OnlineSearches directory — a jurisdiction-by-jurisdiction index to the official free US court and docket searches.

## When to use
You have a `name` and a US county/state and need court records from the authoritative source. Court dockets, case indexes, warrants and judgments live on scattered official portals of varying quality. This directory routes you straight to the right one instead of guessing URLs — the court-specific counterpart to the broader `[[free-public-records-directory-us]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://publicrecords.onlinesearches.com/courts.htm.
2. Drill down: **state** → **county** → court/docket search type.
3. Follow the **outbound link to the official court portal** and run your `name` there (not in the page's own paid boxes).
4. Read the docket/case-index result — note the case `document-id`, any `dob`, and party names.
5. Pivot: a case number feeds deeper court-record pulls; party names/DOB feed people-search and identity confirmation.

## Inputs → Outputs
- **In:** a `name` plus the US jurisdiction to pick the portal
- **Out:** links to official searches yielding party `name`s, sometimes `dob`, and case `document-id`s
- **Empty/negative result looks like:** the county lists no online court search, or the official portal returns nothing. Many courts are offline-only, so a gap means "not searchable online here," not "no case exists."

## Gotchas & OpSec
- Operated by **Intelius** — the pages mix free official links with paid upsells; use the outbound links, skip the paid boxes.
- **Not for FCRA purposes** (employment/housing/credit) — investigative/locate use only.
- Coverage and detail vary widely by county; always verify on the official court site, which is the source of truth.
- Passive, but each court portal logs its own searches; VPN for sensitive names.

## Overlaps ("do both")
- Overlaps with `[[free-public-records-directory-us]]` (same site, all record types) and `[[state-appellate-and-supreme-courts]]` (BRB's court directory) — cross-check when one lacks a county.
- Feeds people-search once a court record yields a DOB, middle name, or associated parties.

## Trust & verifiability
`trust: community` — a commercial aggregator/signpost, not a source; its value is routing you to authoritative government court portals, where you verify every fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-records-search-directory |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
