---
id: probaterecords-co-uk
name: probaterecords.co.uk
description: Use when you have a deceased person's `name` and want an official sealed copy of their England & Wales will or grant of probate — returns `associate` (executors/beneficiaries), `address`, and death details.
url: https://probaterecords.co.uk/
category: public-records
path:
- public-records
bestFor: Ordering official sealed/certified copies of England & Wales wills and grants of probate via an expedited paid service.
selectorsIn:
- name
- address
selectorsOut:
- associate
- address
- name
status: degraded
pricing: freemium
costNote: Paid document-ordering service (operated by "UK Documents") — you pay per sealed/certified copy of a will or grant. There is no free search; the free first-party equivalent is the GOV.UK probate search (probatesearch.service.gov.uk) which lists the calendar entry and lets you order copies for £1.50. Use probaterecords.co.uk only for expedited/overseas convenience.
opsec: passive
opsecNote: You are ordering a public record from an intermediary, not contacting the subject (who is deceased). Passive, but you disclose your interest and payment/contact details to the service; use a role-based email if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial intermediary (UK Documents, London) that obtains genuine court-sealed probate documents from the Probate Registry; not a first-party government service. Service has at times shown as suspended/degraded.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-6
- gro-gov-uk
aliases:
- Probate Records
- UK Documents probate
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- probate
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# probaterecords.co.uk

> A commercial expediter for England & Wales wills and grants of probate — orders official sealed copies faster than the standard registry route, for a fee.

## When to use
Your subject is deceased and you want the contents of their **will** — which names executors and beneficiaries (strong `associate` links), the estate value, and often addresses — or a **grant of probate** confirming death and estate handling. A will is a rich family-network document for missing-persons and estate work. Reach here specifically when you need an expedited or overseas-friendly ordering route; otherwise the free GOV.UK probate search is the better first stop.

## How to use it (`bestInteractionPattern`: web-manual)
1. First check the free GOV.UK probate calendar at https://probatesearch.service.gov.uk to confirm a probate entry exists (name, death year, registry) — it also lets you order copies for £1.50.
2. If you need expedited/certified handling, open https://probaterecords.co.uk/ and select a service tier (expedited, standard online, or economical postal PA1S).
3. Provide the deceased's `name`, approximate death date, and last-known `address`; pay the fee.
4. Receive the court-sealed will/grant copy by post/PDF within the quoted turnaround (days for expedited, weeks for postal).
5. Pivot: executors and beneficiaries named in the will become new `associate` leads; the estate address and any bequeathed property feed address/property lookups.

## Inputs → Outputs
- **In:** deceased's `name`, death year, last-known `address`
- **Out:** `associate` (executors, beneficiaries, witnesses), `address` (residence, estate property), death/probate details tied to the `name`
- **Empty/negative result looks like:** no probate was granted (many estates never go through probate), so absence here does not mean the person didn't die or leave assets.

## Gotchas & OpSec
- Human-in-the-loop: paid, manually-fulfilled ordering (payment wall + human processing); expect a wait, not an instant download.
- Status is **degraded** — the service has at points advertised suspended/limited expedited processing; confirm it is operating before relying on it.
- It is an intermediary: the same sealed documents are obtainable directly and far more cheaply via GOV.UK — only pay the premium for genuine speed/convenience needs.
- Only covers England & Wales; Scotland and Northern Ireland have separate systems.

## Overlaps ("do both")
- Cross-check the free `[[gov-uk-6]]` GOV.UK probate route first — it confirms the calendar entry cheaply before you pay for a copy.
- Pair with `[[gro-gov-uk]]` for the underlying death registration (date/place of death) that anchors the probate.

## Trust & verifiability
`trust: community` — a legitimate commercial expediter delivering authentic court-sealed documents, but a paid intermediary rather than the registry itself. The documents are authoritative; the service layer is a convenience you should weigh against the free GOV.UK route.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | probaterecords-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → associate, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, manual-review) |
