---
id: internet-census-search
name: Internet Census 2012 Search (EXFiLTRATED)
description: Use when you have an `ip-address` or port and want to see what services it exposed in the 2012 IPv4-wide scan — returns historical open-service/port records for that host.
url: https://www.exfiltrated.com/querystart.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Querying the historical Internet Census 2012 (Carna botnet) dataset for a host's open ports/services as of 2012.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- domain
status: degraded
pricing: free
costNote: Free public research front-end over the openly-published Internet Census 2012 dataset; no account.
opsec: passive
opsecNote: You query a static 2012 dataset held by exfiltrated.com — you never touch the target host, so scanning it here is completely passive and cannot alert anyone. (The original data itself was collected by an illegal botnet; you're only reading the published archive.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party search over data gathered by the unauthorised Carna botnet; the dataset is a fixed 2012 snapshot of uneven completeness, and the front-end is intermittently available.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EXFiLTRATED
- Carna botnet census search
- Internet Census 2012
tags:
- historical-scan
- port-scan
- ipv4-census
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Internet Census 2012 Search (EXFiLTRATED)

> A searchable front-end over the Internet Census 2012 — the IPv4-wide port scan collected by the "Carna" botnet — letting you look up a host's open services *as they were in 2012*.

## When to use
You have an `ip-address` (or want to survey a port across the internet) and need a **historical** view: what services/ports that host exposed during 2012. This is a time-machine pivot — useful for establishing what infrastructure looked like years ago, corroborating an old lead, or seeing a device's past exposure that current scanners (Shodan/Censys) no longer show. It is not a live scanner; everything it returns is a 2012 snapshot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.exfiltrated.com/querystart.php (retry if it's temporarily unavailable — the site is intermittently up).
2. Query by IP address (or explore by port); results cover primarily the top ~1024 ports, with only a sampling of full-range scans.
3. Read the records: each port is categorised (Open, Open/Reset, Open/Timeout, Closed/Reset, Timeout) — "Open" means a service responded to a probe in 2012.
4. Pivot: an open service or reverse-DNS `domain` from 2012 becomes a historical infrastructure lead; compare against present-day Shodan/Censys to see what changed.

## Inputs → Outputs
- **In:** `ip-address` (or a port to survey)
- **Out:** historical open-port/service records, associated `ip-address`/`domain`
- **Empty/negative result looks like:** no record for the IP — it wasn't in the sampled set, or was unresponsive in 2012; absence is not proof the host was closed, given the census's partial coverage.

## Gotchas & OpSec
- Data is a fixed **2012** snapshot — never treat it as current; a host's services have almost certainly changed.
- Coverage is partial (top ports, sampled full scans), so gaps are expected.
- Provenance: the underlying scan was collected by an unauthorised botnet; you are only reading the published archive, which is passive and legal, but cite the caveat.
- The front-end is flaky (degraded) — expect intermittent downtime.

## Overlaps ("do both")
- Complements live host scanners (Shodan, Censys): they show the present, this shows 2012 — do both to build a then-vs-now picture of a host's exposed services.

## Trust & verifiability
`trust: unverified` — a third-party archive of botnet-collected data with uneven completeness; use it strictly for historical leads and corroborate with a live scanner or authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internet-census-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
