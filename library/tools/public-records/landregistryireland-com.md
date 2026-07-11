---
id: landregistryireland-com
name: LandRegistryIreland.com (third-party)
description: Use when you have an Irish property `address`/eircode and want to buy its ownership record — returns owner name, address, and mortgage/associate details (paid).
url: https://www.landregistryireland.com/home
category: public-records
path:
- public-records
bestFor: Buying Irish land-registry folio data (owner name, mortgage) for a specific property, via an unofficial reseller.
selectorsIn:
- address
selectorsOut:
- name
- address
- associate
status: live
pricing: freemium
costNote: Map/property search to locate a folio is free, but the useful data — owner name/address, mortgage details, folio maps — is paywalled (advertised around €28 per property). The official Property Registration Authority of Ireland (PRAI, prai.ie / landdirect.ie) is the authoritative and often cheaper route.
opsec: passive
opsecNote: A records purchase; the property owner is not notified. But you are handing a third-party commercial site an address of interest plus your payment details — pay attention to who you're transacting with, and prefer the official PRAI/landdirect.ie service where possible.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Explicitly an independent reseller, "not affiliated with the PRAI." It resells data that originates from the official registry; convenient but unofficial — for authoritative use, go to landdirect.ie directly.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- Land Registry Ireland
tags:
- propertysites
- Property Related Sites
- ireland
- land-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# LandRegistryIreland.com (third-party)

> An independent (non-official) front-end for buying Irish land-registry folio data — owner name, mortgage, and boundary maps — by address or eircode.

## When to use
You have an Irish property `address` or eircode and you want to know who owns it and what's charged against it. The registry ties a person to real property, which corroborates a current/past `address`, surfaces co-owners or a lender as `associate` links, and confirms assets. This site sells that folio data; note that the official PRAI service (landdirect.ie) is the primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and use the free Map Search / address lookup to locate the property and its folio.
2. Order the folio/ownership report for that property (the owner name/address, mortgage details, and ID map sit behind a paid step, ~€28).
3. Pay and retrieve the report.
4. Pivot: the owner `name` feeds people-search; a co-owner is an `associate`; the lender/mortgage details add financial context; cross-check the same folio on official landdirect.ie.

## Inputs → Outputs
- **In:** `address` / eircode (map search to identify the folio)
- **Out (paid):** owner `name` and `address`, mortgage/charge details (`associate` = co-owners/lender), folio boundary map
- **Empty/negative result looks like:** no folio found for the address, or unregistered land (some Irish land predates compulsory registration) — try the official PRAI, and note not all property is registered.

## Gotchas & OpSec
- Human-in-the-loop: the ownership data is paywalled (payment-wall-partial); only property location/search is free.
- Unofficial reseller: it is not the PRAI. For an authoritative record and often lower cost, use landdirect.ie directly.
- OpSec: passive to the owner, but you disclose the target address and your payment details to a commercial third party.

## Overlaps ("do both")
- Do the lookup on the official landdirect.ie (PRAI) as well — that's the source of truth; this reseller is a convenience layer. Combine owner names with company/registry checks (CRO) when the owner is a company.

## Trust & verifiability
`trust: community` — a self-declared independent reseller of official registry data. The underlying data is authoritative (it comes from the PRAI), but the site is a middleman; verify anything decision-critical against landdirect.ie.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landregistryireland-com |
| category | public-records |
| selectorsIn → selectorsOut | address → name, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
