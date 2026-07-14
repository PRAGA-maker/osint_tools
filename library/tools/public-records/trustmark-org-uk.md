---
id: trustmark-org-uk
name: trustmark.org.uk
description: Use when you have a UK tradesperson/business `name` or trade + location and want to confirm TrustMark registration — returns the registered business name, address, and trade (employer-org details).
url: https://www.trustmark.org.uk/homeowner/find-a-tradesperson
category: public-records
path:
- public-records
bestFor: Verifying that a UK home-improvement tradesperson/business is TrustMark-registered and getting their registered business details.
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
costNote: Free public search operated under the UK government-endorsed scheme; no account.
opsec: passive
opsecNote: A public register of accredited businesses — searching it doesn't notify anyone and reveals only self-published, scheme-vetted business data. Passive; use a sock-puppet browser if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: TrustMark is the UK Government Endorsed Quality Scheme for tradespeople; registrations are vetted, so a listing is authoritative for business accreditation (not for private-individual identity).
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
aliases:
- TrustMark
- Find a Tradesperson
tags:
- professionlicensing
- Profession & Licensing Sites
- public-records
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# trustmark.org.uk

> The UK's government-endorsed tradesperson register: confirm a home-improvement business is TrustMark-accredited and pull its registered details.

## When to use
You have a UK trade business or tradesperson tied to a subject — an employer, a claimed occupation, a company on an invoice — and want to confirm it's a vetted TrustMark member and obtain its registered business name, `address`, and trade. Search is primarily by *what work + where*, so it's strongest for verifying a **business** and its location rather than looking up an arbitrary private individual by name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.trustmark.org.uk/homeowner/find-a-tradesperson.
2. Enter the type of work and a location (town/postcode); or use the guided search.
3. Browse the returned registered businesses — name, trade categories, service area/address, accreditation.
4. Pivot: a confirmed business name/address feeds `[[companies-house]]` for directors/registered office and financial history, tying the trade to named individuals.

## Inputs → Outputs
- **In:** trade + location (and business `name`/`employer-org` to confirm a specific one)
- **Out:** registered business `name`, `address`/service area, trade (`employer-org` context), accreditation status
- **Empty/negative result looks like:** no match — the business isn't TrustMark-registered (many legitimate traders aren't), operates elsewhere, or trades under a different name; absence is not proof the business is fake.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public accreditation register; no notification.
- Scope: it verifies **businesses/tradespeople in the scheme**, not private individuals — don't expect residential people-search results, and remember non-membership ≠ illegitimacy.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` — TrustMark confirms trade accreditation and locale; Companies House turns a business name into named directors, addresses, and filings.

## Trust & verifiability
`trust: trusted` — a UK government-endorsed scheme with vetted registrations, so a listing authoritatively confirms accreditation. It does not, however, verify the identity of any individual behind the business — corroborate that via Companies House.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trustmark-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
