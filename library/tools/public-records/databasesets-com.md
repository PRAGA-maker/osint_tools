---
id: databasesets-com
name: databasesets.com
description: Use when you have an `employer-org`/company `name` and want registry details, addresses, and corporate credit info — returns company address and organization records.
url: https://user.databasesets.com/index/index/intro.html
category: public-records
path:
- public-records
bestFor: Cross-border company lookups and corporate credit reports across 200+ countries, with a focus on Asia-Pacific registries.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Company name search and basic directory hits are free; full corporate credit reports and detailed registry documents are paid, per-report purchases.
opsec: passive
opsecNote: Searching a company name is passive and does not touch the subject. Buying a report requires registration/payment that identifies you — use a business alias and a dedicated payment method if you must purchase.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial third-party aggregator of company registry/credit data; source and freshness of records are not independently disclosed, so treat specifics as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- DatabaseSets
- databasesets
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# databasesets.com

> A commercial company-data portal for corporate lookups and credit reports across 200+ countries — useful for tying a person to an employer, director role, or registered business address.

## When to use
You have an `employer-org` or a company `name` connected to your subject (an employer, a business they founded, a company on a document) and want the registered address, jurisdiction, and corporate profile — especially for Asia-Pacific entities (Singapore, Japan, Australia and others) where free registries are patchy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site in a sock-puppet browser (the domain is heavily bot-filtered; a normal logged-out browser session works, automated fetches get 403).
2. Enter the company `name` in the search box; optionally filter by country to disambiguate common names.
3. Read the free directory hits: registered company name, country, and summary. A registered `address` and organization identifiers may appear before the paywall.
4. Decide whether the paid corporate credit report is worth buying for directors/officers detail.
5. Pivot: a registered address or director name feeds people-search and associate-mapping; the confirmed `employer-org` corroborates a subject's stated workplace.

## Inputs → Outputs
- **In:** `employer-org` / company `name` (optionally + country)
- **Out:** `employer-org` registry record, registered `address`, entity `name` variants
- **Empty/negative result looks like:** no matching company for that name/country — either the entity isn't in their coverage or the name/spelling is off; try alternate legal-name forms.

## Gotchas & OpSec
- This is company data, not a people-finder — it helps with the employer/director angle of an investigation, not direct personal locating.
- Paywall: rich detail (directors, financials) sits behind per-report purchase; the free layer is a directory teaser.
- Bot protection returns 403 to scripts/crawlers — interact in a real browser.
- Data provenance is undisclosed; corroborate any address or officer name against an official registry (Companies House, ACRA, etc.).

## Overlaps ("do both")
- Pairs with official national registries because databasesets aggregates many countries in one search but an official registry is the authoritative source you should confirm a hit against.

## Trust & verifiability
`trust: unverified` — commercial reseller of registry/credit data with no disclosed sourcing or update cadence; good for lead generation, not for standalone proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | databasesets-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
