---
id: katrina-spending-search
name: Katrina Spending Search
description: Use when you have a `name` or `employer-org` and want to check Hurricane Katrina federal-aid/contract recipients — returns recipient `name`, `employer-org` and award `address` details.
url: https://b2.caspio.com/dp/a4321000cb4905373d1946e5b33f
category: public-records
path:
- public-records
bestFor: Searching the NOLA.com/Times-Picayune database of federal Hurricane Katrina spending by recipient.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: degraded
pricing: free
costNote: Free public database (a Caspio-hosted datapage originally embedded on NOLA.com). No account needed; note it is a legacy 2005-era dataset and the embedded datapage may be intermittently offline.
opsec: passive
opsecNote: A read-only search of a static historical dataset — no subject is notified and nothing is sent to any target. Queries hit Caspio's hosting; treat like any public-records lookup. Zero interaction risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled by Louisiana's Governor's Office of Homeland Security and Emergency Preparedness and published by NOLA.com | The Times-Picayune (~11,532 records). Reputable journalistic source, but a fixed 2005 snapshot excluding Army Corps spending.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NOLA Katrina spending database
- Hurricane Katrina federal spending search
tags:
- disaster-recovery
- government-spending
- public-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Katrina Spending Search

> A Caspio-hosted, NOLA.com-published database of ~11,532 federal Hurricane Katrina spending records, searchable by recipient — a niche historical public-records source.

## When to use
You have a `name` or `employer-org` (individual, contractor, or organisation) with a Gulf-Coast / Hurricane Katrina (2005) connection and want to check whether they received federal disaster aid or contracts. It is a narrow, historical dataset: useful for background/asset context on a Louisiana-area subject, for corroborating a business's existence and address in that period, or for financial-trail work on post-Katrina recovery spending. Not a general people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Caspio datapage at https://b2.caspio.com/dp/a4321000cb4905373d1946e5b33f (originally embedded in NOLA.com's Katrina spending feature).
2. Enter a recipient `name` or `employer-org` in the search field.
3. Read the matching records: recipient, award/contract detail, amount, and associated location (`address`).
4. If the embedded datapage is down, search NOLA.com's Katrina-spending article for a current mirror of the same GOHSEP dataset.
5. Pivot: a recipient business + address feeds business-registry and `[[familytree]]`/court checks; a name links to other public-records tools.

## Inputs → Outputs
- **In:** `name`, `employer-org`
- **Out:** recipient `name`, `employer-org`, award/spending detail, associated `address`
- **Empty/negative result looks like:** no matching recipient — the subject received no catalogued Katrina federal spending (note the set excludes Army Corps of Engineers spending), or predates/postdates the snapshot. Absence is not proof of no federal funds.

## Gotchas & OpSec
- Human-in-the-loop: none; simple form search.
- OpSec: **passive** — static historical data, zero target interaction.
- **Staleness/liveness:** this is a 2005 snapshot on a third-party Caspio host; the embedded page can be intermittently offline (hence `status: degraded`). Confirm currency and fall back to the NOLA.com source if the datapage fails.

## Overlaps ("do both")
- Pairs with `[[familytree]]` and business-registry lookups — this confirms Katrina-era funding/address; those extend to relatives, current addresses, and identity.

## Trust & verifiability
`trust: community` — the underlying data is from an official state agency via a reputable newsroom, but it is a fixed, partial 2005 snapshot on third-party hosting. Verify any recipient/address against a primary record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | katrina-spending-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
