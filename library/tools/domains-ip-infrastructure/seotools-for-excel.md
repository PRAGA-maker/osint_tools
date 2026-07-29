---
id: seotools-for-excel
name: SEOTools for Excel
description: Use when you have a `domain` (or list of URLs) and want to bulk-extract on-page HTML, domain age, and backlink signals into a spreadsheet — returns per-URL `domain` metadata.
url: http://seotoolsforexcel.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-scraping page titles, meta, headings, links, and domain age for many URLs at once inside Excel.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier of the Excel add-in covers the core on-page/HTTP functions (HtmlTitle, XPathOnUrl, DomainAge, Spider, etc.); a paid license unlocks unlimited use and premium connectors (Majestic, Analytics).
opsec: active
opsecNote: The Spider crawler and Html* functions fetch the target pages directly from your machine, so your IP appears in the target's server logs. Route through a VPN/proxy and throttle crawl rate if the site is monitored.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-running third-party Excel add-in by Niels Bosma; widely used in SEO circles but not an official Microsoft product — treat scraped values as raw, unaudited page data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SeoTools
- SEO Tools for Excel
tags:
- domain-and-ip-research
- scraping
- bulk-analysis
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# SEOTools for Excel

> An Excel add-in that turns spreadsheet cells into web-scraping functions — bulk-pull titles, meta, headings, links, and domain age across hundreds of URLs at once.

## When to use
You have a list of `domain`s or URLs (target's sites, sites that link to them, a set of suspicious pages) and want to extract structured on-page data — titles, meta descriptions, H1s, outbound links, domain age — for all of them in one pass, laid out as a spreadsheet you can sort and filter, rather than opening each page by hand.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the add-in into desktop Excel (Windows) from the tool's site.
2. Paste your URL list down a column.
3. In an adjacent column call a function against that cell, e.g. `=HtmlTitle(A2)`, `=XPathOnUrl(A2,"//h1")`, `=CheckBacklink(...)`, or `=DomainAge(A2)`.
4. Fill the formula down; Excel fetches each page and returns the extracted value per row.
5. For deeper crawls use the built-in Spider to enumerate a site's pages, then run Html* functions over the results.
6. Pivot: sort by domain age / shared meta to cluster related sites, or feed extracted registrant-ish links into WHOIS/infra tools.

## Inputs → Outputs
- **In:** `domain` / URL list
- **Out:** per-URL page metadata (title, meta, headings, links), `DomainAge`, backlink presence
- **Empty/negative result looks like:** `#VALUE!` / blank cells or timeouts — the page blocked the fetch, is offline, or the XPath matched nothing; not proof the content is absent.

## Gotchas & OpSec
- Active: every function call is a live HTTP request from *your* IP to the target — this is scraping, so use a VPN and reasonable rate limits against monitored sites.
- Windows desktop Excel only; the add-in must be installed locally (`localInstall: true`).
- Premium connectors (Majestic backlinks, Google Analytics) need their own API keys/accounts; the free core functions do not.

## Overlaps ("do both")
- Pairs with a dedicated WHOIS tool like [[easywhois]] — SEOTools bulk-harvests *page content* across many URLs, while WHOIS gives the *registration* layer for each domain.

## Trust & verifiability
`trust: community` — a well-established but third-party add-in; the values it returns are raw page scrapes, so verify anything load-bearing by opening the source URL directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seotools-for-excel |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
