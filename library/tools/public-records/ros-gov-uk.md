---
id: ros-gov-uk
name: Registers of Scotland (ros.gov.uk)
description: Use when you have a `name` or Scottish `address` and want property ownership or a will/deed — returns address, owner name and employer-org links from Scotland's official registers.
url: https://www.ros.gov.uk/services/order-a-will
category: public-records
path:
- public-records
bestFor: Searching Scotland's official land/property registers (who owns a property) and ordering wills/deeds held by Registers of Scotland.
selectorsIn:
- name
- address
selectorsOut:
- address
- name
- employer-org
status: live
pricing: freemium
costNote: Basic property searching via ScotLIS is free (viewing summary ownership info); official extracts, title sheets, deeds and wills are ordered for a per-document fee. No subscription needed to search.
opsec: passive
opsecNote: You query the official Scottish registers, not the subject — passive, and the ownership data is public record. Ordering documents needs payment tied to your details; use a research account for paid extracts.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Registers of Scotland is the Scottish Government's official registrar of land, property and related deeds; ownership and register data are authoritative first-party records.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Registers of Scotland
- ScotLIS
- RoS
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- property
- scotland
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Registers of Scotland (ros.gov.uk)

> Scotland's official land, property and deeds registrar — find who owns a Scottish property, or order a will/deed, straight from the authoritative source.

## When to use
You have a Scottish `name` or `address` and want to establish a property link: does the subject own property in Scotland, what is their property `address`, or who owns an address you already have? Property ownership ties a person to a place and often to co-owners or a company (`employer-org`). The same registrar lets you order wills and historic deeds, useful for estate/inheritance and family-link research on someone who has died or moved.

## How to use it (`bestInteractionPattern`: web-manual)
1. For property, use **ScotLIS** (Scotland's Land Information Service) via ros.gov.uk to search by `address` (or map) for the property and its summary ownership.
2. For wills/deeds, use the "order a will"/deeds service at the URL to request documents Registers of Scotland holds.
3. Read the free summary; order the official extract/title sheet/will (paid) when you need documentary proof.
4. Extract the owner `name`(s), property `address`, and any company/`employer-org` owner or co-owners.
5. Pivot: an owner name feeds people-search; co-owners become `associate` leads; a company owner feeds Companies House.

## Inputs → Outputs
- **In:** `name` or Scottish `address`
- **Out:** `address` (property), `name` (owner), `employer-org` (corporate owner/co-owner)
- **Empty/negative result looks like:** no property/register entry — meaning no Scotland-registered property under that name/address, or the title predates registration; England & Wales property is on HM Land Registry instead, so absence here is Scotland-specific.

## Gotchas & OpSec
- **Scotland only** — English/Welsh property is HM Land Registry; don't conclude "no property" UK-wide from this.
- Summary search is free; documentary proof (extracts, deeds, wills) is pay-per-document.
- OpSec: passive over public register data; paid orders tie to your account.

## Overlaps ("do both")
- Pairs with `[[thegenealogist-co-uk]]` (wills/genealogy) and HM Land Registry — use RoS for Scottish property/deeds and the relevant registry for other UK nations, plus genealogy tools for older wills.

## Trust & verifiability
`trust: trusted` — the official Scottish Government registrar; ownership and register data are authoritative primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ros-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, name, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
