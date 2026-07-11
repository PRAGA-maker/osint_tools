---
id: cipfa-org
name: CIPFA Members Directory
description: Use when you have a `name` and want to confirm UK public-finance accountancy credentials — returns whether the person is a CIPFA member/registrant and associated professional details.
url: https://www.cipfa.org/members/members-directory
category: public-records
path:
- public-records
bestFor: Confirming a person is a CIPFA-qualified public-finance accountant in the UK.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free members directory lookup; no account or payment required to search.
opsec: passive
opsecNote: Public directory lookup — the member is not notified. Anonymous; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CIPFA, the UK professional body for public-finance accountancy; a listing authoritatively confirms membership/qualification, though the directory shows only members who are included.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Chartered Institute of Public Finance and Accountancy
- cipfa.org
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# CIPFA Members Directory

> The professional directory of the Chartered Institute of Public Finance and Accountancy — confirms whether a person holds CIPFA public-finance accountancy credentials.

## When to use
You have a `name` and want to verify a claimed public-finance accountancy qualification, or tie a person to a professional standing/employer in the UK public-finance sector. A narrow corroboration tool: it confirms membership of a specific professional body rather than discovering new leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cipfa.org/members/members-directory.
2. Search by member `name` (and any employer/location filter offered).
3. Read the result: whether the person is a listed CIPFA member and any associated professional details.
4. Absence isn't conclusive — not every member opts into public listing, and accountants may be members of other bodies (ICAEW, ACCA) instead.
5. Pivot: a confirmed member + employer feeds company/records lookups and corroborates identity/occupation.

## Inputs → Outputs
- **In:** `name` (+ employer/location filter)
- **Out:** membership confirmation, member `name`, associated professional/`employer-org` details
- **Empty/negative result looks like:** no match — the person isn't a listed CIPFA member (may belong to a different accountancy body or not be listed); scope-limited, not proof.

## Gotchas & OpSec
- One body among several: UK accountants may be ICAEW/ACCA/CIMA instead — check the relevant body.
- Partial listing: only members included in the directory appear.
- OpSec: passive; invisible to the member.

## Overlaps ("do both")
- Pairs with `[[lawsociety-org-uk]]`/`[[optical-org]]` and Companies House — same pattern of confirming a licensed profession and linking to a workplace, across different sectors.

## Trust & verifiability
`trust: trusted` — CIPFA's own professional directory; a listing authoritatively confirms membership, with absence inconclusive due to partial/opt-in listing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cipfa-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
