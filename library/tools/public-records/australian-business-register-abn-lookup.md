---
id: australian-business-register-abn-lookup
name: Australian Business Register ABN Lookup
description: Use when you have a `name` or `employer-org` in Australia and want the official business registration record — returns employer-org, address, name.
url: http://www.abr.business.gov.au
category: public-records
path:
- public-records
bestFor: Resolving an Australian business/trading name or ABN to its registered entity, status, location, and associated names.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Completely free government service; no account or login required to search or view results.
opsec: passive
opsecNote: A read-only query against a public government register — the entity is not notified. No login means no account trail; standard VPN/clean-browser hygiene is more than sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Australian Taxation Office / Australian Business Register — authoritative first-party government data.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- ABN Lookup
- Australian Business Register
- ABR
tags:
- toddington
- company-search
- public-records
- australia
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Australian Business Register ABN Lookup

> Australia's official free business register: a name or ABN returns the registered entity, its status, location, and the individuals/trading names attached to it.

## When to use
You have an Australian business `name`, trading name, ABN, or ACN — or a person you suspect operates as a sole trader — and you want to confirm the registered entity and pull leads. For a sole trader the ABN record ties the business to an individual's `name`; for any entity it gives entity type, GST registration, status (active/cancelled with dates), the registered state/postcode, and historical trading names — all useful for placing a subject's economic footprint in Australia.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://abr.business.gov.au and enter an ABN, ACN, business/company name, or trading name in the search box.
2. For name searches, use the advanced options to filter by state, postcode, or entity status to narrow a common name.
3. Open the record: entity name, ABN status and effective dates, entity type (e.g. Individual/Sole Trader, Company, Trust), GST status, main business location (state + postcode), and any recorded business/trading names.
4. Pivot: a sole-trader `name` feeds people-search; an ACN feeds ASIC company searches for directors/officeholders; the postcode narrows geolocation.

## Inputs → Outputs
- **In:** business/trading `name`, or `employer-org` identifier (ABN/ACN)
- **Out:** registered `employer-org` (entity name + type), `address` (state/postcode of main location), and — for sole traders — an individual `name`
- **Empty/negative result looks like:** "No matching results" — the name/number isn't a registered Australian entity (or is spelled differently). A "Cancelled" status means the business existed but is no longer active.

## Gotchas & OpSec
- Human-in-the-loop: none — public form, no login.
- OpSec: **passive** — no notification to the entity.
- ABN Lookup shows *business* location (state/postcode), not a person's home address, and only officeholder names for sole traders/partnerships; for company directors use ASIC. Common names return many entities — filter by state/postcode.

## Overlaps ("do both")
- Do both with an ASIC company/officeholder search — ABN Lookup confirms the entity and status cheaply; ASIC returns the directors and registered office behind a company.

## Trust & verifiability
`trust: trusted` — first-party Australian government register (ATO/ABR); statuses and identifiers are authoritative and independently verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australian-business-register-abn-lookup |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
