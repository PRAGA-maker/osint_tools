---
id: opensanctions-org
name: Opensanctions.org
description: Use when you have a `name` (person or company) and want to check it against global sanctions, PEP, and watchlist data — returns matches with `associate`, `employer-org`, `dob`, and `address` details.
url: https://opensanctions.org/
category: public-records
path:
- public-records
bestFor: Screening a name against consolidated sanctions lists, politically-exposed-persons data, and criminal/regulatory watchlists.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
- dob
- address
status: live
pricing: freemium
costNote: Free for non-commercial/personal research via the web search; bulk data and the screening API are paid for commercial use.
opsec: passive
opsecNote: You query OpenSanctions' aggregated database, not the subject — no contact and no alert to them. Only public-record designations are returned.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-regarded open-data project aggregating 400+ official government and regulatory sources with transparent provenance for every entity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- OpenSanctions
- opensanctions.org
tags:
- sanctions
- pep
- watchlists
- public-records
source: osint4all
lastVerified: '2026-07-23'
relatedTools:
- opensanctions
---

# Opensanctions.org

> An open database of sanctions targets, politically exposed persons (PEPs), and criminal/regulatory watchlists — aggregated from hundreds of official sources into one searchable index.

## When to use
You have a `name` (individual or organisation) and want to know whether it appears on any sanctions list, is a politically exposed person, or is otherwise flagged by a government or regulator worldwide. Useful for vetting an associate or organisation in an investigation, understanding a subject's official designations, and pulling the linked identifiers (aliases, DOB, nationality, related entities) that each source records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opensanctions.org/ and use the entity search (`/research/`) for the `name`.
2. For fuzzy/structured matching, use the advanced/screening search (`/advancedsearch/`) with extra properties (DOB, nationality) to disambiguate.
3. Open a matched entity: read its designations, source list(s), aliases, `dob`, nationality, addresses, and linked `associate`/`employer-org` relationships.
4. Pivot: aliases feed further name searches; linked entities map a network; the cited source list is the authoritative record to quote.

## Inputs → Outputs
- **In:** `name` (person or company; optionally DOB/nationality to disambiguate)
- **Out:** matched entities with `associate` links, `employer-org`, `dob`, `address`, aliases, and the source designations
- **Empty/negative result looks like:** "no matches" — the name isn't in any aggregated list; this is a clearance signal for these lists only, not proof of a clean record generally.

## Gotchas & OpSec
- Name matches can be false positives (common names, transliteration variants) — always confirm with a secondary identifier (DOB, nationality, linked entity) before asserting a hit.
- Data is only as current as each source's last import; check the entity's source and update metadata.
- OpSec: **passive** — a database lookup, no exposure to the subject.

## Overlaps ("do both")
- Pairs with official government sanctions portals (OFAC, EU, UN) and corporate registries — OpenSanctions federates and cross-links them; go to the primary source to confirm a specific designation.

## Trust & verifiability
`trust: trusted` — a transparent open-data project with per-entity source provenance; verify any actioned hit against the underlying official list it cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensanctions-org |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, employer-org, dob, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
