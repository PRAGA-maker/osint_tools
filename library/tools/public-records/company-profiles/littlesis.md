---
id: littlesis
name: LittleSis
description: Use when you have a `name`/`employer-org` of a public figure or company and want their power network — returns board seats, donations, and relationship graphs of associates.
url: https://littlesis.org/
category: public-records
path:
- public-records
- company-profiles
bestFor: Mapping documented relationships between people, companies, and institutions — board memberships, donations, business ties, and affiliations.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free and open (a nonprofit "involuntary Facebook of the powerful"); public data with a free API.
opsec: passive
opsecNote: Searching LittleSis queries its own database of public-record relationships — it touches nothing about the subject and notifies no one. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Public Accountability Initiative nonprofit; entries are sourced/cited from public records, though it's crowd-maintained — check each relationship's citation.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Little Sis
- PAI LittleSis
tags:
- power-mapping
- relationships
- company-profiles
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# LittleSis

> A free, cited database of who-knows-whom among the powerful — board seats, donations, business ties, and institutional affiliations mapped into relationship graphs.

## When to use
Your subject is a public-facing figure — an executive, politician, donor, board member, or the company they run — and you want their documented network: who they sit on boards with, who funds them, which institutions they're tied to. LittleSis excels at surfacing `associate` links and corporate/political affiliations that reveal a person's real sphere of influence and connections. Strongest for US public figures; ordinary private individuals won't appear.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open littlesis.org and search the subject `name` or `employer-org`.
2. Open the profile: relationships are listed and visualized (people, orgs, board memberships, donations, business ties).
3. For each relationship that matters, click through to its cited source to confirm it.
4. Use the "maps" and network view to see clusters; use the free API for bulk pulls.
5. Pivot: named `associate`s and `employer-org`s become new leads; a documented board/donation tie corroborates a relationship your investigation suspected.

## Inputs → Outputs
- **In:** `name` or `employer-org` (public figure/company)
- **Out:** relationship graph — `associate`s (board/business/donation ties) and `employer-org` affiliations, each with citations
- **Empty/negative result looks like:** no profile — the subject isn't a tracked public figure (LittleSis covers the powerful, not private individuals); absence just means they're not notable/entered.

## Gotchas & OpSec
- Coverage centers on US elites, corporations, and politics — thin for private people and non-US subjects.
- Crowd-maintained: relationships can be incomplete or stale; always follow the citation to the primary source.
- It maps *documented* ties, not secret ones — absence of a link isn't proof none exists.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with corporate registries (e.g. `[[lei-search]]`, OpenCorporates) and campaign-finance databases — LittleSis synthesizes the network; the registries/filings are the primary sources that confirm each edge.

## Trust & verifiability
`trust: trusted` — a reputable accountability nonprofit with cited entries; high-value for leads, but verify each specific relationship against its linked source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | littlesis |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
