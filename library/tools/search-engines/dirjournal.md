---
id: dirjournal
name: DirJournal
description: Use when you have a business `name` or category and want a curated directory listing — returns verified business profiles with contact/address details.
url: https://www.dirjournal.com/
category: search-engines
path:
- search-engines
bestFor: Browsing a human-verified business directory by name or category for contact and address details.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- domain
status: live
pricing: free
costNote: Free to browse and search (no signup); only listing a business costs money. Ad/listing-supported.
opsec: passive
opsecNote: A public business directory — you look up companies, not private individuals, and no subject is notified. Fully passive browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated directory (since 2007, rebuilt 2026) whose entries are editor-verified against an audit; useful but a secondary/aggregated source, not an official registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- DirJournal
- dirjournal.com
tags:
- business-directory
- local-search
- reference
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# DirJournal

> A human-verified business/local directory — search a company by name or category to get a vetted profile with contact, website, and address details.

## When to use
You have a business `name` or an `employer-org` connected to a subject and want a quick, curated profile: website (`domain`), `address`, category, and contact info. DirJournal catalogs tens of thousands of editor-verified entities across industries (legal, financial, healthcare, tech, SaaS, marketing). It's a secondary corroborator — confirming a business is real and pulling its public contact block — rather than an authoritative registry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dirjournal.com/ (free to browse, no signup).
2. Search by business `name`, or browse by industry category.
3. Open a listing: website `domain`, `address`, category, and contact details.
4. Corroborate against an official source (corporate registry, the company's own site) before relying on it.
5. Pivot: the `domain`/`address` feeds domain-OSINT and mapping; the business ties back to your subject.

## Inputs → Outputs
- **In:** business `name` / category (`employer-org`)
- **Out:** `employer-org` profile with `address`, website `domain`, contact info
- **Empty/negative result looks like:** no listing — the directory is curated and finite, so most small/local businesses won't appear; absence means "not curated here," not "doesn't exist."

## Gotchas & OpSec
- **Curated and limited** — coverage is selective (tens of thousands of entities), so it's a spot-check, not comprehensive.
- Secondary source — verify contact/address against the business's own site or an official registry.
- OpSec: **passive** — public directory, no subject contact.

## Overlaps ("do both")
- Complements official corporate registries and mapping tools — DirJournal gives a quick curated contact block; confirm the entity and its officers via an authoritative registry, and verify the address on a map.

## Trust & verifiability
`trust: community` — a real, editor-verified directory, but aggregated/secondary; treat listings as leads to confirm at the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dirjournal |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
