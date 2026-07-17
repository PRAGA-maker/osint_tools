---
id: fullhunt
name: FullHunt
description: Use when you have a `domain` and want to map its external attack surface — returns subdomains, `ip-address`es and hosted assets.
url: https://fullhunt.io/
category: search-engines
path:
- search-engines
bestFor: Enumerating a domain's subdomains and internet-facing assets from a passive attack-surface database.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free "Console" account gives API access to the attack-surface database with a monthly query quota; larger volume and the enterprise platform are paid.
opsec: passive
opsecNote: Queries FullHunt's pre-collected database rather than scanning the target live, so the subject's servers see nothing from you. Your query is logged by FullHunt against your account; use a dedicated research account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Established commercial attack-surface-management vendor; a reputable third-party aggregator, not a primary registry.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- fullhunt.io
tags:
- speciality-search-engines
- attack-surface
- subdomain-enumeration
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# FullHunt

> A passive attack-surface database: give it a `domain` and it returns the subdomains, IPs and cloud assets it has already discovered — no active scanning of the target required.

## When to use
You have a `domain` and want its full internet-facing footprint: subdomains (mail, dev, staging, vpn, admin panels), the `ip-address`es they resolve to, open ports and technologies. This maps an organisation's or individual's infrastructure for pivoting — a `dev.` or `owncloud.` subdomain, or a shared hosting IP, can reveal related properties and services. Because the data is pre-collected, you get breadth without touching the target.

## How to use it (`bestInteractionPattern`: api)
1. Register a free Console account at https://fullhunt.io/ and copy your API key.
2. Query the domain, e.g. `curl -H "X-API-KEY: <key>" "https://fullhunt.io/api/v1/domain/target.com/subdomains"`.
3. Read the JSON: the `hosts`/`subdomains` array lists discovered subdomain `domain`s; each carries resolved `ip-address`es, ports and tech fingerprints.
4. Watch the free-tier quota — batch your queries and cache results.
5. Pivot: run interesting subdomains through DNS/WHOIS history, and feed shared `ip-address`es into reverse-IP lookups to find co-hosted domains.

## Inputs → Outputs
- **In:** `domain`
- **Out:** subdomain `domain`s, `ip-address`es (plus ports/technologies)
- **Empty/negative result looks like:** an empty host list — either the domain is obscure and not in FullHunt's crawl, or it genuinely has a tiny footprint. Cross-check with a second subdomain source before concluding.

## Gotchas & OpSec
- Human-in-the-loop: a free account and API key are required; quota-limited.
- OpSec: **passive** against the target (database lookup), but your queries are tied to your FullHunt account — keep research and personal accounts separate.
- Database freshness varies; a listed asset may be stale and a live one may be missing. Confirm anything actionable directly.

## Overlaps ("do both")
- Pairs with other subdomain/attack-surface sources — each crawler sees a different slice, so union their results for full coverage.

## Trust & verifiability
`trust: community` — a reputable commercial aggregator; treat its findings as leads and verify resolution/ownership against authoritative DNS and WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fullhunt |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
