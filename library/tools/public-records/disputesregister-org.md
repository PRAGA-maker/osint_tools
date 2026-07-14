---
id: disputesregister-org
name: DisputesRegister.org
description: Use when you have an `employer-org` or `name` and want a global directory of official company registries plus a searchable register of public business disputes — returns employer-org, address, and associate leads.
url: https://www.disputesregister.org/advice/company-registries-by-country
category: public-records
path:
- public-records
bestFor: Finding the right official company registry for any country, and checking whether a business/person has a publicly filed dispute.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free to browse the registry directory and search filed disputes; filing a dispute is a separate (registrant) action, not needed for research.
opsec: passive
opsecNote: Browsing the country registry directory and searching filed disputes is passive and does not notify anyone. No account needed to read.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A public complaint-filing platform with a curated worldwide company-registry directory; the directory links are useful, but dispute entries are user-submitted and unvetted — treat them as claims, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
- onlinesearch-mns-mu
aliases:
- Disputes Register
- Business Disputes Register
tags:
- companysites
- Company Related Sites
- registry-directory
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# DisputesRegister.org

> Two things at once: a worldwide directory of official company registries (to find *where* to research a company), and a searchable register of publicly filed business disputes (to find *if* someone has a complaint against them).

## When to use
You have an `employer-org` or a `name` and either (a) don't know which country's official registry to search — the "Company Registries by Country" directory points you to the authoritative registrar for the jurisdiction — or (b) want to check whether the business/person has a publicly filed dispute or complaint, which can surface a residential/business address, a company number, and counterparties (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. For the registry directory: open https://www.disputesregister.org/advice/company-registries-by-country and pick the country to get its official company registry link.
2. Follow that link and search the authoritative registrar for the company/officer.
3. For disputes: search DisputesRegister itself for the company or person name to see any filed complaints.
4. Read dispute entries for disclosed details — company numbers, addresses, named parties — but treat the substance as an unverified claim.
5. Pivot: the registry link feeds an official corporate lookup (e.g. `[[onlinesearch-mns-mu]]`); dispute counterparties feed associate mapping.

## Inputs → Outputs
- **In:** `employer-org` or `name`
- **Out:** the correct official registry link per country; from dispute entries — `employer-org`, `address`, `associate` (counterparties), company numbers
- **Empty/negative result looks like:** no filed disputes for the name (common — most businesses have none) and, in the directory, simply the list of registries. No dispute ≠ clean history.

## Gotchas & OpSec
- The dispute entries are **user-submitted and unvetted** — potentially one-sided or false. Corroborate before treating as fact.
- The most reliable value is the **registry directory** (a curated set of official registrar links), not the complaints themselves.
- Fully passive to read; no account required.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (global company/officer index) and country registries like `[[onlinesearch-mns-mu]]` — use DisputesRegister's directory to find the right registrar, then pull the authoritative record there.

## Trust & verifiability
`trust: unverified` — the registry directory is a helpful curated resource, but dispute filings are unvetted user claims. Verify any dispute against primary records before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disputesregister-org |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
