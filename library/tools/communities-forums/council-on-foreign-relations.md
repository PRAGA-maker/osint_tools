---
id: council-on-foreign-relations
name: Council on Foreign Relations
description: Use when you have an `employer-org` or `name` in the defense/security/geopolitics space and want authoritative background, conflict trackers and expert profiles — returns organizational and analytical context.
url: https://www.cfr.org/defense-and-security
category: communities-forums
path:
- communities-forums
bestFor: Authoritative background and interactive trackers on armed groups, conflicts and security institutions.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Public analysis, trackers and articles are free to read; some events/membership content is gated but not needed for research reading.
opsec: passive
opsecNote: Reading a public think-tank site is passive; the subject is not notified. CFR is a widely-read US foreign-policy institution — visiting it reveals nothing about your target. Standard clean-browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established US foreign-policy think tank publishing sourced expert analysis and maintained trackers (e.g. Global Conflict Tracker); reputable secondary/context source, not a primary record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- global-conflict-tracker
aliases:
- CFR
- cfr.org
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Council on Foreign Relations

> The CFR defense-and-security hub: sourced analysis, expert bios and interactive trackers on conflicts, armed groups and security institutions worldwide.

## When to use
You need authoritative *context* rather than a personal record: understanding an armed group, conflict zone, sanctions regime or security institution that an investigation touches, or reading the published work and affiliations of a named foreign-policy expert. Useful for grounding a case in reliable background before chasing individual selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cfr.org/defense-and-security.
2. Browse or use the site search for a topic (`employer-org`, country, conflict) or a `name` (CFR fellows and cited experts have bio pages).
3. For structured data, use CFR's interactive trackers — e.g. the [[global-conflict-tracker]] — which map active conflicts with background, actors and timelines.
4. Read the analysis and follow its citations to primary sources.
5. Pivot: an expert's bio yields `employer-org`/`associate` links and prior roles; a conflict page yields the named actors and organizations to research further.

## Inputs → Outputs
- **In:** `employer-org` / topic / `name` (of a foreign-policy figure)
- **Out:** background analysis, expert affiliations (`employer-org`, `associate`), conflict/actor context
- **Empty/negative result looks like:** no article or tracker entry matches — CFR covers institutions and macro-security, not ordinary individuals, so most personal-locate queries will miss here by design.

## Gotchas & OpSec
- This is a *context* source, not a people-finder — it won't return addresses, phones, or records on private individuals.
- Analysis reflects CFR's editorial perspective; treat conclusions as informed opinion and follow the cited primary sources for facts.
- OpSec: fully passive; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with [[global-conflict-tracker]] (its own structured tracker) and mainstream news archives — CFR gives vetted analysis and institutional framing, while news gives dated, granular events. Use both when building a security/geopolitics backdrop.

## Trust & verifiability
`trust: trusted` — a long-established think tank with sourced, edited output; reliable as secondary context, but confirm any load-bearing fact against the primary sources it cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | council-on-foreign-relations |
| category | communities-forums |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
