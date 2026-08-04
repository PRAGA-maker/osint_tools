---
id: etda
name: ETDA Threat Group Cards
description: Use when you have a threat-actor name/alias and want its profile — returns aliases, suspected origin, targeted sectors and associated tools/malware from ThaiCERT/ETDA's encyclopedia.
url: https://apt.etda.or.th/cgi-bin/listgroups.cgi
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up an APT/threat-group profile — aliases, attribution, targets and toolset — to contextualise a cyber threat.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public reference; no account or payment.
opsec: passive
opsecNote: A public reference encyclopedia — you read curated profiles, querying nothing about a live target's infrastructure. Nothing is disclosed to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by ThaiCERT / Thailand's ETDA (a government agency); a well-regarded, sourced threat-actor encyclopedia, though attribution is inherently uncertain and should be cross-checked.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ThaiCERT Threat Group Cards
- APT Groups and Operations
- apt.etda.or.th
tags:
- threat-actor-search
- threat-intel
- apt
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# ETDA Threat Group Cards

> ThaiCERT/ETDA's "Threat Group Cards" — a free, sourced encyclopedia of APT and cybercrime groups, giving each one's aliases, suspected origin, targeted sectors/regions and associated tools.

## When to use
Your investigation surfaces a cyber threat actor — a group name in a report, an alias in a leak, a malware family — and you need to place it: who they are, what they're also called, where they're believed to originate, whom they target, and which tools/malware they use. ETDA's database consolidates this into per-group "cards" with references, a fast way to contextualise an actor and reconcile the many aliases the same group is known by.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ETDA Threat Group Cards site and browse or search the APT and "Other" (crime/hacktivist) group lists; filter by suspected country.
2. Open a group's card to read its aliases, origin, active timeframe, targeted sectors/countries, operations and associated tools/malware, with cited sources.
3. Use the alias list to reconcile the same actor across different vendors' names.
4. Pivot: take tool/malware names and aliases into other threat-intel sources (MITRE ATT&CK, vendor reports) and infrastructure tools.

## Inputs → Outputs
- **In:** threat-actor name/alias (or browse)
- **Out:** actor profile — aliases, suspected origin, targets, operations, tools/malware, with references
- **Empty/negative result looks like:** no card for a very new or obscure actor, or a sparse card with thin sourcing — expected at the edges of public reporting.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a read-only reference.
- OpSec: passive — you read a public encyclopedia; no target infrastructure is touched.
- Attribution caveat: threat attribution is uncertain by nature and compiled from public reporting; treat "suspected origin" as a lead and corroborate across sources.

## Overlaps ("do both")
- Pairs with MITRE ATT&CK and vendor threat-actor databases (e.g. `[[socradar-labs]]`) because each catalog differs in coverage and naming — cross-referencing resolves aliases and fills gaps.

## Trust & verifiability
`trust: trusted` — a government-agency-maintained, well-sourced encyclopedia; reliable as a reference, with the standard caveat that attribution itself is probabilistic.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
