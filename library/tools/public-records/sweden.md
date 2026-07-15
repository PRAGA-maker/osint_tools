---
id: sweden
name: Sweden — Bolagsverket Företagsfakta (company registry)
description: Use when you have a Swedish company `name`/`employer-org` or person and want official registry data — returns registered company details, addresses and associated officers from Bolagsverket.
url: https://foretagsfakta.bolagsverket.se/fpl-dft-ext-web/home.xhtml
category: public-records
path:
- public-records
bestFor: Authoritative lookups of Swedish companies (and their registered officers/addresses) via the national companies registration office.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: freemium
costNote: Basic company facts (name, org number, status, registered address) are free to search; some detailed documents/extracts may carry a fee, but the core lookup is free.
opsec: passive
opsecNote: Official government registry lookup; you query the registry, not any individual, and no notification is sent. No login for basic search. Swedish company records are public by law.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Bolagsverket, the Swedish Companies Registration Office — this is the authoritative source of truth for registered Swedish companies.
missingPersonsRelevance: high
coverage:
- se
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bolagsverket
- Företagsfakta
- Swedish company registry
tags:
- companysites
- Company Related Sites
- company-registry
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Sweden — Bolagsverket Företagsfakta (company registry)

> Sweden's official companies-registration office lookup: the authoritative source for registered Swedish company details, addresses and officers.

## When to use
You have a Swedish company `name`/`employer-org` (or an organisation number, or a person you believe is a company officer) and want authoritative registry data: legal name, org number, status, registered `address`, and — where shown — associated officers/`associate`s. Use it to confirm a business a subject is tied to, place that business geographically, and surface linked people. The site is in Swedish.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://foretagsfakta.bolagsverket.se/ (Bolagsverket's Företagsfakta). No login is needed for the basic search.
2. Search by company `name` or organisation number (search terms are in Swedish; use the company name form).
3. Read the record: legal name, org number, registration status, registered `address`, business type, and any listed officers/representatives.
4. For deeper detail, note that formal extracts/documents may require a fee — the free record usually suffices to confirm existence, status and address.
5. Pivot: officer names feed people-search; the registered address feeds mapping; the org number feeds cross-border company databases.

## Inputs → Outputs
- **In:** company `name` / `employer-org` / org number (optionally a person as officer)
- **Out:** registered `employer-org` details, `address`, associated `associate`/officers, status
- **Empty/negative result looks like:** no matching company — meaning no Swedish registration under that name/number, not that the person has no business anywhere.

## Gotchas & OpSec
- Language: the interface and records are in Swedish; translate field labels as needed.
- Human-in-the-loop: none for basic search; only formal document extracts may be paywalled.
- OpSec: fully passive; an official public-registry lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with cross-jurisdiction company aggregators (e.g. OpenCorporates-style tools) — this is the authoritative Swedish source, while aggregators help you connect it to entities in other countries.

## Trust & verifiability
`trust: trusted` — Bolagsverket is the Swedish government registrar, so its records are authoritative; only paid formal extracts add legal weight beyond the free facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sweden |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
