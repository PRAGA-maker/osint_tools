---
id: gov-uk-14
name: gov.uk (HM Land Registry HC1 — historical register/title plan)
description: Use when you have a property `address` (or title number) and want a PAST edition of the HM Land Registry register/title plan — returns historical owner name and address records.
url: https://www.gov.uk/government/publications/historical-registertitle-plan-registration-hc1
category: public-records
path:
- public-records
bestFor: Ordering superseded (historical) editions of an England & Wales property register or title plan to recover former registered owners.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: The HC1 application form itself is free to download, but HM Land Registry charges a statutory fee per historical edition supplied (consult the current HMLR fee schedule). Paid-but-official, not a free dataset.
opsec: passive
opsecNote: This is an official application to a government registry, not a covert query — you submit the HC1 form (and pay a fee), so the request is attributable to whoever files it. There is no notification to the current owner, but do not expect anonymity; the transaction is logged by HMLR.
humanInLoop: true
humanInLoopReason:
- manual-review
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK government (HM Land Registry via GOV.UK) — the authoritative source for England & Wales land title records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-9
- land-registry
aliases:
- HC1
- Land Registry historical register
- historical title plan
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# gov.uk (HM Land Registry HC1 — historical register/title plan)

> The official HM Land Registry HC1 route to order *past* editions of a property's register or title plan — useful for tracing former registered owners of a home in England & Wales.

## When to use
You have a property `address` (or its title number) in England or Wales and the **current** register no longer shows who you need — because ownership has since changed. HMLR keeps superseded editions; the HC1 form lets you request a specific historical edition of the register or title plan, which can name a `former registered proprietor` and their address at the time. This is a targeted records request, not a search engine: use it when a person was tied to a known property in the past.

## How to use it (`bestInteractionPattern`: web-manual)
1. First identify the title number for the address via the current-register service ([[gov-uk-9]] / HMLR "Search for land and property information").
2. Open the HC1 page: https://www.gov.uk/government/publications/historical-registertitle-plan-registration-hc1 and download the HC1 form and guidance.
3. Complete the form specifying the title and which historical edition(s) you want.
4. Submit to HM Land Registry with the required fee (per the current fee schedule).
5. HMLR reviews and supplies the historical register/title-plan edition — read it for the former owner `name`, their contemporaneous `address`, and any company (`employer-org`) proprietor.

## Inputs → Outputs
- **In:** property `address` / title number (and optionally a `name` you're trying to place at that property)
- **Out:** historical registered-owner `name`, their `address` at the time, corporate proprietor (`employer-org`)
- **Empty/negative result looks like:** HMLR holds no historical edition for that title, or the title is unregistered — many older/rural properties in England & Wales remain unregistered and won't appear.

## Gotchas & OpSec
- England & Wales only — Scotland (Registers of Scotland) and Northern Ireland use separate registries.
- Human-in-the-loop: this is a manual, fee-bearing application reviewed by HMLR — not an instant lookup. Turnaround is days, not seconds.
- OpSec: passive toward the subject but fully attributable to you; the request is an official transaction, so treat it as on-the-record.

## Overlaps ("do both")
- Pairs with [[gov-uk-9]] / [[land-registry]] for the *current* register — get the title number and present owner there first, then use HC1 only when you specifically need a superseded historical edition.

## Trust & verifiability
`trust: trusted` — first-party HM Land Registry data delivered through GOV.UK; the authoritative record of registered land title in England & Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-14 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review, payment-wall-partial) |
