---
id: site-analyzer
name: Site Analyzer
description: Use when you have a `domain`/page and want an SEO/technical audit — returns indexability, content, and UX signals about the site (infrastructure/context, not personal data).
url: https://www.site-analyzer.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick SEO/technical audit of a website (indexability, content quality, UX) to profile a domain of interest.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Freemium — free page analysis without a credit card; paid plans for deeper/recurring audits.
opsec: passive
opsecNote: Passive toward any person — you audit a website's public pages. Note that the analyzer fetches the target site (its logs may see the scanner's requests, not necessarily yours), and you submit the URL to a third-party SaaS that logs it. Fine for public sites; avoid submitting sensitive/private URLs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial SEO-analysis SaaS (100k+ users); reliable for the technical/SEO signals it reports, but it profiles websites, not people.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Site Analyzer
tags:
- toddington
- seo
- website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Site Analyzer

> An SEO/technical website auditor — profile a domain's structure, content, and indexability; context on a site, not on a person.

## When to use
You have a `domain` tied to a subject (a personal site, a business, a suspicious page) and want a quick technical/SEO profile: is it indexed, how is it structured, what content/keywords define it, any obvious issues. It characterises the *site*, useful for context and pivots (keywords, linked platforms), not for identifying a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.site-analyzer.com/.
2. Enter the target `domain`/page URL and run the free analysis.
3. Read the output: an SEO/technical score across indexability, content, and UX, with prioritised issues and keyword signals.
4. Pivot: use surfaced keywords/tech/links as leads; combine with WHOIS/DNS and archive tools for a fuller domain picture.

## Inputs → Outputs
- **In:** a `domain` / page URL
- **Out:** SEO/technical audit signals about the `domain` (indexability, content, UX, keywords)
- **Empty/negative result looks like:** a page that can't be fetched (blocked/removed) returns no audit — try an archived copy or a different tool.

## Gotchas & OpSec
- **Site-level, not person-level** — no PII output; it profiles the website.
- Free tier limits depth/frequency; deeper audits are paid.
- Human-in-the-loop: none. OpSec: passive; don't submit private URLs to the SaaS.

## Overlaps ("do both")
- Do both with WHOIS/DNS and archive tools — those give ownership/history; Site Analyzer gives on-page/SEO structure.

## Trust & verifiability
`trust: community` — reputable SEO SaaS; its technical signals are reliable but tangential to identifying an individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | site-analyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
