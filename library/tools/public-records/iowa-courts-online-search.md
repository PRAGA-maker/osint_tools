---
id: iowa-courts-online-search
name: Iowa Courts Online Search
description: Use when you have a `name` and want Iowa state court case history (civil, criminal, traffic) — returns `document-id` (case numbers), `dob`/age, and confirmed `name`/party links.
url: https://www.iowacourts.state.ia.us/esawebapp/defaultframe
category: public-records
path:
- public-records
bestFor: Statewide search of Iowa district, appellate and supreme court case records by party name.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- associate
status: live
pricing: free
costNote: Basic case-index searching and viewing is free with no account across all 99 counties. Some detailed documents may require a clerk login or a per-document fee; the party/case search itself is free.
opsec: passive
opsecNote: Queries hit the Iowa Judicial Branch's own public docket system — the subject is not notified. This is an official government portal; your search is logged server-side like any public-records lookup. Nothing is sent to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Iowa Judicial Branch; this is the authoritative primary source for Iowa court records, not a third-party reseller.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Iowa Courts Online
- ICO
- iowacourts.state.ia.us
tags:
- court
- inmate
- public-records
- legal
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Iowa Courts Online Search

> The Iowa Judicial Branch's official public docket search — party-name lookup across every Iowa court, free and authoritative.

## When to use
You have a `name` for someone with an Iowa connection and want their court footprint: criminal, civil, traffic, and family cases across all 99 counties plus the Court of Appeals and Supreme Court. Court records confirm identity (they tie a name to a birth year and case history), surface `associate` links (co-parties, co-defendants), and can reveal current addresses of record or custody status — all high-value in a missing-persons or identity-confirmation workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Iowa Courts Online at https://www.iowacourts.state.ia.us/ (the party/case search entry point; the older `esawebapp/defaultframe` frame loads the same ESAWebApp search).
2. Choose the name/party search; enter the subject's `name` (full or partial). Add a county or date range to narrow if the name is common.
3. Submit and read the case index: case numbers (`document-id`), party names, case type, filing dates, and often a birth year (`dob`) used to disambiguate.
4. Open a case to see parties, charges/claims, and hearing history; note co-parties as `associate` leads.
5. Pivot: feed confirmed identity/birth-year back into `[[familytree]]`; take a case number to the clerk for full documents.

## Inputs → Outputs
- **In:** `name` (+ optional county/date range)
- **Out:** `document-id` (case numbers), `name` party confirmations, `dob`/birth year, `associate` (co-parties)
- **Empty/negative result looks like:** "no cases found" — the subject has no Iowa court record in the online index, or older records predate digitisation (those exist only at the clerk's office). Not proof of a clean record everywhere.

## Gotchas & OpSec
- Human-in-the-loop: none for the free index search; deeper document access may prompt a clerk login/fee.
- OpSec: **passive** — official portal, subject not notified.
- Common-name collisions are frequent; always confirm with the birth year or case detail before attributing a case to your subject. Records are Iowa-only.

## Overlaps ("do both")
- Pairs with `[[familytree]]` — FamilyTreeNow supplies the relatives/address graph; Iowa Courts Online confirms identity and adds legal history for the Iowa footprint.

## Trust & verifiability
`trust: trusted` — first-party government source. The case index is authoritative; still confirm the birth year/party details to avoid same-name misattribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iowa-courts-online-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
