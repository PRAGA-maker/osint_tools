---
id: slovenia
name: AJPES ePRS (Slovenian Business Register)
description: Use when you have a company `name`, `address`, or registration number in Slovenia and want official registry data — returns employer-org details, registered address, and names of directors/representatives.
url: https://www.ajpes.si/prs/Default.asp?language=english
category: public-records
path:
- public-records
bestFor: Verifying a Slovenian company and identifying its registered address, status, and directors/legal representatives.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free of charge. Basic search works without login; the full ePRS entry view requires a free AJPES web portal account (registration first). Certified extracts are issued in Slovenian only.
opsec: passive
opsecNote: Official government register; searches are read-only against a public database and do not notify the subject. Registering an account ties queries to that account — use a research-only login if you want separation from your identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by AJPES, the Agency of the Republic of Slovenia for Public Legal Records — the authoritative national business registry.
missingPersonsRelevance: high
coverage:
- si
auth: account
api: false
localInstall: false
registration: true
aliases:
- AJPES
- ePRS
- Slovenian Business Register
- PRS
tags:
- companysites
- Company Related Sites
- business-register
- europe
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# AJPES ePRS (Slovenian Business Register)

> Slovenia's official company register: the authoritative source for who owns/runs a Slovenian business and where it is registered.

## When to use
You have a subject linked to Slovenia through a company — an `employer-org`, a business `name`, or a registered `address` — and you need to confirm the entity is real and pull its officers. Directors and legal representatives are named in the register, so a company can become a bridge to a person (and vice versa: a person's name can surface the companies they represent).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ajpes.si/prs/Default.asp?language=english (English interface).
2. Enter search criteria in one or more fields — company name (or part of a word), registration number, tax number, or address.
3. Run the search; results list the official name, registration/tax number, legal form, registered address, incorporation date, and status (active / in liquidation / deleted).
4. For the full entry (including directors and legal representatives), log in with a free AJPES portal account — register once if you don't have one.
5. Pivot: a named director/representative feeds a person search; a registered address feeds `[[permits-and-inspections-search-by-state]]`-style property/records work in the relevant jurisdiction, or the `[[opencorporates]]` cross-border graph.

## Inputs → Outputs
- **In:** company `name` / `employer-org`, `address`, or registration/tax number
- **Out:** `employer-org` (official record), registered `address`, `name`s of directors/legal representatives, status and dates
- **Empty/negative result looks like:** "no entries found." Note the English interface translates field labels but document content (extracts, financial statements) is Slovenian only — an empty result on an English keyword may just mean the registered name is in Slovenian.

## Gotchas & OpSec
- Human-in-the-loop: basic search is open, but director/representative detail and certified extracts require a free logged-in account.
- Language: search on the Slovenian legal name where possible; partial-word matching helps.
- OpSec: **passive** and read-only; a government register does not alert the subject.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — OpenCorporates aggregates Slovenia into a cross-jurisdiction graph, while AJPES is the primary source with the most current status and the full officer list.

## Trust & verifiability
`trust: trusted` — this is the government registry itself, so its records are authoritative and court-usable within Slovenia.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slovenia |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
