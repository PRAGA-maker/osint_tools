---
id: officialusa-usa-official
name: OfficialUSA / USA-Official
description: Use when you have a US `name` and want a free directory-style lookup — returns associated `address`es, `phone`s, and possible relatives/`associate`s.
url: https://www.officialusa.com/
category: people-search
path:
- people-search
bestFor: Free first-pass US people lookup by name for addresses, phones, and relative links before paying for a deeper report.
selectorsIn:
- name
selectorsOut:
- name
- address
- phone
- associate
status: live
pricing: freemium
costNote: Free directory listings and basic results; deeper "background report" pages upsell paid third-party services.
opsec: passive
opsecNote: Passive — you query a data-broker aggregator, not the person; they are not notified. The broker logs your query. Note it is a data-broker with an opt-out process; treat its data as scraped/aggregated, and only use for legitimate investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A US data-broker/directory aggregator; data is compiled from public and commercial sources and is often stale or conflated — a lead source, not authoritative.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OfficialUSA
- USA-Official
tags:
- people-search
- directory
- data-broker
source: inteltechniques-tools
lastVerified: '2026-07-19'
enrichment: full
---

# OfficialUSA / USA-Official

> A free US people-directory aggregator — a quick, no-cost first pass for a name's addresses, phones, and likely relatives.

## When to use
You have a US person's `name` and want a fast, free set of leads — current/prior `address`es, `phone`s, and possible relatives/`associate`s — to seed a search before committing to a paid people-search report. Best as a starting point, corroborated elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.officialusa.com/ and use the people/name search (state filters help disambiguate common names).
2. Enter the `name`; add a state/city if known.
3. Read the output: matching individuals with associated addresses, phone numbers, and linked relatives. Some detail pages push a paid third-party report — the free listing is usually enough for leads.
4. Pivot: run the surfaced address/phone/relatives through authoritative sources (voter records, county assessors) and a second people-search to confirm.

## Inputs → Outputs
- **In:** a US `name` (optionally + location)
- **Out:** `address`es, `phone`s, `name` variants, and relative/`associate` links
- **Empty/negative result looks like:** no matches for a name can mean a common-name mismatch, an opt-out, or thin data — try alternate spellings and a second broker before concluding.

## Gotchas & OpSec
- Data-broker data is frequently outdated or conflates different people — verify before acting.
- The site upsells paid reports; you rarely need them for lead generation.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Do both with another free people-search and authoritative public records — brokers disagree, so triangulate addresses/relatives across sources.

## Trust & verifiability
`trust: community` — aggregated broker data; treat every field as a lead to confirm against an authoritative record, not as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | officialusa-usa-official |
| category | people-search |
| selectorsIn → selectorsOut | name → name, address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
