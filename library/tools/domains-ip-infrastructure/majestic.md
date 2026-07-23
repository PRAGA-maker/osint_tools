---
id: majestic
name: Majestic
description: Use when you have a `domain` and want to map who links to it — returns the backlinking `domain`s and link-intelligence metrics (Trust Flow / Citation Flow) that expose a site's network and affiliations.
url: https://majestic.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Backlink / inbound-link intelligence — discovering which sites link to a target domain and how reputable that link neighborhood is.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free Lite tier and rotating free demo searches give limited backlink/Site Explorer data; full backlink profiles require a paid subscription. Free browser plugin and basic backlink checker available.
opsec: passive
opsecNote: You query Majestic's crawl index, never the target site, so the domain owner sees no visit from you. Deeper use requires a Majestic account, which ties the searches to your registration — use a dedicated investigative account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial link-intelligence provider (operating since 2004) with its own large-scale web crawl; widely used in SEO and investigations, though free-tier data is deliberately capped.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- ahrefs
aliases:
- Majestic SEO
- MajesticSEO
tags:
- domain-and-ip-research
- backlinks
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Majestic

> A long-running backlink-intelligence platform: point it at a `domain` and it maps the web of sites linking in, scored by its Trust Flow / Citation Flow metrics.

## When to use
You have a `domain` — a target's website, a scam or disinformation site, a business front — and you want to understand its network: which other sites link to it (revealing affiliates, mirrors, partner networks, or a coordinated cluster) and how reputable that neighborhood is. Backlink structure often exposes relationships that the site itself hides, and Trust Flow gives a quick read on whether a domain sits in a spammy or legitimate link ecosystem.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://majestic.com. Try a rotating free demo search, or log into a (free Lite or paid) account for a specific domain.
2. Enter the target `domain` in Site Explorer.
3. Read the summary: Trust Flow, Citation Flow, Topical Trust Flow (what subjects the link neighborhood covers), and referring-domain counts.
4. Open the referring-domains / backlinks tab to list the actual linking `domain`s (depth here is what the paywall limits).
5. Pivot: unexpected referring domains feed a link-graph and further WHOIS/infra checks; Topical Trust Flow flags the site's thematic associations.

## Inputs → Outputs
- **In:** `domain`
- **Out:** backlinking `domain`s, Trust Flow / Citation Flow / Topical Trust Flow metrics, referring-domain counts
- **Empty/negative result looks like:** near-zero referring domains and no Trust Flow — either a brand-new/obscure site Majestic has barely crawled, or a genuinely isolated one. Cross-check with a second backlink tool before concluding "no network."

## Gotchas & OpSec
- Human-in-the-loop: the free tier caps how many backlinks you can see per domain; the full referring-domain list sits behind a paid plan (partial paywall).
- Data is from Majestic's own crawl (Fresh vs Historic Index) — coverage is broad but not exhaustive, and differs from competitors, so numbers won't match Ahrefs exactly.
- OpSec: passive toward the target; deeper searches are logged against your Majestic account, so keep a dedicated investigative login.

## Overlaps ("do both")
- Pairs with `[[ahrefs]]` — both are backlink-intelligence engines with independent crawls, so running the same domain through both catches referring domains one index missed and lets you triangulate the true link network.

## Trust & verifiability
`trust: trusted` — a well-established commercial provider (since 2004) with its own large web crawl; the metrics are proprietary but reputable, with the main caveat that free-tier depth is intentionally limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | majestic |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
