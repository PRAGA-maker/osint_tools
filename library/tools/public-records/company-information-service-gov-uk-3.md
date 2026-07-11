---
id: company-information-service-gov-uk-3
name: Companies House - Disqualified Officers Search
description: Use when you have a `name` and want to check whether someone is a disqualified UK company director — returns name, dob, the disqualification, and past companies (employer-org).
url: https://find-and-update.company-information.service.gov.uk/search/disqualified-officers
category: public-records
path:
- public-records
bestFor: Checking if a named person is a banned/disqualified UK company director, with the reasons and dates.
selectorsIn:
- name
selectorsOut:
- name
- dob
- employer-org
- address
status: live
pricing: free
costNote: Free official register on the GOV.UK Companies House service; no account.
opsec: passive
opsecNote: A public-register lookup; the individual is not notified and nothing is sent to them. Records may include a partial date of birth and a service/correspondence address — handle personal data responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Companies House (UK government); the authoritative register of director disqualifications.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Companies House disqualified directors
- disqualified officers register
tags:
- companysites
- Company Related Sites
- uk
- companies-house
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Companies House - Disqualified Officers Search

> The UK government's public register of banned company directors — search a name to see whether someone is disqualified, why, and for how long.

## When to use
You have a `name` and want to know whether that person has been disqualified from acting as a UK company director. A hit is a strong integrity signal (fraud, unfit conduct, insolvency misconduct) and links the person to the companies involved and a date-of-birth/address that help confirm identity. Useful for due diligence and for corroborating a subject's identity/business history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the disqualified-officers search on find-and-update.company-information.service.gov.uk.
2. Enter the person's `name` (browse alphabetically or search).
3. Open the matching officer record: full name, partial `dob`, the disqualification start/end and grounds, and the companies (`employer-org`) connected to it.
4. Pivot: the named companies feed the main Companies House company search (co-directors, filings); the DOB/address help disambiguate the person across other records.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, partial `dob`, disqualification period & reason, connected companies (`employer-org`), service `address`
- **Empty/negative result looks like:** no match — the person isn't a disqualified director (the vast majority aren't). Absence says nothing about whether they're a current director — use the main Companies House officer search for that.

## Gotchas & OpSec
- This register is *only* disqualifications; for a person's active/past directorships use the main Companies House "officers" search.
- Common names: confirm with the partial DOB and connected companies before asserting a match.
- OpSec: passive public-register lookup; no notification.

## Overlaps ("do both")
- Pairs with the main Companies House company/officer search and the Insolvency Service register — this flags the ban, the officer search maps the person's full directorship network, and insolvency records add the bankruptcy/restriction picture.

## Trust & verifiability
`trust: trusted` — first-party Companies House data; authoritative for UK director disqualifications. Verify you have the right individual (name + DOB + companies) before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-information-service-gov-uk-3 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
