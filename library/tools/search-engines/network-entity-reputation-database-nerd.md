---
id: network-entity-reputation-database-nerd
name: Network Entity Reputation Database (NERD)
description: Use when you have an `ip-address` and want its threat reputation and history — returns malicious-activity reports, first/last seen, and origin `geolocation`.
url: https://nerd.cesnet.cz/
category: search-engines
path:
- search-engines
bestFor: Checking whether an IP has been reported as malicious and reviewing its abuse history.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free public access to the reputation data via web and API; some raw Warden alert data is restricted to trusted CSIRT partners.
opsec: passive
opsecNote: Passive — you query NERD's aggregated database, not the target IP itself, so the address you look up is never contacted. Run by CESNET (Czech academic network); assume queries are logged by the operator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CESNET's Liberouter team (Czech National Research and Education Network); aggregates reputable feeds (Warden, DShield, AlienVault OTX, MISP, public blacklists).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ip-search-network-entity-reputation-database
aliases:
- NERD
- CESNET NERD
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
- ip-reputation
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Network Entity Reputation Database (NERD)

> A free reputation database of malicious IPs — aggregates multiple threat feeds into one searchable, API-accessible record of "everything we know" about an address.

## When to use
You have an `ip-address` (from a log, an email header, a login alert, a suspicious connection) and want to know whether it has a history of malicious behaviour — scanning, brute-forcing, spam, botnet activity — and when/where it was reported. NERD consolidates many feeds so you don't have to poll each blacklist separately.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nerd.cesnet.cz/ (free; no account for basic lookups).
2. Search by `ip-address` — or filter across the database by country code, ASN, tag, or blacklist presence for bulk research.
3. Read the entity page: reputation score, categories of reported activity, first/last-seen timestamps, ASN/`employer-org`, and origin `geolocation`.
4. For automation, use the NERD API.
5. Pivot: the ASN/network owner feeds infrastructure mapping; a "clean" verdict shifts suspicion elsewhere in the trace.

## Inputs → Outputs
- **In:** `ip-address` (or bulk filters: country, ASN, tag)
- **Out:** reputation score, reported-activity categories, first/last seen, ASN owner (`employer-org`), `geolocation`
- **Empty/negative result looks like:** no record / neutral reputation — the IP hasn't been reported to NERD's feeds; not a guarantee it is benign.

## Gotchas & OpSec
- Coverage is only as good as its source feeds — a malicious-but-unreported IP shows clean.
- Reputation is about the *address*, which can be shared, reassigned (CGNAT, VPN, cloud), or spoofed — don't attribute it to a specific person.
- The richest raw data (Warden alerts) is restricted to vetted CSIRT partners; public users see the aggregated view.
- Historical reports may reflect past tenants of a reassigned IP.

## Overlaps ("do both")
- Pairs with [[ip-search-network-entity-reputation-database]] and general IP-enrichment tools ([[checkip]]) — NERD gives the reputation/history angle, while geolocation/passive-DNS tools add ownership and hosting context.

## Trust & verifiability
`trust: trusted` — maintained by an established national research-and-education network (CESNET) and built on well-known threat feeds; the aggregation methodology is documented.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | network-entity-reputation-database-nerd |
| category | search-engines |
| selectorsIn → selectorsOut | ip-address → geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
