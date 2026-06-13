---
id: blacklist-checker
name: Blacklist Checker
description: Use when you have an `ip-address`, `domain`, or `email` and want to know if its mail infrastructure is on spam blacklists — returns per-list flagged/clean status.
url: https://blacklistchecker.com/
category: email
path:
- email
bestFor: Checking an IP/domain/email against 100+ email spam blacklists.
selectorsIn:
- ip-address
- domain
- email
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: 50 free requests per month; higher volume and monitoring require a paid API plan. Free tier suffices for occasional checks.
opsec: passive
opsecNote: Queries public DNS-based blacklists about the supplied IP/domain/email; no contact with the subject. You disclose the queried value to blacklistchecker.com.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial blacklist-monitoring service (web checker + REST API) listed by awesome-osint. Reflects authoritative public DNSBLs, so results are objective.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- blacklistchecker.com
tags:
- email-search-email-check
- blacklist
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# Blacklist Checker

> A spam-blacklist (DNSBL) lookup: is this IP, domain, or email's mail infrastructure flagged on 100+ blocklists?

## When to use
You have an `ip-address`, `domain`, or `email` and want infrastructure reputation context — whether the associated mail server is listed on spam blacklists. In a missing-persons workflow this is peripheral: it qualifies a domain/server (e.g. is an address tied to throwaway/abused infra) rather than identifying a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blacklistchecker.com/.
2. Enter the `ip-address`, `domain`, or `email` to check.
3. Read the per-list results — which of the 100+ blacklists flag it vs. report it clean.
4. For automation/monitoring, use the REST API (JSON, 50 free requests/month) with daily alerts.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, or `email`
- **Out:** per-blacklist flagged/clean status for that infrastructure
- **Empty/negative result looks like:** "not listed on any blacklist" — the infra is clean per these lists; says nothing about the person.

## Gotchas & OpSec
- Free tier is capped at 50 requests/month; heavy use is paid.
- OpSec: passive; you only disclose the queried value to the service.
- Relevance to people-finding is low — this is infrastructure reputation, useful mainly to flag disposable/abused mail domains.

## Overlaps ("do both")
- Standalone infrastructure check; no people-search overlap. Use alongside domain-OSINT tools when vetting a mail domain rather than a person.

## Trust & verifiability
`trust: community` — a commercial front-end over authoritative public DNSBLs, so listing results are objective and reproducible across any DNSBL client.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blacklist-checker |
| category | email |
| selectorsIn → selectorsOut | ip-address, domain, email → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
