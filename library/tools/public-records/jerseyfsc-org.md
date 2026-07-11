---
id: jerseyfsc-org
name: Jersey Financial Services Commission Registry
description: Use when you have an `employer-org` or `name` tied to a Jersey company/entity and want official registry data — returns entity existence, status, type, and registered address.
url: https://www.jerseyfsc.org/registry/
category: public-records
path:
- public-records
bestFor: Official Jersey (Channel Islands) company/entity lookups — status, type, and registered address.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: Basic entity name/number search is available online (myRegistry); ordering filed documents and some registry services carry per-item fees.
opsec: passive
opsecNote: Public registry lookups are passive and anonymous — the entity is not notified. As in other offshore registers, beneficial-ownership and some controller data are NOT public; stay within the public entity search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Jersey Financial Services Commission — the statutory, first-party registrar for Jersey companies, business names, foundations, and partnerships. Authoritative, though visible officers may be nominees.
missingPersonsRelevance: high
coverage:
- je
auth: none
api: false
localInstall: false
registration: false
aliases:
- JFSC Registry
- jerseyfsc.org
- Jersey companies registry
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Jersey Financial Services Commission Registry

> Jersey's official corporate registrar — the authoritative source for whether a Jersey company, foundation, or partnership exists, its status, and its registered address.

## When to use
You have an `employer-org` (company/entity name or number) or a `name` you suspect is an officer of a Jersey entity, and you want the official record: entity existence, status, type, and registered `address`. Relevant when a subject is linked to Channel Islands offshore structures — a common holding jurisdiction — and you need to place them at an entity or find a registered address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jerseyfsc.org/registry/ and use the register search (via the myRegistry portal).
2. Search by entity name/number (`employer-org`) — or a person's `name` where officer search is supported.
3. Read the result: entity name, number, status, type (company, business name, foundation, partnership), and registered address.
4. To obtain officer detail or filings, order documents through the portal (per-item fees apply).
5. Pivot: a registered `address` and officer `name`s feed other records; a directorship corroborates a subject's business footprint. Cross-check `[[gov-im]]` for related IoM structures.

## Inputs → Outputs
- **In:** `employer-org` (name/number), `name` (officer), or `address`
- **Out:** entity status/type, registered `address`, officer/associated-party `name`s (via filings)
- **Empty/negative result looks like:** no match — the entity may be dissolved, foreign, or spelled differently; not proof of non-existence.

## Gotchas & OpSec
- Nominees: Jersey structures frequently use professional nominee directors — a listed officer may not be the beneficial owner.
- Beneficial ownership is not public: don't expect (or attempt to access) the private BO register.
- Fees: detailed officer data and filings usually require paying per document.

## Overlaps ("do both")
- Pairs with `[[gov-im]]` (Isle of Man) and other Crown-dependency/UK registries plus OpenCorporates — the JFSC record is authoritative for Jersey, while aggregators help you discover the link and connect it across jurisdictions.

## Trust & verifiability
`trust: trusted` — a first-party statutory registrar; entity existence, status, and registered address are authoritative, subject to the nominee-officer caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jerseyfsc-org |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
