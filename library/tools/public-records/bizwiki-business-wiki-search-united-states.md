---
id: bizwiki-business-wiki-search-united-states
name: Bizwiki Business Wiki Search (United States)
description: Use when you have a US business `name` and a location and want its listing — a free crawler-built directory; returns `employer-org` details with `address` and `phone`.
url: https://www.bizwiki.com
category: public-records
path:
- public-records
bestFor: Free US business-directory lookup by company name and location, returning address, phone, and category.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free directory; listings are bot-generated. Owners can claim/update listings for free.
opsec: passive
opsecNote: Passive — you browse a public, crawler-built business directory, transmitting nothing about a personal target. Relevant only when a subject is tied to a US business.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large US business directory built by an automated crawler; coverage is broad but listings can be stale, auto-generated, or inaccurate — a lead source, not authoritative.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Bizwiki
tags:
- toddington
- company-search
- business-directory
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bizwiki Business Wiki Search (United States)

> A free, crawler-built US business directory — look up a company by name and location for its address, phone, and category.

## When to use
Your subject is linked to a US business and you want the listing: `address`, `phone`, category, and any web presence. Because Bizwiki is bot-generated it often has entries even for small businesses, giving you a lead to bridge business→person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bizwiki.com/.
2. Search by company `name` and location (city/state).
3. Read the output: matching `employer-org`s with `address`, `phone`, category, and links.
4. Pivot: use the business address/phone to connect it to the person; confirm against the state business registry (Secretary of State) and a people-search.

## Inputs → Outputs
- **In:** a business `name` + US location
- **Out:** `employer-org` listing with `address`, `phone`, category
- **Empty/negative result looks like:** no listing means the crawler hasn't indexed it (small/new/offline business) — check the SoS registry and other directories.

## Gotchas & OpSec
- Auto-generated listings can be outdated or conflated — verify before relying on them.
- Surfaces businesses, not people directly; bridge to the person yourself.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Do both with the state Secretary of State business registry — Bizwiki gives a quick listing; the registry gives authoritative registration/officers.

## Trust & verifiability
`trust: community` — crawler-built directory; treat every field as a lead to confirm against an official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bizwiki-business-wiki-search-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
