---
id: bevigil-cli
name: BeVigil-CLI
description: Use when you have a `domain` or mobile-app package id and want assets extracted from scanned apps — returns subdomains, urls and s3 buckets.
url: https://github.com/Bevigil/BeVigil-OSINT-CLI
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Pulling hostnames, URLs and S3 buckets that BeVigil harvested from scanning mobile apps.
selectorsIn:
- domain
- device-id
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free API tier available after registering at bevigil.com for an API key; higher volume is paid. The CLI/library itself is open source and free.
opsec: passive
opsecNote: Queries hit BeVigil's pre-collected scan database, not the target's apps or servers, so nothing touches the subject. Your API key ties every query to your BeVigil account — assume BeVigil logs what you look up.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Published by BeVigil (CloudSEK); the data comes from their crawling of public mobile apps, so coverage and freshness depend on what they have scanned. Repo last released 2022 — usable but not actively developed.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- BeVigil OSINT CLI
- Bevigil/BeVigil-OSINT-CLI
tags:
- other-tools
- attack-surface
- subdomain-enumeration
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# BeVigil-CLI

> A CLI/Python client for the BeVigil OSINT API — surfaces the subdomains, URLs, parameters and S3 buckets that BeVigil extracted by scanning public mobile apps.

## When to use
You are mapping a target organisation's attack surface and want assets that only show up *inside mobile apps* — hardcoded API hostnames, dev/staging subdomains, exposed S3 buckets, and URL parameters that classic web crawling misses. Give it a `domain` (to find associated app packages and hosts) or an Android package id (to extract that app's embedded assets).

## How to use it (`bestInteractionPattern`: cli)
1. Register at bevigil.com and obtain a free API key.
2. `pip install bevigil-cli`, then `bevigil-cli init --api-key <API_KEY>`.
3. Run a query, e.g. subdomains for a domain, hosts/URLs/S3 buckets for an Android `packageid`, or keyword-based S3 bucket search.
4. Review the returned assets — treat hostnames as candidates to resolve and verify, not confirmed live infrastructure.
5. Pivot: resolved `domain`/`ip-address` assets feed subdomain and infra tooling (`[[subdomain-finder]]`); exposed buckets feed a manual review.

## Inputs → Outputs
- **In:** `domain`, or an Android app `device-id`/package id, or a keyword
- **Out:** `domain` (subdomains/hosts), URLs, URL params, S3 bucket URLs, associated app packages; resolvable to `ip-address`
- **Empty/negative result looks like:** no assets returned — BeVigil hasn't scanned an app that references the target, not proof none exists. Combine with other enumeration.

## Gotchas & OpSec
- Human-in-the-loop: an **API key** (free registration) is required before any query works.
- Coverage is bounded by BeVigil's app-scan corpus; niche or region-locked apps may be absent, and data can be dated.
- OpSec: **passive** toward the target, but every lookup is attributed to your BeVigil account/key.

## Overlaps ("do both")
- Complements passive web enumerators like `[[subdomain-finder]]` — BeVigil finds mobile-app-only assets those miss; run both for fuller coverage.

## Trust & verifiability
`trust: community` — a vendor tool (CloudSEK/BeVigil) over their own scan data. Reliable as *leads* mined from real apps, but verify each host is live and actually belongs to the target before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bevigil-cli |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, device-id → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
