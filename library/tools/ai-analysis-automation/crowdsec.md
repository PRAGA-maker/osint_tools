---
id: crowdsec
name: CrowdSec
description: Use when you have an `ip-address` and want crowd-sourced threat reputation on it — CrowdSec's CTI shows whether the IP is a known attacker, its behaviors, and geolocation/AS.
url: https://github.com/crowdsecurity/crowdsec
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Checking an IP's crowd-sourced malicious reputation (attack categories, ranges, first/last seen) via CrowdSec CTI.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
costNote: The engine and community blocklist are open source (MIT) and free. The CTI reputation lookup (console/API) has a free tier requiring a free account/API key; higher query volumes need a paid plan.
opsec: passive
opsecNote: Looking up an IP in CrowdSec CTI queries CrowdSec's database, not the host at that IP, so the target machine isn't contacted or alerted. Running the CrowdSec agent on your own server is a separate, defensive deployment. Use a dedicated account/API key for CTI queries.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Widely-adopted open-source security project (crowdsecurity); CTI is aggregated from a large community sensor network, so reputation reflects observed behavior, not attribution of a person.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
aliases:
- CrowdSec
- crowdsec CTI
tags:
- ip-reputation
- threat-intel
- crowd-sourced
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# CrowdSec

> An open-source, crowd-sourced security engine whose CTI turns an IP address into a reputation verdict — is this IP a known scanner/attacker, what has it done, and where does it sit.

## When to use
You have an `ip-address` (from a log, a header, a connection, a suspicious message) and want to know if it's flagged as malicious by a large community sensor network. CrowdSec CTI reports attack categories, the ranges/AS it belongs to, first/last-seen, and geo — useful for triaging an IP tied to a scam, intrusion, or suspicious contact in an investigation, and for deciding whether an IP is infrastructure worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Fastest path: query CrowdSec CTI via its console/API (create a free account for an API key) — or run the open-source engine and use `cscli` if you operate a sensor.
2. Submit the target `ip-address`.
3. Read the CTI record: reputation/aggression score, attack scenarios observed, background noise vs targeted, AS/range, and geolocation (`selectorsOut`).
4. Pivot: the AS/range and behavior class point to hosting/botnet infrastructure; geo/AS feeds broader IP-infrastructure mapping.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `ip-address` reputation (attack categories, ranges, first/last seen), `geolocation`/AS context
- **Empty/negative result looks like:** "clean"/unknown IP — no community reports, meaning the IP isn't a known offender in CrowdSec's data, NOT that it's proven benign.

## Gotchas & OpSec
- Human-in-the-loop: CTI queries need a free account/API key (`api-key`).
- OpSec: passive — you query CrowdSec's aggregated data, not the target host.
- Reputation is behavioral and community-sourced: it tells you what an IP has *done*, not who used it; dynamic/shared IPs can be flagged for prior tenants.

## Overlaps ("do both")
- Pairs with AbuseIPDB, GreyNoise, and Shodan — cross-check an IP across reputation sources, since each has different sensor coverage; GreyNoise distinguishes internet-wide noise, CrowdSec adds community attack context.

## Trust & verifiability
`trust: community` — a well-established open-source project with a large sensor network; its verdicts are reliable indicators of observed malicious behavior, but they classify an address, not a person, so treat attribution cautiously.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crowdsec |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
