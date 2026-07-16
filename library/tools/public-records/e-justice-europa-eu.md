---
id: e-justice-europa-eu
name: EU e-Justice — Land Registers
description: Use when you have a `name` or `address` and a property question in an EU country and want the official routing to that country's land/property registry — returns links to ownership, address and property-holder (employer-org) records.
url: https://e-justice.europa.eu/109/EN/land_registers_in_eu_countries
category: public-records
path:
- public-records
bestFor: Finding the official national land/property registry for any EU country to look up property ownership.
selectorsIn:
- name
- address
selectorsOut:
- address
- name
- employer-org
status: live
pricing: free
costNote: The e-Justice portal directory is free. The national registries it points to vary — some allow free index searches, others charge per-document or require a professional/registered account.
opsec: passive
opsecNote: Browsing the EU portal is passive and leaks nothing about the subject. OpSec and any login/fees apply at the destination national registry, which you should assess per country. No login on the portal itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The European e-Justice Portal is the official EU-operated navigation hub; the registries it links to are national government authorities. Authoritative routing to authoritative sources.
missingPersonsRelevance: high
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- European e-Justice Portal land registers
- e-justice.europa.eu
tags:
- propertysites
- land-registry
- property-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- european-union-open-data-portal
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
---

# EU e-Justice — Land Registers

> The EU's official portal for finding each member state's land/property registry — a navigation hub, not a database, that routes you to the authoritative national source for ownership records.

## When to use
You have a `name` or `address` and a property-ownership question tied to an EU country, and you need the correct official registry rather than guessing per country. Land/property ownership is a powerful locate-and-assets signal; this is the reliable first step to reach the right national register (Grundbuch, cadastre, Land Registry, etc.).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://e-justice.europa.eu/109/EN/land_registers_in_eu_countries.
2. Select the relevant EU country (flag/link) to read how its land registry works and access it.
3. Follow through to that national registry and search by owner `name` or property `address` per its rules.
4. Note the destination's access model — some are free index searches, others charge per extract or require a registered/professional account.
5. Pivot: confirmed ownership ties a person to an `address` and sometimes a holding `employer-org`/company; feed the address into people-search and the company into corporate-registry checks.

## Inputs → Outputs
- **In:** `name` or property `address` (used at the destination registry)
- **Out:** routing to ownership records revealing `address`, owner `name`, and holding-company `employer-org` — via the national registry, not the portal itself
- **Empty/negative result looks like:** the portal always shows its country directory; empty results happen only at the destination registry. Many EU registries restrict owner-name searches (address-only lookups) for privacy — a "search by name not permitted" is common and expected.

## Gotchas & OpSec
- The portal returns nothing about a person by itself — record the destination national registry as your source.
- Access models vary widely by country; several EU registries do not allow searching by owner name at all, only by parcel/address.
- Language: destination registries are often in the national language — plan for translation.
- OpSec: passive at the portal; assess each national registry separately.

## Overlaps ("do both")
- Pairs with EU corporate registries (e.g. the Business Registers Interconnection / national company registers) — property records and company records together map a subject's assets and roles.

## Trust & verifiability
`trust: trusted` — an official EU-operated portal linking to authoritative national government registries; the ownership data itself comes from those first-party registers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | e-justice-europa-eu |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
