---
id: ubersuggest
name: Ubersuggest
description: Use when you have a `domain` and want its SEO/traffic footprint — returns estimated traffic, top keywords, and backlink/competitor data for site profiling.
url: https://neilpatel.com/ubersuggest/
category: search-engines
path:
- search-engines
bestFor: Quick SEO/traffic profiling of a domain — estimated visits, ranking keywords, and backlinks.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: A few free lookups per day (with a free account); higher volume and full reports require a paid plan or lifetime license.
opsec: passive
opsecNote: Ubersuggest reports from its own crawl/SEO index, so it never touches the target site — passive and invisible to the subject. Free use is tied to a (sock-puppet) account/login that logs your queries. Metrics are *estimates*, not ground truth, so treat traffic/keyword figures as directional.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A mainstream commercial SEO tool (Neil Patel Digital); estimates are modeled, not measured, so figures are approximate and best cross-checked against another SEO source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Ubersuggest
- Neil Patel Ubersuggest
tags:
- keywords-discovery-and-research
- seo
- domain-profiling
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- neilpatel-backlinks-analyzer
- ubersuggest-keyword-creator
---

# Ubersuggest

> A mainstream SEO tool repurposed for OSINT: profile a domain's estimated traffic, the keywords it ranks for, and its backlinks — a quick read on a site's reach and focus.

## When to use
You have a `domain` and want a fast sense of its scale and subject matter: roughly how much traffic it gets, which keywords/topics it ranks for (hinting at its real focus or audience), and who links to it. Useful for sizing up a target's web presence or spotting the themes behind a site. SEO/marketing data, so OSINT relevance is indirect and missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://neilpatel.com/ubersuggest/ (the old `ubersuggest.org` redirects here) and sign in with a sock-puppet account for the free daily lookups.
2. Enter the target `domain` for a Traffic Overview: estimated monthly visits, top pages, and ranking keywords.
3. Check the Keywords and Backlinks reports to infer the site's topics/audience and its linking network (related `domain`s).
4. Treat every figure as an **estimate**; cross-check against another SEO tool before drawing conclusions.
5. Pivot linking/related domains into WHOIS/passive-DNS to test for common ownership.

## Inputs → Outputs
- **In:** `domain`
- **Out:** estimated traffic, ranking keywords/topics, backlink/referring `domain`s
- **Empty/negative result looks like:** near-zero traffic / no keywords — the site is small, new, or not in Ubersuggest's index; low estimates are unreliable for small sites, so don't over-read a blank.

## Gotchas & OpSec
- All metrics are **modeled estimates**, not real analytics — directional only; a second SEO source is wise.
- Free tier is capped to a few lookups/day behind a login; heavy use needs a paid plan.
- Small/regional sites are poorly covered — the index favors higher-traffic domains.

## Overlaps ("do both")
- Overlaps with backlink tools like [[openlinkprofiler]] and site overviews like [[web-check]] — Ubersuggest adds traffic/keyword estimates; cross-reference its backlink list with a dedicated backlink source before trusting it.

## Trust & verifiability
`trust: community` — a legitimate commercial SEO tool, but its figures are modeled estimates; use them to orient, and verify anything decision-relevant (traffic, links) against an independent source.
