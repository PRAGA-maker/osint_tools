---
id: ebra-be
name: ebra.be (EBRA Worldwide Registers)
description: Use when you have an `employer-org` or `name` and need the official company register for a given country — returns a directory link toward employer-org, address, and director-name data.
url: https://ebra.be/worldwide-registers/
category: public-records
path:
- public-records
bestFor: A country-by-country directory of official government business/company registries worldwide — the jump-off point to authoritative corporate records.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: The EBRA directory page is free; it links out to each country's official registry, some of which charge per search or per document.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about your target. OpSec considerations shift to the individual national registry you follow through to — some (e.g. UK Companies House) are fully anonymous, others may require an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: EBRA (European Business Registry Association AISBL) is the official association of European and international business registers; its directory links to genuine government registries, not scrapers.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
- cyprusregistry-com
aliases:
- EBRA
- European Business Registry Association
- worldwide company registers
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ebra.be (EBRA Worldwide Registers)

> The European Business Registry Association's directory of official company registers by country — a trusted map to ~150+ government corporate registries worldwide.

## When to use
You have an `employer-org` (company name) or a `name` you believe is a company director/officer, and you need the **authoritative** registry for the relevant jurisdiction rather than a third-party aggregator. Use EBRA when your target's corporate footprint is in a country you don't already know the registry for — it routes you straight to the official source, where director names, registered addresses, and filings live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ebra.be/worldwide-registers/ and use the map or the alphabetical country list.
2. Click the country where the company is (or is likely) registered.
3. You're directed to that jurisdiction's official business registry website.
4. Search there by company name or officer name per that registry's interface.
5. Read the official record: `employer-org` details, registered `address`, director/officer `name`s and, in many jurisdictions, beneficial-owner data. Pivot officer names into people-search; pivot addresses into property/records tools.

## Inputs → Outputs
- **In:** `employer-org` / `name` / `address` (to search once you reach the right registry)
- **Out:** a link to the official registry, which then yields `employer-org`, registered `address`, and director/officer `name`s
- **Empty/negative result looks like:** EBRA lists no registry for a jurisdiction, or the linked registry is offline/limited — small territories may lack an online registry; fall back to an aggregator like [[opencorporates]].

## Gotchas & OpSec
- EBRA is a *directory*, not a search engine — it doesn't hold company data itself; the actual lookup happens on the national registry.
- National registries vary wildly in cost, language, and access rules; some charge per document, some require an account.
- OpSec: passive at the directory stage; assess anonymity on the specific registry you land on.

## Overlaps ("do both")
- Pairs with [[opencorporates]] (cross-jurisdiction aggregator that's faster for a first sweep) and jurisdiction-specific tools like [[cyprusregistry-com]] — use EBRA to find the authoritative source, then aggregators to correlate across borders.

## Trust & verifiability
`trust: trusted` — EBRA is the official association of business registers, and every link points to a genuine government registry. The directory itself is authoritative for *where* to look; verifiability of the data rests with each national registry (which is the primary source).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ebra-be |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
