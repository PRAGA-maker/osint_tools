---
id: web-tech-survey
name: WebTechSurvey
description: Use when you have a `domain` and want its technology stack, or a technology and want every site using it — returns detected tech per site and reverse tech-to-sites lists.
url: https://webtechsurvey.com/website/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting a website's tech stack and, in reverse, enumerating all sites that share a given technology or recently switched it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier profiles a site's tech and gives limited reverse-lookup; deeper/bulk technology-to-sites lists and filters are behind one-time-purchase/subscription plans.
opsec: passive
opsecNote: WebTechSurvey reads from its own pre-crawled index of ~120M sites, so a lookup does NOT touch the target's server or alert them. (If you use its live "scan" feature it fetches the site fresh, which does hit the target — prefer the indexed lookup for passive work.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party technology-fingerprinting index; detection is signal-based (headers, scripts, cookies, DNS) and can miss or mislabel, and index freshness varies per site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Web Tech Survey
- webtechsurvey.com
tags:
- technology-lookup
- tech-stack
- reverse-technology
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# WebTechSurvey

> A website technology profiler with a reverse mode: "what is this site built with?" and, crucially, "what other sites use this same technology?"

## When to use
You have a `domain` and want its stack — CMS, frameworks, web server, analytics, plugins, outdated components. Or you have a technology (or a specific tracking/analytics ID pattern) and want the *reverse*: every indexed site using it. That reverse pivot is the OSINT value — linking a person's/org's multiple sites that share the same rare technology, hosting fingerprint, or a switch made at a specific time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Forward lookup: go to `https://webtechsurvey.com/website/<domain>` (append the target domain) to see its detected stack.
2. Reverse lookup: use `https://webtechsurvey.com/technology/<tech>` (or the technology-scan/filters UI) to list sites using a technology, filterable by version, category, country, IP location, language, and TLD.
3. Read the signals — detection is based on HTML, script/stylesheet includes, cookies, DNS records, and HTTP headers.
4. Pivot: a shared, uncommon technology across sites suggests common ownership/authorship; feed candidate `domain`s into WHOIS/DNS-history tools to confirm the link.

## Inputs → Outputs
- **In:** `domain` (forward) or a technology name (reverse)
- **Out:** detected technologies for a site, or a list of `domain`s sharing a technology
- **Empty/negative result looks like:** "no technologies detected" or an empty site list — the site may be outside the ~120M-site index, or the tech leaves no detectable signal; absence is not proof.

## Gotchas & OpSec
- Prefer the **indexed** lookup (passive) over the live scan feature (which fetches the target's server directly).
- Detection is heuristic: common on false negatives for custom/obfuscated stacks and can mislabel versions.
- Reverse lookups at scale and full filtering are paid; the free tier is limited.

## Overlaps ("do both")
- Pairs with WHOIS/DNS-history and analytics-ID tools (e.g. Wappalyzer, BuiltWith, DNSlytics): WebTechSurvey suggests sites sharing a technology, and registration/analytics-ID tools confirm whether they share an *owner* — do both to turn a tech coincidence into an ownership link.

## Trust & verifiability
`trust: community` — a useful third-party fingerprinting index, but signal-based detection and variable freshness mean every match is a lead to corroborate, not a confirmed fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-tech-survey |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
