---
id: global-terrorism-database
name: Global Terrorism Database
description: Use when you have a place, group `name`, or date and want records of terrorist incidents — returns coded attack records (date, location, perpetrator, casualties) for research and context.
url: https://www.start.umd.edu/research-projects/global-terrorism-database-gtd
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- academic-research
bestFor: Researching historical terrorist incidents by group, location, or date for context and base rates.
selectorsIn:
- name
- geolocation
selectorsOut:
- associate
status: live
pricing: free
costNote: Free for non-commercial/academic use; downloading the full dataset requires agreeing to terms and registering.
opsec: passive
opsecNote: Passive academic research against a curated historical database; nothing is queried about any living private individual and no target is contacted. It is context/base-rate data, not a person-lookup.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by START (National Consortium for the Study of Terrorism and Responses to Terrorism) at the University of Maryland; a widely-cited, methodologically documented academic dataset.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- start-consortium-for-the-study-of-terrorism-and-responses-to-terrorism
- street-drug-slang
aliases:
- GTD
- START GTD
tags:
- terrorism
- academic-dataset
- research
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Global Terrorism Database

> The standard academic dataset of terrorist incidents worldwide (maintained by START at the University of Maryland) — coded records of attacks for research, context, and base rates, not a lookup on individuals.

## When to use
You need historical context on terrorism: incidents in a `geolocation`, attacks attributed to a group `name`, or activity over a date range. Reach for the GTD to establish base rates, map a group's attack history, or verify claims about a specific incident (date, location, casualties, perpetrator attribution). It is a curated research dataset — use it for context and corroboration, not to identify or locate a private living person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GTD project page at START (start.umd.edu) and use the online GTD search/portal, or register and agree to the terms to download the dataset.
2. Filter by country/region, perpetrator group, date range, attack type, or target type.
3. Read the coded records: date, location, perpetrator (or "unknown"), weapon, casualties, and source notes.
4. For analysis, download the dataset and work it in your stats tool; mind the documented methodology and any coverage gaps/year boundaries.
5. Pivot: a group's incident history (`associate`/attribution links) feeds broader research; individual records cite sources you can chase for detail.

## Inputs → Outputs
- **In:** a group `name`, `geolocation`, or date range
- **Out:** coded incident records (date, place, perpetrator attribution, casualties) — group/campaign `associate` context
- **Empty/negative result looks like:** no records for a filter, or "perpetrator unknown" — attribution is often unresolved, and the dataset has defined start/end years and coding rules, so gaps reflect methodology, not certainty.

## Gotchas & OpSec
- Human-in-the-loop / legal-gate: full-dataset download requires accepting non-commercial/academic terms.
- It's coded historical data with documented inclusion criteria and time coverage — read the codebook; don't over-interpret gaps or "unknown" attributions.
- OpSec: passive; it's research data, with no exposure to any subject.

## Overlaps ("do both")
- Pairs with `[[start-consortium-for-the-study-of-terrorism-and-responses-to-terrorism]]` for related research and with news/primary-source archives to flesh out individual incidents. Use it for aggregate context alongside event-level reporting.

## Trust & verifiability
`trust: trusted` — a rigorously documented, widely-cited academic dataset from START/UMD; records are authoritative for research, with attribution uncertainty and coverage boundaries clearly stated in its methodology.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-terrorism-database |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, geolocation → associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
