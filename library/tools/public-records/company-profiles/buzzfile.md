---
id: buzzfile
name: Buzzfile
description: Use when you have an `employer-org` or a person's `name` tied to a US business and want its profile — returns `employer-org` details, `address`, and executive `name`s.
url: https://www.buzzfile.com/Home/Basic
category: public-records
path:
- public-records
- company-profiles
bestFor: Quick US business lookup by company name, location, or executive to get address, size, and key people.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Basic company search and core profile fields are free/no-login; deeper features (industry lists, list-builder, some contact detail) require a paid subscription.
opsec: passive
opsecNote: Queries run through Buzzfile's servers against aggregated public/business data; the target isn't contacted. No login needed for basic lookups, so no account of yours is tied to the search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial business-data aggregator compiling public records and firmographics; useful as a lead but figures (revenue/employee estimates) are modelled, not filed, so verify against a primary registry.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- international-registries
aliases:
- buzzfile.com
tags:
- company
- corporate
- employer
- business-directory
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Buzzfile

> A fast US business directory: name a company (or an executive) and get its address, size, industry, and named people — a lead-generator to corroborate with primary sources.

## When to use
You have an `employer-org` a subject claims to work for/own, or a `name` you suspect is a business owner or executive, and you want a quick profile: registered/operating `address`, employee count, industry (SIC/NAICS), and associated people. Handy for tying a person to a workplace, mapping colleagues, or confirming a business a subject mentioned actually exists in the US.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.buzzfile.com/Home/Basic.
2. Enter the company name (optionally add city/state/zip/county), or search an executive/person name.
3. Open the profile: address, employee/revenue estimates, industry codes, and a link to "all companies at that location."
4. Note that the free view covers the core profile; industry lists and some contact fields prompt a sign-in / paid tier.
5. Pivot: an executive `name` feeds people-search; the "companies at this location" link surfaces co-located related businesses; verify the entity in an official registry.

## Inputs → Outputs
- **In:** `employer-org` (company name), executive `name`, and/or `address`/location
- **Out:** business profile — `employer-org` details, `address`, executive/contact `name`s, employee/revenue estimates, industry codes
- **Empty/negative result looks like:** no matching company (common for very small/unregistered or non-US businesses), or a bare stub with the deeper fields locked behind the paywall.

## Gotchas & OpSec
- Human-in-the-loop: none for basic search; the paywall gates advanced features (payment-wall-partial applies only to those, so recorded as no HIL for the free path).
- Revenue and employee numbers are **modelled estimates**, not filed figures — treat as approximate.
- Coverage is US-only; for foreign companies route through [[international-registries]] instead.
- OpSec: passive; no login required for the free lookups, so nothing ties the search to you.

## Overlaps ("do both")
- Pairs with [[international-registries]] — Buzzfile is the quick US aggregate; the registry index gives you the authoritative, primary-source filing to confirm what Buzzfile modelled.

## Trust & verifiability
`trust: community` — a commercial aggregator, useful for leads and firmographics, but its estimates and compiled contacts should be corroborated against an official company registry or filing before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buzzfile |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name, address → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
