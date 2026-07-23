---
id: dark-web-informer
name: Dark Web Informer
description: Use when you have a threat-actor/group `name` and want a reference profile — returns a searchable database of threat actors, APT groups, and ransomware crews (sourced from MISP Galaxy).
url: https://darkwebinformer.com/threat-actor-database/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up known threat actors / ransomware groups and their aliases from a community-sourced database.
selectorsIn:
- name
selectorsOut:
- associate
status: live
pricing: freemium
costNote: The threat-actor database (sourced from the open MISP Galaxy) is free to browse; parts of the wider Dark Web Informer site are gated behind paid membership.
opsec: passive
opsecNote: Passive reference reading of a public database — nothing touches any actor or the dark web itself. Safe to browse; no Tor required for this database page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The database mirrors the open-source MISP Galaxy threat-actor data and auto-syncs it; attribution is community-sourced, so cross-check names/aliases against primary vendor reporting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- darkwebinformer.com
- Dark Web Informer threat actor database
tags:
- threat-actor-search
- threat-intelligence
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Dark Web Informer

> A free, searchable threat-actor database (auto-synced from the open MISP Galaxy project) — look up APT groups, ransomware crews, and cyber adversaries with their aliases and context.

## When to use
You come across a threat-actor or ransomware-group `name` and want a quick reference: who they are, their known aliases, and associated context. Reach for Dark Web Informer's threat-actor database to orient on a named adversary using community-curated MISP Galaxy data. It's a CTI reference for actor/group research — not a tool for locating private individuals, and (for this database page) not something requiring the dark web itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://darkwebinformer.com/threat-actor-database/.
2. Search or browse for the actor/group `name`.
3. Read the profile — description and, crucially, known **aliases** and associated groups (the MISP Galaxy synonym set).
4. Use the aliases to reconcile reporting that names the same actor differently.
5. Pivot: cross-reference the actor against MISP Galaxy directly, MITRE ATT&CK, and vendor reporting; feed aliases into other threat-intel sources.

## Inputs → Outputs
- **In:** a threat-actor/group `name`
- **Out:** a profile with aliases and associated (`associate`) groups/campaigns, from MISP Galaxy
- **Empty/negative result looks like:** no entry for a name — the actor may be listed under a different alias (try synonyms) or not yet in MISP Galaxy.

## Gotchas & OpSec
- Data is community-sourced (MISP Galaxy) and auto-synced — treat attribution as a starting point and corroborate with primary vendor reporting.
- Some of the broader Dark Web Informer site is paid; the threat-actor database itself is the free part.
- OpSec: passive; browsing this database exposes nothing and needs no Tor.

## Overlaps ("do both")
- Overlaps `[[fortiguard-labs]]` and other threat-actor encyclopedias, and MISP Galaxy itself (its source) — use several and reconcile aliases, since each vendor names and attributes actors differently.

## Trust & verifiability
`trust: community` — it mirrors the open MISP Galaxy dataset, so it's a convenient view of community CTI rather than an independent authority; verify attribution against MITRE ATT&CK and named-vendor reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dark-web-informer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name → associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
