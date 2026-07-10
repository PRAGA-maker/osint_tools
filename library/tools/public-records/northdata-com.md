---
id: northdata-com
name: northdata.com
url: https://www.northdata.com/
category: public-records
path:
- public-records
description: Use when you have a `name` or `employer-org` and want European company/officer records — returns director/shareholder names, registered addresses and corporate links.
bestFor: Tracing a person through European trade registers — which companies they direct, own or share an address with.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Free web search exposes basic publicly-available register data (companies, officers, links); Power Search, network analytics and bulk/machine-readable data are subscription-based.
opsec: passive
opsecNote: Passive read of published trade-register and filings data; the subject is not contacted and receives no notification. No login is needed for basic search, so lookups are low-attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official European trade registers, gazettes, and patent/trademark registries; source-cited primary data rather than self-reported profiles.
missingPersonsRelevance: high
coverage:
- eu
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- North Data
- northdata European company search
tags:
- companysites
- Company Related Sites
- corporate-registers
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# northdata.com

> A European companies search engine that turns a person's name into the companies they direct or own, their co-officers, and the addresses tying them together.

## When to use
You have a person's `name` (or a company / `address`) and want to map their corporate footprint across Europe — directorships, shareholdings, co-directors, and shared registered addresses. Strong for building an associate network and confirming a real, address-anchored identity when someone appears in business filings. Covers ~24 European countries including UK, Germany, France, Spain, Netherlands and Ireland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.northdata.com/ and use Quick Search.
2. Enter the person's `name` (or a company name / `address`).
3. On a person hit, read the profile: linked companies, roles/dates, co-officers, and the registered addresses used.
4. Follow the network graph to co-directors and shared addresses to surface `associate` links.
5. Pivot: a registered `address` feeds electoral/property searches; co-officer `name`s feed further register lookups or people-search tools.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`
- **Out:** officer/shareholder `name`s, `employer-org` links, registered `address`, `associate` (co-directors, shared-address parties)
- **Empty/negative result looks like:** no company associations found — the person may simply hold no European directorships/shareholdings, not that they don't exist. Common names return many candidates; disambiguate by address/date.

## Gotchas & OpSec
- Common names collide; use an address, company or date to disambiguate the right individual.
- Deep network analytics and bulk data are paid (Power Search / API); the free tier is search + basic profile.
- OpSec: fully passive register aggregation — no login required, no subject notification.

## Overlaps ("do both")
- Pairs with `[[opencorporates-com]]`-style registries and national company registers — North Data adds cross-country linking and network graphs that single-jurisdiction registers miss.

## Trust & verifiability
`trust: trusted` — data is compiled from official European trade registers, gazettes and IP registries with sources cited per record, so it is primary-source grade; verify the individual match by address/role before relying on links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | northdata-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
