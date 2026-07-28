---
id: search-for-a-federal-corporation
name: Search for a Federal Corporation (Corporations Canada)
description: Use when you have a company name or director/officer name in Canada and want the official federal incorporation record — returns employer-org status, address, and named directors/officers.
url: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?locale=en_CA
category: public-records
path:
- public-records
bestFor: Confirming a Canadian federal corporation and pulling its status, registered office, and directors from the official registry.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free official government registry (Corporations Canada / ISED); no account needed to search.
opsec: passive
opsecNote: A passive query against a public government registry; nothing is disclosed to the company and no active probing occurs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Innovation, Science and Economic Development Canada (ISED) / Corporations Canada — the authoritative federal corporate registry.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-business-research
- canadian-copyrights-database
- canadian-department-of-finance
- canadian-importers-database
- canadian-intellectual-property-office
- canadian-trademarks-database
- completed-access-to-information-requests
- federal-corporation-search-canada
- gov-data-canada
- government-of-canada-open-data
aliases:
- Corporations Canada search
- Federal Corporation Search
tags:
- company-registry
- public-records
- canada
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Search for a Federal Corporation (Corporations Canada)

> The official Corporations Canada registry — confirm a federal corporation and see its status, registered office, and the people listed as directors/officers.

## When to use
You have a Canadian federally-incorporated `employer-org` (or a person you suspect is a director/officer) and want the authoritative record: does it exist, is it active/dissolved, where is its registered office, and who are the named directors? This connects a company to real people (an `associate`/business link for a subject) and vice versa. It covers **federal** corporations only — provincial ones need the relevant provincial registry or Canada's Business Registries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search page (ised-isde.canada.ca — the former ic.gc.ca link now redirects here).
2. Search by corporate name, corporation number, or business number (BN); filter by province of registered office, status, or governing act.
3. Open the corporation's profile to read: status (active/dissolved), registered office `address`, governing legislation, and the list of **directors** (`name`s → potential `associate` links).
4. Note incorporation/annual-filing dates to gauge whether the entity is live and compliant.
5. Pivot: a director `name` → people-search and other directorships; the office `address` → address-based records.

## Inputs → Outputs
- **In:** an `employer-org` name / corporation number / BN, or a director `name`.
- **Out:** corporation status, registered office `address`, governing act, and named directors/officers (`associate`).
- **Empty/negative result looks like:** "no results" — the entity may be provincially (not federally) incorporated, dissolved and purged, or spelled differently; try Canada's Business Registries or a provincial registry.

## Gotchas & OpSec
- **Federal only** — a huge share of Canadian companies are provincial and won't appear here.
- Director lists reflect the latest filing; recent changes may lag, and dissolved companies show historical data.
- The legacy ic.gc.ca URL redirects to the ISED domain — use the current link to avoid confusion.

## Overlaps ("do both")
- Pairs with provincial registries and Canada's Business Registries (aggregator): use this for federal corps, those for provincial ones — together they cover the whole country.

## Trust & verifiability
`trust: trusted` — the authoritative federal registry operated by ISED; records are official and directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-for-a-federal-corporation |
