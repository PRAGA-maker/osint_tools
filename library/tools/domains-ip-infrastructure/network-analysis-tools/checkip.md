---
id: checkip
name: checkip
description: Use when you have an `ip-address` and want a one-command dossier — returns `geolocation`, `domain` (reverse DNS), ASN/network, and threat-reputation data.
url: https://github.com/jreisinger/checkip
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- network-analysis-tools
bestFor: Aggregating geolocation, DNS, ASN and abuse-reputation for an IP in a single CLI call.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- domain
- employer-org
status: live
pricing: free
costNote: Free and open source (MIT). Core checks work with no keys; a few enrichers (VirusTotal, AbuseIPDB) need free API keys.
opsec: active
opsecNote: Mostly passive database lookups, but by default it also runs active probes (ping, TLS handshake) against the target IP — pass `-no-active` to stay fully passive. Some enrichers submit the IP to third-party APIs (VirusTotal, etc.), which log the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Go project by Jozef Reisinger; auditable code, but a single-maintainer community tool rather than an accredited service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- jreisinger/checkip
- checkip cli
tags:
- domain-and-ip-research
- ip-reputation
- cli
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# checkip

> A single-command CLI (and Go library) that fans an `ip-address` out across many geolocation, DNS, ASN and threat-intel sources and prints a consolidated verdict.

## When to use
You have an `ip-address` — from an email header, a login-alert, a server log, or an image's connection metadata — and want fast, scriptable enrichment: where it geolocates, what `domain` it reverse-resolves to, which network/ASN owns it, and whether it is flagged as malicious.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/jreisinger/checkip@latest` (or grab a release binary).
2. (Optional) export free API keys for VirusTotal / AbuseIPDB to unlock reputation checks; core checks run without them.
3. Run: `checkip 1.2.3.4` — or pipe many IPs via stdin, or add `-j` for JSON.
4. Add `-no-active` to skip ping/TLS probes and stay strictly passive.
5. Read the report: geolocation, reverse DNS, ASN/org, TLS cert details, and a malicious-probability score. Pivot the reverse-DNS `domain` and ASN into WHOIS/passive-DNS tooling.

## Inputs → Outputs
- **In:** `ip-address` (one or many)
- **Out:** `geolocation`, reverse-DNS `domain`, ASN/network owner (`employer-org`), TLS/cert info, malicious-probability rating
- **Empty/negative result looks like:** private/reserved IPs and un-routed addresses return little or no data; a low malicious score is "not currently flagged," not "proven clean."

## Gotchas & OpSec
- Default mode is **active** (ping + TLS to the target) — use `-no-active` when the target must not see you.
- Geolocation is ISP-level, not a street address; treat city-level results as approximate.
- Reputation/enrichment depth depends on which API keys you supply; without them results are thinner.
- Data quality varies by source (db-ip, iptoasn, VirusTotal) — corroborate a critical finding across at least two.

## Overlaps ("do both")
- Pairs with dedicated IP-geolocation and passive-DNS services — checkip gives a fast local roll-up, while those give deeper single-source detail; run checkip first to decide where to dig.

## Trust & verifiability
`trust: community` — MIT-licensed, source-auditable, but it only aggregates other providers' data, so its accuracy is exactly that of the underlying sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkip |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
