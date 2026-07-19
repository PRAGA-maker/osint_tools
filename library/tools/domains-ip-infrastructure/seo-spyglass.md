---
id: seo-spyglass
name: SEO SpyGlass
description: Use when you have a `domain` and want to map who links to it — returns referring domains, anchor text, and hosting IPs/C-blocks.
url: https://www.link-assistant.com/seo-spyglass/free-backlink-checker-tool.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating the backlink profile of a target domain to discover affiliated sites, networks, and shared hosting infrastructure.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free desktop edition analyzes up to ~1,100 backlink entries per project; the online tool has a daily report cap. Full/unlimited analysis is paid, but the free tier is usable for scoping.
opsec: passive
opsecNote: Queries link-assistant's own backlink index, not the target's server, so the target site is not touched or alerted. The desktop app runs locally; only your account/IP is exposed to link-assistant.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: desktop-app
trust: community
trustNote: A commercial SEO vendor (LinkAssistant / SEO PowerSuite); backlink data is aggregated from its own crawl and third parties, so coverage and freshness vary versus other backlink indexes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- SEO PowerSuite backlink checker
- LinkAssistant SpyGlass
tags:
- domainsandips
- Domains & IPs
- backlinks
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# SEO SpyGlass

> A backlink-profiling tool: hand it a domain and it enumerates the sites linking to it, the anchor text they use, and the IPs/C-blocks those links sit on — a map of a domain's web neighborhood.

## When to use
You have a `domain` tied to a subject (a personal site, a business, a scam/phishing page) and want to discover the wider network around it: who links to it, what other sites share its backlink patterns or hosting C-blocks, and which anchor texts reveal branding or aliases. Backlink analysis surfaces affiliated properties that a simple WHOIS or DNS lookup misses.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the free SEO SpyGlass desktop app (part of SEO PowerSuite) or use the online free backlink checker page.
2. Create a project for the target `domain`.
3. Read the report: referring domains, backlink count, dofollow/nofollow split, anchor-text list, and unique IPs/C-blocks (`ip-address` grouping) of linking pages.
4. Pivot: unusual anchor texts can reveal brand names/aliases; shared C-blocks/referring domains point to sibling sites; feed discovered domains into WHOIS/DNS tools.

## Inputs → Outputs
- **In:** `domain`
- **Out:** referring `domain`s, anchor texts, linking-page `ip-address`/C-blocks
- **Empty/negative result looks like:** few or zero backlinks — either a new/obscure site or one outside this index's coverage; cross-check with another backlink source before concluding it's isolated.

## Gotchas & OpSec
- Backlink indexes are never complete; a low count here may just mean this crawler missed links another index has.
- The free tier caps entries/reports — enough for scoping, not exhaustive enumeration.
- OpSec: passive; the target domain's server is not contacted.

## Overlaps ("do both")
- Complements WHOIS/reverse-IP and other backlink checkers — run more than one backlink source, since each index sees a different slice of the link graph.

## Trust & verifiability
`trust: community` — vendor-aggregated backlink data; reliable enough for lead generation but corroborate any specific link/relationship against a second index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seo-spyglass |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
