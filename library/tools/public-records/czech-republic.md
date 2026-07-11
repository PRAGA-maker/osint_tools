---
id: czech-republic
name: Czech Justice Registers
description: Use when you have a `name` or `employer-org` linked to the Czech Republic and want registered companies, officers and addresses — returns `employer-org`, `associate`, `address`, `name`.
url: https://esm.justice.cz/ias/issm/rejstrik
category: public-records
path:
- public-records
bestFor: Tying a Czech company or person to registered officers and addresses via the Ministry of Justice registers.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- associate
- address
- name
status: degraded
pricing: free
costNote: Free. The public commercial register (or.justice.cz) is fully open; the beneficial-ownership register at this stub's URL (esm.justice.cz) had its public access restricted from December 2025 and now needs authentication for most users.
opsec: passive
opsecNote: Official Czech state registers; queries hit justice.cz, not the subject. The commercial register needs no login. The beneficial-ownership register now requires authenticated access (data box) for full extracts, which ties the request to a Czech-authorized identity.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Czech Ministry of Justice; authoritative primary source. Note the beneficial-ownership portal's public access is now curtailed.
missingPersonsRelevance: medium
coverage:
- cz
auth: none
api: false
localInstall: false
registration: false
aliases:
- justice.cz
- Czech commercial register
- Obchodní rejstřík
- Evidence skutečných majitelů
tags:
- companysites
- Company Related Sites
- corporate-registry
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Czech Justice Registers

> The Czech Ministry of Justice registers: the authoritative record of companies, their officers and beneficial owners — though the beneficial-ownership portal's public access is now restricted.

## When to use
You have a `name` or company `employer-org` with a Czech link and want the corporate footprint: companies a person directs or owns, co-officers (`associate`), and registered addresses. For most OSINT the free public **commercial register** is the workhorse; the separate beneficial-ownership register (this stub's URL) is now largely locked behind authentication.

## How to use it (`bestInteractionPattern`: web-manual)
1. For open access, use the public commercial register at **https://or.justice.cz/ias/ui/rejstrik** — search by company name, ID number (IČO), or person.
2. Open an entity to read officers/board, ownership structure, registered address, filings and status.
3. For beneficial-owner extracts, the register at https://esm.justice.cz/ias/issm/rejstrik now requires authenticated access (Czech data box) for most users — public access was curtailed in December 2025.
4. Note co-officers and addresses as pivots.
5. Pivot: run associates back through the register; cross-check with EU BRIS/OpenCorporates.

## Inputs → Outputs
- **In:** `name`, company `employer-org`, or IČO
- **Out:** `employer-org`, `associate` (officers), `address`, `name`; beneficial-owner data via the (restricted) esm portal
- **Empty/negative result looks like:** no matching entity/person — no Czech company under that name/ID; try Czech spelling/diacritics variants.

## Gotchas & OpSec
- Use **or.justice.cz** (commercial register) for open searching; the **esm.justice.cz** beneficial-ownership portal is access-restricted since Dec 2025.
- Czech names carry diacritics (ř, š, č) — try variants.
- A registered address is the company's, not a home.

## Overlaps ("do both")
- Pairs with OpenCorporates and the EU BRIS — use the primary Czech register to confirm aggregator data.

## Trust & verifiability
`trust: trusted` — official state registers; data is authoritative. Marked `degraded` because the beneficial-ownership portal at the stub URL no longer offers open public access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | czech-republic |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, associate, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
