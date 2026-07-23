---
id: reverse-google-adsense
name: Reverse Google Adsense
description: Use when you have a `domain` and want to find other sites run by the same owner by matching their Google AdSense/Analytics publisher ID — returns co-owned `domain`s.
url: https://osint.sh/adsense/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Uncovering a network of sites sharing one owner via a common AdSense/Analytics publisher ID.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free web lookup on osint.sh; the site offers a paid API/higher limits, but the basic AdSense reverse lookup is free.
opsec: passive
opsecNote: You query osint.sh's index, not the target site, so the domain owner sees no visit from you. osint.sh logs the domains you look up; use a clean session for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: osint.sh is a well-known free OSINT toolkit aggregator; its AdSense/Analytics reverse index is a convenient community resource, not an authoritative registry, so confirm links before relying on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- osint.sh AdSense
- Reverse AdSense
tags:
- domain-and-ip-research
- publisher-id
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Reverse Google Adsense

> A reverse publisher-ID lookup: extract a site's Google AdSense (`pub-…`) or Analytics ID and find every other domain that carries the same ID — i.e. is run by the same person.

## When to use
You have a `domain` and suspect the operator runs a whole network — scam sites, content farms, sock-puppet blogs, mirrored stores. When someone monetizes multiple sites through one Google AdSense or Analytics account, all those sites embed the same publisher ID in their source. Reverse-lookup turns that shared ID into a list of co-owned domains, exposing infrastructure the owner tried to keep separate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/adsense/.
2. Enter the target `domain`. The tool extracts its AdSense/Analytics publisher ID and searches its index for other domains using the same ID.
3. Read the returned list of `domain`s tied to that ID.
4. Repeat with any newly found domain to widen the cluster.
5. Pivot: each co-owned domain feeds WHOIS/hosting checks and a link graph; a shared ID across seemingly unrelated brands is strong attribution evidence.

## Inputs → Outputs
- **In:** `domain`
- **Out:** other `domain`s sharing the same AdSense/Analytics publisher ID
- **Empty/negative result looks like:** no ID found on the page (the site may not run AdSense/Analytics, or hides it) or only the queried domain returned — meaning no *indexed* siblings, not proof the owner has no other sites.

## Gotchas & OpSec
- Only works if the target actually embeds an AdSense/Analytics ID and osint.sh has indexed the siblings; sophisticated operators rotate or omit IDs.
- The index is a third-party crawl and can be stale — a returned domain may have since changed ownership, so treat matches as leads to verify.
- OpSec: passive — you touch osint.sh, never the target; the target owner won't see your lookup.

## Overlaps ("do both")
- Pairs with other publisher-ID/tracker tools (e.g. SpyOnWeb, DNSlytics reverse-tracker) — different indexes hold different domain sets, so run the ID across several to catch every sibling site.

## Trust & verifiability
`trust: community` — a handy free aggregator index rather than an authoritative source; a shared publisher ID is strong evidence of common ownership, but confirm each returned domain independently before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-google-adsense |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
