---
id: mitre-att-and-ck
name: MITRE ATT&CK
description: Use when you have observed adversary behaviour and want to classify it — a free knowledge base of tactics, techniques and threat-actor/software profiles.
url: https://attack.mitre.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ttps
bestFor: Mapping observed attacker tactics/techniques (TTPs) to a standard taxonomy and cross-referencing known threat groups and their tooling.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open — usable by anyone at no charge.
opsec: passive
opsecNote: A public reference knowledge base; you read it, you query no target. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by MITRE, a US non-profit R&D organisation; the de-facto industry-standard TTP framework built on real-world observations.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ATT&CK
- MITRE ATT&CK Matrix
- attack.mitre.org
tags:
- threat-intelligence
- ttps
- framework
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- mitre-ttps
---

# MITRE ATT&CK

> The industry-standard, free knowledge base of adversary tactics and techniques — a shared vocabulary for describing how attackers operate, with linked group and software profiles.

## When to use
You have observed or suspected adversary behaviour (from logs, an incident, or threat reporting) and want to classify it against a standard taxonomy, or you want to look up a known threat group's typical techniques and tooling. This is a reference framework for cyber-threat work, not a person-finding tool — its OSINT relevance is threat-actor attribution and reporting, not locating individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://attack.mitre.org/ and pick the relevant matrix (Enterprise, Mobile, ICS).
2. Navigate tactics (the "why" — e.g. Persistence, Exfiltration) to their techniques/sub-techniques (the "how").
3. Look up a specific technique for description, detection guidance and mitigations, or browse the Groups/Software pages to see which actors use it.
4. Use the technique IDs (e.g. T1566) as a common language in your reporting.
5. For automation, pull the underlying data via the ATT&CK STIX/TAXII feeds.

## Inputs → Outputs
- **In:** none (you navigate by tactic/technique/group)
- **Out:** structured TTP descriptions, threat-group and malware/software profiles, detections & mitigations
- **Empty/negative result looks like:** behaviour that doesn't map cleanly to an existing technique — note it as such rather than forcing a fit; ATT&CK evolves and gaps exist.

## Gotchas & OpSec
- It's a taxonomy/reference, not a live threat feed or a lookup that identifies people.
- Mapping is judgement-based; two analysts may classify the same behaviour differently.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with threat-intel platforms and IOC feeds — ATT&CK provides the framework/vocabulary; those provide the current indicators and campaign data to map onto it.

## Trust & verifiability
`trust: trusted` — authoritative, community-standard framework maintained by MITRE; grounded in documented real-world observations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mitre-att-and-ck |
