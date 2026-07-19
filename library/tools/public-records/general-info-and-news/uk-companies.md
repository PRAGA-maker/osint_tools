---
id: uk-companies
name: UK Companies (Companies House)
description: Use when you have a UK company or a person's `name` and want official corporate records — returns registered details, officers, directors' addresses and filing history.
url: https://www.gov.uk/get-information-about-a-company
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Authoritative UK company data — directors, officers, registered/correspondence addresses, ownership, and full filing history — free from the official register.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- address
- associate
- employer-org
status: live
pricing: free
costNote: Fully free official UK government service (Companies House); no account needed, and a free API is available for bulk/automated access.
opsec: passive
opsecNote: Companies House searches are anonymous public lookups; the company and its officers are not notified. Nothing about you is exposed to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official UK register of companies; data is authoritative, though it relies on companies self-filing so entries can be outdated or (rarely) fraudulent.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Companies House
- get information about a company
tags:
- corporate-records
- companies-house
- uk
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# UK Companies (Companies House)

> The UK's official company register — free, authoritative records of directors, officers, ownership, and filings, and one of the best OSINT sources anywhere because it exposes directors' names, partial DOBs, and correspondence addresses.

## When to use
Your subject is a UK company director, shareholder, or business owner — or you have a UK company and want the people behind it. Companies House lists every registered company's officers by name with month/year of birth, a correspondence address, nationality, occupation, and their other directorships, making it a powerful way to link a `name` to businesses, co-directors (`associate`s), and addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gov.uk/get-information-about-a-company (Companies House search).
2. Search by company name/number, or search officers by a person's `name` to find all companies they're tied to.
3. Open a company: registered office `address`, status, SIC (activity), and the People/officers list.
4. Open an officer to see partial DOB, nationality, occupation, correspondence address, and their full list of appointments across companies.
5. Open the Filing history for annual accounts, confirmation statements, and PSC (persons of significant control) filings that reveal beneficial ownership.
6. Pivot: co-directors → `associate` mapping; correspondence `address` → address tools; PSC → true ownership; other appointments → the person's wider business footprint.

## Inputs → Outputs
- **In:** `employer-org` (company name/number) or a person's `name` (officer search)
- **Out:** registered details, officers/directors (`name`), correspondence `address`es, `associate` co-directors, ownership (PSC), and full filing history
- **Empty/negative result looks like:** no matching company/officer — the subject may not be a UK company officer, or may appear under a variant name/spelling. Try name variants and check dissolved companies (still listed).

## Gotchas & OpSec
- Self-filed data: mostly reliable but can be stale or, rarely, fraudulent (fake directors, hijacked addresses) — corroborate.
- Officer addresses are usually a correspondence/service address, not necessarily a home address (home addresses were largely suppressed after reforms).
- Common names produce many same-name officers; use DOB month/year and appointment overlap to disambiguate.
- OpSec: fully passive and anonymous.

## Overlaps ("do both")
- Complements OCCRP's `[[investigative-dashboard]]` and beneficial-ownership tools — Companies House is the authoritative UK source; use cross-border registry indexes when a director's other companies are foreign.

## Trust & verifiability
`trust: trusted` — the official UK statutory register; its records are authoritative and legally filed, with the caveat that accuracy depends on companies filing honestly, so flag anomalies rather than assuming fraud.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-companies |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, address, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
