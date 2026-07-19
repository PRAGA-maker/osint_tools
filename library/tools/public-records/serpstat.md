---
id: serpstat
name: Serpstat
description: Use when you have a `domain` and want its SEO/traffic footprint — returns keywords, competitors, backlinks and estimated visibility to profile a site or organization.
url: https://serpstat.com
category: public-records
path:
- public-records
bestFor: Profiling a domain's search footprint, backlinks and competitor set to understand an organization's online presence.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Freemium — a free account gives a small daily quota of lookups; deep backlink/keyword data needs a paid plan or the 7-day trial.
opsec: passive
opsecNote: You query Serpstat's own index, not the target's server, so the site owner is not directly pinged. A free account requires registration (email), which is attributable — use a research identity. Nothing is written to the target.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial SEO analytics vendor; metrics (traffic, keyword volume, visibility) are Serpstat's estimates from its own crawl, so treat figures as directional, not exact.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Serpstat SEO
tags:
- company-research
- domain-analytics
- seo
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Serpstat

> An SEO/domain analytics platform — point it at a `domain` to profile its keywords, competitors, backlinks and estimated traffic when you're investigating an organization's web presence.

## When to use
You have a `domain` tied to a person or organization and want to understand its footprint: what it ranks for, who its "competitors" (thematically similar sites) are, which sites link to it, and roughly how much traffic it draws. Backlink and competitor data can reveal an organization's network — partner sites, aliases, affiliated projects — that isn't obvious from the site itself. It's a company/infrastructure-profiling aid, not a people-lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free Serpstat account (or start the 7-day trial for full data) at https://serpstat.com.
2. Enter the target `domain` in Domain Analysis; read visibility, top keywords, and estimated traffic.
3. Open the Backlinks report to see linking domains — these often expose affiliated or partner sites.
4. Check the "competitors" list for thematically-linked domains that may share ownership or interest.
5. Pivot: newly-surfaced `domain`s feed WHOIS/DNS and further web-presence tools.

## Inputs → Outputs
- **In:** `domain`
- **Out:** keywords, competitor `domain`s, backlink sources, estimated traffic/visibility
- **Empty/negative result looks like:** little or no keyword/backlink data — meaning the domain is new, tiny, or de-indexed, not necessarily inactive.

## Gotchas & OpSec
- Human-in-the-loop: the free tier is quota-limited (a handful of reports/day) and requires an email registration — use a research account and pace your lookups.
- Metrics are Serpstat's estimates, not ground truth — directional only.
- Full backlink/keyword depth is paywalled; the free tier still gives enough for a first-pass footprint.

## Overlaps ("do both")
- Pairs with WHOIS/DNS and other backlink tools — this profiles search visibility and link neighbours, those resolve registration and hosting.

## Trust & verifiability
`trust: community` — a commercial vendor's estimated analytics; useful for shape and relationships, but confirm any specific claim (ownership, affiliation) against registration/primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | serpstat |
| category | public-records |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
