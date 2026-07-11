---
id: gov-im
name: Isle of Man Companies Registry
description: Use when you have an `employer-org` or `name` linked to an Isle of Man company and want official registry data — returns company status, officers/directors, and registered address.
url: https://services.gov.im/companies-registry/
category: public-records
path:
- public-records
bestFor: Official Isle of Man company/director lookups — registered address, officers, and company status.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: Basic company name/number search is free. Copies of filed documents (incorporation, annual returns, officer details) are typically charged per document.
opsec: passive
opsecNote: Public registry lookups are passive and anonymous — the company/officers are not notified. Note the beneficial-ownership register is NOT public; attempting to access it without authorisation is a criminal offence under Isle of Man law. Stay within the public company search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Isle of Man Government's Department for Enterprise — the statutory, first-party company register. Authoritative, though visible officers may be nominees.
missingPersonsRelevance: high
coverage:
- im
auth: none
api: false
localInstall: false
registration: false
aliases:
- Isle of Man Companies Registry
- services.gov.im companies registry
- Companies Registry IoM
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Isle of Man Companies Registry

> The Isle of Man's official corporate register — the authoritative source for whether an IoM company exists, who its officers are, and its registered address.

## When to use
You have an `employer-org` (company name/number) or a `name` you suspect is an officer of an Isle of Man company, and you want the official record: company status, incorporation details, directors/secretaries, and the registered `address`. Relevant when a subject is tied to offshore/IoM corporate structures — a common holding jurisdiction — and you need to place them at a company or find a registered address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://services.gov.im/companies-registry/ and go to the company search service.
2. Enter the company name or number (`employer-org`), or search for a person's `name` among officers where supported.
3. Read the free result: exact company name, number, status (active/dissolved), type (1931/2006 Act, LLC, foreign), and registered address.
4. To see officer details or filings, order the relevant filed documents (a per-document fee applies).
5. Pivot: a registered `address` and officer `name`s feed other records; a director link corroborates a subject's business footprint. Cross-check `[[opencorporates]]`-style aggregators.

## Inputs → Outputs
- **In:** `employer-org` (company name/number), `name` (officer), or `address`
- **Out:** company status/type, registered `address`, officer `name`s, incorporation data
- **Empty/negative result looks like:** "no results" for the name/number — the company may be dissolved (search dissolved records separately), foreign, or the name spelt differently; not proof of non-existence.

## Gotchas & OpSec
- Nominee directors are common in IoM structures — a publicly listed officer may be a professional nominee, not the beneficial owner.
- The beneficial-ownership register is **not** public; do not attempt to access it — unauthorised access is a criminal offence on the Island.
- Full officer/filing detail usually requires paying for filed documents.

## Overlaps ("do both")
- Pairs with OpenCorporates and other UK/Crown-dependency registries — the primary IoM registry is authoritative, while aggregators help you discover the IoM link in the first place and connect it to companies in other jurisdictions.

## Trust & verifiability
`trust: trusted` — a first-party statutory register; company existence, status, and registered address are authoritative, subject to the nominee-officer caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-im |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
