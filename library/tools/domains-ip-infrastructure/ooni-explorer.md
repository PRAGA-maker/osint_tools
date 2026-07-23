---
id: ooni-explorer
name: OONI Explorer
description: Use when you have a `domain`/URL and want to know if and where it is blocked/censored — returns country-by-country reachability measurements.
url: https://explorer.ooni.org/search
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether a website is censored or blocked in specific countries, with dated measurements.
selectorsIn:
- domain
selectorsOut:
- domain
- geolocation
status: live
pricing: free
costNote: Fully free and open. All measurement data is public (CC-BY / open) and downloadable; no account needed to search.
opsec: passive
opsecNote: You are reading OONI's public measurement archive, not testing the site yourself, so nothing touches the target and the subject sees nothing. Only your query is exposed to OONI. (Running the OONI Probe app to *create* a measurement is a different, active act — this entry is only about reading Explorer.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Open Observatory of Network Interference (OONI), a well-established nonprofit; measurements are crowd-sourced from volunteers running OONI Probe, so individual data points vary in quality but the aggregate is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- OONI
- Open Observatory of Network Interference
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
- censorship
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# OONI Explorer

> The world's largest open dataset on internet censorship — search a domain to see where and when it has been found blocked, across 240+ countries since 2012.

## When to use
You have a `domain` or URL and need to understand its *reachability* around the world: is it blocked in a given country, when did blocking start, and by what method (DNS tampering, TCP/IP reset, TLS interference). Useful for context on a site tied to an investigation — e.g. corroborating that a service is censored in a region, or dating a takedown/blocking event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://explorer.ooni.org/search .
2. Enter the target `domain`/URL and optionally filter by country and date range.
3. Review the measurement list: each row is a real test from a volunteer's network, flagged OK / anomaly / confirmed-blocked, with the country, network (ASN), date, and detected interference type.
4. Open a measurement for the raw detail (DNS answers, HTTP status, TLS handshake) to understand *how* it was blocked.
5. Pivot: the ASN/geolocation of anomalies feeds network/infrastructure context; for programmatic use, pull the same data from the OONI API/data lake.

## Inputs → Outputs
- **In:** `domain` / URL (optionally + country + dates)
- **Out:** dated reachability measurements per country/network, interference type, and `geolocation` (country/ASN) of each test
- **Empty/negative result looks like:** no measurements for that domain — meaning no volunteer has ever tested it, not that it is unblocked. Absence of data ≠ evidence of reachability.

## Gotchas & OpSec
- Coverage depends on where volunteers run OONI Probe; a country with few probes will have sparse or no data.
- A single "anomaly" can be a transient network fault; look for "confirmed" flags and repeated measurements before concluding censorship.
- OpSec: **passive** — reading Explorer touches only OONI. Do not confuse this with running a probe yourself, which sends real requests to the target from your network.

## Overlaps ("do both")
- Complements reachability/uptime checkers and Censys/Shodan — OONI answers "is it *blocked* and where", those answer "is it *up* and what's running". Use together to separate censorship from downtime.

## Trust & verifiability
`trust: trusted` — OONI is a respected nonprofit and its dataset is open and citable. Treat individual volunteer measurements as noisy but the aggregated, "confirmed" signals as reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ooni-explorer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
