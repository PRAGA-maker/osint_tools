---
id: expireddomains-net
name: Expireddomains.net
description: Use when you have a `domain` name or keyword and want to find recently deleted/expired domains and their history/metrics — returns matching `domain`s with backlink, archive and DNS data.
url: https://www.expireddomains.net/deleted-domains/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Searching hundreds of millions of expired/deleted domains with age, backlink and archive metrics.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free to search after a free account registration; full filters and complete listings require the (free) login, with premium tiers for heavier use.
opsec: passive
opsecNote: You query expireddomains.net's own aggregated index, not any target's live infrastructure — passive. Register with a sock-puppet email; the account is what unlocks filters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established, widely-used dropped-domain search engine; metrics are aggregated from third-party sources (backlinks, Archive.org) and are indicative rather than authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- ExpiredDomains.net
- deleted domains search
tags:
- domains-ip-infrastructure
- domains
- passive-dns
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Expireddomains.net

> A search engine over hundreds of millions of expired and freshly-deleted domains, with age, backlink, archive and DNS metrics attached.

## When to use
You have a `domain`, brand, or keyword and want to know whether related domains have expired/dropped — to catch a former online presence, find an abandoned domain tied to a subject, monitor for a name coming available, or research a domain's lineage. The "Deleted Domains (last 7 days)" view tracks very recent drops.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.expireddomains.net/ and register the free account (needed to see full listings and filters). Use a sock-puppet email.
2. Search by keyword or `domain`, or browse the deleted/expired lists; filter by TLD, length, age, backlinks, Archive.org history, etc.
3. Read each row's metrics: registration/expiry dates, backlink counts, Wayback history flag, and DNS status across TLD variants.
4. Pivot: an interesting dropped `domain` feeds Wayback/`[[wayback-machine]]` to recover its old content and passive-DNS to see what it once hosted.

## Inputs → Outputs
- **In:** `domain` / keyword (+ filters)
- **Out:** matching `domain`s with age, backlink, archive and DNS metrics
- **Empty/negative result looks like:** no rows for your keyword in the deleted set — the domain hasn't dropped (still registered) or falls outside the 7-day deleted window; broaden filters or check the full expired index.

## Gotchas & OpSec
- Human-in-the-loop: a (free) login is required to see complete listings and use filters.
- Metrics are third-party aggregates — treat backlink/authority numbers as indicative, and confirm archive content directly in the Wayback Machine.
- The 7-day deleted view is a rolling window; older drops need the broader search.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — this finds the dropped domain and its metrics; Wayback recovers what the domain actually contained before it lapsed.

## Trust & verifiability
`trust: community` — a long-established dropped-domain search engine; its own listing data is solid, but the attached SEO/backlink metrics come from third parties and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expireddomains-net |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
