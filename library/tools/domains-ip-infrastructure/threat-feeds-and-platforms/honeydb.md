---
id: honeydb
name: HoneyDB
description: Use when you have an `ip-address` and want to know whether it has been caught attacking honeypots — returns threat/reputation data and recent malicious-activity logs for that host.
url: https://honeydb.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Checking whether an IP appears in a live honeypot-network threat feed and what services it has been probing.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Free account gives access to the community threat feed and API with rate limits; higher-volume/commercial use is on paid subscription tiers.
opsec: passive
opsecNote: You query HoneyDB's collected honeypot data, not the target IP itself — no packet ever touches the host you are looking up, so this is passive. Registering creates an account tied to your email; use an operational address.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent honeypot-network project with a public real-time feed; data is observational (what its sensors saw), not an authoritative blocklist.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- HoneyDB threat feed
tags:
- threat-intelligence
- ip-reputation
- honeypot
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# HoneyDB

> A honeypot-network threat feed — tells you whether an `ip-address` has been seen attacking sensors, and which protocols it probed.

## When to use
You have an `ip-address` from your investigation (a login source, a scanner hitting your infra, a suspicious host in a log) and want to know if it is known-malicious. HoneyDB aggregates real-time interactions across its honeypot network (RDP, HTTP, SIP, Telnet, etc.), so a hit tells you the host has been conducting attacks and adds threat context to an IP pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://honeydb.io/ and generate API credentials if scripting.
2. Look up the `ip-address` in the "Bad Hosts" / threat-feed view, or query the API endpoint for that IP.
3. Read the record: whether the IP appears, how recently, and which services/ports it was seen attacking.
4. Pivot: a flagged IP feeds broader infrastructure OSINT (WHOIS, passive DNS, hosting/ASN) to characterise the actor; a clean result means it's just not in HoneyDB's sensor data.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** reputation/threat verdict and recent honeypot-attack activity for that `ip-address`
- **Empty/negative result looks like:** the IP is absent from the feed — this means HoneyDB's sensors haven't logged it, NOT that the host is proven clean (honeypot coverage is partial).

## Gotchas & OpSec
- Observational data: HoneyDB reports what its honeypots saw. Absence ≠ safe; presence ≠ the IP's only activity.
- Free tier is rate-limited; heavy automated lookups need a paid plan.
- Best treated as one signal in an IP-reputation stack, not a definitive blocklist.

## Overlaps ("do both")
- Pair with other IP-reputation/threat feeds (AbuseIPDB, GreyNoise, passive-DNS tools) — cross-referencing multiple honeypot/telemetry sources catches hosts any single sensor network misses.

## Trust & verifiability
`trust: community` — an independent honeypot project publishing its own sensor observations; credible telemetry but self-generated and partial, so corroborate a verdict against a second feed before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | honeydb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
