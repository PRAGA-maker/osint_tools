---
id: spyfu
name: SpyFu
description: Use when you have a `domain` and want its SEO/PPC footprint — keywords, ad history and competitors — to profile the business behind a site; returns employer-org and domain leads.
url: https://www.spyfu.com
category: public-records
path:
- public-records
bestFor: Profiling the marketing footprint of a company website (paid keywords, ad copy, competitors) to understand the business behind a domain.
selectorsIn:
- domain
selectorsOut:
- employer-org
- domain
status: live
pricing: freemium
costNote: Free searches return limited/preview data (top keywords, some competitors); full keyword lists, ad history and exports require a paid plan.
opsec: passive
opsecNote: You query SpyFu's own crawled database, not the target site, so the domain owner is not notified. A SpyFu account (optional) ties searches to you — use a sock-puppet login if you want to unlock more free previews anonymously.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial SEO/PPC intelligence vendor; data is estimated/modeled from crawls, so figures are directional, not exact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- spyfu.com
tags:
- company-research
- seo
- ppc
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# SpyFu

> A competitive-marketing intelligence service: enter a domain and see the keywords it ranks for, the Google Ads it has run, and its competitors — a fast profile of the business behind a website.

## When to use
This is a business/context tool, not a person-finder. When an investigation centers on a company `domain` — a shell site, an employer, a scam page — SpyFu tells you how commercially active it is: whether it buys ads, what it markets, and which competitors sit alongside it. That helps characterize the `employer-org` behind a site and surface related `domain`s in the same niche.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spyfu.com and enter the target domain in the search box.
2. Review the free overview: estimated organic keywords, top paid keywords, sample ad copy, and named competitors.
3. Note the competitor list and any recurring brand/company names — these characterize the business and its market.
4. For deeper data (full keyword/ad history, exports, backlinks) a paid plan or trial is required; stop at the free preview if you only need a profile.
5. Pivot: competitor domains and ad copy → related `domain`s and the `employer-org`'s positioning; combine with WHOIS/registration tools to attribute ownership.

## Inputs → Outputs
- **In:** `domain`
- **Out:** SEO/PPC profile of the site → characterization of the `employer-org` and related competitor `domain`s.
- **Empty/negative result looks like:** "no data" for the domain — the site is too new, too small, or non-commercial to appear in SpyFu's crawl, which is itself a signal it isn't an active advertiser.

## Gotchas & OpSec
- All figures are *estimates* modeled from crawls — treat traffic, spend, and keyword counts as directional, not authoritative.
- The free tier caps how much you can see; the deep data is behind a paywall (`payment-wall-partial`).
- Coverage skews to sites that do SEO/PPC; a low-profile or brand-new domain may show nothing even if legitimate.

## Overlaps ("do both")
- Pairs with a WHOIS / domain-registration lookup — SpyFu describes what a site *does* commercially, while WHOIS tells you *who registered* it.

## Trust & verifiability
`trust: community` — a reputable commercial vendor, but its numbers are modeled estimates; verify any specific keyword/spend claim before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spyfu |
| category | public-records |
| selectorsIn → selectorsOut | domain → employer-org, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
