---
id: threatingestor
name: ThreatIngestor
description: Use when you want to automate collecting indicators (`domain`, `ip-address`, hashes) from many threat feeds, RSS, and Twitter into one place — returns extracted, deduped IOCs.
url: https://github.com/InQuest/ThreatIngestor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Automated, scheduled extraction of IOCs from RSS/Twitter/threat feeds into a store or downstream system.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (InQuest, Apache-2.0); self-hosted, so cost is only the feeds/APIs you point it at.
opsec: passive
opsecNote: Runs on your own infrastructure and pulls from public feeds; nothing about a target is queried. Configure source API keys as secrets. Passive by nature, but you control where extracted IOCs are sent.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by InQuest, an established threat-intelligence vendor; widely used open-source project.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- iocextract
- omnibus
aliases:
- ThreatIngestor
- InQuest ThreatIngestor
tags:
- threat-intel
- ioc
- automation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# ThreatIngestor

> A configurable pipeline that watches threat feeds, RSS, and social sources and automatically extracts the indicators from them — the collection layer for an IOC workflow.

## When to use
You are tracking infrastructure over time and want indicators (`domain`s, `ip-address`es, URLs, hashes, YARA) pulled automatically from many public sources — security-blog RSS, Twitter/X accounts, threat feeds — rather than copy-pasting by hand. ThreatIngestor runs on a schedule, extracts IOCs, and forwards them to a store (CSV, SQLite, MISP, a beanstalk queue, etc.) for enrichment or alerting.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install threatingestor` (needs Python 3); optionally add extras for specific sources/operators.
2. Write a `config.yml` defining **sources** (RSS URLs, Twitter handles/searches, web pages) and **operators** (where extracted IOCs go — CSV, SQLite, MISP, etc.).
3. Run `threatingestor config.yml`; schedule it (cron/systemd) for continuous collection.
4. It extracts and dedupes indicators from each source into your chosen operator.
5. Pivot: feed the harvested `domain`s/`ip-address`es into WHOIS, passive DNS, and Shodan, or enrich with `[[iocextract]]` / `[[omnibus]]`.

## Inputs → Outputs
- **In:** configured public sources (RSS/Twitter/web) — not a per-target selector
- **Out:** extracted, deduped IOCs — `domain`s, `ip-address`es, URLs, hashes, YARA — in your chosen store
- **Empty/negative result looks like:** no IOCs written — sources produced nothing new, a source/API credential is misconfigured, or a source went offline.

## Gotchas & OpSec
- It is infrastructure you run and maintain — quality depends entirely on the sources you configure; garbage feeds in, garbage IOCs out.
- Store API keys (Twitter, etc.) as secrets, not in a committed config.
- OpSec: passive collection from public feeds; nothing targets a subject. Mind where you route extracted IOCs.

## Overlaps ("do both")
- Pairs with `[[iocextract]]` (the extraction library it builds on for pulling indicators from text) and `[[omnibus]]` — use ThreatIngestor to collect continuously and those to extract/enrich ad hoc.

## Trust & verifiability
`trust: trusted` — an open-source project by InQuest, a recognised threat-intel vendor; the code is auditable and the tool only reports what your configured public sources contain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threatingestor |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | — → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
