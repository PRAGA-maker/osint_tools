---
id: ukrlp-co-uk
name: UK Register of Learning Providers (UKRLP)
description: Use when you have a training/education provider `name` or UKPRN and want its official registration — returns `employer-org`, `address`, contact and `document-id` (UKPRN).
url: http://www.ukrlp.co.uk/
category: public-records
path:
- public-records
bestFor: Confirming and locating a UK learning/training provider — legal name, address, contact and UKPRN.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- document-id
- name
status: live
pricing: free
costNote: Free official public register (Department for Education); no account or payment.
opsec: passive
opsecNote: Official DfE register; searching is passive and needs no login. Nothing is sent to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Register of Learning Providers, managed for the Department for Education; provider registration data is authoritative.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- UKRLP
- UK Register of Learning Providers
tags:
- professionlicensing
- Profession & Licensing Sites
- education
- corporate-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# UK Register of Learning Providers (UKRLP)

> The DfE's official register of UK learning/training providers: look up a provider by name or UKPRN to get its legal name, registered address, contact and unique provider reference number.

## When to use
You have a UK education/training provider — a college, training company, apprenticeship provider, university — as a `name`, `employer-org`, or UKPRN, and want to confirm it exists and pin its registered details. Useful for vetting an employer/education claim, tying a subject to an institution, or resolving a UKPRN seen in other records to an organisation and address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ukrlp.co.uk/ and use the provider search.
2. Search by provider name, UKPRN (UK Provider Reference Number), town or postcode.
3. Read the record: legal/registered provider name, address, primary contact, verification/registration status, and UKPRN.
4. Use the UKPRN as a stable `document-id` to correlate with other education datasets (ESFA, Companies House).
5. Pivot: run the provider name through Companies House and general search; the address anchors location.

## Inputs → Outputs
- **In:** provider `name`/`employer-org`, UKPRN, or `address`/postcode
- **Out:** `employer-org` (legal name), `address`, contact, `document-id` (UKPRN)
- **Empty/negative result looks like:** no match — the organisation isn't a registered learning provider (many educators aren't UKRLP-registered), or the name differs from the registered one; absence doesn't disprove it operates.

## Gotchas & OpSec
- Covers **registered learning providers** only — a narrow slice of all UK education/training bodies.
- The registered contact/address is the provider's, not a home address.
- UK-only; a public API is available for programmatic lookups.

## Overlaps ("do both")
- Pairs with Companies House and Get Information About Schools (GIAS) — UKRLP gives the provider registration/UKPRN, those add corporate ownership and school-level detail.

## Trust & verifiability
`trust: trusted` — an official DfE register, so registration data is authoritative; still confirm the provider is the specific one you mean (similar names exist) before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukrlp-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
