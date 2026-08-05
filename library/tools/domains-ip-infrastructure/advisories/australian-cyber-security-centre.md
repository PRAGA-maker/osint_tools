---
id: australian-cyber-security-centre
name: Australian Cyber Security Centre
description: Use when you're researching a threat, vulnerability, or campaign and want authoritative Australian-government cyber advisories, alerts, and IOCs — a trusted advisory source, not a per-target lookup.
url: https://www.cyber.gov.au/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- advisories
bestFor: Authoritative government cyber advisories, alerts, and threat guidance (Australia/ASD).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public government resource; no account required.
opsec: passive
opsecNote: Reading published government advisories is fully passive and discloses nothing about a target. No sock-puppet needed beyond normal hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Australian Signals Directorate's Australian Cyber Security Centre — a first-party government authority for its advisories.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ACSC
- cyber.gov.au
- ASD ACSC
tags:
- advisories
- threat-intelligence
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Australian Cyber Security Centre

> The Australian government's official cyber-security authority (ASD's ACSC) — advisories, alerts, and threat guidance you can cite as authoritative.

## When to use
Threat-context research, not person-finding. When you're investigating a vulnerability, malware family, or campaign — especially anything with an Australian nexus — the ACSC publishes advisories, alerts, and mitigation guidance (often with IOCs and affected-product details) that carry government authority. Use it to ground your understanding of a threat and to cite a trusted source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cyber.gov.au/.
2. Browse or search Advisories/Alerts for the CVE, product, actor, or campaign of interest.
3. Read the advisory for affected systems, IOCs (`domain`s/IPs/hashes where given), and mitigations.
4. Note any indicators to check against your own environment or investigation.
5. Pivot: advisory IOCs (`domain`s/IPs) → infrastructure OSINT; actor/campaign names → threat-actor research.

## Inputs → Outputs
- **In:** a threat/vuln/actor query (and IOCs like a `domain` to cross-check)
- **Out:** authoritative advisory text with `domain`/IOC and mitigation details
- **Empty/negative result looks like:** no advisory on your specific threat — the ACSC covers selected, often ANZ-relevant issues; check CISA/NCSC or vendor advisories too.

## Gotchas & OpSec
- Coverage is **selective and ANZ-weighted** — it's not a comprehensive IOC feed; complement with other national CERTs.
- It's reference/guidance, not a target lookup — it tells you about threats, not about a person.
- Fully passive public reading.

## Overlaps ("do both")
- Cross-reference peer government advisories (CISA, UK NCSC) and vendor bulletins — each covers different threats, and corroboration strengthens attribution.

## Trust & verifiability
`trust: trusted` — a first-party government authority; its advisories are authoritative for the threats they cover, though not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australian-cyber-security-centre |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
