---
id: osint-tools-bulgaria
name: OSINT-Tools-Bulgaria
description: Use when a subject, company or vehicle ties to Bulgaria and you need country-specific registries and search resources — returns a curated directory of Bulgarian people/company/geo OSINT sources.
url: https://github.com/LinaYorda/OSINT-Tools-Bulgaria
category: public-records
path:
- public-records
bestFor: A starting directory of Bulgaria-specific registries and OSINT sources (people, companies, geo).
selectorsIn:
- name
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Free open GitHub repository (curated list); no account needed to read.
opsec: passive
opsecNote: Reading a GitHub resource list is passive. The linked Bulgarian registries themselves vary in OpSec — some may require accounts or log queries; assess each source individually when you follow a link, and use a sock puppet for any that need login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained curated list (LinaYorda); it points to third-party Bulgarian sources whose quality/availability the author explicitly notes is uneven — treat as a signpost, verify each source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osinttools-linayorda
aliases:
- OSINT Tools Bulgaria
- LinaYorda Bulgaria OSINT
tags:
- public-records
- bulgaria
- curated-directory
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# OSINT-Tools-Bulgaria

> A community-curated GitHub list of Bulgaria-specific OSINT resources — the go-to signpost when a case touches Bulgaria and you need local registries rather than global tools.

## When to use
Your subject, a company, a phone number, or a vehicle has a Bulgarian connection and generic global tools fall short. This repo collects Bulgaria-specific sources — government/commercial registers, phone registries, map/DNS/IP utilities, and personal-info portals — so you can jump straight to the right local database instead of guessing. It's a directory, not a lookup itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/LinaYorda/OSINT-Tools-Bulgaria and read the README.
2. Find the relevant section (people, companies, geographic/technical) for your selector.
3. Follow a linked Bulgarian source and run your actual query there (`name`, company, etc.).
4. Heed the author's caveat: many Bulgarian government registers are incomplete or not fully electronic, so cross-check across several listed sources.
5. Pivot: a company register hit yields officers/`associate` links; a people portal yields contact/address leads to corroborate elsewhere.

## Inputs → Outputs
- **In:** `name` / `employer-org` (applied at the *linked* Bulgarian source, not here)
- **Out:** none directly — it returns *pointers* to sources; the data comes from the sites it links
- **Empty/negative result looks like:** no listed source covers your exact need — expected given uneven Bulgarian register coverage; supplement with global tools and official EU-level registers.

## Gotchas & OpSec
- It's a curated list, so freshness depends on the maintainer — a linked source may have moved or died; verify before relying on it.
- Bulgarian government data is often incomplete/offline per the author's own note — don't treat an empty local register as definitive.
- OpSec: reading the list is passive; the *linked* sources have their own login/logging characteristics — check each.

## Overlaps ("do both")
- Pairs with EU-wide company registers (e.g. the Business Registers Interconnection / national commercial register) and global people-search — use this list for the Bulgaria-specific entry points, then corroborate in cross-border sources.

## Trust & verifiability
`trust: community` — a helpful community directory whose value is the curation; every source it points to is third-party and must be verified independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tools-bulgaria |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
