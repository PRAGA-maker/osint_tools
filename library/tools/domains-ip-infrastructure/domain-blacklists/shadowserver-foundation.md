---
id: shadowserver-foundation
name: Shadowserver Foundation
description: Use when you have a `domain`/`ip-address` or a network you're authorized over and want abuse/exposure intelligence — returns reputation, malicious activity, and exposed-service reports.
url: https://www.shadowserver.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Authoritative, non-profit abuse and exposure intelligence on IPs/domains, plus free daily network reports for networks you own.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Non-profit; core data and reports are free. Detailed victim/network reports are provided free to the verified owner of a network/CIDR or a national CSIRT (subscription with proof of authority).
opsec: passive
opsecNote: Shadowserver's data comes from its own honeypots, sinkholes, and internet-wide scanning — you query their datasets, not the target, so the subject is not alerted. Free network reports require you to prove authority over the network you're asking about.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, respected non-profit security organisation working with CSIRTs and law enforcement worldwide; data is high-quality and mission-driven.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- shadowserver
aliases:
- Shadowserver
- shadowserver.org
tags:
- threat-intel
- abuse-intelligence
- exposed-services
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Shadowserver Foundation

> A non-profit that watches the internet for malicious and exposed hosts, and hands the intelligence — free — to network owners, CSIRTs, and researchers.

## When to use
You're investigating infrastructure behind a `domain`/`ip-address` and want reputable abuse intelligence: is this IP part of a botnet, sinkholed, running an exposed/vulnerable service, or associated with compromise? Or you legitimately operate a network and want Shadowserver's free daily reports of infected/exposed hosts on it. It's an infrastructure/abuse-intelligence source; direct missing-persons value is low (vetting hosting behind a case).

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at https://www.shadowserver.org/ — explore public dashboards (the Shadowserver Dashboard shows aggregate scanning/exposure trends by country and ASN) and documentation.
2. For **general research**: use the public reports/dashboard and the API to look at exposure and malicious-activity statistics tied to networks/`domain`s.
3. For **detailed host-level reports on a network you control**: subscribe via Shadowserver — you must prove authority over the CIDR/ASN (or be a national CSIRT). Reports then arrive daily by email/API.
4. Read: infected hosts, exposed services, sinkhole hits, honeypot observations. Pivot: correlate flagged `ip-address`es/`domain`s with passive DNS, `[[alienvault-otx]]`, and GreyNoise.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, ASN/CIDR (for owned-network reports)
- **Out:** abuse/reputation signals, exposed-service and malicious-activity reports, related `ip-address`es/`domain`s
- **Empty/negative result looks like:** no observations for a host — Shadowserver's sensors/scans didn't see it doing anything notable; that's reassuring but not proof of cleanliness, and detailed data may simply require network-ownership verification you don't have.

## Gotchas & OpSec
- **Legal gate:** the rich, host-level victim reports are restricted to verified network owners/CSIRTs — you can't pull another organisation's detailed report.
- Public dashboards are aggregate/statistical; per-target depth needs authorised access.
- OpSec: passive — you query Shadowserver, never the target.

## Overlaps ("do both")
- Complements `[[alienvault-otx]]`, GreyNoise, and passive-DNS feeds — Shadowserver's honeypot/sinkhole/scan vantage catches exposure and botnet membership those may miss, and vice versa. See also the related `[[shadowserver]]` entry.

## Trust & verifiability
`trust: trusted` — a mission-driven non-profit relied on by CSIRTs and law enforcement globally; the data is authoritative, with the caveat that the most detailed reports are access-gated by network ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadowserver-foundation |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
