---
id: fortiguard-labs
name: FortiGuard Labs
description: Use when you have a threat-actor `name` or group and want a reference profile — returns adversary encyclopedia entries with attribution, aliases, and operational context.
url: https://www.fortiguard.com/threat-actor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up known threat actors/APT groups and their attributed context in a free security encyclopedia.
selectorsIn:
- name
selectorsOut:
- associate
status: live
pricing: free
costNote: The threat-actor encyclopedia is free to browse; Fortinet's protective products are separate paid services.
opsec: passive
opsecNote: Passive reference reading — you browse FortiGuard's public encyclopedia; nothing touches any actor or target. Safe to use freely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by FortiGuard Labs, Fortinet's established threat-research division; profiles reflect vendor attribution and should be cross-checked against other vendors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fortiguard-reputation-service
aliases:
- FortiGuard threat encyclopedia
- fortiguard.com threat-actor
tags:
- threat-actor-search
- threat-intelligence
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# FortiGuard Labs

> A free, searchable encyclopedia of known threat actors — nation-state APTs, ransomware crews, hacktivists — with attribution, aliases, and operational context from Fortinet's research team.

## When to use
You encounter a threat-actor or group `name` (in an incident report, a ransom note, a malware attribution, a news story) and want a quick reference profile: who they are, what aliases they go by, their attributed origin, and how they operate. Reach for FortiGuard's encyclopedia to orient yourself on a named adversary. This is a cyber-threat-intelligence reference for actor/group research, not a tool for locating private individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fortiguard.com/threat-actor.
2. Search for the actor/group `name`, or filter by adversary type (APT, RaaS, hacktivist, cybercriminal).
3. Open a profile for its description, known aliases, attributed geolocation/origin, TTPs, and associated campaigns.
4. Note the aliases and linked groups — these are pivots into other vendors' naming and reporting.
5. Pivot: cross-reference the actor against MITRE ATT&CK, other vendors' encyclopedias, and IOC feeds; use aliases to unify reporting that uses different names.

## Inputs → Outputs
- **In:** a threat-actor/group `name` or type
- **Out:** an encyclopedia profile — aliases, attributed origin, TTPs, associated (`associate`) groups/campaigns
- **Empty/negative result looks like:** no profile for a given name — the actor may be tracked only under a different alias (try synonyms) or not covered by FortiGuard.

## Gotchas & OpSec
- Attribution is vendor-specific: FortiGuard's naming and origin claims may differ from CrowdStrike/Mandiant/Microsoft — always map across vendors via aliases.
- Coverage skews to actors relevant to Fortinet telemetry; niche or very new actors may be absent.
- OpSec: passive reference reading; zero exposure.

## Overlaps ("do both")
- Pairs with `[[fortiguard-reputation-service]]` for domain/IP reputation, and with MITRE ATT&CK / other threat-intel encyclopedias — use several to reconcile conflicting attribution and alias sets.

## Trust & verifiability
`trust: trusted` — a reputable vendor research source; treat individual attribution claims as one vendor's assessment and corroborate origin/identity across multiple threat-intel providers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fortiguard-labs |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name → associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
