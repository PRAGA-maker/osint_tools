---
id: ubersuggest-keyword-creator
name: Ubersuggest
description: Use when you have a `domain` and want its traffic, top pages, backlinks, and competitor/related domains — returns `domain` leads and site-footprint data.
url: https://neilpatel.com/ubersuggest/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Profiling a website's traffic, top content, backlinks, and competitor domains for domain/infrastructure OSINT.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier allows a small number of searches per day (historically ~3); deeper reports, more results, and history sit behind a subscription or lifetime plan.
opsec: passive
opsecNote: You query Ubersuggest's own aggregated SEO index, not the target's server, so the lookup is passive and unseen by the site owner. A free account is typically prompted after the first search.
humanInLoop: true
humanInLoopReason:
- rate-limit
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A well-known commercial SEO tool (NP Digital / Neil Patel); traffic and backlink figures are modeled estimates, not ground truth, so treat them as directional.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- neilpatel-backlinks-analyzer
- ubersuggest
aliases:
- ubersuggest
- neilpatel ubersuggest
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- seo
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Ubersuggest

> An SEO/traffic-analysis tool that, for OSINT, profiles a `domain`'s footprint — estimated traffic, top pages, keywords, backlinks, and competitor domains — surfacing related sites and content an owner would rather you didn't connect.

## When to use
You have a `domain` tied to your subject (their business site, blog, or a domain from a WHOIS pivot) and want to understand its footprint: how much traffic it gets, which pages matter, what keywords it ranks for, and — most usefully for link analysis — its **backlinks and competitor/related domains**. Backlinks can reveal other sites the subject controls or is affiliated with; top pages can surface content (bios, contact pages, staff lists) worth reading directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://neilpatel.com/ubersuggest/ in a sock-puppet browser.
2. Enter the target `domain` and run the domain overview.
3. Review: estimated traffic, top pages, ranking keywords, and the **backlinks** and "similar/competitor domains" reports.
4. Free searches are capped per day and a login is prompted — register a sock-puppet account; stop when you hit the paywall rather than paying.
5. Pivot: feed backlink and competitor `domain`s into WHOIS/registrant tools to find shared ownership; open top pages directly for names, emails, and addresses.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** traffic estimate, top pages, keywords, backlink `domain`s, competitor/related `domain`s
- **Empty/negative result looks like:** little or no data for an obscure/new domain (Ubersuggest models popular sites best), or a paywall gate before the useful detail loads.

## Gotchas & OpSec
- **Estimates, not facts:** traffic and backlink numbers are modeled — use them to find *connections* (which other domains), not to assert exact figures.
- Human-in-the-loop: a hard daily free-search cap and a login prompt; deep data is paid — don't pay, pivot to free tools instead.
- OpSec: passive; the target's server is never touched.

## Overlaps ("do both")
- Pairs with `[[neilpatel-backlinks-analyzer]]` (same provider) and with WHOIS/registrant and reverse-IP tools — Ubersuggest surfaces related domains; those confirm shared ownership/hosting behind them.

## Trust & verifiability
`trust: unverified` — a legitimate commercial SEO product, but its metrics are estimates; verify any domain relationship it suggests via WHOIS/DNS before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ubersuggest-keyword-creator |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
