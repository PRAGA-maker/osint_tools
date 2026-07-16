---
id: courtlistener-recap
name: CourtListener / RECAP
description: Use when you have a `name` and want free US court opinions and PACER federal dockets — returns matching case parties (`name`), docket/case numbers (`document-id`) and employer/organisation litigants.
url: https://www.courtlistener.com/
category: public-records
path:
- public-records
bestFor: Free search of US federal and state court opinions plus PACER dockets liberated via the RECAP archive — finds a person's litigation history without PACER fees.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free to search and read opinions and RECAP-archived dockets. Run by the non-profit Free Law Project. Fetching a PACER document not yet in RECAP may incur PACER's own per-page fee.
opsec: passive
opsecNote: Searching CourtListener does not touch the subject or the courts directly; it queries an archive. No login needed for search. Using the RECAP browser extension while logged into PACER ties fetches to your PACER account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Free Law Project, a respected US legal-transparency non-profit; opinions and dockets are court-sourced, and RECAP mirrors real PACER filings.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- Recap
- CourtListener
- Free Law Project
tags:
- court
- legal
- records
- pacer
source: inteltechniques-tools
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- courtlistener
- free-law-recap-archive
- recap-court-doc-repo
---

# CourtListener / RECAP

> The Free Law Project's open legal database — search US court opinions and PACER federal dockets (via the RECAP archive) for free, finding a person's litigation trail without paying PACER.

## When to use
You have a `name` and want to know whether the subject appears in US federal or state litigation — as a party, attorney, or in an opinion. Court dockets expose addresses, employers, co-parties, financial disputes, and timelines that reliably place and characterize a person. CourtListener is the go-to when you want federal (PACER) coverage without racking up PACER fees, plus a large body of appellate/state opinions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.courtlistener.com/ and use the search bar; switch between **Opinions**, **RECAP** (dockets), **Oral Arguments**, and **Judges** tabs.
2. Search the subject's `name` (quote it for exact match); filter by court, date, and jurisdiction to cut noise.
3. Open a matching docket to read parties, docket/case number (`document-id`), filings list, and often attorneys and litigant organisations (`employer-org`).
4. If a needed PACER document isn't yet archived, either buy it on PACER or use the RECAP browser extension to fetch-and-donate it into the archive.
5. Pivot: co-parties/attorneys → `associate`; litigant company → corporate registries; case number → the court's own PACER/state docket for the authoritative record.
6. Automate at scale with the free CourtListener API.

## Inputs → Outputs
- **In:** `name` (party/attorney/judge)
- **Out:** `name` (confirmed parties), `document-id` (docket/case numbers), `employer-org` (litigant organisations), plus filings, dates, and opinion text
- **Empty/negative result looks like:** no hits — the person may have no US court record, the matter may be sealed or state-court-only outside coverage, or the name differs. Common names over-match; disambiguate with jurisdiction/date.

## Gotchas & OpSec
- RECAP is a crowd-sourced mirror of PACER — coverage of any given docket depends on whether someone has fetched it; absence in RECAP ≠ absence in PACER.
- State-court coverage is uneven; for state matters also check state portals.
- OpSec: **passive** — no subject notification. If you use the RECAP extension, fetches are tied to your logged-in PACER session.

## Overlaps ("do both")
- Pairs with `[[on-demand-court-records]]` and state court portals — CourtListener/RECAP is strongest for federal PACER; state-specific tools fill the state gaps.
- Feed litigant organisations into corporate registries like `[[cyprus]]`/OpenCorporates.

## Trust & verifiability
`trust: trusted` — a well-established legal-transparency non-profit mirroring authoritative court records. Still, confirm any decisive docket against the originating court's PACER/state record, since RECAP is a mirror.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | courtlistener-recap |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
