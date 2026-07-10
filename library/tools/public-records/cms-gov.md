---
id: cms-gov
name: cms.gov (Open Payments)
description: Use when you have a US doctor's `name` and want financial-industry ties — CMS Open Payments returns payments from drug/device firms, the paying `employer-org`, and the physician's practice `address`.
url: https://openpaymentsdata.cms.gov/
category: public-records
path:
- public-records
bestFor: Confirming a US physician/teaching hospital and mapping their payments from pharma/device companies (name, specialty, practice location, payers).
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free official US government (CMS) database; no account needed to search or download.
opsec: passive
opsecNote: Searching a public federal transparency database is passive and does not notify the physician. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US Centers for Medicare & Medicaid Services (CMS) data, mandated by the Sunshine Act; authoritative for reported physician/industry financial relationships.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ama-assn-org
aliases:
- CMS Open Payments
- Open Payments Sunshine Act
- openpaymentsdata.cms.gov
tags:
- professionlicensing
- Profession & Licensing Sites
- healthcare
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# cms.gov (Open Payments)

> The US government's Open Payments (Sunshine Act) database — search a physician or teaching hospital and see payments they received from drug and device companies, confirming identity, specialty, location, and industry ties.

## When to use
Your subject is (or claims to be) a US physician, and you want to confirm and profile them: Open Payments lists doctors by `name` with their specialty, practice `address`, and every reported payment/transfer of value from pharmaceutical and medical-device companies. It both verifies a medical identity and surfaces `employer-org`/`associate` links to the companies paying them — useful for corroboration and conflict-of-interest/network mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://openpaymentsdata.cms.gov/ and search the physician `name` (add state/specialty to disambiguate).
2. Open the physician's profile: specialty, practice `address`, and a breakdown of payments by paying company and category (research, consulting, meals, travel).
3. Note the paying companies (`employer-org`) and amounts as relationship leads.
4. For bulk work, use the CMS API/downloadable datasets.
5. Pivot: practice address feeds location work; payer companies feed corporate lookups; confirm the medical license/identity via `[[ama-assn-org]]` or the NPI registry.

## Inputs → Outputs
- **In:** physician `name` (+ state/specialty), or a paying `employer-org`
- **Out:** confirmed physician (specialty, practice `address`), paying companies (`employer-org`/`associate`), payment detail
- **Empty/negative result looks like:** no record — the person may not be a covered US physician, may be a non-physician provider, or received no reportable payments; absence isn't proof they're not in medicine.

## Gotchas & OpSec
- Covers US physicians and teaching hospitals with **reportable industry payments** — a doctor with none won't show payments (but may still be listed with basic info).
- Name matching can hit namesakes; confirm with specialty/location/NPI.
- OpSec: passive; a public database, no notification.
- Moderate MP value: strongest when the subject has a medical angle.

## Overlaps ("do both")
- Pairs with `[[ama-assn-org]]` and the NPI registry to confirm licensure/identity; the payer companies can be run through company-registry tools.

## Trust & verifiability
`trust: trusted` — first-party CMS data mandated by federal law, so reported relationships are authoritative. Verify identity against a licensing/NPI source when names are common.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cms-gov |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
