---
id: rpx-corp
name: RPX Corp
description: Use when you have a company/inventor `name` or patent number and want US patents, applications, and district-court patent litigation tied to an entity — returns patents, cases, and party `employer-org` records.
url: http://www.rpxcorp.com
category: search-engines
path:
- search-engines
bestFor: Free search of US patents, applications, and all district-court patent litigation since 2000, linked to owning/litigating entities.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- document-id
- associate
status: live
pricing: free
costNote: RPX Search (patents.rpxcorp.com / search.rpxcorp.com) is free with no login for public patent/litigation/entity data. Only RPX's premium client products (Empower, member portal) are paid — you do not need them for the public search.
opsec: passive
opsecNote: Searching the public patent/litigation index reveals nothing to any subject and needs no account. Passive. Note that patents and court filings are inherently public records.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RPX Corporation is an established patent-risk firm; RPX Search draws on US patent office and PACER-style district-court records, so the underlying data is authoritative public information.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- RPX Search
- rpxcorp patent search
tags:
- patents
- litigation
- entity-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# RPX Corp

> A free public search engine for US patents, patent applications, and every district-court patent lawsuit since 2000 — with the owning and litigating entities linked together.

## When to use
You want to tie a person or company to intellectual property or patent litigation: is a subject named as an inventor, does their company own patents, or is an entity a plaintiff/defendant in patent suits? RPX Search connects patents, applications, and court cases to the parties involved, so a `name`/`employer-org` yields inventions, assignees, co-inventors (`associate`s), and litigation history — useful for establishing a subject's professional footprint, business relationships, or corporate ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the free RPX Search (patents.rpxcorp.com — reachable from rpxcorp.com). No login is required for public search.
2. Search by inventor/company `name`, patent number, or entity.
3. Read results: matching patents/applications (with inventors and assignees) and any district-court patent litigation involving the party.
4. Pivot: co-inventors and assignee companies (`associate`/`employer-org`) feed people- and business-search; a patent number links out to the full USPTO record; litigation names other parties and law firms.

## Inputs → Outputs
- **In:** inventor/company `name`, `employer-org`, or a patent number (`document-id`).
- **Out:** patents/applications, assignee/owner `employer-org`, co-inventor `associate`s, litigation parties and case history.
- **Empty/negative result looks like:** no patents or cases for the name — most people hold none; absence says nothing beyond "not a patenting/litigating party under that name."

## Gotchas & OpSec
- Scope is US patents/applications and US district-court patent litigation — not general civil suits, and not non-US IP.
- Name matches can collide (common names, name variants) — confirm the entity via assignee/company details before attributing.
- The free RPX Search is distinct from RPX's paid member products; you only need the public search here.

## Overlaps ("do both")
- Cross-check inventors/assignees against USPTO/Google Patents and general business-registry tools to confirm identity and corporate structure.

## Trust & verifiability
`trust: trusted` — built on authoritative public patent-office and court records. RPX's aggregation is reliable; verify a critical patent or case against the primary USPTO/court record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rpx-corp |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
