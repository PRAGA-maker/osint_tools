---
id: dataset-domainsproject-org
name: Domains Project Dataset
description: Use when you have a `domain` fragment or keyword and want to enumerate matching registered domains — returns a bulk `domain` list for pattern/infrastructure analysis.
url: https://dataset.domainsproject.org/
category: public-records
path:
- public-records
bestFor: Bulk offline enumeration of registered domain names for pattern matching, brand/typosquat discovery, and infrastructure mapping.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: The full dataset is free and open — mirrored via the GitHub repo (git clone + unpack.sh). The direct dataset host may require registration; GitHub is the reliable free path.
opsec: passive
opsecNote: You grep a locally-downloaded text file, so no query touches any target or third party — fully offline once downloaded. The download itself is a large public dataset fetch; nothing target-specific is transmitted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source community project (tb0hdan/domains on GitHub); the world's largest open Internet-domains dataset, but a crawl snapshot — it lists domains that resolved, without ownership or liveness guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DomainsProject
- domains project dataset
- tb0hdan/domains
tags:
- Datasets
- domain-enumeration
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Domains Project Dataset

> An open, downloadable list of billions of registered domain names — grep it offline to enumerate every domain matching a brand, keyword, or pattern.

## When to use
You have a `domain`, a brand string, or a naming pattern and need to find *all* the domains that contain it: to hunt typosquats and phishing lookalikes tied to a subject, to map a person's or org's domain portfolio, or to seed an infrastructure investigation with candidate hostnames. Because it is a bulk text dataset you query locally, it is fast, silent, and unrate-limited — unlike live WHOIS/cert-transparency queries.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the open mirror: `git clone https://github.com/tb0hdan/domains.git` then run `./unpack.sh` (the raw dataset is also mirrored at dataset.domainsproject.org).
2. The data is plain text — one domain per line across many files.
3. Grep for your pattern, e.g. `grep -rih 'targetbrand' data/ | sort -u`, or match a regex for typo variants.
4. Feed the resulting candidate domains into live enrichment (WHOIS, DNS, certificate transparency) to check which actually resolve and who owns them.
5. Pivot: resolved candidate domains feed `[[whois]]`-style ownership lookups and passive-DNS tools to tie infrastructure back to a person or org.

## Inputs → Outputs
- **In:** `domain` fragment / brand / keyword / regex
- **Out:** `domain` list (bulk candidate hostnames)
- **Empty/negative result looks like:** no lines match your pattern — the domain was never crawled, is newer than the snapshot, or genuinely does not exist. It is a snapshot, so recent registrations may be absent.

## Gotchas & OpSec
- It is a crawl snapshot, not a live registry: it says a domain existed at crawl time, not that it resolves now or who owns it — always verify hits live.
- The dataset is large (tens of GB unpacked); ensure disk space before cloning.
- No ownership/registrant data is included — pair with WHOIS to attribute domains.

## Overlaps ("do both")
- Pairs with certificate-transparency search (crt.sh) and passive DNS — this gives exhaustive offline name enumeration, those give liveness and ownership; together they turn a keyword into an attributed infrastructure map.

## Trust & verifiability
`trust: community` — a well-known open-source dataset (tb0hdan/domains) widely used by researchers; comprehensive but unverified per-record, so treat every hit as a candidate to confirm with a live lookup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dataset-domainsproject-org |
| category | public-records |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
