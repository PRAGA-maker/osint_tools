---
id: sarenka
name: Sarenka
description: Use when you have a `domain`/`ip-address` and want a self-hosted tool to pull attack-surface data from Shodan/Censys and CVE sources in one place — returns host services and `ip-address`/CVE context.
url: https://github.com/pawlaczyk/sarenka
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A self-hosted OSINT dashboard that aggregates attack-surface data (Shodan, Censys, CVEs) for a host.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: degraded
pricing: free
costNote: Free and open-source (self-hosted Django/React app); some data sources need your own API keys (Shodan/Censys).
opsec: passive
opsecNote: It queries third-party databases (Shodan, Censys) about the target host rather than the host itself, so the subject is not directly probed — but those services log the queries against your API keys. Use research keys, not identity-linked ones.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: docker
trust: unverified
trustNote: Community open-source project (pawlaczyk); useful as an aggregator but may be unmaintained and depends on external APIs whose free tiers change — verify it still runs before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- SARENKA
tags:
- Tools collections/toolkits
- attack-surface
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Sarenka

> A self-hosted OSINT aggregator that pulls a host's attack-surface picture — Shodan/Censys service data plus CVE context — into one local dashboard.

## When to use
You are profiling infrastructure (`domain`/`ip-address`) and want a single self-hosted place that queries Shodan and Censys and correlates known CVEs, instead of visiting each service separately. Best for the infrastructure side of an investigation; it surfaces no personal identifiers.

## How to use it (`bestInteractionPattern`: docker)
1. Clone https://github.com/pawlaczyk/sarenka and run it locally (Docker/Django backend + React frontend, per the repo README).
2. Add your own Shodan and Censys API keys in the config.
3. Query a `domain`/`ip-address`; SARENKA fetches open services, banners, and associated CVE data.
4. Review the aggregated host picture; export findings for the case file.
5. Pivot: exposed services and hostnames feed `[[censys-ipv4]]` and vulnerability-context lookups.

## Inputs → Outputs
- **In:** `domain` / `ip-address`
- **Out:** open services/ports, host metadata, and CVE context (`ip-address`/`domain` infrastructure)
- **Empty/negative result looks like:** empty results usually mean missing/expired API keys or a host with no scan record — check keys and quotas before concluding "nothing."

## Gotchas & OpSec
- **Degraded/self-hosted:** you must run and maintain it; it may lag upstream API changes.
- Human-in-the-loop: requires your own Shodan/Censys `api-key`s; those services meter and log usage.
- OpSec: **passive** to the target (queries go to Shodan/Censys, not the host), but attributable via your API keys.

## Overlaps ("do both")
- Overlaps heavily with using `[[censys-ipv4]]` and Shodan directly; SARENKA's value is aggregation — if it will not run, go to those sources individually.

## Trust & verifiability
`trust: unverified` — community project reselling third-party data; verify each finding at the upstream source (Shodan/Censys) it came from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sarenka |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (api-key) |
