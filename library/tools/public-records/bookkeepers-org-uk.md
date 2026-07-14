---
id: bookkeepers-org-uk
name: bookkeepers.org.uk
description: Use when you have a UK bookkeeper/business `name` or location and want to confirm ICB membership — returns the certified bookkeeper's business name, area, and practice details (employer-org/address hints).
url: https://www.bookkeepers.org.uk/Find-a-Bookkeeper/Browse-Directory/
category: public-records
path:
- public-records
bestFor: Verifying a UK bookkeeper is an ICB-certified member and getting their practice name and service area.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free public "find a bookkeeper" directory run by the ICB; no account.
opsec: passive
opsecNote: A public professional directory — searching it doesn't notify anyone and reveals only self-published, scheme-vetted practice data. Passive; use a sock-puppet browser if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Institute of Certified Bookkeepers (ICB); a listing authoritatively confirms current ICB membership, though it covers only bookkeepers who chose to list.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- companies-house
- trustmark-org-uk
aliases:
- ICB Find a Bookkeeper
- bookkeepers.org.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- public-records
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# bookkeepers.org.uk

> The ICB's public "find a bookkeeper" directory: confirm a UK bookkeeper is a certified member and get their practice name, area, and services.

## When to use
You have a subject who claims to be (or is linked to) a UK bookkeeper/accounting practice and want to confirm ICB certification and obtain their listed business name, service area, and specialisms. Strongest for verifying a **practitioner/business** and locality rather than looking up an arbitrary individual by name; a listing corroborates occupation and ties them to a practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bookkeepers.org.uk/Find-a-Bookkeeper/Browse-Directory/.
2. Search/browse by location (and name/practice where possible).
3. Read the member listing: bookkeeper/practice name, service area, contact and specialisms, membership grade.
4. Pivot: a confirmed practice name/area feeds `[[companies-house]]` for directors and registered office; compare with other UK trade registers like `[[trustmark-org-uk]]`.

## Inputs → Outputs
- **In:** `name` / location / `employer-org` (practice)
- **Out:** confirmed `name`, practice `employer-org`, service-area `address` hint, membership status
- **Empty/negative result looks like:** no match — the person isn't an ICB member, isn't listed, or trades under a different name; non-membership is not proof they aren't a bookkeeper (many use other bodies like AAT).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public directory; no notification.
- Scope: ICB members who opted to list only — a "not found" says nothing about non-ICB bookkeepers or other accounting bodies.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` (named directors + filings behind a practice) and `[[trustmark-org-uk]]` (other UK trade accreditation) — cross-reference to confirm occupation and the people behind a business.

## Trust & verifiability
`trust: trusted` — a first-party professional-body directory, so a listing authoritatively confirms current ICB membership. It does not verify the individual's broader identity — corroborate that via Companies House.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bookkeepers-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
