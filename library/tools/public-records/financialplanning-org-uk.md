---
id: financialplanning-org-uk
name: financialplanning.org.uk (Find a Planner)
description: Use when you have a `name`, firm or UK location and want to confirm a certified financial planner — returns the planner's name, firm/employer and business location from the CISI professional directory.
url: https://www.financialplanning.org.uk/wayfinder/find-planner
category: public-records
path:
- public-records
bestFor: Confirming and locating a UK certified/chartered financial planner and the firm they work for.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public "find a planner" directory run by the professional body; no account or payment needed.
opsec: passive
opsecNote: Public professional-register lookup; you query the directory, not the individual, and no notification is sent. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Chartered Institute for Securities & Investment (CISI) / Financial Planning body; entries are vetted certifications, so a listing is an authoritative professional-status signal.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- CISI Find a Planner
- Wayfinder financial planner search
tags:
- professionlicensing
- Profession & Licensing Sites
- professional-register
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# financialplanning.org.uk (Find a Planner)

> The UK financial-planning profession's "find a planner" directory: confirm a person is a certified/chartered financial planner and see the firm and location they practise from.

## When to use
You have a `name` (or a firm/`employer-org` or UK `address`/area) and want to confirm the subject is a certified financial planner and pin down their professional footprint — firm, business location, and credential. This corroborates a claimed profession, links a person to a business `address`, and can confirm identity where the subject works in UK financial planning.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.financialplanning.org.uk/wayfinder/find-planner.
2. Search by planner `name`, firm, or filter by UK location/area.
3. Read the listing: the planner's `name`, their firm/`employer-org`, business `address`/area, and the certification held.
4. Corroborate: a listing confirms professional standing at a firm — cross-check the firm via a company registry to tie down current employment.
5. Pivot: the firm name feeds Companies House / company-registry lookups; the business location feeds mapping; the confirmed identity feeds people-search.

## Inputs → Outputs
- **In:** `name` / `employer-org` (firm) / `address` (UK area)
- **Out:** `name`, `employer-org` (firm), business `address`/location, certification
- **Empty/negative result looks like:** no matching planner — meaning the person isn't a CISI-certified financial planner in this directory, not that they have no finance role at all.

## Gotchas & OpSec
- Human-in-the-loop: none — open, free directory.
- Scope: this lists certified financial *planners*; someone in finance who isn't certified here won't appear. Absence isn't proof of no finance career.
- OpSec: fully passive; a public register lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with UK company-registry and Companies House tools — this confirms the professional credential and firm; the registry confirms the firm's directors/status and current employment.

## Trust & verifiability
`trust: trusted` — it is the profession's own vetted directory, so a listing is an authoritative certification signal; only current-employment detail should be re-checked against a company registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | financialplanning-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
