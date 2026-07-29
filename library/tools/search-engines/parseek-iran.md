---
id: parseek-iran
name: Parseek (Iran)
description: Use when you need current Persian-language news headlines aggregated from Iranian sources — returns categorized Iranian news links, not a people-search index.
url: http://www.parseek.com
category: search-engines
path:
- search-engines
bestFor: Monitoring Iranian/Persian news across many sources from one aggregated headline feed.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public news aggregator; no account. Persian-language interface and content.
opsec: passive
opsecNote: You read an aggregated headline feed — no subject query is submitted, so it's fully passive. As with any Iranian site, connect via a clean/VPN session if you don't want the request tied to you; the site itself collects no target selector.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running Persian news aggregator that republishes headlines from third-party outlets; it disclaims responsibility for source content, so treat items as pointers to verify at the origin.
missingPersonsRelevance: low
coverage:
- ir
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- parseek
aliases:
- Parseek
- parseek.com
tags:
- news
- iran
- persian
- news-aggregator
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Parseek (Iran)

> A Persian-language news aggregator that pulls headlines from dozens of Iranian outlets into one categorized feed — regional-context reading, not a searchable people database.

## When to use
Your case has an Iran nexus and you need situational context or event-tracking from Persian-language media. Parseek auto-collects headlines across categories (Iran, World, Economics, Society, Science & Tech, Culture & Arts, Sports) so you can scan many Iranian sources at once. It's for **context and leads** — spotting coverage of an event, place, or organization — not for querying a specific person; it takes no selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.parseek.com (Persian interface — use browser translation if needed).
2. Browse by category or scan the latest headlines feed.
3. Click through to the original outlet for the full article (Parseek only aggregates headlines).
4. Corroborate any claim at the source and against a second outlet before using it.
5. Pivot: names, places, and orgs surfaced in coverage become selectors for your other tools.

## Inputs → Outputs
- **In:** none (browse/scan; not selector-driven)
- **Out:** categorized Iranian news headlines with links to source outlets
- **Empty/negative result looks like:** a category with stale or sparse items — it reflects source publishing, not a query miss. There is no "no result," only the current feed.

## Gotchas & OpSec
- **Aggregator, not a search engine** — no people/entity search; it points to third-party articles it doesn't vouch for.
- Persian-only; rely on translation and verify translated claims at the source.
- OpSec: **passive** — nothing about your subject is transmitted; use a VPN for your own hygiene when browsing regional sites.

## Overlaps ("do both")
- Complements mainstream news/search tools for the Iran beat — use Parseek to see what Iranian outlets are running, then verify and expand via primary sources and broader search engines.

## Trust & verifiability
`trust: community` — a real, live aggregator, but it only relays third-party headlines and disclaims their content; always confirm at the originating outlet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | parseek-iran |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
