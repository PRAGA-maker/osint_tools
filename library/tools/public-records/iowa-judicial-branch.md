---
id: iowa-judicial-branch
name: Iowa Courts Online Search
description: Use when you have a `name` and want Iowa state court cases — returns civil, criminal, traffic and other case records with parties, charges and document IDs.
url: https://www.iowacourts.gov/
category: public-records
path:
- public-records
bestFor: Searching Iowa state trial-court records by party name to find a person's civil, criminal and traffic cases.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- address
status: live
pricing: free
costNote: Free online case search via Iowa Courts Online; registration may be required for the full search portal, and some documents/details are access-controlled.
opsec: passive
opsecNote: You query an official public court system, not the subject, so nobody is alerted. Court data is sensitive personal information — use lawfully and avoid unnecessary re-publication.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Iowa Judicial Branch case-search system; authoritative for Iowa state courts, though it covers Iowa only (not federal cases or other states).
missingPersonsRelevance: high
coverage:
- us-ia
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- court-electronic-records-pacer
aliases:
- Iowa Courts Online
- iowacourts.gov
- Iowa Judicial Branch
tags:
- court
- inmate
- iowa
- legal
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Iowa Courts Online Search

> Iowa's official state-court case search — look up a person by name to find their civil, criminal, traffic and other Iowa court matters, with parties, charges and filing detail.

## When to use
You have a `name` and want to know a person's court involvement in Iowa: criminal charges, civil suits, small claims, traffic, protective orders, or family cases. Court records anchor a person in time and place and often expose date of birth, addresses, co-parties, attorneys and case documents — strong corroboration in a locate/missing-person case. It's Iowa state courts only; use PACER for federal matters.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.iowacourts.gov/ and open Iowa Courts Online Search (register/accept terms if prompted).
2. Search by party `name` (last, first); narrow with county or date if the name is common.
3. Open a matching case: parties, charge/claim, filing dates, dispositions, and (where available) the `document-id`/case number and documents.
4. Confirm identity with DOB/address before attributing a case to your subject.
5. Pivot: co-parties and attorneys are `associate` leads; addresses feed people-search; for federal cases use `[[court-electronic-records-pacer]]`.

## Inputs → Outputs
- **In:** `name` (party)
- **Out:** Iowa court cases → `name`, `dob`, `address`, case/`document-id`, charges/dispositions
- **Empty/negative result looks like:** no cases — no *Iowa state* court record (they may have cases in another state or federally); absence is not proof of a clean record.

## Gotchas & OpSec
- **Iowa state courts only** — not federal, not other states; check those separately.
- Same-name collisions are common; confirm with DOB/address.
- Some case types/documents are restricted (juvenile, sealed); you won't see everything.
- OpSec: passive public-record query; handle personal data responsibly.

## Overlaps ("do both")
- Complements `[[court-electronic-records-pacer]]` (federal) and other states' court portals — do the relevant jurisdictions to cover all of a person's court footprint.

## Trust & verifiability
`trust: trusted` — authoritative state-court data; reliable for Iowa, with the scope caveat that it's one state's trial courts only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iowa-judicial-branch |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
