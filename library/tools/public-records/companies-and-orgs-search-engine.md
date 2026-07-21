---
id: companies-and-orgs-search-engine
name: Companies & Orgs Search Engine
description: Use when you have a company or organization `name` (or an `employer-org` lead) and want a Google Custom Search Engine tuned to corporate/org registries and directories — returns company records and links.
url: https://cse.google.com/cse?cx=72ea9d8cfefc142d3
category: public-records
path:
- public-records
bestFor: A pre-tuned Google Custom Search Engine focused on company and organization registries/directories.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account or payment required.
opsec: passive
opsecNote: This is a Google-hosted search box; queries go to Google like any web search. Passive with respect to the target, but log in to a sock-puppet Google account (or use a clean session) if you don't want the searches tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-built Google CSE; its value depends entirely on the (opaque, unverifiable) list of sites its creator configured, and that config can silently degrade or narrow over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Companies and Orgs CSE
tags:
- google-cse
- companies
- organizations
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Companies & Orgs Search Engine

> A community-curated Google Custom Search Engine that restricts results to company and organization registries and directories — a shortcut to corporate records without hand-writing site filters.

## When to use
You have a company or organization `name` (or an `employer-org` your subject is tied to) and want to search across corporate registries, business directories, and org databases at once. Useful for confirming an employer claim, finding a business's registration/address, or mapping the organizations a subject is linked to — pivoting a person to the companies around them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cse.google.com/cse?cx=72ea9d8cfefc142d3.
2. Enter the company/organization `name` (add a country or director name to disambiguate) in the search box.
3. Review results — the CSE limits them to the corporate/directory sites its creator configured, cutting general-web noise.
4. Follow promising hits into the underlying registry or directory for full records (officers, addresses, filings).
5. Pivot: a company record's registered `address` and officer names feed people-search and public-records lookups; an officer's name links the organization back to individuals.

## Inputs → Outputs
- **In:** company/organization `name` or `employer-org`
- **Out:** company/org records and links, potentially yielding a registered `address` and associated officer names (`employer-org`)
- **Empty/negative result looks like:** no results or only tangential hits — the org isn't covered by the CSE's configured sites, or the custom config has degraded. Fall back to a primary registry (e.g. a national companies register) directly.

## Gotchas & OpSec
- A Google **Custom Search Engine's coverage is opaque and creator-defined** — you can't see which sites it includes, and that list can quietly shrink or break over time. Treat it as a convenience layer, not an authoritative source.
- Because the config is unverifiable, always confirm hits in a primary corporate registry.
- OpSec: **passive** — it's a Google search box; queries are ordinary web searches. Use a sock-puppet/clean session for sensitive work.

## Overlaps ("do both")
- Pairs with authoritative company registries (national business registers, OpenCorporates-style databases) — the CSE helps you *cast wide*, the primary registry gives you the *verified* record.

## Trust & verifiability
`trust: community` — a hobbyist-built CSE with unknown site coverage; marked `status: degraded` because a Custom Search Engine's usefulness silently erodes as its config ages. Never treat its results as complete or authoritative; verify downstream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | companies-and-orgs-search-engine |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
