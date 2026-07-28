---
id: criminal-ip-search
name: Criminal IP Search
description: Use when you have an `ip-address` or `domain` and want its exposed services, open ports, risk score and hosting context — returns asset fingerprints, geolocation and vulnerability data.
url: https://www.criminalip.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Fingerprinting an internet-facing IP or domain (open ports, running services, risk score, geolocation) from an indexed dataset rather than by scanning the target yourself.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Free account gives ~10 searches/day with limited data and no API; CVE-filter searches and API access require a paid Starter plan or higher.
opsec: passive
opsecNote: Queries Criminal IP's pre-collected scan dataset, so the target host does not see a connection from you — your reconnaissance is not visible to the subject. You do, however, log in to Criminal IP, so the platform sees which assets you investigate.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial cyber-threat-intelligence search engine (AISPERA / Criminal IP); data is machine-collected scan output, so treat fingerprints and risk scores as leads to confirm, not ground truth.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- shodan
- censys
- radb
aliases:
- Criminal IP
- criminalip.io
tags:
- Domain/IP investigation
- attack-surface
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Criminal IP Search

> A Shodan-style internet-asset search engine: give it an IP or domain and it returns the ports, services, geolocation and a risk score it has already collected — no active scanning from your side.

## When to use
You have an `ip-address` or `domain` tied to a subject (a server, a home router seen in headers, a site they run) and you want to know what it exposes: open ports, running services and versions, TLS certs, hosting/geolocation and a threat/risk assessment. Because the data is pre-indexed, you learn all this without touching the target host — useful when infrastructure is the pivot and you must stay passive.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://www.criminalip.io/ and log in (search requires login).
2. Choose the search type: **Asset Search** (IP), **Domain Search**, **Exploit Search** (CVE) or **Image Search** (device screenshots).
3. Enter the `ip-address` or `domain` and run the query.
4. Read the report: open ports and services, product/version fingerprints, geolocation and ASN, associated domains, and the risk/threat score.
5. Pivot: service versions feed CVE lookups; the ASN/geolocation and co-hosted domains feed `[[radb]]` and reverse-IP/WHOIS work; corroborate anything important against `[[shodan]]` or `[[censys]]`.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** open ports/services, `geolocation`, ASN/hosting, associated `domain`s, risk score
- **Empty/negative result looks like:** "no result" means the host isn't in Criminal IP's index (never scanned, offline, or firewalled) — it does not prove the host doesn't exist; cross-check another scanner.

## Gotchas & OpSec
- Human-in-the-loop: mandatory login, and the free tier caps you at ~10 searches/day with reduced fields — you'll hit the wall on any real IP list.
- Passive toward the target, but Criminal IP logs your searches; use a research account.
- Scan data can be stale or fingerprint-guessed; a "risk score" is a heuristic, not a verdict — verify before acting on it.

## Overlaps ("do both")
- Pairs with `[[shodan]]` and `[[censys]]` — each scanner indexes a different slice of the internet at different times, so an asset missing from one often appears in another. Run the same IP through all three.
- Feeds `[[radb]]` for the routing/ASN registration behind the address.

## Trust & verifiability
`trust: unverified` — a commercial CTI product with useful coverage, but the results are automated scan output and proprietary scoring; treat them as leads to confirm against a second source, not as authoritative fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | criminal-ip-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
