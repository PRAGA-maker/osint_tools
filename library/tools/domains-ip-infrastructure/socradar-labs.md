---
id: socradar-labs
name: SOCRadar LABS
description: Use when you have a `domain`, `ip-address` or threat-actor name and want free threat-intel context — returns threat-actor profiles, digital-footprint and exposure data.
url: https://socradar.io/labs/threat-actor/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Free lookups of threat-actor profiles and a domain/company's exposed digital footprint.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
status: live
pricing: freemium
costNote: The LABS tools (threat-actor DB, digital footprint, etc.) are free and mostly need no account; the full SOCRadar platform is a paid enterprise product.
opsec: passive
opsecNote: You query SOCRadar's own intelligence datasets about a domain/actor, not the target's own infrastructure, so the subject is not directly touched. A free account may be requested for some tools.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial threat-intelligence vendor's free tools; profiles are vendor-compiled and marketing-adjacent, so corroborate specific indicators against primary sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SOCRadar Labs
- socradar.io/labs
tags:
- threat-actor-search
- threat-intel
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# SOCRadar LABS

> A suite of free threat-intelligence tools from vendor SOCRadar — most usefully a 500+ threat-actor database, plus digital-footprint and exposure lookups for a domain or company.

## When to use
Your case has a cyber/threat angle: a `domain` or `ip-address` you want exposure context on, or a named threat actor/ransomware group you need profiled. SOCRadar LABS gives free access to actor profiles (aliases, targeted regions/industries, malware, TTPs, IOCs) and to digital-footprint checks that surface a company's internet-facing exposure — helpful for scoping the infrastructure and actors around a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://socradar.io/labs/ and pick a tool — Threat Actor database, digital footprint, or another free lookup.
2. For the actor DB, search by group/alias to read its profile (origins, targets, malware, MITRE ATT&CK techniques, IOCs).
3. For footprint tools, enter a `domain`/company to see reported exposed assets and indicators.
4. Pivot: take IOCs/domains into WHOIS, DNS and infrastructure tools; take actor aliases into further threat-intel sources.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / threat-actor name
- **Out:** threat-actor profiles (aliases, TTPs, IOCs), digital-footprint/exposure indicators, related `domain`s
- **Empty/negative result looks like:** no profile for an obscure actor, or a footprint check returning nothing notable — the free tier is summarised, so gaps are expected.

## Gotchas & OpSec
- Human-in-the-loop: some free tools prompt for a free account.
- OpSec: passive — you query SOCRadar's datasets, not the target's servers.
- Vendor framing: profiles are compiled by a commercial vendor and can lag or simplify; verify specific IOCs/attribution against primary reporting before acting.

## Overlaps ("do both")
- Pairs with other threat-actor trackers and infrastructure tools because each vendor's dataset differs — cross-check attribution and IOCs across sources.

## Trust & verifiability
`trust: community` — free tools from a commercial threat-intel vendor; treat profiles as leads and corroborate indicators against authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
