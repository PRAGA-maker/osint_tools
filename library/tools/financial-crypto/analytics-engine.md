---
id: analytics-engine
name: analytics-engine
description: Use when you want a self-hosted pipeline that pulls live crypto/stock market data into dashboards for ongoing financial monitoring — returns queryable datasets and visualizations (no subject PII).
url: https://github.com/mashiox/analytics-engine
category: financial-crypto
path:
- financial-crypto
bestFor: Standing up a self-hosted market-data collection and dashboarding stack for continuous financial monitoring.
selectorsIn: []
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Open source under MIT; free to self-host. You pay only for whatever hosting/data feeds you attach.
opsec: passive
opsecNote: Runs on your own infrastructure and pulls from public market feeds, so it does not touch any investigation subject. OpSec exposure is limited to the API keys/data sources you configure — keep those in a controlled environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: A small open-source project wiring together n8n, PostgreSQL, and Metabase; auditable, but a personal-scale stack rather than a vetted investigative product.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- mashiox/analytics-engine
tags:
- crypto
- market-data
- financial-monitoring
- self-hosted
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# analytics-engine

> A Docker-Compose stack (n8n + PostgreSQL + Metabase) for collecting and visualising live market data — a self-hosted way to keep a standing eye on crypto and stock feeds rather than a one-off lookup.

## When to use
Niche and infrastructural: reach for it when a financial investigation needs *ongoing* monitoring rather than a single query — e.g. tracking prices, volumes, or on-chain/market signals over time on your own infrastructure. It builds a data pipeline and dashboards; it does not identify people. Most people-finding work will use a blockchain explorer instead, and pull this out only when continuous market observation is the requirement.

## How to use it (`bestInteractionPattern`: docker)
1. Clone `https://github.com/mashiox/analytics-engine` and start it with Docker Compose (minimal config).
2. Configure n8n workflows to retrieve the market/crypto data feeds you care about into PostgreSQL.
3. Build or open Metabase dashboards to visualise and SQL-query the collected data.
4. Pivot: anomalies you spot (a price/volume spike tied to a wallet or event) feed a blockchain explorer or chain-analysis tool for the who-and-how.

## Inputs → Outputs
- **In:** market/crypto data feeds you configure (no subject PII)
- **Out:** stored, SQL-queryable datasets and Metabase visualizations/dashboards
- **Empty/negative result looks like:** empty dashboards because a feed/workflow is misconfigured or rate-limited — a setup issue, not a market signal.

## Gotchas & OpSec
- Human-in-the-loop: none at runtime, but real setup effort (Docker, n8n workflows, feed keys) is required.
- OpSec: passive — self-hosted and fed by public data; it never contacts a subject. Guard the API keys you add.
- It is a monitoring/analytics scaffold, not an attribution tool — it will not tell you who owns anything; pair it with explorers for that.

## Overlaps ("do both")
- Pairs with attribution/explorer tools like [[matbea]] — this watches market data over time, the explorer names the wallets behind a movement; use both to turn a monitored signal into an identified actor.

## Trust & verifiability
`trust: community` — a small, auditable open-source stack. The data is only as good as the public feeds you connect; treat its dashboards as your own analysis, not an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analytics-engine |
| category | financial-crypto |
| selectorsIn → selectorsOut |  → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
