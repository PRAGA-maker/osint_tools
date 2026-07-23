---
id: threatminer-org
name: ThreatMiner.org
description: Use when you have a `domain`, `ip-address`, file hash, or SSL cert and want linked threat-intel — returns related domains/IPs, WHOIS, and malware/APT associations to pivot on.
url: https://www.threatminer.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Pivoting an indicator (domain/IP/hash/cert) into related infrastructure and threat-report associations.
input: Domain, IP, file hash (MD5/SHA1/SHA256), SSL certificate, or URL
output: Threat reports, IOC data, WHOIS info, malware associations, related indicators
selectorsIn:
- domain
- ip-address
- document-id
selectorsOut:
- domain
- ip-address
status: live
pricing: free
opsec: passive
opsecNote: ThreatMiner serves aggregated data from many upstream sources, so you query ThreatMiner rather than the target — the subject/host isn't contacted or alerted. Data can be stale; treat associations as leads and re-verify freshness at the primary source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Non-profit threat-intel aggregation portal (CC BY 4.0) with large domain/host/file datasets; community-run, data quality varies by source and age.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ThreatMiner
- threatminer.org
tags:
- threat-intel
- ioc-pivoting
- passive-dns
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# ThreatMiner.org

> A free threat-intelligence data-mining portal — drop in a domain, IP, hash, or certificate and it returns the related indicators, WHOIS, passive DNS, and malware/APT reports tied to it.

## When to use
You have an indicator from an investigation — a suspicious `domain`, an `ip-address`, a file hash (`document-id`), or a TLS certificate — and want to see what else is connected to it: co-hosted domains, resolving IPs, associated malware samples, and APT report mentions. ThreatMiner is built for *pivoting*: each result surfaces new indicators to chase, which helps map the infrastructure behind a scam, phishing kit, or malicious host in a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.threatminer.org/ and enter your indicator (domain/IP/hash/cert/URL).
2. Browse the tabbed results: WHOIS, passive DNS, related samples, subdomains, URIs, and report references (`selectorsOut`).
3. Follow the related indicators to expand the graph; each domain/IP is clickable to pivot further.
4. Automate with the `/api.php` endpoint or the Maltego transforms for bulk pivoting; corroborate anything important at the primary source.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `document-id` (MD5/SHA1/SHA256 hash), or TLS certificate/URL
- **Out:** related `domain`s and `ip-address`es, WHOIS, passive DNS, malware/APT associations
- **Empty/negative result looks like:** no associations for the indicator — it may be clean, too new, or simply absent from ThreatMiner's sources; absence isn't proof of benignity.

## Gotchas & OpSec
- Human-in-the-loop: none (open access + free API).
- OpSec: passive — aggregated data, no contact with the target host.
- Freshness varies: ThreatMiner mirrors upstream feeds that can lag; re-check current state (live DNS/WHOIS) before acting on an association.

## Overlaps ("do both")
- Pairs with VirusTotal, [[censys]], and passive-DNS/WHOIS-history services — cross-check indicators, since each aggregator has different source coverage and update cadence; VirusTotal often has fresher sample data.

## Trust & verifiability
`trust: community` — a non-profit aggregator (CC BY 4.0) with large datasets, useful for lead generation and pivoting. Because it re-serves third-party data of varying age, treat findings as leads and confirm the critical ones at the authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threatminer-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, document-id → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
