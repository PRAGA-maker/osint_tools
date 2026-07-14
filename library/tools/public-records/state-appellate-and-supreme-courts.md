---
id: state-appellate-and-supreme-courts
name: BRB Free Public Record Site Search (State Courts)
description: Use when you have a name and a US state and want the official free court-record search for that jurisdiction — returns links to state appellate/supreme and county court record sites.
url: https://www.brbpublications.com/free-sites
category: public-records
path:
- public-records
bestFor: Finding the authoritative free US court-record search site (state appellate/supreme and county) for a given jurisdiction.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: The BRB free directory and the official government searches it links to are free; BRB also sells the paid Public Record Research System (PRRS) for professionals, but the free-sites directory needs no account.
opsec: passive
opsecNote: Browsing the directory is passive and alerts no one. Each outbound court search runs on a government site with its own logging. Use a VPN for sensitive lookups; treat court records within lawful investigative scope.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: BRB Publications is a long-established, respected public-records research publisher; its free directory curates links straight to authoritative government court sources.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- BRB Publications free sites
- BRB public record directory
- brbpub free resources
tags:
- court
- inmate
- public-records-directory
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# BRB Free Public Record Site Search (State Courts)

> BRB Publications' curated directory of *official* free US public-record sites — the fast route to the correct state appellate/supreme or county court search for your jurisdiction. (The old `brbpub.com/freeresources` path is retired; the live directory is at brbpublications.com/free-sites.)

## When to use
You have a `name` and a US state, and you want court records from the authoritative government source rather than a data broker. Appellate and supreme court dockets, and county trial-court records, live on scattered official portals of wildly varying quality. BRB's directory indexes those portals by state and record type — including state appellate & supreme court resources — so you go straight to the real search instead of guessing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.brbpublications.com/free-sites.
2. Select the **state**, then the record category (courts / criminal / appellate & supreme).
3. Follow the outbound link to the **official court search portal** and run your `name` there.
4. Read the docket/index result — note the case `document-id`, any `dob` shown, and party names.
5. Pivot: a case number/document ID feeds deeper court-record pulls; party names and DOB feed people-search and identity confirmation.

## Inputs → Outputs
- **In:** a `name` plus the US state/jurisdiction to pick the right portal
- **Out:** links to official searches yielding party `name`s, sometimes `dob`, and case `document-id`s
- **Empty/negative result looks like:** the state offers no free online court search (many don't, or index only names with no detail). BRB notes fewer than half of courts offer online docket equivalency — absence here means "not searchable online," not "no case exists."

## Gotchas & OpSec
- Coverage is uneven: many free court sites show only name indexes/summary data, not document images.
- BRB is a directory/signpost — verify every fact on the official court site it links to, which is the source of truth.
- BRB also markets a paid research system (PRRS); the free-sites directory is the part you need here.
- Passive, but each court portal logs its own searches; VPN for sensitive names.

## Overlaps ("do both")
- Pairs with `[[free-public-records-directory-us]]` (OnlineSearches) — both are directories to official US records; cross-check when one lacks a county.
- Feeds people-search tools once a court record yields a DOB, middle name, or associated parties.

## Trust & verifiability
`trust: trusted` — BRB Publications is an established public-records research house and its free directory points to authoritative government portals; reliability of any specific record rests on that official source, which you should always open and confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-appellate-and-supreme-courts |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
