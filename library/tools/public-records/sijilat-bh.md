---
id: sijilat-bh
name: sijilat.bh (Bahrain Commercial Registry)
description: Use when you have a company `name`/`employer-org` (or owner name) in Bahrain and want the official commercial-registration record — returns registered business name, activity, address and status.
url: https://www.sijilat.bh/public-search-cr/search-cr-2.aspx
category: public-records
path:
- public-records
bestFor: Verifying a Bahraini company's registration and pulling its official activity, location and status to link a person to a business.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public commercial-registry search operated by Bahrain's Ministry of Industry & Commerce. No account needed for public searches (account only for business-management services).
opsec: passive
opsecNote: Passive — you query an official government registry, not the subject. No notification is sent. Ordinary browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Bahrain government commercial-registration system (Sijilat, Ministry of Industry & Commerce) — authoritative for registered Bahraini entities.
missingPersonsRelevance: high
coverage:
- bh
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Sijilat
- Bahrain commercial registry
- sijilat.bh
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# sijilat.bh (Bahrain Commercial Registry)

> Bahrain's official commercial-registration search (Sijilat) — the authoritative way to verify a Bahraini company and tie a subject to a registered business.

## When to use
Your investigation touches Bahrain and you have a company `name`/`employer-org` (or want to confirm a business a subject claims to run/work for). Sijilat's public search returns the official registration: registered name, activity classification (ISIC4), location/area, and status. Use it to confirm an employer, place a person geographically via a business address, or validate a commercial claim.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sijilat.bh/public-search-cr/search-cr-2.aspx.
2. Search by business `name`, ISIC4 activity code, activity/sector, and/or governorate (Muharraq, Manama, Northern/Central/Southern).
3. Read the output: matching registered entities with official name, activity, area/address, and registration status. Related searches cover agency registration and authorized dealers.
4. Pivot: a confirmed company address (`address`) places associated people geographically; the registered name/entity feeds cross-border corporate and sanctions checks; activity/sector corroborates a claimed occupation.

## Inputs → Outputs
- **In:** `employer-org`/company `name` (or activity/area filters)
- **Out:** `employer-org` (official registered entity), `address` (registered area/location), `name`
- **Empty/negative result looks like:** no matching registration — the business may be unregistered, dissolved, or named differently. Try the trade name and activity/area filters before concluding it doesn't exist.

## Gotchas & OpSec
- Public search exposes registration and activity/location; detailed ownership/officer data may require the authenticated business portal.
- Bahrain-only — irrelevant for entities registered elsewhere.
- OpSec: fully passive; official government registry.

## Overlaps ("do both")
- Pairs with international company registries and corporate-aggregator tools — Sijilat is authoritative for Bahrain; use the aggregators to connect a Bahraini entity to cross-border structures and officers.

## Trust & verifiability
`trust: trusted` — first-party Bahraini government commercial-registration system, authoritative for registered entities in the Kingdom.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sijilat-bh |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
