---
id: ukas-com
name: UKAS – Find an Organisation
description: Use when you have an `employer-org` name (a lab, cert body or inspection firm) and want to verify its UK accreditation — returns the org's accredited status, scope and address.
url: https://www.ukas.com/find-an-organisation/
category: public-records
path:
- public-records
bestFor: Verifying that a UK testing lab, certification body or inspection organisation is genuinely UKAS-accredited, with its scope and location.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public directory; no account or payment to search or view accreditation details.
opsec: passive
opsecNote: A public accreditation directory lookup; no target interaction and nothing is logged against you beyond a normal site visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: UKAS is the UK's sole national accreditation body, recognised by government. Its directory is the authoritative source for whether a body is UKAS-accredited.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- aat-org-uk
aliases:
- United Kingdom Accreditation Service
- UKAS directory
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# UKAS – Find an Organisation

> The UK's national accreditation body's directory: confirm whether a lab, certification body or inspection firm is really UKAS-accredited, and see its scope and address.

## When to use
You have an `employer-org` — a company claiming to be an accredited testing lab, certification body, calibration or inspection provider — and need to verify that claim or locate the organisation. Useful for vetting a business tied to a subject, confirming a credential is legitimate (fake "accredited" claims are a fraud signal), and getting an authoritative address/scope for the entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ukas.com/find-an-organisation/.
2. Search by organisation `name`, or filter by type (testing lab, certification body, inspection body, medical lab, etc.), UK region, or category.
3. Read the listing: accredited organisation `name`, `address`, accreditation type and the specific scope it is accredited for.
4. Cross-check the claimed accreditation against the actual scope — a body may be accredited for X but not Y.
5. Pivot: a verified `address`/`employer-org` feeds company-records (Companies House) and people-search on directors/staff.

## Inputs → Outputs
- **In:** `employer-org`/`name` (± region/type)
- **Out:** accredited `employer-org`, `address`, accreditation scope
- **Empty/negative result looks like:** no match. That is itself meaningful — a firm claiming UKAS accreditation that does not appear here is a red flag (or is accredited by a different national body).

## Gotchas & OpSec
- Accreditation is scope-specific: presence in the directory does not mean the org is accredited for *everything* it claims — read the scope.
- UK-only; overseas accreditation is handled by other national bodies (via ILAC/IAF mutual recognition).
- OpSec: passive; purely a public directory read.

## Overlaps ("do both")
- Pairs with `[[aat-org-uk]]` and other professional-licensing registries — UKAS verifies *organisational* accreditation; those verify *individual* professional membership. Do both when vetting a firm and its people.
- Follow with Companies House to link the accredited entity to its directors.

## Trust & verifiability
`trust: trusted` — UKAS is the single government-recognised UK national accreditation body, so its directory is authoritative for accreditation status. The only caveat is reading the accreditation *scope* correctly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukas-com |
</content>
