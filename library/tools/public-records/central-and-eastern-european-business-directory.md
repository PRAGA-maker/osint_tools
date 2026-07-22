---
id: central-and-eastern-european-business-directory
name: Central & Eastern European Business Directory
description: Use when you have an `employer-org` in Central/Eastern Europe and want a company-research gateway — returns a curated link to a CEE business directory via MSU's globalEDGE.
url: https://globaledge.msu.edu/global-resources/resource/1274
category: public-records
path:
- public-records
bestFor: Reaching a vetted Central & Eastern European company directory through globalEDGE's resource catalogue.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: globalEDGE (Michigan State University) is a free academic resource portal; the CEE directory it links to may have its own access terms, but the gateway itself is free.
opsec: passive
opsecNote: You are reading an academic resource catalogue and following an outbound link — no target is contacted. Standard passive browsing; the destination directory's own site sees your visit if you click through.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: globalEDGE is a well-regarded international-business knowledge portal run by Michigan State University's CIBER; the catalogue entry is curated, though the linked third-party directory is not MSU-operated.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- global-edge-resource-directory
- globaledge
- globaledge-database-of-international-business-statistics
aliases:
- CEE Business Directory
- globalEDGE resource 1274
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Central & Eastern European Business Directory

> A curated globalEDGE catalogue entry that points to a Central & Eastern European company directory — a vetted gateway for company research in a region where finding the right register is half the battle.

## When to use
You have an `employer-org` (or a person's business tie) in Central or Eastern Europe and need a starting point for company research there. globalEDGE, Michigan State University's international-business portal, curates external resources by region; this entry is its pointer to a CEE-focused business directory. Use it to reach a regionally-scoped source rather than guessing which national register to hit first.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the globalEDGE resource page at https://globaledge.msu.edu/global-resources/resource/1274 .
2. Read the entry's description to confirm the directory's scope and coverage, then follow its outbound link to the actual CEE business directory.
3. On the destination site, search the `employer-org` name for registration, address, and contact details.
4. Pivot: take the company `address`/officers into national company registers and people-search to connect the business to individuals.

## Inputs → Outputs
- **In:** `employer-org` (company name) or a `name` linked to a CEE business
- **Out:** via the linked directory — company `employer-org` details, `address`, contacts
- **Empty/negative result looks like:** the globalEDGE link is stale/dead, or the destination directory has no match — in which case fall back to the specific national business register for the country.

## Gotchas & OpSec
- This is a **gateway/pointer**, not the dataset itself — the value depends on the third-party directory it links to, which globalEDGE does not operate and which can change or lapse.
- Coverage is broad-region ("Central & Eastern Europe"); for authoritative data, drill down to the relevant country's official register.
- OpSec: passive; only the destination site sees your click-through.

## Overlaps ("do both")
- Pair with `[[globaledge]]` and `[[global-edge-resource-directory]]` for other regional gateways, and always cross-check a hit against the country's national company register for authoritative filings.

## Trust & verifiability
`trust: trusted` — the globalEDGE catalogue is a reputable academic resource, so the pointer is trustworthy; the linked directory itself is third-party, so verify its data against an official register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | central-and-eastern-european-business-directory |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
