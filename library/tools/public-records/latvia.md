---
id: latvia
name: Latvian Register of Enterprises
description: Use when you have a `name` or `employer-org` linked to Latvia and want to find company records, directors, and registered addresses — returns officer names, business addresses, and company links.
url: https://www.ur.gov.lv/en/
category: public-records
path:
- public-records
bestFor: Looking up Latvian companies and their officers/registered addresses to link a person to a business.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Basic company search and current data are free; official certificates, full historical records, and some non-public documents are paid per-request. No account needed to run a basic search.
opsec: passive
opsecNote: Querying a public government registry is passive and anonymous; no target notification. Use standard clean-browser hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Register of Enterprises of the Republic of Latvia (Latvijas Republikas Uzņēmumu reģistrs); authoritative national company data.
missingPersonsRelevance: high
coverage:
- lv
auth: none
api: true
localInstall: false
registration: false
aliases:
- Uzņēmumu reģistrs
- Latvia company registry
- ur.gov.lv
tags:
- companysites
- Company Related Sites
- corporate-registry
- latvia
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Latvian Register of Enterprises

> Latvia's official corporate registry: link a person to Latvian companies via directorships, ownership, and registered addresses.

## When to use
You have a `name` (or a `employer-org` company name) with a Latvian connection and want to establish the person's business footprint — companies they direct or own, co-directors (`associate`s), and the registered/business `address`. This is a primary source for cross-border investigations touching Latvia and a way to surface addresses and known associates that people-search tools miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ur.gov.lv/en/ and go to the information/data search portal ("View data").
2. Search by company name/registration number, or by a person's `name` to find entities where they are an officer or beneficial owner.
3. Read the record: officers and their roles, beneficial owners, registered address, status, and links to related entities.
4. For a formal certificate or full historical/non-public documents, use the paid "Details and Payments" request flow.
5. Pivot: co-officers become `associate` leads; the registered `address` feeds address-based lookups; company links map the person's network.

## Inputs → Outputs
- **In:** `name` or `employer-org` (Latvian nexus)
- **Out:** `employer-org` company records, officer/owner `name`s, registered `address`, co-officer `associate`s
- **Empty/negative result looks like:** no matching entity or person — the individual may have no Latvian corporate role, or be listed only under a transliterated/Latvian spelling of their name (try diacritic variants).

## Gotchas & OpSec
- Names may be recorded in Latvian transliteration; try alternate spellings and include the personal ID format where known.
- Full historical filings and certified extracts are behind a per-document fee; the free tier gives current data.
- OpSec: passive; the registry does not notify the entities you look up.

## Overlaps ("do both")
- Pairs with pan-European registry aggregators and other national registries for subjects with companies across borders — do both, because each national register only holds its own jurisdiction's filings.

## Trust & verifiability
`trust: trusted` — first-party data from the Republic of Latvia's official Register of Enterprises.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | latvia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
