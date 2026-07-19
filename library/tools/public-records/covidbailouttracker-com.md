---
id: covidbailouttracker-com
name: COVID Bailout Tracker
description: Use when you have an `employer-org` (or business name/owner) and want to know if it took CARES Act relief — returns PPP/airline-bailout records with amounts and locations.
url: https://covidbailouttracker.com/
category: public-records
path:
- public-records
bestFor: Checking whether a named business received PPP or airline pandemic-relief funds, with amount and location.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free public-interest transparency site (donation-supported); no account or payment to search.
opsec: passive
opsecNote: Anonymous browsing of a published transparency database. No login, nothing written, no subject notification. The underlying records are already public federal disclosures, so lookups are low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by transparency advocates (Accountable.US / affiliated groups) from official SBA and Treasury disclosures; the data mirrors government releases but is a third-party compilation, so verify individual records against the primary SBA/Treasury data.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- COVID Bailout Tracker
- covidbailouttracker
tags:
- ppp
- covid-relief
- financial-records
- business-records
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# COVID Bailout Tracker

> A searchable transparency database of US pandemic relief — Paycheck Protection Program (PPP) loans and airline bailouts — that ties a business name to a funded amount and location.

## When to use
You have a business (`employer-org`) or an owner's `name` and want to establish a financial/organizational fact: did this entity receive federal COVID relief, how much, and where was it registered for the loan? A PPP record links a business to a location, an approximate size (loan bracket / jobs reported), and a lender — useful to confirm a company existed and operated at a claimed address during 2020–2021, or to tie an individual to a business they ran. It also maps reported fraud cases, which can flag an entity worth deeper scrutiny.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://covidbailouttracker.com/ and use the PPP/recipient search (or browse by state and program).
2. Enter the business name (or owner) and read the matched record: loan amount/bracket, city/state, lender, and jobs reported.
3. Check the fraud map/section if you're vetting an entity for misconduct.
4. Cross-verify the specific record against the official SBA PPP disclosure or Treasury data before relying on it.
5. Pivot: a confirmed business `address` and `employer-org` feed a corporate-registry lookup; a linked owner name feeds people-search.

## Inputs → Outputs
- **In:** `employer-org` (business name) or `name` (owner/applicant)
- **Out:** relief record — funded `employer-org`, `address`/city-state, loan amount bracket, lender, jobs reported
- **Empty/negative result looks like:** no matching recipient — meaning the entity didn't take PPP/airline relief (or applied under a different legal name), not that it never existed.

## Gotchas & OpSec
- Human-in-the-loop: none; it's an open search.
- It's a compilation of official disclosures — a match is a strong lead, but verify amounts/identities against the primary SBA/Treasury release.
- Businesses often apply under a formal legal name or DBA that differs from the trading name; try variants.
- US-only and time-bounded to the CARES Act relief programs.

## Overlaps ("do both")
- Pairs with a state corporate/business registry — this confirms the relief funding and location, that confirms incorporation, officers, and registered agent.

## Trust & verifiability
`trust: community` — a public-interest project compiling official SBA/Treasury data; reliable as a pointer, but confirm any load-bearing record against the primary government disclosure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | covidbailouttracker-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
