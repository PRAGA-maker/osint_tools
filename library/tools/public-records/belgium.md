---
id: belgium
name: Belgium UBO Register
description: Use when you have a Belgian company `employer-org` or a person's `name` and want the ultimate beneficial owners behind it — returns name, address, dob, and associate links (access-restricted).
url: https://financien.belgium.be/nl/E-services/Ubo-register
category: public-records
path:
- public-records
bestFor: Identifying the ultimate beneficial owners (controlling natural persons) behind Belgian companies, associations, foundations, and trusts.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- address
- dob
- associate
status: live
pricing: free
costNote: Government service with no fee, but public access was curtailed after the 2022 CJEU ruling — you must authenticate and, in most cases, demonstrate a legitimate interest to view another entity's beneficial owners.
opsec: active
opsecNote: Access is via authenticated login (Belgian eID/itsme/eIDAS or the ForREG portal for foreigners). Every query is logged against your identity, and legitimate-interest requests are reviewed. This is a named, auditable government interaction — not anonymous. Do not attempt to access it under a false identity.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official register operated by the Belgian Federal Public Service Finance; the data is legally mandated and authoritative.
missingPersonsRelevance: high
coverage:
- be
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- opencorporates-com
- gleif-org
aliases:
- UBO-register
- Belgian beneficial ownership register
- Register van uiteindelijke begunstigden
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Belgium UBO Register

> Belgium's mandatory beneficial-ownership register: find the real natural persons who own or control a Belgian legal entity — behind a heavy access gate.

## When to use
You have a Belgian `employer-org` (company, non-profit, foundation, or trust) and need to pierce the corporate veil to the ultimate beneficial owners — the natural persons who actually own or control it — or you have a `name` and want to know which Belgian entities they beneficially own. Registered UBO records include the owner's name, address, date of birth, and the nature/extent of their control, which can tie a subject to assets, businesses, and co-owners.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://financien.belgium.be/nl/E-services/Ubo-register and open the MyMinfin UBO application.
2. Authenticate: Belgian residents use eID or itsme; other EU citizens use eIDAS; non-EU users register via the ForREG portal.
3. To consult an entity you are not the legal representative of, you must lodge a legitimate-interest request, which is subject to review.
4. Once granted, search by the entity's enterprise number (or name) and read the beneficial-owner list.
5. Pivot: named owners and their DOB/address feed people-search and other registries; cross-border ownership chains can be followed via BORIS/EU interconnection.

## Inputs → Outputs
- **In:** `employer-org` (entity / enterprise number) or `name`
- **Out:** `name`, `address`, `dob` of beneficial owners, plus the nature and percentage of control (`associate` links between co-owners)
- **Empty/negative result looks like:** access denied (no legitimate interest granted) or, if you reach the record, an entity with no registered UBOs — which for Belgian entities usually signals non-compliance rather than genuinely no owner.

## Gotchas & OpSec
- **Public access was removed** after the November 2022 Court of Justice of the EU ruling. General open-public consultation no longer exists; only competent authorities, obliged entities (banks, notaries), and parties demonstrating a legitimate interest can view another entity's UBOs.
- Human-in-the-loop: mandatory authenticated login **and** a reviewed legitimate-interest gate.
- OpSec: **active and named** — every access is tied to your verified identity and logged. Treat this as a formal, auditable request, not covert OSINT.

## Overlaps ("do both")
- Pairs with [[opencorporates-com]] and [[gleif-org]] — those give you the Belgian entity's directors and LEI without the access gate; use them first to identify the company, then the UBO register (if you have standing) for the true owners behind nominee directors.

## Trust & verifiability
`trust: trusted` — it is the official Belgian government beneficial-ownership register with legally mandated, penalty-backed filings, so the data is authoritative where you can access it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | belgium |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, address, dob, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
