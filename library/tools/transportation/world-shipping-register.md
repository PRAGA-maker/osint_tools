---
id: world-shipping-register
name: World Shipping Register
description: Use when you have a ship `name`/IMO or an owner and want vessel registration details — returns owner/manager/builder links and vessel specs.
url: http://www.world-ships.com
category: transportation
path:
- transportation
bestFor: Looking up a vessel by name/IMO and pivoting to its owner, manager, builder, flag, and technical particulars.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free searching with basic vessel details; full data (up to ~70 fields per ship) and some records require registration/login and may be paid.
opsec: passive
opsecNote: Passive query of a maritime registry database; no vessel owner or operator is notified. Registration exposes your account/email to the operator — use a sock-puppet account if you register.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial maritime registry aggregating >100,000 vessels; useful for cross-links (ship↔owner↔manager↔builder), but registration data can lag ownership changes — corroborate with IMO/flag-state sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- world-ships.com
- World Ships register
tags:
- maritime
- vessel-registration
- transportation
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# World Shipping Register

> A searchable database of 100,000+ vessels with cross-links between each ship and its owner, manager, and builder — the pivot from a ship to the companies (and people) behind it.

## When to use
You have a ship `name`, IMO number (`document-id`), or a suspected owner, and you want to map the vessel to its beneficial/registered owner, manager, builder, flag, and specs. Maritime OSINT often starts from a hull and works toward the corporate/individual interests controlling it — this register provides those cross-links plus technical particulars to confirm you have the right vessel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.world-ships.com and search by Ship Name, Ex-name, IMO, Call Sign, Flag, Owner, Manager, or Builder.
2. Open the vessel record: owner/manager/builder (`employer-org`/`associate` links), flag, class, tonnage, dimensions, build year.
3. Register (free) if a needed field is gated; use the cross-links to jump between related ships and companies.
4. Pivot: an owner/manager company feeds corporate-registry research; the IMO number feeds AIS/vessel-tracking tools; the flag/class points to the flag-state registry.

## Inputs → Outputs
- **In:** ship `name` or IMO `document-id` (or an owner name)
- **Out:** `employer-org` (owner/manager/builder), `associate` company links, vessel specs, flag/class
- **Empty/negative result looks like:** "No results found" — the vessel may be too small/old to be listed, recently renamed, or outside coverage; cross-check the IMO against a flag-state or IMO source.

## Gotchas & OpSec
- Ownership is frequently layered through shells/managers; the listed owner may be a holding entity, not the beneficial owner.
- Registration data lags real-world sales/renamings — corroborate against IMO GISIS or the flag-state registry.
- Human-in-the-loop: some fields need a (free) login.

## Overlaps ("do both")
- Pairs with AIS/vessel-tracking and corporate-registry tools — this gives the ownership cross-links, those give live position and the corporate layers behind an owner.

## Trust & verifiability
`trust: community` — a broad commercial aggregator; strong for cross-linking vessels and companies, but confirm ownership/registration against authoritative IMO/flag-state records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-shipping-register |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
