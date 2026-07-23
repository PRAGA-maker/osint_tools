---
id: google-subdomains
name: Google Subdomains
description: Use when you have a `domain` and want subdomains and pages that Google has indexed — the `site:` dork returns additional `domain` values and URLs.
url: https://www.google.com/?gws_rd=ssl#q=site:%3Cdomain.com%3E
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Fast passive subdomain and page discovery using Google's search index and the site: operator.
input: 'Domain name (as Google Dork syntax: site:domain.com)'
output: Indexed subdomains and pages from Google search results
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
opsec: passive
opsecNote: Queries Google's index, not the target domain, so the target sees no traffic. Google itself logs your searches and dork-heavy sessions can trigger a CAPTCHA — use a clean/sock-puppet session.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Not a tool but a search technique over Google's public index; reliability is bounded by whatever Google has crawled and chosen to show.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- certificate-search
aliases:
- Google site dork
- 'site: operator'
tags:
- subdomain-enumeration
- google-dork
source: arf-seed
lastVerified: '2026-07-23'
---

# Google Subdomains

> Not a product — the `site:` Google dork used as a passive subdomain and page finder for a target domain.

## When to use
You have a `domain` and want the subdomains and specific pages Google has already indexed, without touching the target's servers. It complements certificate-log and DNS enumeration by surfacing hostnames that actually serve public, crawlable content — often the interesting ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, search `site:domain.com` to see indexed pages for the whole domain.
2. Peel off known hostnames to expose new ones: `site:*.domain.com -www` (exclude the main site), then subtract each subdomain you find (`-mail -shop …`) to force fresh ones to the top.
3. Read the results: each distinct hostname in the URLs is a discovered subdomain; the page titles/paths hint at what it hosts.
4. Pivot: resolve discovered subdomains to IPs, run them through `[[certificate-search]]` and WHOIS, or check archives for removed pages.

## Inputs → Outputs
- **In:** `domain` (as `site:domain.com` dork syntax)
- **Out:** additional `domain` values (indexed subdomains) and page URLs
- **Empty/negative result looks like:** "no results" or only the apex site — means Google hasn't indexed subdomain content (robots.txt/noindex, or private hosts), not that subdomains don't exist.

## Gotchas & OpSec
- Human-in-the-loop: aggressive dorking triggers Google's "unusual traffic" CAPTCHA; solve it manually and slow down.
- Only crawlable, indexed content appears — internal, blocked, or brand-new hosts stay invisible, so this is a complement to, not a replacement for, CT-log and DNS enumeration.
- OpSec: **passive** toward the target (no direct contact), but Google logs your queries; use a sock-puppet session for sensitive work.

## Overlaps ("do both")
- Pairs with `[[certificate-search]]` and dedicated subdomain finders — search-index dorking and certificate-transparency logs reveal different hostnames, so run both and merge.

## Trust & verifiability
`trust: unverified` — a technique, not a curated source; every hostname it surfaces should be independently resolved before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-subdomains |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
