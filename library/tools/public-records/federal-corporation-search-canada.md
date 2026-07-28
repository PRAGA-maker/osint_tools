---
id: federal-corporation-search-canada
name: Federal Corporation Search (Canada)
description: Use when you have a Canadian company/business `name` or a person's `name` and want federally-incorporated company records and directors — returns `employer-org`, `address`, `associate`.
url: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html
category: public-records
path:
- public-records
bestFor: Confirming a Canadian federal corporation and pulling its directors, status, and registered office.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free government search — corporation profiles, director names, and registered office are viewable at no cost.
opsec: passive
opsecNote: Querying Corporations Canada does not notify the company or its directors; searches are anonymous and no account is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Innovation, Science and Economic Development Canada (Corporations Canada) — the official federal corporate registry.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-intellectual-property-office
- canadian-trademarks-database
- canadian-business-research
- canadian-copyrights-database
- canadian-department-of-finance
- canadian-importers-database
- completed-access-to-information-requests
- gov-data-canada
- government-of-canada-open-data
- search-for-a-federal-corporation
aliases:
- Corporations Canada
- Federal Corporation Search
tags:
- toddington
- curated-directory
- company-search
- corporate-registry
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Federal Corporation Search (Canada)

> Corporations Canada's official register of federally-incorporated companies — turn a company or person `name` into the entity, its directors, status, and registered office, all free.

## When to use
Your subject is tied to a Canadian federally-incorporated company and you want to confirm it and see who runs it. Unlike provincial registries, this covers CBCA federal corporations. It's directly useful because director names and the registered office address are shown free — so a company links to a set of `associate` people and an `address`, and a person's name can be searched to find corporations they direct. Relevant when a missing person or associate incorporated, directed, or worked for a Canadian federal company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html.
2. Search by Corporate Name, Corporation Number, or Business Number (BN); or search a person's name to find corporations linking to it.
3. Open the corporation profile: status (active/dissolved), registered office `address`, and the list of current/former directors.
4. Read the output: directors are named `associate` leads; the registered office is an `address` lead; status/dates build a timeline.
5. Pivot: a director name feeds people-search; the registered office feeds property/mapping tools; cross-check provincial registries for non-federal entities.

## Inputs → Outputs
- **In:** `name` (person or corporation), `employer-org`, or a corporation/business number
- **Out:** `employer-org` (the corporation), `address` (registered office), `associate` (directors)
- **Empty/negative result looks like:** no federal corporation matches — the entity may be provincially incorporated (search the relevant province) or not a corporation at all; absence here isn't proof it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none; fully free and open.
- OpSec: passive and anonymous.
- Federal only: many Canadian businesses are provincially incorporated and won't appear — pair with provincial corporate registries.

## Overlaps ("do both")
- Pairs with provincial corporate registries and `[[canadian-trademarks-database]]` — this covers federal corporations and their directors, while provincial registries and IP databases catch entities and assets this misses. Do both to fully map a Canadian business subject.

## Trust & verifiability
`trust: trusted` — the official federal corporate registry run by ISED/Corporations Canada, so corporation status and director data are authoritative primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-corporation-search-canada |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
