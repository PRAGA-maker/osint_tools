---
id: internet-census-2012
name: Internet Census 2012
description: Use when you need a historical 2012 snapshot of an `ip-address`/`domain` — returns that era's reverse-DNS, open-port and geolocation records from a public-domain IPv4 scan.
url: http://census2012.sourceforge.net/paper.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up what an IPv4 address hosted or resolved to in 2012 for historical infrastructure context.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
- geolocation
status: degraded
pricing: free
costNote: All data released into the public domain; free to download, but the datasets are very large (terabytes) and mirror availability varies.
opsec: passive
opsecNote: Fully passive — you query a static, downloaded archive, never the live target. No signal reaches the address you are researching. Note the data was collected via the illegal Carna botnet; it is public-domain and widely cited, but be aware of its provenance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known 2012 research artifact (anonymous author, "Carna botnet"); frequently cited in academic work, but unofficial and the scan method was unauthorized.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Carna Botnet
- Internet Census 2012
- IPv4 census
tags:
- historical-dataset
- ipv4-scan
- infrastructure-analysis
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Internet Census 2012

> A public-domain, one-time scan of the entire IPv4 internet from 2012 — a historical snapshot of reverse-DNS, open ports and geolocation for hundreds of millions of addresses.

## When to use
You need to know what an `ip-address` or `domain` looked like in 2012 — what it reverse-resolved to, which ports/services were open, roughly where it geolocated — as historical context in an infrastructure investigation. This is a frozen archive, not a live lookup, valuable only for that specific era.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the project paper at http://census2012.sourceforge.net/paper.html for scope and data-format notes.
2. Locate a current mirror of the datasets (the original torrents/downloads are large and mirror availability drifts over time).
3. Download the relevant tab-separated log files — reverse DNS (~1B+ records), ICMP ping responses (~420M IPs), service probes, TCP/IP fingerprints, geolocation.
4. Grep/filter locally for the target `ip-address` or `domain`.
5. Pivot: compare the 2012 record against present-day passive-DNS/WHOIS to see how ownership or hosting changed.

## Inputs → Outputs
- **In:** `ip-address` or `domain` (looked up within the downloaded 2012 archive)
- **Out:** 2012-era reverse-DNS `domain`, open-port/service data, `geolocation`
- **Empty/negative result looks like:** no record for the address in the 2012 scan — the census was broad but not exhaustive, and reflects only that single point in time.

## Gotchas & OpSec
- Strictly historical: everything is a 2012 snapshot and says nothing about the address today.
- The datasets are enormous and hosted via drifting mirrors/torrents; expect to hunt for a live copy and to process terabytes locally.
- Provenance caveat: data was gathered by the unauthorized "Carna botnet," which compromised devices with default credentials — the results are public-domain and widely used in research, but the collection method was illegal.

## Overlaps ("do both")
- Pairs with present-day passive-DNS and WHOIS-history tooling — the census gives the 2012 baseline, and those tools show the change over time; use them together to trace an address's lifecycle.

## Trust & verifiability
`trust: community` — an anonymously-authored but heavily-cited research dataset; accurate for 2012 within its coverage, but unofficial and superseded by later legitimate scan projects for anything recent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internet-census-2012 |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
