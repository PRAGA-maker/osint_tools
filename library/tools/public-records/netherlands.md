---
id: netherlands
name: KVK Business Register (Netherlands)
description: Use when you have a `name` or `employer-org` linked to the Netherlands and want registered companies, directors and addresses — returns `employer-org`, `associate`, `address`, `name`.
url: https://www.kvk.nl/bestellen/#/?productfilter=ubo
category: public-records
path:
- public-records
bestFor: Tying a Dutch company or person to registered officers, addresses and (paid) beneficial-owner extracts.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: Free basic search of the Handelsregister (name, address, registration status). Full KVK extracts, corporate history, financial statements and UBO extracts are paid per-document; the UBO register itself has restricted access post-2022 EU ruling.
opsec: passive
opsecNote: Official Dutch Chamber of Commerce register; searching hits KVK, not the subject. Basic search needs no account; ordering paid extracts requires payment details, which attaches your identity to the request — use an investigative account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: KVK is the official Netherlands business register; free basic data is authoritative, paid extracts are the legal record.
missingPersonsRelevance: medium
coverage:
- nl
auth: none
api: true
localInstall: false
registration: false
aliases:
- KVK
- Kamer van Koophandel
- Dutch Business Register
- Handelsregister
tags:
- companysites
- Company Related Sites
- corporate-registry
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# KVK Business Register (Netherlands)

> The Dutch Chamber of Commerce (Kamer van Koophandel) register: the authoritative source for who runs, owns and is registered at any Netherlands company.

## When to use
You have a `name` or company `employer-org` with a Dutch connection and want the corporate footprint — companies a person directs, co-officers (`associate`), registered addresses, and, via paid extracts, beneficial owners and filed accounts. Free search confirms existence and basic details; pay only when you need the certified extract or deeper history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open KVK search (https://www.kvk.nl/en/search/). Enter a company name, KVK number, or (limited) person/trade name.
2. Read the free result: registered name, address, KVK number, legal form, status.
3. To go deeper, order a paid product — KVK Extract (officers, authority), Corporate History, Financial Statements, or a UBO extract (access-restricted).
4. Note co-officers and addresses as pivots.
5. Pivot: run associates back through KVK, cross-check addresses in mapping tools, and confirm against pan-EU aggregators.

## Inputs → Outputs
- **In:** `name`, company `employer-org`, or `address`
- **Out:** `employer-org`, `associate` (officers), `address`, `name`; paid extracts add beneficial owners and financials
- **Empty/negative result looks like:** no registered entity — no Dutch company under that name/number; person search is limited, so absence of a person hit doesn't rule out a directorship.

## Gotchas & OpSec
- Free search is thin; officer/UBO detail sits behind paid extracts and the UBO register is access-restricted since the 2022 EU Court of Justice ruling.
- Person-name search is weaker than company search — start from the company where possible.
- A registered address is the business's, not necessarily a home.
- A public API exists for programmatic access.

## Overlaps ("do both")
- Pairs with OpenCorporates and the EU BRIS — use KVK as the primary source to confirm what aggregators report.

## Trust & verifiability
`trust: trusted` — the official Dutch register; free data is authoritative and paid extracts are the legal record. Confirm a common name maps to the right individual before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netherlands |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
