---
id: moz-link-explorer
name: Moz Link Explorer
description: Use when you have a `domain`/URL and want its backlink profile and linked/linking domains — returns linking `domain`s, anchor text and authority scores.
url: https://moz.com/link-explorer
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping who links to (and from) a site to surface related domains, networks and the reputation of a web property.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier via a free Moz account with a small monthly query allowance and capped result rows; full backlink data requires a paid Moz Pro subscription.
opsec: passive
opsecNote: Queries Moz's own crawl index, not the target's server, so it does not alert the site owner. Passive. Standard sock-puppet account/browser hygiene still advised.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Moz, a long-established SEO vendor with its own large link index; data is reputable though its crawl coverage is not exhaustive.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- followerwonk-tools-for-twitter-analytics-bio-search-and-more
- moz-analytics-open-site-explorer
aliases:
- Open Site Explorer
- Moz Backlink Checker
tags:
- bellingcat-toolkit
- websites
- backlinks
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Moz Link Explorer

> Moz's backlink index for any site — reveals who links to a domain and what it links out to, exposing related properties and networks.

## When to use
You have a `domain` (a subject's site, a suspicious business, a campaign page) and want its backlink profile: which other domains link to it, what anchor text they use, and how authoritative the site is. Backlink overlap is a strong signal for uncovering related/affiliated sites and the wider network around a web property.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a free Moz account at https://moz.com/link-explorer.
2. Enter the target `domain` or a specific URL and run the report.
3. Read Inbound Links (linking domains, anchor text), Linking Domains, and Domain/Page Authority; note recurring linkers that may indicate an owned network.
4. Pivot linking `domain`s into WHOIS/passive DNS to test whether they share registration or hosting with the target.

## Inputs → Outputs
- **In:** `domain` or URL
- **Out:** linking/linked `domain`s, anchor text, authority scores
- **Empty/negative result looks like:** few or no backlinks and low authority — either a new/obscure site or one outside Moz's crawl; corroborate with a second backlink source before concluding it is isolated.

## Gotchas & OpSec
- Human-in-the-loop: free Moz account required; the free tier is rate-limited (few queries/month, capped rows).
- OpSec: passive — you query Moz's index, not the target's server.
- Coverage is Moz's crawl, not the whole web; cross-check against another backlink tool for completeness.

## Overlaps ("do both")
- Overlaps with other backlink/passive-DNS tools: Moz shows the *link graph* around a domain, passive DNS shows the *infrastructure* graph — combine to confirm a suspected network of related sites.

## Trust & verifiability
`trust: trusted` — a reputable commercial index; reliable within its crawl coverage, which is broad but not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | moz-link-explorer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
