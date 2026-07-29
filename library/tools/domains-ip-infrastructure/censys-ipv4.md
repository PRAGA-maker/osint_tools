---
id: censys-ipv4
name: Censys IPv4
description: Use when you have an `ip-address` or `domain` and want Censys's internet-wide scan data on that host — returns open ports, services, certs, and linked `domain`/infrastructure.
url: https://search.censys.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up what services, ports, and certificates a given IP/host exposes from Censys's internet-wide scans.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free account gives a limited monthly query/result quota on Censys Search; higher volume and API access are paid. (The old censys.io/ipv4 path now redirects to search.censys.io.)
opsec: passive
opsecNote: You query Censys's own scan database, not the target host, so the subject's server sees nothing from your lookup. Censys logs your searches against your account — use a research account, not one tied to your identity, for sensitive work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Censys is a reputable internet-measurement platform (originating from University of Michigan research); its host data is authoritative scan data, though snapshots can lag reality.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- censys
- censys-certificates
- search-censys-io
aliases:
- Censys host search
tags:
- infrastructure
- host-scan
- certificates
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Censys IPv4

> Censys's internet-wide host search — enter an IP or hostname and see the ports, services, banners, and certificates it exposes, plus the domains and infrastructure tied to it.

## When to use
You have an `ip-address` or `domain` from an investigation (a server hosting a subject's site, a mail server, a suspicious host) and want to know what it runs and what else is linked to it — sibling domains via shared certs, other services on the same IP, hosting/ASN context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://search.censys.io/ (free account) — the legacy `censys.io/ipv4` URL redirects here.
2. Search a `host:` IP or a `domain`; open the host record.
3. Read exposed ports/services, software banners, and TLS certificates (the certificate names often reveal other hostnames/`domain`s on the same infrastructure).
4. Pivot certificate SANs and shared IPs to enumerate related hosts; feed those into WHOIS/passive-DNS and `[[censys-certificates]]`.
5. Watch the quota — free accounts cap queries/results per month.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** open ports/services, TLS certs, and linked `domain`/`ip-address` infrastructure
- **Empty/negative result looks like:** a host with no recent scan record, or "no results" — the IP may be firewalled from Censys's scanners, not necessarily inactive.

## Gotchas & OpSec
- Human-in-the-loop: account login required (`account-login`); free tier is quota-limited.
- Scan snapshots can be days/weeks old — treat as "last seen," corroborate for current state.
- OpSec: **passive**; you never touch the target host, only Censys's database.

## Overlaps ("do both")
- Pairs with `[[censys-certificates]]` and `[[search-censys-io]]`, and complements Shodan-class scanners — do both, since each internet scanner sees a slightly different view of the same host.

## Trust & verifiability
`trust: trusted` — authoritative internet-measurement data; verify freshness via the scan timestamp before relying on a finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | censys-ipv4 |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
