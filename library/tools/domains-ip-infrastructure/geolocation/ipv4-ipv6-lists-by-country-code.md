---
id: ipv4-ipv6-lists-by-country-code
name: IPverse — IPv4/IPv6 lists by country code
description: Use when you have an `ip-address` or a country and want the authoritative CIDR ranges allocated to that country — returns ip-address ranges / geolocation-by-allocation.
url: https://github.com/ipverse/rir-ip
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- geolocation
bestFor: Mapping a country code to its allocated IP ranges (or checking which country an IP's block belongs to).
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
status: live
pricing: free
costNote: Free, open data (public GitHub repos, updated from RIR delegation files). Clone/download or fetch raw files; no account.
opsec: passive
opsecNote: You download static allocation lists from GitHub and process them locally — nothing touches the target or their network. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community project (ipverse) that mirrors the Regional Internet Registries' delegation data into per-country CIDR files. Source data is authoritative (RIRs); the repo is a convenience packaging, so confirm freshness against the last update.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- domain-dossier
- ipinfo-io
tags:
- ip-geolocation
- cidr
- country-allocation
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# IPverse — IPv4/IPv6 lists by country code

> Per-country CIDR lists built from the Regional Internet Registries' delegation files — the bulk, offline way to answer "which IP ranges belong to country X" or "which country was this block allocated to".

## When to use
You need country-level IP context in bulk: building a geofence/allowlist, filtering a dataset of IPs by country, or sanity-checking a geolocation claim about an `ip-address` against its registry allocation. Works offline once cloned, so it scales to large IP lists without hammering a live geo-IP API.

## How to use it (`bestInteractionPattern`: cli)
1. Go to the ipverse GitHub org and grab the country files (e.g. the `rir-ip` repo), by clone or raw download.
2. For "ranges for a country": open the file named by ISO country code to get its IPv4/IPv6 CIDR blocks.
3. For "country of an IP": match the IP against the CIDR sets (a script or `grepcidr`-style check).
4. Use the ranges to filter, geofence, or corroborate.
5. Pivot: a matched block → `[[domain-dossier]]`/whois for the owning network/ASN; a single IP needing city-level detail → a live geo-IP service like `[[ipinfo-io]]`.

## Inputs → Outputs
- **In:** an ISO country code, or an `ip-address` to classify
- **Out:** `ip-address` CIDR ranges for a country / the allocated-country `geolocation` for an IP
- **Empty/negative result looks like:** an IP that matches no country file (unallocated/bogon/reserved space, or newly reassigned) — meaning registry data doesn't place it, not that it's untraceable.

## Gotchas & OpSec
- **Allocation ≠ physical location:** RIR delegation shows where a block was *allocated*, which can differ from where the host physically sits (VPNs, clouds, sub-assignments). Use for country-scale, not street-level, geolocation.
- Data is a snapshot of RIR files — check the repo's last update; allocations change.
- Fully passive and offline once downloaded.

## Overlaps ("do both")
- Pairs with a live geo-IP lookup (`[[ipinfo-io]]`) for single-IP, city-level detail, and with `[[domain-dossier]]` for the owning network/ASN behind a range.

## Trust & verifiability
`trust: community` — a repackaging of authoritative RIR delegation data. The underlying source is reliable at country granularity; verify freshness and never over-read allocation as precise physical location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipv4-ipv6-lists-by-country-code |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
