---
id: apt-groups-and-operations
name: APT Groups and Operations
description: Use when you have an APT/threat-group name or alias and want to reconcile it — returns a cross-referenced matrix of named actors, their aliases, and toolsets across vendors.
url: https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml?pli=1
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping the many vendor names/aliases for the same advanced-persistent-threat group and their associated operations/tools.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free published Google Sheet; view/copy without an account.
opsec: passive
opsecNote: A read-only reference document — you look up actor names, not a live target, and nothing about your subject is transmitted. Standard Google Docs access logging applies to your own view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-cited community-maintained matrix (originating with Florian Roth / @cyb3rops) reconciling vendor naming; attribution itself is inherently contested, so treat entries as a cross-reference aid, not ground truth.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- APT groups matrix
- Florian Roth APT groups spreadsheet
tags:
- threat-actor-search
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# APT Groups and Operations

> The community "Rosetta Stone" for threat-actor names — one big spreadsheet reconciling the dozens of vendor aliases (APT28 = Fancy Bear = Sofacy = …) for the same group, plus their known operations and tools.

## When to use
You've encountered a threat-group name in a report, IOC feed, or news item and need to know who else calls them what, and what they're associated with. Because every vendor coins its own name, a single actor can appear under many labels; this matrix lets you collapse those into one entity and see the operations, malware and tooling attributed to it. A niche resource in a missing-persons context, but essential when an investigation touches state-linked or organised cyber activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the published Google Sheet at the URL above.
2. Search (browser find / sheet search) for the actor name or alias you have (`employer-org` — the group as an organisation).
3. Read across the row: the group's aliases across vendors, attributed operations, and associated toolsets/malware.
4. Pivot: the canonical/aliased names feed threat-intel platforms and reporting searches; associated tooling feeds malware/IOC research.

## Inputs → Outputs
- **In:** a threat-group name/alias (`employer-org`)
- **Out:** the reconciled set of aliases and attributed operations/tools for that actor (`employer-org`)
- **Empty/negative result looks like:** no matching row — a newly-named or very niche group may not be catalogued, or your alias predates/differs from the sheet's; absence ≠ the group doesn't exist.

## Gotchas & OpSec
- **Attribution is contested:** vendors disagree, and the same alias is sometimes used loosely — treat mappings as a cross-reference, not confirmed identity.
- A community spreadsheet lags fast-moving naming; verify against current vendor/MITRE ATT&CK group pages for anything decisive.
- It profiles *groups*, never individuals — don't over-read it toward attributing a person.

## Overlaps ("do both")
- Pairs with MITRE ATT&CK's Groups pages and vendor threat-intel reporting — use this sheet to unify the names, then those sources for current, sourced detail.

## Trust & verifiability
`trust: community` — a respected, well-known community reference, but built on inherently disputed attribution; corroborate mappings against authoritative, dated sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apt-groups-and-operations |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
