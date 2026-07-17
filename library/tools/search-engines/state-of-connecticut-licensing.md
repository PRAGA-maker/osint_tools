---
id: state-of-connecticut-licensing
name: State of Connecticut License Lookup (eLicense)
description: Use when you have a `name` (or business) licensed in Connecticut and want to verify the credential — returns `employer-org`, `address`, license status, and `document-id`.
url: https://www.elicense.ct.gov/Lookup/LicenseLookup.aspx
category: search-engines
path:
- search-engines
bestFor: Verifying a Connecticut professional or occupational license by name/business and pulling status, license number, and the address on file.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free public state license-verification portal; no account.
opsec: passive
opsecNote: A state-government license lookup — passive and unobservable by the licensee. License records are public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official State of Connecticut eLicense system; records are authoritative primary licensing data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- connecticut-license-verification
- connecticut-registered-voter-verification
aliases:
- CT eLicense
- Connecticut License Lookup
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# State of Connecticut License Lookup (eLicense)

> Connecticut's official license-verification portal — confirm whether a person or business holds a state credential, and read the status, number, and address on record.

## When to use
You have a `name` (or business) you believe is licensed in Connecticut — a nurse, contractor, real-estate agent, cosmetologist, security guard, or one of dozens of regulated professions — and want to verify it and extract detail. A license record confirms a person's occupation, ties them to a business/employer, and often exposes a city/town or business `address` and a license number for further cross-referencing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the eLicense lookup page.
2. Search by last/first name, business name, license number, or profession/town filters.
3. Open the matching record: license type, status (active/expired/disciplined), issue/expiry dates, license `document-id`, and the address/town on file.
4. Check for disciplinary actions attached to the record.
5. Pivot: the address/town narrows a geographic search; the profession/employer feeds people- and company-search; the license number cross-references other CT records.

## Inputs → Outputs
- **In:** `name` or `employer-org` (or license number)
- **Out:** `employer-org` (profession/business), `address`/town on file, `document-id` (license number), and license status/discipline.
- **Empty/negative result looks like:** no record — the person isn't licensed in Connecticut in a covered profession (or the name differs); absence isn't proof they lack any credential, only none in CT's system.

## Gotchas & OpSec
- Scope is Connecticut and only professions regulated through eLicense; other states and unregulated jobs won't appear.
- Common names return multiple licensees — disambiguate by profession/town/license number.
- OpSec: passive public-records query.

## Overlaps ("do both")
- Pairs with `[[connecticut-license-verification]]` and voter/records tools — licensing confirms occupation and an on-file address; voter and court records add residence and legal history.

## Trust & verifiability
`trust: trusted` — the official state licensing system; records are authoritative and directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-of-connecticut-licensing |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
