---
id: seo-resources-search-engine
name: SEO Resources Search Engine
description: Use when you want to search across a curated set of SEO/marketing sites at once — returns web results scoped to that niche (no personal selectors).
url: https://cse.google.com/cse/publicurl?cx=005797772976587943970:i7q6z1kjm1w
category: social-networks
path:
- social-networks
bestFor: A niche vertical Google search restricted to SEO and web-marketing resource sites.
selectorsIn: []
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free Google Programmable Search Engine; no account needed to run a query.
opsec: passive
opsecNote: This is a normal Google search scoped to a preset site list; queries hit Google, not any target, so it is passive. Standard search-engine logging applies — use a sock-puppet Google session if you care about query attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom/Programmable Search Engine; coverage is whatever site list the (anonymous) creator picked and can silently rot as the config ages.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SEO CSE
- SEO resources custom search
tags:
- Search engines
- custom-search-engine
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# SEO Resources Search Engine

> A preset Google Programmable Search Engine that limits results to SEO/marketing resource sites — a vertical search, not an investigative data source.

## When to use
You are doing infrastructure/marketing-adjacent research — profiling how a domain is promoted, finding SEO tool references, or scanning marketing communities — and want Google results confined to a hand-picked set of SEO sites instead of the whole web. Its relevance to people-finding is marginal; it earns a place only as a topical filter when the rest of your investigation touches a subject's web/marketing footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL: https://cse.google.com/cse/publicurl?cx=005797772976587943970:i7q6z1kjm1w
2. Type your query (a `domain`, a marketing term, a tool name) into the embedded search box.
3. Results come back as normal Google links, restricted to the CSE's configured sites.
4. Pivot: a hit tells you which SEO/marketing property mentions a `domain`, feeding a broader domain-footprint workflow.

## Inputs → Outputs
- **In:** a free-text query (keyword or `domain`)
- **Out:** web results (`domain` links) scoped to the SEO site list
- **Empty/negative result looks like:** zero results, or the CSE fails to load — likely because the underlying config was removed or the creator's site list is stale.

## Gotchas & OpSec
- Human-in-the-loop: none; it is an embedded search box.
- OpSec: passive — it is Google under the hood. Use a clean session if query attribution matters.
- This is an anonymously-built CSE; its scope is opaque and can degrade without notice — treat results as "within this niche," not comprehensive. Marked `status: degraded` because such public CSEs are frequently abandoned.

## Overlaps ("do both")
- Pairs with a plain `site:`-scoped Google search — if the CSE is dead or too narrow, replicate it manually with `site:` operators against the SEO sites you care about.

## Trust & verifiability
`trust: community` — it is genuine Google search, but the value-add (the site list) is set by an unknown third party and unverifiable; confirm any lead by re-running it on open Google.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seo-resources-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | — → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
