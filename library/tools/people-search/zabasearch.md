---
id: zabasearch
name: ZabaSearch
description: Use when you have a US `name` and want a free first-pass people search — returns current/prior `address`, `phone`, and approximate `dob`/age from public records.
url: https://www.zabasearch.com/
category: people-search
path:
- people-search
bestFor: Free US people search by name for address and phone, with paid-partner reports for deeper data.
selectorsIn:
- name
- address
selectorsOut:
- address
- phone
- dob
status: live
pricing: freemium
costNote: Free name search returns basic address/phone/age; detailed background reports are handed off to paid partners (Intelius/PeopleConnect family). Ad-supported.
opsec: passive
opsecNote: A public-records query is passive and does not notify the subject. Your query and any purchase are logged by ZabaSearch/its partners; use a sock-puppet browser and skip the paid upsell unless needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running US people-search aggregator (part of the Intelius/PeopleConnect ecosystem); free data is a useful lead source but can be stale and merge namesakes.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- spokeo
- familytreenow
- thatsthem-phone-search
- zaba-search
aliases:
- Zaba Search
- zabasearch.com
tags:
- people-investigations
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ZabaSearch

> A long-standing free US people-search — search a name for current and prior addresses, phone numbers, and approximate age before reaching for paid data.

## When to use
You have a US subject's `name` and want a quick, free look at their `address` history, associated `phone` numbers, and approximate `dob`/age. It's a solid first-pass identity/locate check whose free tier is enough to triage before spending on a paid report.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zabasearch.com and enter the subject `name`, optionally narrowing by state.
2. Review the result list and open the matching person.
3. Read the free fields: current/prior `address`es, phone numbers, and age.
4. The "full background report" links hand off to paid partners — only pay if the free data is insufficient.
5. Pivot: addresses feed reverse-address lookups; run the same subject through `[[familytreenow]]` (relatives) and phones through `[[thatsthem-phone-search]]`.

## Inputs → Outputs
- **In:** `name` (+ state), or an `address`
- **Out:** current/prior `address`, `phone`, approximate `dob`/age
- **Empty/negative result looks like:** no match or only namesakes — narrow by state; absence isn't proof, and common names over-match.

## Gotchas & OpSec
- Free data can be stale and can conflate different people with the same name — corroborate before trusting a record.
- Heavy paid-report upsells route to partner sites; treat those as sales, not new evidence.
- OpSec: passive; the subject isn't notified. Use a sock puppet; queries/purchases are logged.

## Overlaps ("do both")
- Overlaps with `[[spokeo]]` and `[[familytreenow]]` — different aggregators with different freshness; run the name through several and reconcile. Feed phones into `[[thatsthem-phone-search]]`.

## Trust & verifiability
`trust: community` — an established aggregator good for leads, not authoritative. Verify specific addresses/phones against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zabasearch |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, phone, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
