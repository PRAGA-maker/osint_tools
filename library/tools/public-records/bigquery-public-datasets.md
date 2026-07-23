---
id: bigquery-public-datasets
name: BigQuery Public Datasets
description: Use when you need to query large public datasets at scale with SQL — census, GitHub, patents, crypto ledgers, geospatial and more — returns query results joining across public data.
url: https://cloud.google.com/bigquery/public-data/
category: public-records
path:
- public-records
bestFor: SQL analysis of massive public datasets (blockchain ledgers, GitHub activity, census, patents, weather) hosted in Google BigQuery.
selectorsIn:
- crypto-wallet
- username
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: The datasets are free to access; you pay only for query compute beyond Google's free 1 TB/month query allowance. A Google Cloud account is required.
opsec: passive
opsecNote: Passive — you query Google-hosted copies of public data; no target is contacted. Note that queries run under YOUR authenticated Google Cloud project, so Google logs your usage/billing; use a dedicated project if you want investigation activity separated.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google Cloud service hosting curated public datasets (many maintained by the data owners); authoritative for the datasets it mirrors.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- BigQuery public data
- Google BigQuery datasets
tags:
- datasets
- sql
- blockchain
- big-data
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# BigQuery Public Datasets

> Google's warehouse of large public datasets you can query with SQL — from full blockchain ledgers and GitHub history to census, patents and weather.

## When to use
You have an analysis that needs *scale* — join millions of rows, aggregate a full crypto ledger, mine GitHub commit metadata, or cross-reference census/geographic data — beyond what a web form can do. For OSINT specifically, the on-chain datasets (Bitcoin, Ethereum, etc.) let you trace a `crypto-wallet`'s transactions and counterparties with SQL, and the GitHub datasets expose developer activity patterns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create/sign in to a Google Cloud project and open the BigQuery console.
2. Browse the public datasets (Marketplace → public datasets) — e.g. `bigquery-public-data.crypto_bitcoin`, `github_repos`, `census_bureau_acs`.
3. Write SQL against the tables (mind the free 1 TB/month query quota — filter and select narrowly).
4. Run and export results (CSV/Sheets/API) for further analysis.
5. Pivot: on-chain counterparties (`crypto-wallet`/`associate`) or developer handles feed dedicated crypto/social tools.

## Inputs → Outputs
- **In:** a SQL query keyed on your selector (e.g. a `crypto-wallet` address, GitHub `username`)
- **Out:** query results — transaction graphs, `associate`/counterparty addresses, activity records
- **Empty/negative result looks like:** zero rows — the selector isn't in that dataset or your filter excluded it; check table/date coverage (datasets have cut-off dates).

## Gotchas & OpSec
- **Costs scale with data scanned** — an unfiltered query on a huge table can blow the free quota; always restrict columns and partitions.
- Requires a Google Cloud account; activity is billed/logged to your project.
- Datasets have freshness cut-offs — confirm the snapshot date before treating results as current.

## Overlaps ("do both")
- Pairs with specialized blockchain explorers and GitHub-OSINT tools — BigQuery does bulk SQL analysis while those give a polished per-entity view; use BigQuery to find candidates, the explorer to confirm.

## Trust & verifiability
`trust: trusted` — first-party Google-hosted public data, much of it maintained by the original data owners; results are reproducible by re-running the SQL.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bigquery-public-datasets |
