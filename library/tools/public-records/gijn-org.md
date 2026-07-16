---
id: gijn-org
name: GIJN Resource Centre
description: Use when you need a vetted methodology or country/sector guide for an investigation (e.g. tracing companies or people abroad) — returns curated how-to guides, tool lists, and source pointers, not queryable data.
url: https://gijn.org/
category: public-records
path:
- public-records
bestFor: Methodology and country/topic guides for investigating companies and people, with curated tool/source recommendations.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free to read. GIJN is a nonprofit network; guides, tool lists, and its Help Desk resources are freely accessible.
opsec: passive
opsecNote: Reading GIJN is passive — you are consuming published guides, querying nobody about your target. No subject is touched. Standard browsing hygiene is enough.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Global Investigative Journalism Network is a respected nonprofit of investigative journalism organisations; its guides are authored/vetted by professional investigators.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Global Investigative Journalism Network
- gijn.org
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- gijn-online-research-tools
- gijn-org-3
- gijn-org-4
---

# GIJN Resource Centre

> Not a lookup tool but a vetted methodology library — the Global Investigative Journalism Network's guides tell you *how* to investigate a person, company, or region and *which* authoritative sources to use.

## When to use
You are stuck on *method* rather than a single query: how to trace a company in a jurisdiction you don't know, how to investigate a person across borders, which registries/records exist in a given country. GIJN's resource centre and country/topic guides (for example, its guide to investigating Chinese companies) point you to the right authoritative sources and techniques. Reach for it to plan an approach or unblock an investigation, then execute with the specific tools it recommends.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gijn.org/ and browse the Resource Centre / Reporter's Guides, or search for your topic, country, or entity type.
2. Read the relevant guide — it explains the workflow and lists concrete registries, databases, and tools for that context.
3. Note the recommended primary sources (company registries, court records, sanctions/leaks databases) and go query those directly.
4. Cross-check with GIJN's Help Desk and other guides for the same region to fill gaps.
5. Pivot: the guide hands you a shortlist of authoritative sources — treat GIJN as the map, and the named registries/tools as the terrain to actually search.

## Inputs → Outputs
- **In:** a research question / country / entity type (conceptual, not a selector query)
- **Out:** methodology, curated source and tool lists, pointers to authoritative `employer-org`/records databases — *no* raw data about a specific person
- **Empty/negative result looks like:** no guide covering your exact niche; you'll still get adjacent methodology. Do not expect it to return facts about an individual — it returns how-to knowledge.

## Gotchas & OpSec
- Not a database: GIJN does not hold searchable person/company records — it tells you where those live. Don't mistake it for a query tool.
- Human-in-the-loop: you read and apply the methodology yourself; there is no automated output.
- Currency: guides are dated — confirm that a recommended source is still live before relying on it.

## Overlaps ("do both")
- Pairs with every primary-source tool in this library — GIJN is the meta-layer that tells you which of them to use for a given country/entity; use it to *choose* between records tools like `[[gov-im]]`, Companies House, or OpenCorporates rather than instead of them.

## Trust & verifiability
`trust: trusted` — a respected nonprofit investigative-journalism network whose guides are written and vetted by professionals; authoritative as methodology, though it is guidance, not primary evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gijn-org |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
