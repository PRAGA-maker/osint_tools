---
id: permits-city-of-vancouver-application-permit-search-by-address
name: City of Vancouver Permit & Application Search
description: Use when you have a Vancouver (BC) `address` and want the building/development permit applications tied to it, which often name owners, applicants and contractors — returns name, employer-org and associate.
url: https://plposweb.vancouver.ca/public/default.aspx
category: people-search
path:
- people-search
bestFor: Linking a Vancouver property address to the people and firms who applied for permits on it.
selectorsIn:
- address
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public search on the City of Vancouver's POSSE portal; browsing/searching needs no account. An account is only required to submit an application, not to search.
opsec: passive
opsecNote: Public municipal record; searching an address is anonymous and does not notify the property owner. Only use the public search side — do not register/log in with real identity for OSINT, as the applicant portal is attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official City of Vancouver permitting system (POSSE); the authoritative municipal record of permit applications, though the personal detail surfaced varies by application and redaction.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Vancouver POSSE permits
- City of Vancouver permit search
- plposweb.vancouver.ca
tags:
- address
- permits
- property
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# City of Vancouver Permit & Application Search

> The City of Vancouver's official permit portal — search by address to find building/development applications that frequently name the owner, applicant, and contractor.

## When to use
You have a `address` in Vancouver, British Columbia and want to know who has applied for building, development, or trade permits there. Permit records commonly list the property owner or applicant `name`, and the contractor/architect `employer-org`, giving you an address→person(s) bridge and a set of associated parties (owner, agent, builder) to develop further.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://plposweb.vancouver.ca/public/default.aspx (the POSSE public portal).
2. Use the public **Search** function (no login needed) to search permits/applications by address; broaden or narrow by permit type and date if offered.
3. Open a matching permit. Read the parties listed — owner/applicant `name`, contractor/architect firm (`employer-org`), and the site address — plus status/dates.
4. Pivot: an owner name feeds BC people-search and land-title lookups; a contractor firm feeds business registries; multiple permits at one address over time build an occupancy timeline and an `associate` set (owners, agents, builders).

## Inputs → Outputs
- **In:** `address` (Vancouver, BC)
- **Out:** `name` (owner/applicant), `employer-org` (contractor/architect), `associate` (parties to the permit)
- **Empty/negative result looks like:** no permits returned for the address — the property may simply have no recent permit activity, not that the address is wrong.

## Gotchas & OpSec
- Covers the City of Vancouver only — neighbouring municipalities (Burnaby, Richmond, Surrey, etc.) run separate portals.
- Detail varies: some permits show full applicant names, others show only a company or are partly redacted.
- The site has scheduled maintenance windows; if the portal is down, retry later.
- Passive: address searches are anonymous. Do not create an applicant account with real identity for OSINT.

## Overlaps ("do both")
- Pairs with BC land-title / assessment lookups — the permit names the applicant/contractor, while title/assessment records confirm registered ownership; cross-check the two to resolve owner vs. applicant.

## Trust & verifiability
`trust: trusted` — an authoritative municipal permitting system. What it records (that an application was filed, by/for whom) is reliable; completeness of personal detail depends on the individual application.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | permits-city-of-vancouver-application-permit-search-by-address |
| category | people-search |
| selectorsIn → selectorsOut | address → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
