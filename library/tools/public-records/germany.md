---
id: germany
name: Germany
description: Use when you have a German company/association (`employer-org`) or a `name` behind one and want beneficial-ownership and registry data — returns `employer-org` detail, `associate` officers/owners, and `address`.
url: https://www.transparenzregister.de/treg/de/start;jsessionid=70446A1E6E977FEDA187BC388AE0B5B7.app11?0
category: public-records
path:
- public-records
bestFor: Looking up German beneficial owners and the people/addresses behind companies and associations.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: The Transparenzregister is free to search, but access requires a free registered account (introduced under the 2017/2020 transparency rules); some documents/extracts may carry a small fee.
opsec: passive
opsecNote: Querying the register is passive and not disclosed to the company or individuals. Note that under German rules the register can log who accessed certain beneficial-owner records; use an account that isn't tied to a sensitive investigation identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Germany's statutory Transparency Register (operated for the Federal Ministry of Finance by Bundesanzeiger Verlag); authoritative for registered beneficial-ownership data.
missingPersonsRelevance: high
coverage:
- de
auth: account
api: false
localInstall: false
registration: true
aliases:
- Transparenzregister
- German Transparency Register
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Germany

> Germany's official **Transparenzregister** (Transparency Register) — the statutory record of beneficial owners behind German companies, partnerships, and associations, and the people and addresses tied to them.

## When to use
Your subject is linked to a German company, GmbH, or Verein (association) — as owner, director, or beneficial owner — and you want the people behind the entity. The register discloses beneficial owners (name, month/year of birth, nationality, nature of interest) and connects an `employer-org` to real individuals (`associate`) and `address` data — a strong pivot when a corporate shell stands between you and a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.transparenzregister.de/ and create a free account (registration is required to search).
2. Search by company/association name (`employer-org`) or by a person's `name`.
3. Open the entry — read registered beneficial owners, their roles/interests, and associated addresses.
4. Pivot: named owners/officers (`associate`) feed people-search and Handelsregister (commercial register) cross-checks; addresses feed geolocation.

## Inputs → Outputs
- **In:** `employer-org` (company/association) or `name`
- **Out:** beneficial owners (`associate`), nature of control, `address`, linked `employer-org`s
- **Empty/negative result looks like:** no entry — some entities are exempt or not yet filed, and small associations may not appear; absence isn't proof of no ownership, cross-check the Handelsregister.

## Gotchas & OpSec
- Human-in-the-loop / **account-login**: free registration is mandatory to search; access to some beneficial-owner records is logged.
- German-language interface; entity types (GmbH, e.V., KG) matter — know what you're searching.
- Coverage is **Germany only**; for the corporate filings themselves pair with the Handelsregister/Unternehmensregister.

## Overlaps ("do both")
- Pairs with the German Handelsregister and `[[sherpaintelligence-substack-com]]` (org→people methodology) — the Transparenzregister names beneficial owners; the commercial register adds filings and officers.

## Trust & verifiability
`trust: trusted` — it is Germany's statutory transparency register with legally-mandated data; authoritative, though filings can lag reality, so treat a stale-looking entry with care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | germany |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
