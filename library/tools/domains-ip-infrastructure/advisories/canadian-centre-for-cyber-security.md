---
id: canadian-centre-for-cyber-security
name: Canadian Centre for Cyber Security
description: Use when you have a product/CVE or domain-context question and want authoritative Canadian government security alerts and guidance — returns advisories, alerts, and threat reports.
url: https://www.cyber.gc.ca/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- advisories
bestFor: Reading official Canadian cyber advisories, alerts, and threat guidance.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public government resource; no account.
opsec: passive
opsecNote: Passive — you read published government advisories; nothing about any target is transmitted, and the site sees only a normal page visit. No sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada's official national cyber-security authority (part of the Communications Security Establishment); its alerts and advisories are authoritative first-party government publications.
missingPersonsRelevance: low
coverage:
- ca
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CCCS
- cyber.gc.ca
- Canadian Centre for Cyber Security
tags:
- advisories
- government
- threat-intel
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Canadian Centre for Cyber Security

> Canada's official cyber-security authority: the authoritative source of Canadian security alerts, vendor advisories, and threat guidance.

## When to use
You're assessing infrastructure or a product in an investigation and want an authoritative, government-issued read on known vulnerabilities, active threats, or defensive guidance — especially where a Canadian nexus matters. A reference/context source rather than a selector-lookup: it tells you what official Canada is warning about, not who owns a given domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cyber.gc.ca/ (bilingual; `/en/` for English).
2. Browse the **Alerts and advisories** feed for current critical vulnerabilities (e.g. named CVEs in widely-used software) and vendor patch advisories.
3. Search or filter by product/vendor to see whether infrastructure relevant to your case is covered by an active advisory.
4. Use the **Guidance** section for threat assessments and hardening baselines.
5. Pivot: a CVE/advisory affecting a `domain`'s stack contextualises risk and timing; cross-reference with US CISA/other national CERT feeds for corroboration.

## Inputs → Outputs
- **In:** a product/vendor/CVE or `domain`-context question
- **Out:** official advisories, alerts, and guidance documents (context that informs `domain`/infrastructure assessment)
- **Empty/negative result looks like:** no advisory matching your product/CVE — it may simply not have been the subject of a Canadian bulletin (check CISA/other CERTs), not that no issue exists.

## Gotchas & OpSec
- It's an advisory/guidance publisher, not an investigative lookup — it won't resolve a domain, IP, or person.
- Canada-centric emphasis; for full coverage pair with other national CERTs.
- Advisories are point-in-time; check dates and follow-ups.
- OpSec: fully passive — reading public government pages.

## Overlaps ("do both")
- Read alongside US CISA advisories and other national CERT feeds — the major agencies often cover the same critical CVEs, and cross-referencing confirms severity and affected-version details.

## Trust & verifiability
`trust: trusted` — a first-party national government cyber authority; its advisories are authoritative, with the only caveat being scope (Canada-focused) rather than reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-centre-for-cyber-security |
