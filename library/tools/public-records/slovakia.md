---
id: slovakia
name: RPVS – Register of Public Sector Partners (Slovakia)
description: Use when you have a company `name`/`employer-org` or a `name` doing business with the Slovak state and want its verified beneficial owners — returns name, dob, address, associate, employer-org.
url: https://rpvs.gov.sk/rpvs/
category: public-records
path:
- public-records
bestFor: Unmasking the real beneficial owners (with DOB and address) behind any entity that contracts with, or receives funds from, the Slovak public sector.
selectorsIn:
- name
- employer-org
- address
- dob
selectorsOut:
- name
- dob
- address
- associate
- employer-org
- document-id
status: live
pricing: free
costNote: Free, public, no login; a Slovak government transparency registry.
opsec: passive
opsecNote: Searching a public government registry is passive and leaves no trace to the target. No account needed; still query over a clean IP as good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Slovak government registry (rpvs.gov.sk) mandated by the anti-shell-company transparency law; beneficial-owner entries are lawyer-verified filings, making it unusually authoritative for ownership data.
missingPersonsRelevance: high
coverage:
- sk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- RPVS
- Register partnerov verejného sektora
- Slovak beneficial ownership register
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# RPVS – Register of Public Sector Partners (Slovakia)

> Slovakia's mandatory beneficial-ownership registry: for any entity doing business with the state it names the real humans behind it, with dates of birth and addresses — a rare, verified ownership source.

## When to use
You have a Slovak company `name`/`employer-org` (or a person you suspect is a hidden owner) that touches public money — government contracts, subsidies, EU funds — and you need the natural persons who ultimately own or control it. Because filings must be verified and lodged by an authorised person (typically a lawyer), the beneficial-owner data here (name + `dob` + `address`) is far stronger than a normal company register, and those personal identifiers are highly pivotable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rpvs.gov.sk/rpvs/.
2. Use basic or advanced search. Query by public-sector-partner `name`, IČO (company `document-id`), a beneficial owner's `name`, or `dob`.
3. Open the matching entry ("vložka"): it lists the partner entity, its beneficial owners (name, DOB, address, citizenship) and the authorised person who filed.
4. Pivot: a beneficial owner's name + DOB + address feeds people-search and cross-border corporate registries; the authorised person links to advisers; the IČO links to the standard Slovak business register.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `document-id` (IČO), or `dob`
- **Out:** `name`, `dob`, `address` of beneficial owners; `associate` (co-owners, authorised person); `employer-org` (the partner entity); `document-id` (IČO/entry number)
- **Empty/negative result looks like:** no matching entry — meaning the entity is not (or no longer) a registered public-sector partner, not that it has no owners. Deregistered partners may show a terminated status.

## Gotchas & OpSec
- Scope is limited to entities transacting with the Slovak public sector — an ordinary private company with no state dealings won't appear.
- Records are in Slovak; use field labels (partner verejného sektora = public-sector partner; konečný užívateľ výhod = beneficial owner) to navigate.
- OpSec: passive; it's an official open registry, so browsing does not alert anyone.

## Overlaps ("do both")
- Pairs with a general EU/company registry for entities without state dealings — RPVS is uniquely strong precisely where standard registers hide the beneficial owner behind nominees.

## Trust & verifiability
`trust: trusted` — a first-party Slovak government registry whose entries are legally verified filings; the beneficial-ownership data is authoritative rather than scraped or self-asserted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slovakia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address, dob → name, dob, address, associate, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
