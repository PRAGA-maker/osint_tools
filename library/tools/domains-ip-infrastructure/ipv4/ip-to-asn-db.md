---
id: ip-to-asn-db
name: IP to ASN DB
description: Use when you have an `ip-address` and want the ASN, network prefix and owning organization it belongs to — returns the ASN, prefix and org (`domain`).
url: https://iptoasn.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Fast, free IP-to-ASN/organization mapping via a downloadable dataset or a simple lookup.
selectorsIn:
- ip-address
selectorsOut:
- domain
status: live
pricing: free
costNote: Free; the full IP-to-ASN dataset is downloadable (updated hourly) and there is no account or API key.
opsec: passive
opsecNote: Lookups run against a published dataset, not the target host, so the subject is never contacted. Downloading the dataset for offline use is the most private option.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Frank Denis (jedisct1) from public BGP/routing data; the dataset is open and its mapping is verifiable against RIR records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- onyphe
aliases:
- iptoasn.com
- IP to ASN
tags:
- ip-research
- asn
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# IP to ASN DB

> A free, open IP-to-ASN mapping — feed it an IP and get the autonomous system number, the covering prefix, and the organization that operates it, from a dataset you can also download whole.

## When to use
You have an `ip-address` (from a log, email header, or another tool) and need to know *whose network* it lives on: the ASN, the routing prefix, and the operator (ISP/hosting/company). That's the first step in attributing an IP to a provider and clustering multiple IPs that share the same AS or org.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iptoasn.com/ and enter the `ip-address` for a quick lookup, or download the full TSV dataset for offline/bulk use.
2. Read the result: ASN, AS description/organization, the country, and the announced prefix covering the IP.
3. For many IPs, load the downloadable dataset locally and join your IPs against it — no rate limits.
4. Pivot: the ASN/org (`domain`) tells you the hosting provider or ISP; group other IPs in the same AS/prefix as related infrastructure.

## Inputs → Outputs
- **In:** an `ip-address` (IPv4/IPv6)
- **Out:** ASN, AS organization/description (`domain`), covering prefix, country
- **Empty/negative result looks like:** an unrouted/reserved/private IP maps to no public ASN — that's expected (not globally announced), not a lookup failure.

## Gotchas & OpSec
- ASN/org identifies the *network operator*, not the end user — a residential or cloud IP's org is the ISP/host, not the person.
- The dataset is a periodic snapshot of BGP announcements; very recent reassignments may lag.
- OpSec: fully passive; offline dataset use leaks nothing at all.

## Overlaps ("do both")
- Pairs with `[[onyphe]]` and WHOIS/RIR lookups — this gives the ASN/org fast, those add exposed services, certificates and the registry's assignment details for the same IP.

## Trust & verifiability
`trust: trusted` — an open dataset built from public routing data by a well-known maintainer; every mapping can be cross-checked against RIR/BGP records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-to-asn-db |
