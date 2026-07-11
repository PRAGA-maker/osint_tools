---
id: fca-org-uk
name: fca.org.uk (FCA Mutuals Public Register)
description: Use when you have an `employer-org` or `name` tied to a UK mutual (credit union, co-op, friendly society) and want its registration and filings — returns employer-org, address, and document-id.
url: https://mutuals.fca.org.uk/
category: public-records
path:
- public-records
bestFor: Searching the FCA's register of UK mutual societies — co-operatives, community benefit societies, credit unions, building & friendly societies — for registration details and filings.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free to search by society name or registration number; basic details downloadable as CSV. No account needed.
opsec: passive
opsecNote: Official public register — searching it does not notify anyone and reveals only your IP to the FCA. A fully passive records lookup; no sock-puppet strictly needed, but use one if the wider case is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK regulator (Financial Conduct Authority); the register is the authoritative record of mutual societies, though the FCA notes it does not warrant absolute accuracy of submitted material.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- companies-house
- ebra-be
aliases:
- FCA Mutuals Public Register
- mutuals.fca.org.uk
tags:
- companysites
- Company Related Sites
- regulator-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# fca.org.uk (FCA Mutuals Public Register)

> The FCA's authoritative register of UK mutual societies — where credit unions, co-operatives, community benefit and friendly societies are recorded, with their filings and registered offices.

## When to use
You have an `employer-org` that is (or may be) a mutual — a credit union, co-op, community benefit society, building society, or friendly society — or a `name` you suspect is an officer/registrant of one, and you want authoritative registration data. These entities don't all appear at Companies House, so the Mutuals Register is the right source. Useful for confirming an organization exists, its registered `address`, and its filing history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mutuals.fca.org.uk/.
2. Search by society name or FCA registration number.
3. Open the society record: registration status, registered `address`, society type, and filed documents (`document-id` references such as annual returns/rules).
4. Download the CSV of basic details if you need to work across many societies.
5. Pivot: a registered office `address` and named officers feed people/property searches; if the entity is actually a company, cross-check [[companies-house]].

## Inputs → Outputs
- **In:** `employer-org` (society name) or registration number; a `name` to match against officers
- **Out:** `employer-org` registration details, registered `address`, filing/document references (`document-id`)
- **Empty/negative result looks like:** no match — the organization may be a normal company (check Companies House), a charity (Charity Commission), or dissolved; absence here only rules out *mutual* registration.

## Gotchas & OpSec
- Scope is **mutual societies only** — ordinary limited companies are at Companies House, charities at the Charity Commission; pick the right register.
- The FCA disclaims warranty on submitted material — treat filings as authoritative-but-self-reported.
- OpSec: passive — an official public register with no notification to anyone.

## Overlaps ("do both")
- Pairs with [[companies-house]] (UK companies) and [[ebra-be]] (routing to registries in other jurisdictions) — the Mutuals Register covers the specific society types those may miss.

## Trust & verifiability
`trust: trusted` — first-party FCA data; the authoritative UK record for mutual societies. Registration facts are reliable; individual filings are self-reported by the society.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fca-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
