---
id: analyticsrelationships
name: AnalyticsRelationships
description: Use when you have a `domain` and want to find other sites run by the same owner via a shared Google Analytics ID — returns co-owned `domain`s, including relationships hidden in historical/archived pages.
url: https://github.com/Josue87/AnalyticsRelationships
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Discovering domains linked by a common Google Analytics UA/tracking ID, including from archived snapshots.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (Go/Python versions); no account.
opsec: passive
opsecNote: It fetches the target's page (and public sources like the Wayback Machine / crawl data) to extract the Analytics ID, then queries third-party indexes for matches — the initial page fetch is a direct visit, so proxy it for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool from a known researcher (Josue87); auditable, and the technique (shared GA IDs = common ownership) is a well-established OSINT method.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- metafinder
aliases:
- Josue87/AnalyticsRelationships
tags:
- Domain/IP/Links
- Website analyze
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# AnalyticsRelationships

> A CLI that finds the network behind a site: it extracts a domain's Google Analytics tracking ID (from the live page and archived snapshots) and returns every other domain sharing that ID — i.e. the same owner's other sites.

## When to use
You have a `domain` and suspect the operator runs more sites — a scam ring, a content-farm network, sock-puppet blogs. When one Analytics account tracks multiple sites, they all embed the same `UA-`/`G-` ID. This tool pulls that ID (crucially, also from *historical* page versions, catching IDs since removed) and reverse-looks-up co-owned domains, exposing infrastructure the owner tried to separate.

## How to use it (`bestInteractionPattern`: cli)
1. Install from the repo (Go binary or the Python version).
2. Run against the target: `analyticsrelationships -u https://example.com` (or the Python equivalent).
3. It extracts the Analytics ID from the current page and archived copies, then queries public indexes for other domains using it.
4. Read the returned list of related `domain`s.
5. Pivot: repeat on each new domain to widen the cluster; feed the set into WHOIS/hosting checks and a relationship graph.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** other `domain`s sharing the same Google Analytics ID
- **Empty/negative result looks like:** no ID extracted (site never used GA, or hid it) or no siblings found — meaning no *indexed* matches, not proof the owner has no other sites. Try the historical-ID angle and a reverse-tracker web tool as a cross-check.

## Gotchas & OpSec
- Modern sites increasingly use GA4 (`G-`) and tag managers, and reverse-lookup indexes cover the old `UA-` IDs better — coverage varies, so a null isn't conclusive.
- The pulled ID may be stale (from an archived page); a returned domain may have since changed hands — verify each match.
- OpSec: the ID-extraction step fetches the target page; proxy it for sensitive work.

## Overlaps ("do both")
- Pairs with `[[reverse-google-adsense]]` and web reverse-tracker tools (SpyOnWeb, DNSlytics) — AdSense and Analytics IDs are different signals, and each index holds different domain sets, so run both to catch the whole network.

## Trust & verifiability
`trust: community` — auditable open-source tooling built on a proven OSINT technique; a shared Analytics ID is strong evidence of common ownership, but confirm each returned domain independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analyticsrelationships |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
