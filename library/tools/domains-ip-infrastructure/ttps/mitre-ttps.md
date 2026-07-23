---
id: mitre-ttps
name: MITRE ATT&CK
description: Use when you have observed adversary behavior or malware and want to classify the tactics/techniques — returns technique document-ids and a shared taxonomy; a reference framework, not a people source.
url: https://attack.mitre.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ttps
bestFor: A standardized catalog of adversary tactics, techniques, and procedures for classifying and communicating observed behavior.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open; the full knowledge base is downloadable (STIX/TAXII) and there is a public API — no account.
opsec: passive
opsecNote: You read a public knowledge base; nothing about a target is transmitted, so it is entirely passive with no leakage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by MITRE (a US non-profit R&D organization); ATT&CK is the de-facto industry-standard adversary-behavior taxonomy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mitre-att-and-ck
aliases:
- MITRE ATT&CK
- ATT&CK
- Mitre TTPs
tags:
- threat-intel
- ttp
- reference
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# MITRE ATT&CK

> The industry-standard catalog of adversary tactics and techniques — a shared vocabulary for classifying what an attacker (or a piece of malware) was observed doing.

## When to use
You are doing the technical/security side of an investigation — reviewing malware behavior, incident logs, or a threat-actor profile — and want to map observed behavior to a standardized `document-id` (e.g. T1566 Phishing) so it can be communicated and cross-referenced. It's a reference framework and taxonomy; it returns nothing about an individual person and is peripheral to person-finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://attack.mitre.org/ and search a technique, tactic, or named threat group.
2. Read the technique page: description, sub-techniques, real-world procedure examples, detections, and mitigations, each with an ATT&CK ID (`document-id`).
3. Browse the **Groups** and **Software** matrices to see which actors/tools use a given technique — useful for attributing a pattern to a known cluster.
4. For tooling, pull the knowledge base via STIX/TAXII or the API, or model coverage in the ATT&CK Navigator.
5. Pivot: a mapped technique + a known group profile guides where to look next in logs or threat-intel feeds.

## Inputs → Outputs
- **In:** an observed behavior, technique/tactic name, or threat-group/software name (no personal selectors).
- **Out:** technique `document-id`s, descriptions, procedure examples, detections/mitigations, and group/software associations.
- **Empty/negative result looks like:** a behavior with no clean ATT&CK mapping (novel or too generic) — the framework is a classification aid, not exhaustive coverage of every action.

## Gotchas & OpSec
- It's a taxonomy, not live threat intel — it tells you what techniques exist, not who is attacking you right now.
- Mapping is interpretive; the same log line can fit several techniques, so document your reasoning.
- Group/software attributions summarize public reporting and can lag or oversimplify real-world activity.

## Overlaps ("do both")
- Complements [[osv-vulnerability-library]] and threat-intel feeds: OSV/advisories tell you what's vulnerable, ATT&CK frames how adversaries exploit and operate.

## Trust & verifiability
`trust: trusted` — maintained by MITRE and the community standard; every technique page cites the public reporting behind its procedure examples.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mitre-ttps |
