---
id: mihari
name: Mihari
description: Use when you have an `ip-address`/`domain` indicator and want to hunt and monitor related infrastructure across many OSINT sources at once — returns correlated matches persisted to a database.
url: https://github.com/ninoseki/mihari
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Running one query across Shodan/Censys/VirusTotal/SecurityTrails/etc. and continuously monitoring for new matching infrastructure.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open-source (Ruby gem, MIT). The upstream data sources it queries need their own (often free-tier) API keys.
opsec: passive
opsecNote: Queries are sent to third-party intel services (Shodan, Censys, VT…), not to the target, so you don't touch the subject's infrastructure. Those providers see your queries and API-key identity.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained framework by ninoseki (2k+ commits). It aggregates other services' results; accuracy is inherited from those sources.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- mitaka
- miteru
aliases: []
tags:
- Tools collections/toolkits
- threat-hunting
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Mihari

> A query-aggregator for OSINT threat hunting — write one rule, fan it out across 16+ intel services, persist the hits, and get alerted when new matching infrastructure appears.

## When to use
You have an `ip-address` or `domain` indicator (a suspicious host, a piece of malicious infrastructure) and want to (a) find everything related across many sources in one shot and (b) keep watching for new assets that match your rule over time. Built for continuous infrastructure hunting; peripheral to missing-persons work but useful for tracking a target's changing online infrastructure.

## How to use it (`bestInteractionPattern`: cli)
1. Install the gem: `gem install mihari` (or run via Docker).
2. Add API keys for the sources you'll use (Shodan, Censys, VirusTotal, SecurityTrails, GreyNoise…) via env vars/config.
3. Write a YAML rule describing the query/selectors and which sources to hit.
4. Run the rule (`mihari search <rule.yml>`); results are correlated and stored in Mihari's database.
5. Schedule it to re-run for monitoring; pivot on new `ip-address`/`domain` matches as they surface.

## Inputs → Outputs
- **In:** `ip-address` / `domain` (plus selectors like certs, favicon hash) in a rule
- **Out:** correlated `ip-address`/`domain` matches across sources, persisted for diffing over time
- **Empty/negative result looks like:** no matches — either the indicator is clean/isolated, or (common) the relevant sources lack API keys or hit free-tier limits. Check your keys before trusting an empty result.

## Gotchas & OpSec
- Human-in-the-loop: you must supply API keys; free tiers rate-limit and cap results.
- OpSec: **passive** toward the target (you query intel services, not the host), but those services log your queries against your key.
- It's an aggregator — coverage and accuracy are only as good as the configured sources.

## Overlaps ("do both")
- Pairs with `[[mitaka]]` (the browser-extension companion for one-off indicator lookups) and `[[miteru]]` (phishing-kit hunting) from the same author — Mihari is the automated, persistent-monitoring layer.

## Trust & verifiability
`trust: community` — an actively maintained, widely-used framework; it faithfully aggregates upstream results, so verify any critical finding against the originating source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mihari |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
