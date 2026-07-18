---
id: australian-securities-and-investments-commission
name: Australian Securities & Investments Commission
description: Use when you have a company/business `name` or a person's `name` in Australia and want registered company, business-name, and officeholder records — returns `employer-org`, `address`, `associate`.
url: https://connectonline.asic.gov.au/RegistrySearch/faces/landing/SearchRegisters.jspx
category: public-records
path:
- public-records
bestFor: Confirming Australian companies/business names and linking a person to registered entities and addresses.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Name/existence searches on ASIC Connect are free; full extracts (officeholders, historical details) are pay-per-document, purchased through ASIC or an information broker.
opsec: passive
opsecNote: Querying the register does not notify the company or person. Free searches are anonymous; buying a paid extract requires payment details, which are attributable — use appropriate billing if you go that far.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Australian government corporate regulator's register — authoritative for company and business-name status.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ASIC
- ASIC Connect
- ASIC company register
tags:
- toddington
- curated-directory
- company-search
- corporate-registry
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Australian Securities & Investments Commission

> Australia's official corporate regulator register — turn a company or person `name` into registered entities, business names, and (via paid extracts) officeholders and addresses.

## When to use
Your subject is in Australia, or tied to an Australian business, and you want to confirm a company/business name exists, who runs it, and what address it registers. Free searches confirm existence and status (registered/deregistered) and current business-name holders; paid extracts add officeholders/directors, which turn a company into a set of `associate` and `address` leads. Relevant when a missing person or an associate ran, worked for, or owned an Australian entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ASIC Connect register search (https://connectonline.asic.gov.au/RegistrySearch/faces/landing/SearchRegisters.jspx).
2. Choose the register (Companies & Organisations, Business Names) and enter the `name` or ACN/ABN.
3. Read the free result: entity name, ACN/ABN, type, and status (registered/deregistered/strike-off).
4. For officeholders and the registered address, order a paid company extract (pay-per-document) — that's where director `name`s and the registered `address` appear.
5. Pivot: a director name feeds people-search; a registered address feeds property/records work; a business-name holder links the entity to a real person.

## Inputs → Outputs
- **In:** `name` (person or company) or `employer-org`
- **Out:** `employer-org` (registered entities), `address` (registered/principal address, via extract), `associate` (officeholders/directors, via extract)
- **Empty/negative result looks like:** "no matches found" for the name — the entity isn't ASIC-registered, or the spelling differs; try ABN Lookup as a cross-check before concluding it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: the useful officeholder/address detail is behind a per-document paywall; the free tier is existence/status only.
- OpSec: passive and anonymous for free searches; a paid extract ties a purchase to you.
- Deregistered companies still appear — status matters; don't treat a struck-off entity as active.

## Overlaps ("do both")
- Pairs with the free ABN Lookup and general company-search tools — ASIC gives regulator-grade company/officeholder detail, while ABN Lookup gives quick free trading-name/GST cross-checks. Do both to confirm an Australian entity.

## Trust & verifiability
`trust: trusted` — it is the Australian government's official corporate register, so entity status and officeholder data are authoritative (the paid extract is the primary source, not a re-seller's copy).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australian-securities-and-investments-commission |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
