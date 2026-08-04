---
id: control-validation-compass
name: Control Validation Compass
description: Use when you have an attacker technique or a `document-id`-style detection/IOC and want related detections and offensive tests — returns rules and tests mapped to ATT&CK techniques.
url: https://controlcompass.github.io/
category: search-engines
path:
- search-engines
bestFor: A searchable, ATT&CK-aligned repository of 10,000+ detection rules and 2,100+ offensive security tests for threat-modeling and purple-team work.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, publicly accessible aggregator hosted on GitHub Pages; no account. It links out to third-party rule/test repos.
opsec: passive
opsecNote: Passive research over public rule/test databases; you query techniques, not a target. Nothing about a subject is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by security practitioners (TropChaud / @IntelScott) under the ControlCompass GitHub org; it aggregates third-party content, so individual rules/tests carry their own authors' reliability.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Control Compass
- controlcompass.github.io
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
- threat-modeling
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Control Validation Compass

> A threat-modeling aide that maps thousands of public detection rules and offensive tests onto attacker techniques — a defensive/purple-team reference, tangential to person-finding.

## When to use
You are working a security/threat-intel angle of an investigation and want, for a given attacker technique or behaviour, the associated detection rules (blue-team) and offensive tests (red-team). It is a technique-to-content index; it does not look up people, domains, or IPs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://controlcompass.github.io/.
2. Search or browse by attacker technique (ATT&CK-aligned) or by keyword.
3. Review the linked detection rules and offensive tests; follow each out to its source repo for the full content.
4. Use it to plan detections/validations or to understand how a given TTP is spotted and tested.

## Inputs → Outputs
- **In:** an attacker technique / TTP keyword (not a personal selector)
- **Out:** mapped detection rules and offensive security tests
- **Empty/negative result looks like:** a technique with no mapped public content — the behaviour may be niche; consult primary threat-intel sources.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; you disclose nothing about a subject.
- It is an aggregator — the quality of any linked rule/test depends on its original author, so verify at the source.

## Overlaps ("do both")
- Complements MITRE ATT&CK and rule repos (Sigma, Atomic Red Team): Control Compass is the cross-index that ties a technique to both the detections and the tests, then sends you to the primaries.

## Trust & verifiability
`trust: community` — a respected practitioner-maintained index; reliable as a map, but confirm each linked artifact against its upstream repository.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | control-validation-compass |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
