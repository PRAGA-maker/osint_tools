---
id: neuskool
name: Neuskool
description: Use when you have one selector and want to query it across many services from one page — returns a start-page launcher for Google, YouTube, Wikipedia, Twitter, and more.
url: https://neuskool.com/
category: search-engines
path:
- search-engines
bestFor: A privacy-minded personal start page that launches one query into many search and content services.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free personal start page; no account. States it collects no personally identifiable information.
opsec: passive
opsecNote: The page forwards your query straight to each service and says it does not collect PII, so exposure equals whatever the destination service logs. Use a sock-puppet/VPN when the underlying searches are sensitive; the launcher itself adds little footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent start page; it aggregates links to third-party engines and adds no data of its own.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- search-it
aliases:
- Neuskool
- neuskool.com
tags:
- toddington
- curated-directory
- search-engines
- start-page
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Neuskool

> A tidy, privacy-minded start page that puts many search and content services on one screen — launch a name or handle into Google, YouTube, Wikipedia, Twitter, AI tools, and shops from a single box.

## When to use
You want a fast, low-friction hub to run the same `name` or `username` across a broad set of services (web search, video, encyclopedia, social, shopping) without maintaining your own bookmarks. Like other start pages, Neuskool is a launcher — it holds no data itself and simply forwards your query to each destination's native search. Handy for opening a wide reconnaissance sweep quickly, especially since it emphasises not collecting personal data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://neuskool.com/.
2. Enter your query and select a service (Google, YouTube, Wikipedia, Twitter, an AI tool, a shop, etc.).
3. The query opens in that service's own results; step through the services relevant to your selector.
4. Note which services surface the subject and where.
5. Pivot: any hit becomes a `social-profile` or reference to enrich with a dedicated tool; reused handles feed a cross-site username checker.

## Inputs → Outputs
- **In:** `name` / `username`
- **Out:** launched searches surfacing candidate `social-profile`s and references across services
- **Empty/negative result looks like:** empty results on the destination services — the launcher merely forwarded the query; judge each service's output on its own, not the start page.

## Gotchas & OpSec
- No independent search power: results are only as good as the destination engines, so this is a convenience/time-saver.
- Exposure is whatever each destination logs; the page's no-PII claim covers the launcher, not the third-party services it opens.
- As a single-maintainer site, its link set can drift; if a service link fails, go to that service directly.

## Overlaps ("do both")
- Pairs with `[[search-it]]` (a near-identical launcher with a different service set) and with automated cross-site username tools — use a start page for quick manual sweeps, an enumerator for structured, repeatable fan-out.

## Trust & verifiability
`trust: community` — an independent start-page aggregator that only links to established services and adds no data of its own; verify any lead on the destination platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | neuskool |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
