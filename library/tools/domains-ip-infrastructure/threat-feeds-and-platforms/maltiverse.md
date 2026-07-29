---
id: maltiverse
name: Maltiverse
description: Use when you have an `ip-address`, `domain`, URL, or file hash and want a threat-intel verdict — returns malicious/suspicious classification, sources, and related indicators.
url: https://maltiverse.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Checking whether an IP/domain/URL/hash is a known bad indicator, with aggregated sourcing and links to related IOCs.
selectorsIn:
- ip-address
- domain
- document-id
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free community account gives web search and limited API access to the IOC dataset; higher API volume, feeds, and enterprise features are paid.
opsec: passive
opsecNote: You query Maltiverse's aggregated IOC database, not the indicator's owner — the target infrastructure is not touched, so it's passive and doesn't tip anyone off. You do disclose the indicator you're researching to Maltiverse; use hash/indicator lookups (which reveal nothing new) rather than uploading anything sensitive.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: An established threat-intelligence platform aggregating and scoring IOCs from many feeds; reputable, though (like all aggregators) a verdict is only as current as its sources.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- virustotal
- urlscan-io
aliases:
- Maltiverse
- maltiverse.com
tags:
- threat-intel
- ioc
- reputation
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Maltiverse

> A threat-intelligence platform that aggregates and scores indicators of compromise — look up an IP, domain, URL, or hash and get a malicious/suspicious verdict with sourcing and related IOCs.

## When to use
This is **infrastructure/artifact triage**, not people search. When a subject's trail includes an `ip-address`, `domain`, URL, or file hash (`document-id`) and you need to know whether it's flagged as malicious — a C2 server, phishing host, malware sample — Maltiverse gives a fast reputation verdict plus the feeds that reported it and connected indicators to pivot on. In a missing-persons context it's narrow: e.g. assessing a suspicious link or host tied to an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free community account and sign in at https://maltiverse.com/.
2. Search the indicator: an `ip-address`, `domain`/hostname, URL, or file hash.
3. Read the result: classification (malicious/suspicious/neutral), the sources/feeds that reported it, first/last seen, and related IOCs.
4. Pivot: related `domain`/`ip-address` indicators expand your infrastructure map; cross-check with a second engine.
5. For automation, use the community API within its limits.

## Inputs → Outputs
- **In:** `ip-address` / `domain` / URL / file hash (`document-id`)
- **Out:** threat classification, reporting sources, first/last-seen, related `ip-address`/`domain` IOCs
- **Empty/negative result looks like:** "not found / neutral" — the indicator isn't in the aggregated feeds; that's reassuring but not proof it's clean. Corroborate with `[[virustotal]]`.

## Gotchas & OpSec
- **Aggregator verdict:** accuracy depends on source freshness; a clean result can lag a new threat. Confirm with another platform for anything important.
- Free tier is rate/volume-limited and needs an account (human-in-the-loop login).
- OpSec: **passive** — you query the DB, not the target; still, you disclose the indicator to Maltiverse.

## Overlaps ("do both")
- Pairs with `[[virustotal]]` and `[[urlscan-io]]` — VirusTotal for multi-engine detection, urlscan.io for live sandboxed URL analysis, Maltiverse for aggregated IOC scoring and relationships. Run more than one and reconcile.

## Trust & verifiability
`trust: trusted` — a reputable, sourced threat-intel platform; verdicts cite their feeds, so they're checkable, but treat any single aggregator's score as one input.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maltiverse |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain, document-id → ip-address, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
