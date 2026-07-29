---
id: kloth
name: Kloth
description: Use when you have a `domain` or `ip-address` and want quick web-based DNS/network lookups (DNS records, DNSBL/blacklist checks) without a shell — returns DNS/`ip-address` data.
url: http://www.kloth.net/services
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Browser-based DNS record and DNS-blacklist (RBL) lookups for a domain or IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: degraded
pricing: free
costNote: Free web-based network query services; no account.
opsec: passive
opsecNote: DNS/RBL lookups run from Kloth's servers against public DNS, not against the target's host, so the subject is not alerted. As with any hosted lookup, the operator (Kloth) sees your queries — use a VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing personal/community network-tools site (kloth.net); a thin web front-end over standard DNS queries. Confirm results against a second resolver; the site is old and its uptime is not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- kloth.net
tags:
- domain-and-ip-research
- dns
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Kloth

> A veteran web-tools site offering browser-based DNS lookups and DNS-blacklist (RBL) checks — handy when you want a quick DNS answer for a domain/IP and have no shell to hand.

## When to use
You have a `domain` or `ip-address` and want to resolve its DNS records or check whether an IP is listed on mail blacklists (DNSBL/RBL) — e.g. assessing a mail server tied to a subject — without installing `dig`/`nslookup` or from a locked-down machine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.kloth.net/services and pick the relevant tool (DNS query / DNSBL check).
2. Enter the `domain` or `ip-address` and the record type (A, MX, TXT, PTR, etc.).
3. Read the returned records or blacklist status.
4. If the site is slow/unavailable, fall back to a modern resolver (command-line `dig`, or a service like a hosted DNS-lookup tool).
5. Pivot: MX/PTR records and resolved IPs feed WHOIS, passive-DNS, and host-scan tools (`[[censys-ipv4]]`).

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** DNS records (A/MX/TXT/PTR…), DNSBL listing status
- **Empty/negative result looks like:** NXDOMAIN / empty record set, or a not-listed RBL result — confirm against a second resolver, since a single old service can be stale or misconfigured.

## Gotchas & OpSec
- **Degraded:** the site is old and availability is inconsistent — treat it as a convenience, not a dependable primary.
- Always corroborate DNS answers with another resolver.
- OpSec: **passive**; queries go to public DNS via Kloth, not to the target.

## Overlaps ("do both")
- Interchangeable with any DNS-lookup service and superseded by command-line `dig`; pair resolved hosts with `[[censys-ipv4]]` for what those IPs actually run.

## Trust & verifiability
`trust: community` — a thin front-end over public DNS; results are verifiable by re-querying any resolver.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kloth |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
