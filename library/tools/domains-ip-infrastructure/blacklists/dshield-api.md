---
id: dshield-api
name: DShield API
description: Use when you have an `ip-address` and want to know if it has been seen attacking networks — returns attack/report counts, targeted-systems totals, ASN, and threat-feed associations.
url: https://isc.sans.edu/api/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Checking whether an IP has a history of malicious/attack activity from SANS ISC honeynet data.
selectorsIn:
- ip-address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Completely free, no authentication or API key required; best-effort with soft rate limits (may return HTTP 429 under load).
opsec: passive
opsecNote: Fully passive — you query SANS ISC's aggregated honeypot data about an IP; the IP's owner is never contacted and sees nothing. Only SANS logs your API request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Run by the SANS Internet Storm Center, a respected security-community project; data is aggregated from a broad honeynet of contributing sensors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- sans-internet-storm-center-diary-full-text
aliases:
- SANS ISC API
- Internet Storm Center API
- isc.sans.edu/api
tags:
- threat-intelligence
- ip-reputation
- blacklists
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# DShield API

> A free, no-auth REST API over the SANS Internet Storm Center honeynet: hand it an IP and learn whether the wider internet has seen it attacking things.

## When to use
You have an `ip-address` — from a log, an email header, a link-tracker, a server hit — and want a reputation signal: is this IP a known source of scanning/attacks, and against how many targets? Reach for DShield to add threat context to an IP you've already geolocated. A high report count with recent activity suggests a compromised host, VPN/hosting used for abuse, or a scanner — useful for judging whether an IP represents the actual person or shared/abused infrastructure.

## How to use it (`bestInteractionPattern`: api)
1. Query the IP endpoint directly (no key needed): `https://isc.sans.edu/api/ip/<IP>` — append `?json` for JSON, default is XML.
2. Read the returned fields: total packets/reports, number of targeted systems, first/last-seen date range, AS number and name, network CIDR, and any threat-feed memberships.
3. Interpret: many reports across many targets = an IP actively involved in attacks; zero reports = simply not seen by ISC sensors (not proof it's clean).
4. Use related endpoints for context — `/api/port/<n>` for port activity, `/api/threatlist/` for feeds.
5. Pivot: the ASN/CIDR feeds infrastructure mapping; a "known-attacker" verdict downgrades how much the IP tells you about a specific person.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** attack/report counts, targeted-systems count, date range, `employer-org` (ASN/AS name/CIDR), threat-feed associations
- **Empty/negative result looks like:** zero reports and no feed hits — the IP simply hasn't been observed by ISC's honeynet; treat as "no signal", not "confirmed benign".

## Gotchas & OpSec
- Coverage is honeynet-based: absence of reports ≠ innocence, and residential IPs behind NAT are noisy/ambiguous.
- Best-effort service — expect occasional HTTP 429; back off and retry.
- OpSec: passive and safe; the target is never touched.

## Overlaps ("do both")
- Pairs with `[[sans-internet-storm-center-diary-full-text]]` for narrative threat context, and with IP-geolocation/proxy tools — geolocation says *where* the IP is, DShield says *whether it misbehaves*. Cross-check reputation against a second feed (e.g. AbuseIPDB) before acting.

## Trust & verifiability
`trust: trusted` — SANS ISC is a long-standing, well-regarded community project; the data is aggregated sensor telemetry, authoritative as a signal but always to be corroborated with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dshield-api |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
