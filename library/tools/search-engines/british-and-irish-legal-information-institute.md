---
id: british-and-irish-legal-information-institute
name: British and Irish Legal Information Institute
description: Use when you have a `name` and want to find court judgments, tribunal decisions, or legislation naming them across UK and Irish jurisdictions — returns full-text case law (document-id) that can reveal litigation, addresses, associates, and life events.
url: http://www.bailii.org/
category: search-engines
path:
- search-engines
bestFor: Free full-text search of British and Irish case law, tribunal decisions, and legislation by party name or keyword.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- associate
- address
status: live
pricing: free
costNote: Free public-interest service (charity-run); no account needed. Terms prohibit bulk scraping — use it interactively.
opsec: passive
opsecNote: Searching BAILII queries a third-party legal archive, not the subject, so nothing is disclosed to them. Their terms forbid automated bulk downloading; search manually rather than scraping.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the BAILII charity; judgments are authoritative primary legal texts sourced from the courts themselves, so the content is reliable (subject to court redactions/anonymisation).
missingPersonsRelevance: medium
coverage:
- uk
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- BAILII
- bailii.org
tags:
- legal
- case-law
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# British and Irish Legal Information Institute

> BAILII — the free archive of British and Irish court judgments, tribunal decisions, and legislation. Searching a subject's `name` here can surface litigation that names them, exposing addresses, relatives, employers, financial disputes, and dated life events.

## When to use
You have a `name` (or an `employer-org`/business) and want to check whether the subject appears in the public legal record: civil or family judgments, employment or immigration tribunals, insolvency, probate, or criminal appeals across England & Wales, Scotland, Northern Ireland, and Ireland. Court documents are unusually rich for OSINT — they often state a party's address, occupation, family members, and a precise chronology — making BAILII a high-value corroboration source for people investigations in those jurisdictions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.bailii.org/.
2. Use the search: "Case Law Search" for full text, or search by case name/party; filter by jurisdiction and database (courts, tribunals, Law Commission, legislation).
3. Enter the subject `name` (try quoted exact form and variants); review hits for the person as a party, witness, or subject.
4. Open a judgment and read for identifying detail — address, occupation, named relatives/associates, dates — noting the neutral citation for reference.
5. Pivot: named `associate`s and `address`es feed people-search and address tools; an employer or business named feeds company lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `document-id` (court judgments/decisions), plus `associate` and `address` details revealed inside the text
- **Empty/negative result looks like:** no matching judgments — common, since most people never litigate at a reported level; absence is not evidence of a clean record, only of no *reported* case.

## Gotchas & OpSec
- Human-in-the-loop: none; interactive search only.
- OpSec: **passive** toward the subject. BAILII's terms prohibit bulk scraping and declare it "a site for people, not bots" — respect that and search manually.
- Family and some other cases are anonymised (initials/ciphers); common names produce false matches — confirm identity via corroborating detail in the text, not the name alone.
- Coverage is reported case law, weighted to higher courts; routine lower-court matters may not appear.

## Overlaps ("do both")
- Pairs with national court/registry portals and with company-registry tools — BAILII gives the full reasoned judgment (rich narrative detail), while official registers give case status and filings; company registries resolve businesses named in a judgment.

## Trust & verifiability
`trust: trusted` — BAILII is a long-standing charity publishing primary legal texts sourced directly from the courts; the documents are authoritative, and each carries a neutral citation you can cross-check against official court records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | british-and-irish-legal-information-institute |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
