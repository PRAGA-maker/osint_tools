---
id: docket-alarm
name: Docket Alarm
description: Use when you have a `name` (party) or docket/case number and want US litigation records — returns dockets, filings, and case status across federal and many state courts.
url: https://docketalarm.com
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Searching US court dockets by party name or case number to find lawsuits and filings a person is involved in.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- associate
- address
status: live
pricing: freemium
costNote: A few free searches and views of already-in-system documents per week; unlimited access is paid ($99/mo flat, or pay-as-you-go). Fresh PACER pulls incur per-document fees.
opsec: passive
opsecNote: Searching court records is passive — parties aren't notified who looked. Registration is needed for most use, so your account is tied to your searches; use a dedicated account. Court records are public but sensitive; handle party PII carefully.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Docket Alarm (a Fastcase/vLex product) aggregates authoritative court/PACER data; the records are official, the platform a commercial front-end.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- pacer
- courtlistener
- unicourt
aliases:
- docketalarm.com
- Docket Alarm
tags:
- court-records
- litigation
- pacer
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Docket Alarm

> A litigation search-and-alert platform over US court data — find and track the lawsuits, filings, and case status attached to a person or company.

## When to use
Your subject may be a party to litigation and you want to find it: a civil suit, bankruptcy, IP dispute, or criminal case across federal courts and 34+ states. Court filings frequently expose current addresses, employers, relatives/associates, and a person's whereabouts and situation at a point in time — high-value in a missing-persons or background context. Use Docket Alarm to search by party `name` or `document-id` (docket number) and to set alerts on new filings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://docketalarm.com (needed for most searches; a limited free tier exists).
2. Search by party name, docket number, judge, attorney, or keyword; filter by court, case type, date, and status.
3. Open a docket to read the filing list and case status; documents already in Docket Alarm's system are viewable within your free/paid quota (fresh PACER pulls cost per document).
4. Set an alert on a case/party to be notified of new filings.
5. Pivot: addresses/employers/relatives named in filings → people-search and address tools; a docket number → the same case on `[[pacer]]`/`[[courtlistener]]`.

## Inputs → Outputs
- **In:** party `name` or docket/case number (`document-id`)
- **Out:** matching dockets, filing lists, case status; filings often reveal `address`, `associate`, and employer
- **Empty/negative result looks like:** no cases — the person isn't a party in covered courts, the name is spelled differently, or the matter is in a court/coverage gap (not all state courts included); cross-check CourtListener/PACER.

## Gotchas & OpSec
- Freemium caps: only a handful of free searches/views weekly, and *new* PACER documents cost money — budget for depth.
- Coverage is broad but not total (federal + many, not all, states); a null isn't proof of no litigation.
- Registration ties searches to your account — use a dedicated one; treat party PII in filings responsibly.

## Overlaps ("do both")
- Pairs with `[[courtlistener]]` — a free alternative with strong federal + growing state coverage; run the party name on both, since indexes differ.
- Pairs with `[[pacer]]` for the authoritative federal source, and `[[unicourt]]` for additional state-court reach.

## Trust & verifiability
`trust: trusted` — the underlying data is official court/PACER records (authoritative), aggregated by an established legal-tech provider. Verify a critical detail against the original docket on PACER/CourtListener.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | docket-alarm |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
