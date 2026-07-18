---
id: www-infogo-gov-on-ca-infogo-home-html
name: INFO-GO (Ontario Government Employee Directory)
description: Use when you have a `name` and think the subject works for the Ontario government — returns their ministry/`employer-org`, office `phone`, and work `address`.
url: https://www.infogo.gov.on.ca/infogo/home.html
category: public-records
path:
- public-records
bestFor: Finding an Ontario provincial-government employee's ministry, office, phone, and address by name.
selectorsIn:
- name
selectorsOut:
- employer-org
- phone
- address
status: live
pricing: free
costNote: Free official Government of Ontario employee/organization directory; no account required.
opsec: passive
opsecNote: Passive — you search a public government staff directory; the employee is not notified. Contact details are work-related and published by the province. Standard site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Ontario (gov.on.ca) employee and organization directory; authoritative for Ontario public-service staff listings.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- INFO-GO
- Ontario government employee directory
tags:
- public-records
- government-directory
- ontario
- canada
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# INFO-GO (Ontario Government Employee Directory)

> The Government of Ontario's official staff directory — look up a provincial public servant by name to get their ministry, office phone, and work address.

## When to use
You have a `name` and reason to think the subject is (or was) an employee of the Government of Ontario. INFO-GO resolves the person to their ministry/branch (`employer-org`), work `phone`, and office `address` — confirming employment, current role, and a reachable work channel. Useful for corroborating a subject's occupation and location, and for reaching someone through official channels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infogo.gov.on.ca/infogo/home.html.
2. Search by employee `name` (you can also browse by ministry/organization).
3. Review the listing: name, job title, ministry/branch (`employer-org`), office `phone`, and work `address`.
4. Pivot: the ministry/title feeds LinkedIn/professional searches; the office location is a `geolocation` anchor; the work number is an official contact route.

## Inputs → Outputs
- **In:** `name` (or ministry/organization to browse).
- **Out:** job title, ministry/branch (`employer-org`), office `phone`, and work `address`.
- **Empty/negative result looks like:** no listing — the person isn't a current Ontario provincial employee in the directory (they may work federally/municipally, in the broader public sector, or have left), not proof they never did.

## Gotchas & OpSec
- Scope: Ontario **provincial** public service only — not federal, municipal, or broader-public-sector (hospitals, schools) staff.
- Work details only: it publishes office contact info, not home addresses.
- Currency: departures/reorganizations may lag; a listing reflects a recent-but-not-guaranteed-current role.
- OpSec: passive; public government directory.

## Overlaps ("do both")
- Pairs with LinkedIn/professional searches and federal/municipal directories — INFO-GO confirms the Ontario provincial role, those cover other employers and history.

## Trust & verifiability
`trust: trusted` — the official Government of Ontario directory; authoritative for provincial public-service listings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | www-infogo-gov-on-ca-infogo-home-html |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, phone, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
