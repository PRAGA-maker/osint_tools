---
id: lazarusholic
name: Lazarusholic (lazarus.day)
description: Use when you have an IoC or actor name tied to North Korean APT activity — returns linked reports, incidents, and indicators (domains, IPs, hashes, wallets).
url: https://lazarus.day/actors/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Researching North Korean / Lazarus-cluster threat actors and pivoting on their published indicators of compromise.
selectorsIn:
- domain
- ip-address
- crypto-wallet
selectorsOut:
- domain
- ip-address
- crypto-wallet
status: live
pricing: free
costNote: Free, community-driven, licensed CC BY-SA 4.0; no account needed to read.
opsec: passive
opsecNote: You query an aggregated open-source threat-intel index — you don't touch actor infrastructure and nothing is disclosed. If you go on to investigate a listed IoC (visit a domain, trace a wallet), apply the appropriate isolation/OpSec for that step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open, community-submitted database curating public reporting (Mandiant, Google, Qihoo360, etc.) on DPRK-linked actors, with data through 2026. Aggregation of third-party reports — verify each IoC against its cited source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- malpedia
- virustotal
- mandiant-advantage
aliases:
- lazarus.day
- Lazarusholic
tags:
- threat-intel
- apt
- north-korea
- ioc
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Lazarusholic (lazarus.day)

> An open, community-curated database on North Korean / Lazarus-cluster APTs — actors, incidents, reports, and their published indicators of compromise, all cross-linked.

## When to use
When an investigation touches DPRK-linked cyber activity (crypto theft, exchange hacks, supply-chain intrusions) and you have an indicator — a `domain`, `ip-address`, hash, `crypto-wallet`, or an actor name (Lazarus, Kimsuky, Bluenoroff, Andariel, Scarcruft) — and want the associated reporting and related IoCs. Especially useful for crypto-theft cases where wallet indicators tie an incident to a known actor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lazarus.day/ and browse Actors, Reports, Incidents, or IoCs.
2. Search or filter by your indicator (`domain`/`ip-address`/hash/`crypto-wallet`) or by actor/incident name.
3. Read the linked entries: which actor/incident an IoC belongs to, and the source reports (Mandiant, Google, etc.).
4. Follow the cited report to confirm the indicator's provenance — this is an aggregator, so the original report is the authority.
5. Pivot: related `domain`s/`ip-address`es/`crypto-wallet`s feed `[[virustotal]]`, blockchain explorers, and `[[malpedia]]` for malware family context.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / hash / `crypto-wallet` / actor or incident name
- **Out:** linked reports, incidents, and related IoCs (`domain`, `ip-address`, `crypto-wallet`, hashes, YARA, ASNs)
- **Empty/negative result looks like:** no match — the indicator isn't associated with DPRK activity in this dataset (scope is narrow to that cluster); use a general threat-intel source.

## Gotchas & OpSec
- Scope is specifically the North Korean APT cluster — not a general threat-intel database.
- It aggregates third-party reporting; each IoC is only as reliable as its cited source — verify against the original report before attributing.
- Community-submitted, so completeness varies; absence isn't exoneration.

## Overlaps ("do both")
- Pairs with `[[malpedia]]` (malware family / actor reference) and `[[virustotal]]` (file/infra reputation). Do both: Lazarusholic for DPRK-actor context and IoC linkage, the others for sample and infrastructure detail.

## Trust & verifiability
`trust: community` — an open, well-referenced aggregation of reputable public reporting. Reliable as an index; confirm each indicator against the cited primary source before acting on attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lazarusholic |
