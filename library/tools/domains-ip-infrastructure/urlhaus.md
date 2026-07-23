---
id: urlhaus
name: URLhaus
description: Use when you have a `domain`/URL, host or `ip-address` and want to know if it distributes malware — returns malicious URLs, payloads and hosting details.
url: https://urlhaus.abuse.ch
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether a domain/URL/host is a known malware-distribution site, with associated payloads.
selectorsIn:
- domain
- ip-address
- document-id
selectorsOut:
- domain
- ip-address
- document-id
status: live
pricing: free
costNote: Free and public — browsable database, downloadable feeds, and a free API (incl. bulk). Operated by abuse.ch (Spamhaus).
opsec: passive
opsecNote: You query URLhaus's own database of already-collected malicious URLs, not the malware sites — the subject sees nothing. Only URLhaus sees your query. Never browse the listed URLs directly; they serve live malware. Analyse payloads by hash in a sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by abuse.ch (now part of Spamhaus) — a highly reputable, community-standard threat-intel source consumed across the industry. A listing is authoritative; freshness is good but a clean result isn't proof of safety.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- abusech
- malwarebazaar
- yaraif
- zeus-c2-tracker
- zeus-tracker
aliases:
- abuse.ch URLhaus
- urlhaus.abuse.ch
tags:
- domain-and-ip-research
- malware
- threat-intel
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# URLhaus

> abuse.ch's database of malware-distribution URLs — check a domain, URL, host, or IP against a large, authoritative record of sites known to serve malware, with the payloads they delivered.

## When to use
You have a suspicious `domain`/URL, a hosting `ip-address`, or a payload hash and want to know whether it's tied to malware distribution. Strong for triaging a link in a case, enriching an IOC, or pivoting: from a malicious URL to its hosting infrastructure and the malware family/hashes it dropped.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://urlhaus.abuse.ch and search the `domain`/URL, host, or `ip-address` (or query the free API / bulk feeds for automation).
2. Read the entry: the malicious URL(s), status (online/offline), hosting IP/ASN, associated malware family, and payload hashes (`document-id`).
3. Treat a match as authoritative "known malware distribution"; record the URL/IP/hash as IOCs.
4. **Never open a listed URL** in a real browser — analyse payload hashes in a sandbox / `[[metadefender]]` / VirusTotal instead.
5. Pivot: hosting `ip-address` feeds infrastructure clustering; payload hash feeds `[[malwarebazaar]]` and sample analysis.

## Inputs → Outputs
- **In:** `domain`/URL, `ip-address`, or payload hash (`document-id`)
- **Out:** malicious URLs, hosting `ip-address`/ASN, malware family, and payload hashes (`document-id`)
- **Empty/negative result looks like:** no match — the indicator isn't in URLhaus, which is *inconclusive*, not clearance. Cross-check other feeds.

## Gotchas & OpSec
- A clean result means "not tracked by URLhaus", not "safe" — combine with other threat-intel sources.
- Entries carry status (online/offline); an "offline" URL may still be significant historically.
- OpSec: **passive** on URLhaus's pages, but the listed links are live malware — sandbox everything, never click through.

## Overlaps ("do both")
- Part of the abuse.ch suite — pairs with `[[malwarebazaar]]` (samples by hash) and other trackers, plus phishing feeds like `[[https-openphish-com-feed-txt]]`. Cross-reference for full coverage.

## Trust & verifiability
`trust: trusted` — abuse.ch/Spamhaus is an industry-standard, widely-consumed threat-intel provider. A listing is high-confidence; corroborate current status and analyse samples in a sandbox before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urlhaus |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, document-id → domain, ip-address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
