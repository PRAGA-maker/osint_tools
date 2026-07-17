---
id: asic-business-name-search
name: ASIC Registry Search (Australia)
description: Use when you have an `employer-org`/business name or a director `name` in Australia and want the official record — ASIC's registry returns company/business-name status, ABN/ACN, and registered details.
url: https://connectonline.asic.gov.au/RegistrySearch
category: search-engines
path:
- search-engines
bestFor: Authoritative Australian company/business-name lookups — status, identifiers and registration details.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: Searching the register (name, status, ABN/ACN) is free. Purchasing extracts/historical documents with full officer/address detail costs a small per-document fee.
opsec: passive
opsecNote: Searching the government register is passive and anonymous; the business is not notified. Paid document purchases require an ASIC/BizPay account that identifies you — use an investigative account for those.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Australian Securities and Investments Commission registry — the authoritative source for Australian companies and registered business names.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- national-company-registers
aliases:
- ASIC Connect
- connectonline.asic.gov.au
tags:
- company-research
- australia
- corporate-registry
- toddington
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# ASIC Registry Search (Australia)

> Australia's official corporate registry — confirm a company or registered business name, get its ACN/ABN and status, and (for a small fee) pull the extract that lists officers and addresses.

## When to use
Your investigation touches an Australian business (`employer-org`) or someone who may be a director/business-name holder there. ASIC is the authoritative register: a free search confirms whether a company/business name is registered, its status (registered/deregistered/strike-off), its ACN/ACN identifiers, and registration dates. To tie *people* to the entity — directors, registered office `address`, document history — you purchase the paid extract. This is the primary source for Australian corporate OSINT; prefer it over aggregators for anything you need to stand up.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://connectonline.asic.gov.au/RegistrySearch.
2. Search by organisation/business `name` or by ACN/ABN. (Note: free search is entity-centric; it isn't a general "find all companies for person X" people-search.)
3. Read the free results: entity name, type, status, identifiers, registration/renewal dates.
4. For officers, shareholders, registered office `address` and document history, purchase the current/historical **company extract** (paid, per-document — a human-in-the-loop budget step needing an account).
5. Pivot: registered address → geolocation; officers named in the extract → people-search and `[[national-company-registers]]` for their other roles.

## Inputs → Outputs
- **In:** `employer-org`/business name, or ACN/ABN (or a person's `name` to check business-name holdings)
- **Out:** entity status/identifiers free; officers, `associate` directors and registered `address` via the paid extract
- **Empty/negative result looks like:** no matching entity — the business may be unregistered, a trading name only, deregistered long ago, or spelled differently. Try name variants and the ABN Lookup service.

## Gotchas & OpSec
- Free tier confirms the entity and status; the **people/address detail is paywalled** in the extract — plan for the small fee.
- It's entity-first: you generally search a company/name, not reverse-search all companies tied to a person from this screen.
- Business names vs companies are distinct ASIC record types; make sure you're reading the right one.

## Overlaps ("do both")
- Use `[[national-company-registers]]` to confirm you're on the right national register and to cover officers' roles in other countries. ASIC is the authoritative AU source; corroborate cross-border footprints elsewhere.

## Trust & verifiability
`trust: trusted` — ASIC is the official Australian government corporate regulator; its register is the authoritative record. Free search data and paid extracts both come straight from the registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | asic-business-name-search |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
