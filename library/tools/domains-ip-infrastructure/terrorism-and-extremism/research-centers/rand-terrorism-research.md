---
id: rand-terrorism-research
name: RAND Terrorism Research
description: Use when you have a group, actor `name`, or topic and want authoritative think-tank research and analysis on terrorism/extremism — returns document-id, associate.
url: https://www.rand.org/topics/terrorism.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- research-centers
bestFor: Authoritative, citable research and analysis on terrorism, extremism, and related security topics.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
status: live
pricing: free
costNote: Free public access to RAND's terrorism research library; most reports download as free PDFs.
opsec: passive
opsecNote: Passive — reading published public research; nothing touches any subject and no query is attributable to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RAND Corporation is a long-established nonpartisan nonprofit research institution; its terrorism work is methodologically reviewed and citable at source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- RAND terrorism
- rand.org terrorism
tags:
- terrorism
- research
- think-tank
source: arf-seed
lastVerified: '2026-07-29'
relatedTools:
- terrorism-incidents-database
enrichment: full
---

# RAND Terrorism Research

> RAND's topic hub for terrorism and extremism — a deep, citable library of policy research, reports, and commentary for context on groups, actors, and trends.

## When to use
You need **authoritative background** on a terrorist/extremist group, a security actor, a tactic, or a region — not raw incident data but analysed, sourced research. Use it to understand who a named group (`name`) is, its history and affiliations (`associate`), and the wider policy context, and to pull citable reports that ground an investigation's framing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rand.org/topics/terrorism.html and use the search/filter to find a group, actor, tactic, or region.
2. Browse the reports, research briefs, and commentary; filter by date to find current analysis.
3. Open a report to read the analysis and download the free PDF; note the authors and bibliography for further leads.
4. Pivot: named actors/groups (`associate`) feed further OSINT; report citations point to primary sources and datasets; pair with an incident database for the underlying events.

## Inputs → Outputs
- **In:** a group, actor `name`, tactic, or topic
- **Out:** `document-id` (reports/briefs), named actors and affiliations (`associate`), and citations to primary sources
- **Empty/negative result looks like:** no RAND publication on that specific niche actor — RAND covers major groups/trends analytically, so obscure individuals may not appear (not evidence about them).

## Gotchas & OpSec
- No login; public and free.
- This is **analysis, not a live incident feed** — for who/what/where/when of specific attacks, use an incident database instead.
- RAND reflects a U.S. policy-research vantage; weigh its framing and corroborate factual claims against primary sources.

## Overlaps ("do both")
- Pairs with `[[terrorism-incidents-database]]` — RAND gives the analytical context while an incident database gives the structured event records; use both to move between "what happened" and "what it means."

## Trust & verifiability
`trust: trusted` — an established nonpartisan research institution; its reports are peer/methodology-reviewed and fully citable, though still secondary analysis to verify against primaries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rand-terrorism-research |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name → document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
