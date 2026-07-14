---
id: icaew-com
name: ICAEW — Find a Chartered Accountant
description: Use when you have a `name` or firm and want to confirm a UK chartered accountant / ICAEW-regulated firm — returns the firm/member `employer-org`, `address` and services offered.
url: https://find.icaew.com/
category: public-records
path:
- public-records
bestFor: Verifying that an accountant or accountancy firm is ICAEW-regulated and finding their firm name, location and service areas.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public directory operated by the ICAEW (Institute of Chartered Accountants in England and Wales); no account or payment.
opsec: passive
opsecNote: A read-only directory search — the subject is not notified. The site sees your IP/query like any website; a sock-puppet browser suffices for a sensitive lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party directory of the ICAEW, the UK chartered-accountancy body; authoritative for ICAEW membership/regulation, though it lists firms/services rather than exhaustive individual detail.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- eca-co-uk
- architects-register-org-uk
aliases:
- find.icaew.com
- Find a Chartered Accountant
- icaew.com
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- accountancy
- regulator
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# ICAEW — Find a Chartered Accountant

> The ICAEW's public directory of chartered accountants and regulated firms — confirms a subject's accountancy credentials and locates their firm.

## When to use
You have a `name`, firm (`employer-org`), or `address`/area and want to establish whether an accountant or accountancy practice is ICAEW-regulated. This verifies a claimed profession, ties a person to a specific firm and location, and confirms the practice is subject to ICAEW oversight (useful for legitimacy checks).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://find.icaew.com/.
2. Search by name, firm, location, or service required.
3. Read the results: firm/member `employer-org`, `address`/location, and the services the firm offers.
4. Disambiguate common names using firm and location.
5. Pivot: the firm + address feed Companies House and business-registry searches; confirmed regulation corroborates a claimed career.

## Inputs → Outputs
- **In:** `name`, `employer-org` (firm), or `address`/area
- **Out:** firm/member `employer-org`, `address`/location, confirmed `name`, services offered
- **Empty/negative result looks like:** no match — the person/firm is not ICAEW-regulated (they may belong to another body such as ACCA or CIMA, or be unregulated), not proof they aren't an accountant.

## Gotchas & OpSec
- UK/ICAEW-specific: accountants regulated by ACCA, CIMA, AAT, etc. won't appear here — check the relevant body.
- The directory emphasises firms and services; it is not a full personal-record source.
- OpSec: fully passive; a routine directory lookup.

## Overlaps ("do both")
- Pairs with `[[eca-co-uk]]`, `[[architects-register-org-uk]]` and other UK profession registers — do both when pinning down which regulated body a subject belongs to, and with Companies House to link the firm to a legal entity.

## Trust & verifiability
`trust: trusted` — first-party ICAEW directory; a match is authoritative for ICAEW regulation specifically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icaew-com |
