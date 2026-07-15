---
id: infocreditgroup-com
name: Infocredit Group
description: Use when you have a company `name` or a person's `name` tied to a business and want credit, ownership, and due-diligence/KYC data across 130+ countries — returns employer-org, associate, and address records.
url: https://www.infocreditgroup.com/
category: public-records
path:
- public-records
bestFor: Commercial business-intelligence, credit-risk, and due-diligence/KYC reports on companies and their principals across 137+ countries.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: freemium
costNote: Paid B2B/enterprise service — reports, API access, and the ComplianceSuite/Nexis Diligence platforms are purchased per-report or by subscription. There is no free public lookup; the site's marketing pages are open but any actual report requires a paid account. Author-listed as freemium only because the enum has no "paid" value.
opsec: passive
opsecNote: Standard commercial data-broker query — running a report does not notify the subject. Because it requires a registered corporate account, your identity and the searches you run are logged by Infocredit; use an appropriate investigative account, not a personal one, and be mindful of the legal basis for KYC/credit searches on individuals (GDPR/DPA where applicable).
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established provider (founded 1972) with ISO 9001/22301/27001 certifications, sourcing from official company registries and credit data; a reputable commercial due-diligence house, not a scraper.
missingPersonsRelevance: medium
coverage:
- global
- eu
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- opencorporates
- dnb
aliases:
- Infocredit World
- InfocreditWorld.com
- Infocredit Group Ltd
tags:
- companysites
- Company Related Sites
- business-intelligence
- kyc
- due-diligence
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Infocredit Group

> A 50-year-old commercial business-intelligence and due-diligence house: company credit reports, ownership, and KYC/AML screening across 137+ countries.

## When to use
You are working a subject who is tied to a company — a director, shareholder, or business owner — and you need to establish the corporate structure, financial standing, registered addresses, and associated people (officers, beneficial owners). Or you have a company `name` and need due-diligence/KYC screening. This is a paid, authoritative layer to reach for when free registry lookups (OpenCorporates) don't go deep enough, especially outside your home jurisdiction.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.infocreditgroup.com/ and register a business/investigative account (required for any actual data).
2. Choose the relevant product: **credit report** (financials, credit score), **due diligence / Nexis Diligence** (adverse media, ownership, sanctions), or **ComplianceSuite** (AML/KYC screening).
3. Search by company `name`, registration number, `address`, or a principal's `name`.
4. Order the report; read the structure — registered office `address`, directors/shareholders (`associate`s), group companies (`employer-org` links), and risk flags.
5. Pivot: named directors/owners become person-search targets; linked group companies extend the corporate map; addresses feed property/registry lookups.

## Inputs → Outputs
- **In:** company `name` / registration number, a business `address`, or a person's `name` in a business context.
- **Out:** `employer-org` details (financials, status, ownership), registered `address`es, and connected people as `associate`s/directors.
- **Empty/negative result looks like:** "no record" for a company that may trade under a different registered name, or thin data for a country with limited registry coverage — absence of a report is not proof the entity doesn't exist.

## Gotchas & OpSec
- Payment wall: nothing usable is free; you must have a paid account, so this is a "call it when the case justifies the cost" resource, not a first pass.
- Coverage and freshness vary sharply by country — Western European and larger markets are strong; some jurisdictions are thin or delayed.
- Searches are logged to your corporate account, and KYC/credit screening of individuals carries data-protection obligations (GDPR/DPA) — ensure you have a lawful basis.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and `[[dnb]]` — start free with OpenCorporates to map the corporate skeleton, then use Infocredit (or D&B) for the paid financial, beneficial-ownership, and adverse-media depth OpenCorporates lacks.

## Trust & verifiability
`trust: trusted` — a long-established, ISO-certified provider drawing on official registry and credit sources. Reports are authoritative for the covered jurisdictions, though (as with any aggregator) verify a critical fact against the primary registry when it drives a decision.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infocreditgroup-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
