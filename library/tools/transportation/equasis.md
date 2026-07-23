---
id: equasis
name: Equasis
description: Use when you have a vessel IMO/`name` or a shipping company and want ownership, management, and safety records — returns employer-org (owner/manager/operator) and fleet links.
url: https://www.equasis.org/
category: transportation
path:
- transportation
bestFor: Free (registration-required) lookup of vessel ownership/management chains and company fleets from official maritime safety data.
selectorsIn:
- name
- document-id
- employer-org
selectorsOut:
- employer-org
- vehicle-plate
- associate
status: live
pricing: free
costNote: Completely free of charge, but you must register a free account to run ship and company searches. No paid tier.
opsec: passive
opsecNote: Equasis aggregates official regulatory/classification data; querying it does not touch the vessel, owner, or crew, so there's no alert. Register with a sock-puppet identity/email since account creation is required. Ownership can be layered through shell companies — the registered owner may not be the beneficial owner.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Public-interest platform backed by maritime administrations (EC and multiple national authorities); data is compiled from official classification societies and regulators.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- equasis.org
tags:
- vessel-ownership
- maritime
- bellingcat-toolkit
- transport
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Equasis

> The go-to free source for who owns and manages a ship — enter an IMO number and get the registered owner, manager, operator, and their other vessels, drawn from official maritime data.

## When to use
You have a vessel (by IMO number or `name`) or a shipping `employer-org` and need the ownership/management chain and safety history. Central to maritime investigations: it links a ship to its registered owner, ISM manager, and commercial operator, and lets you pivot from a company to its whole fleet — mapping a network of vessels and corporate entities behind a person or business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.equasis.org/ and register a free account (search is login-gated).
2. Ship search: enter the IMO number (best) or vessel `name`; Company search: enter the company name.
3. Read the ship page: identity/particulars, registered owner, ISM manager, operator, flag/class history, and inspection records (`selectorsOut`).
4. Pivot: click a company to see its full fleet (`associate` vessels/entities); feed company names into corporate registries; use the IMO to cross-check FleetMon/MarineTraffic for live position.

## Inputs → Outputs
- **In:** `name` (vessel/company), `document-id` (IMO), or `employer-org` (company)
- **Out:** `employer-org` (owner/manager/operator companies), `vehicle-plate` (IMO), `associate` (a company's other vessels/related entities), safety/inspection history
- **Empty/negative result looks like:** no vessel/company match, or an owner field showing an opaque management shell — meaning further corporate digging is needed, not that ownership is unknowable.

## Gotchas & OpSec
- Human-in-the-loop: free registration/login required (`account-login`).
- OpSec: passive — official aggregated data; nobody is notified. Use a puppet account.
- Beneficial ownership is often hidden behind single-ship holding companies and management firms; treat the "registered owner" as one layer, then trace the companies onward.

## Overlaps ("do both")
- Pairs with live AIS trackers [[fleetmon]] / MarineTraffic (Equasis gives ownership, they give position) and with corporate registries to unwind the company chain Equasis surfaces.

## Trust & verifiability
`trust: trusted` — a public-interest platform backed by the European Commission and national maritime administrations, compiling data from classification societies and regulators, making it the authoritative free source for vessel ownership/safety records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | equasis |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id, employer-org → employer-org, vehicle-plate, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
