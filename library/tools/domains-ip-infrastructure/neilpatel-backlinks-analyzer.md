---
id: neilpatel-backlinks-analyzer
name: Neilpatel backlinks analyzer
description: Use when you have a `domain`/page and want to see which other sites link to it — returns referring `domain`s and backlink details, exposing a site's network and promoters.
url: https://app.neilpatel.com/en/seo_analyzer/backlinks
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping who links to a target site — referring domains that reveal its network, affiliates and promotion.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Part of Ubersuggest (Neil Patel). A few free lookups per day; fuller reports/exports need a paid plan or login.
opsec: passive
opsecNote: Queries Ubersuggest's own backlink index, not the target site, so nothing touches the subject's server. Ubersuggest logs your query and prompts for a login for deeper data.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party backlink index (Ubersuggest). Coverage is a sample, not exhaustive; treat counts as indicative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ubersuggest
- ubersuggest-keyword-creator
aliases:
- Ubersuggest backlinks
tags:
- Domain/IP/Links
- Backlinks analyze
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Neilpatel backlinks analyzer

> The backlinks view of Ubersuggest — see which sites link to a target `domain`, exposing the network of affiliates, promoters and related properties around it.

## When to use
You have a `domain`/page and want to know who points at it. Inbound links reveal relationships a site won't advertise: partner and affiliate sites, the same operator's other domains, forums/blogs promoting it, and PR footprints. For OSINT this maps a target's web neighbourhood and surfaces new `domain`s to investigate. Peripheral to missing-persons cases; useful for entity/infrastructure mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.neilpatel.com/en/seo_analyzer/backlinks and enter the `domain`.
2. Read the list of referring domains and individual backlinks (anchor text, link URL, authority).
3. Note clusters of related sites and repeated referrers — candidate affiliates or same-owner properties.
4. Free lookups are rate-limited (a few per day); sign in or space out queries for more.
5. Pivot: a referring `domain` becomes a new target; shared referrers across sites hint at common ownership.

## Inputs → Outputs
- **In:** `domain`/page URL
- **Out:** referring `domain`s and backlink details (anchor text, source URLs) → candidate related sites
- **Empty/negative result looks like:** few/no backlinks for a new, private, or obscure site — Ubersuggest's index is a sample, so absence isn't proof; a dedicated backlink tool may show more.

## Gotchas & OpSec
- Human-in-the-loop: daily free-query rate limit; a login prompt gates deeper reports.
- OpSec: **passive** — you query Ubersuggest's index, not the target. Use a burner account if you log in.
- Backlink coverage is partial and sometimes stale; corroborate an important link relationship with a second index.

## Overlaps ("do both")
- Pairs with `[[ubersuggest]]` and `[[ubersuggest-keyword-creator]]` (same platform) for keyword/traffic context, and with any second backlink index to widen coverage.

## Trust & verifiability
`trust: unverified` — a third-party backlink sample; directionally useful for mapping a network, but never treat its counts as complete.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | neilpatel-backlinks-analyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
