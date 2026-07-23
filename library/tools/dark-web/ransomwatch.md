---
id: ransomwatch
name: ransomwatch
description: Use when you have a company `name`/`employer-org` and want to check whether a ransomware group has claimed it as a victim — returns leak-site claims (victim, group, date).
url: https://ransomwatch.telemetry.ltd/#/INDEX
category: dark-web
path:
- dark-web
bestFor: Checking whether an organisation appears as a claimed victim on ransomware leak sites.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
status: degraded
pricing: free
costNote: Free; open-source (Unlicense). The project is archived/unmaintained, so the hosted index may be stale or go offline — treat as a historical snapshot.
opsec: passive
opsecNote: A clearnet mirror of ransomware leak-site claim data — you read an aggregated index, not the .onion sites directly, so it's passive. Do not navigate to the underlying leak sites without proper OpSec (Tor, isolated VM).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community project ("transparent ransomware claim tracker"); now archived, so data freshness is not guaranteed — verify against current trackers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ransomwatch tracker
tags:
- dark-web
- ransomware
- threat-intel
- leak-sites
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# ransomwatch

> A clearnet aggregator of ransomware-group leak-site claims — search whether an organisation has been named as a victim, without touching the .onion sites yourself.

## When to use
You have a company `name`/`employer-org` and want to know whether a ransomware group has publicly claimed to have breached it (posted it on their extortion/leak site). Useful for incident context, supply-chain risk on a subject's vendors, and corroborating a breach. Because ransomwatch mirrors leak-site postings to the clearnet, you avoid directly visiting hostile .onion infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ransomwatch.telemetry.ltd/ (or self-host from the archived GitHub repo).
2. Search/browse the index for the `employer-org`/`name`.
3. Read the entry: victim name, claiming group, and post date.
4. Pivot: a claim points to the group's leak site (visit only via Tor/isolated VM) and to incident-response reporting; cross-check the date against news coverage.

## Inputs → Outputs
- **In:** company `name` / `employer-org`
- **Out:** ransomware leak-site claims (`employer-org` victim, group, date)
- **Empty/negative result looks like:** no claim listed — the org hasn't been posted (or the archived index is stale and missed it); confirm with a currently-maintained tracker.

## Gotchas & OpSec
- The project is ARCHIVED/unmaintained — data may be stale and the hosted instance can disappear; treat results as a snapshot and verify against live trackers (e.g. ransomlook-style successors).
- A "claim" is the attacker's assertion, not confirmation a breach occurred — corroborate.
- Never open the underlying leak sites without Tor and an isolated environment.

## Overlaps ("do both")
- Complements live ransomware trackers and breach-notification sources — ransomwatch is one (now-static) view; cross-check a claim against a maintained tracker and official disclosures.

## Trust & verifiability
`trust: community` — a community tracker mirroring attacker claims; now archived, so freshness is uncertain and every claim needs independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ransomwatch |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org, name → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
