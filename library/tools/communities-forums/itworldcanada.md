---
id: itworldcanada
name: ITWorldCanada
description: Use when you have a `name` or `employer-org` in Canadian tech/IT and want trade-press coverage — returns articles naming people, companies and roles.
url: https://www.itworldcanada.com
category: communities-forums
path:
- communities-forums
bestFor: Finding Canadian IT/tech trade-press coverage of a person, company, or product.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to read and search; no paywall or account for most articles.
opsec: passive
opsecNote: Reading and searching the site is passive and discloses nothing to any subject. Use a VPN if you want the query itself kept private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running Canadian IT trade-news publication; edited reporting, generally reliable, though it is press coverage rather than a primary record.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IT World Canada
- itworldcanada.com
tags:
- toddington
- curated-directory
- news-journalism
- technology
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# ITWorldCanada

> Canada's long-running IT trade press — a niche but useful place to find named coverage of tech professionals, executives, vendors, and Canadian technology companies.

## When to use
You have a `name` or `employer-org` connected to the Canadian technology sector — an IT executive, a vendor, a startup, a security incident — and want trade-press coverage that names people and their roles. Trade journalism often names individuals (appointments, quotes, project leads, breach disclosures) who don't appear in mainstream news, corroborating a person's employer, title, and professional timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.itworldcanada.com and use the site search, or a site-scoped Google query: `site:itworldcanada.com "<name>"`.
2. Search the `name` or `employer-org`/product.
3. Read matches for role, company affiliation, quotes, dates, and named colleagues.
4. Pivot: a confirmed title/employer feeds LinkedIn and company-registry lookups; named colleagues become `associate` leads.

## Inputs → Outputs
- **In:** `name` or `employer-org` (Canadian tech context)
- **Out:** articles naming the person/company — role, affiliation (`employer-org`), quotes, dates, colleagues
- **Empty/negative result looks like:** no coverage — expected for anyone not publicly active in Canadian tech; absence is not meaningful.

## Gotchas & OpSec
- Scope is **narrow** — Canadian IT/tech only; irrelevant for people outside that sector.
- Press coverage is edited reporting, not a primary record; confirm titles/affiliations against LinkedIn or a company registry.
- A site-scoped Google search often beats the on-site search for finding a specific name.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pair with LinkedIn and Canadian company registries — trade coverage supplies the story and named roles, while those confirm current employment and corporate detail.

## Trust & verifiability
`trust: trusted` — an established trade publication with editorial standards; reliable as reporting, with the usual caveat that professional details should be confirmed against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itworldcanada |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
