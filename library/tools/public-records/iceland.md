---
id: iceland
name: Iceland
description: Use when you have an Icelandic `employer-org`, `name`, or `address` and want official company-registry details — returns `employer-org`, `address`, `name`, and the kennitala `document-id`.
url: https://www.rsk.is/fyrirtaekjaskra/#tab1
category: public-records
path:
- public-records
bestFor: Confirming an Icelandic company's registration, address, and ID number from the national business register.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
- document-id
status: live
pricing: free
costNote: Basic registry search (company existence, ID number, registered address, status) is free. Detailed certificates/extracts and some data may require a paid order.
opsec: passive
opsecNote: Searching the official register is passive — you query the state registry, not the subject. No login is needed for basic lookups, so nothing is attributed to you beyond a normal web request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Skatturinn (the Iceland Revenue and Customs / tax authority); this is the authoritative national company register (Fyrirtækjaskrá).
missingPersonsRelevance: high
coverage:
- is
auth: none
api: false
localInstall: false
registration: false
aliases:
- Fyrirtaekjaskra
- Iceland business register
- RSK / Skatturinn company registry
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Iceland

> Iceland's official company register (Fyrirtækjaskrá), run by the tax authority Skatturinn — look up a company's registration, kennitala (ID number), and registered address.

## When to use
Your subject is linked to an Icelandic company, or you have a company `name`/`address`/`employer-org` and need to confirm it is really registered, find its kennitala (national ID number), verify its registered address, and check its status. A key node when tracing business affiliations of an Icelandic person or an Iceland-registered entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rsk.is/fyrirtaekjaskra/ (redirects to `skatturinn.is/fyrirtaekjaskra/`; Icelandic interface, with an English section available).
2. Search by company `name` (nafn), `address` (heimilisfang), kennitala (ID), or VAT number (VSK-númer).
3. Read the record: registered `employer-org` name, kennitala (`document-id`), registered `address`, entity type and status.
4. For beneficial-ownership data, use the separate "Raunverulegir eigendur" (beneficial owners) section, which exists for AML compliance.
5. Pivot: a kennitala or address links to other Icelandic registries and to individuals; the registered address feeds map/property checks.

## Inputs → Outputs
- **In:** company `name`, `address`, `employer-org`, kennitala, or VAT number
- **Out:** `employer-org` (registered name), kennitala `document-id`, `address`, entity status; beneficial owners via the separate module
- **Empty/negative result looks like:** no match — the entity may be dissolved, spelled differently in Icelandic, or never registered. Standard search returns limited director/ownership detail; deep ownership lives in the separate beneficial-owners section.

## Gotchas & OpSec
- Interface is primarily Icelandic; Icelandic characters (þ, ð, æ) and name ordering matter — use the English pages or translation.
- The basic search is company-oriented; person-level detail is limited unless you use the beneficial-owners module.
- Kennitala is a strong, unique key — carry it into other Icelandic sources rather than re-searching by name.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and pan-EU registers like `[[e-justice-europa-eu]]` — cross-reference because the national register is authoritative and current while aggregators add cross-border links and history.

## Trust & verifiability
`trust: trusted` — first-party government register operated by Skatturinn, so company name, ID, and status are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iceland |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
