---
id: luxembourg
name: Luxembourg Business Registers (RCS)
description: Use when you have a `name` or `employer-org` and want official Luxembourg company records — returns directors/officers (name, associate), the company (employer-org), and its registered address.
url: https://www.lbr.lu/mjrcs-lbr/jsp/IndexActionNotSecured.action
category: public-records
path:
- public-records
bestFor: Looking up Luxembourg companies and their directors/managers in the official Registre de Commerce et des Sociétés (RCS).
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- associate
- address
- employer-org
status: live
pricing: freemium
costNote: Basic name/company search and the register index are free; full company extracts and filed documents (statutes, accounts) are paid per-document.
opsec: passive
opsecNote: A registry search does not notify anyone. Buying document extracts may require an LBR account and payment, which are logged; use investigative-context details.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Luxembourg Business Registers (RCS), operated under a state economic-interest grouping; authoritative for Luxembourg entities and their officers.
missingPersonsRelevance: high
coverage:
- lu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
- disputesregister-org
aliases:
- LBR Luxembourg
- RCS Luxembourg
- Registre de Commerce et des Sociétés
tags:
- companysites
- Company Related Sites
- corporate-records
- luxembourg
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Luxembourg Business Registers (RCS)

> Luxembourg's official company register — a key jurisdiction for holding companies and funds, where you can tie a person to a Luxembourg entity and pull its registered address and officers.

## When to use
Your investigation touches Luxembourg, a major EU corporate/holding jurisdiction. You have an `employer-org` (a Luxembourg company name/RCS number) and want its managers/directors and registered address; or you have a `name` and want the Luxembourg entities behind them. This is the authoritative Registre de Commerce et des Sociétés (RCS).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lbr.lu/ and use the RCS search.
2. Search by company name/RCS number, or by a person's `name`, to find matching entities and officers.
3. Read the free register data: entity name, RCS number, legal form, registered office (`address`), and listed managers/directors (`name` / `associate`).
4. For statutes, accounts, or full extracts, order the (paid) documents.
5. Pivot: officers feed people-search and PEP checks; the registered address feeds geolocation; co-managers feed associate mapping.

## Inputs → Outputs
- **In:** `employer-org` (company / RCS number) or `name` (officer)
- **Out:** `name` (managers/directors), `associate` (co-officers), `address` (registered office), `employer-org`, legal form & status
- **Empty/negative result looks like:** no matching entity/officer — the person may not be a registered Luxembourg officer, or the entity is a fund/vehicle with limited public officer disclosure. Absence isn't proof.

## Gotchas & OpSec
- Free tier gives the register index and basic details; statutes/accounts are **paid per document**.
- Interface is French/German/English — some filings are only in French.
- Luxembourg hosts many holding/fund structures; beneficial ownership may sit in a separate register (RBE), not the RCS.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (free cross-border officer index — check there first) and `[[disputesregister-org]]` (registry directory). Use free indices first; buy the RCS extract when you need the authoritative document.

## Trust & verifiability
`trust: trusted` — the official Luxembourg company register. Authoritative; note that full documents are paid and ultimate ownership may require the separate beneficial-owners register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | luxembourg |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, associate, address, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
