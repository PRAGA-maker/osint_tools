---
id: better-chrome-web-store-search-engine
name: Better Chrome Web Store Search Engine
description: Use when you have a developer `name`/`username` and want their Chrome extensions — a Google CSE over the Chrome Web Store returning social-profile and domain.
url: https://cse.google.com/cse/publicurl?cx=006205189065513216365:pn3lumi80ne
category: search-engines
path:
- search-engines
bestFor: A Google Custom Search Engine that searches the Chrome Web Store more precisely than its native search.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account required.
opsec: passive
opsecNote: Searching a public CSE is passive and reveals nothing to any developer. Standard search hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-configured Google CSE scoped to the Chrome Web Store; results are Google's index of store pages.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Chrome Web Store CSE
- Better Chrome Web Store Search
tags:
- chrome-extensions
- custom-search-engine
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Better Chrome Web Store Search Engine

> A Google Custom Search Engine scoped to the Chrome Web Store — a precise way to find a developer's browser extensions and the identity clues attached to them.

## When to use
You are attributing browser extensions to a person or brand — for example, confirming what a developer published, finding an extension tied to a `username`/company, or pivoting from an extension to its listed developer, support site, and contact. The native store search is weak; this CSE lets you use Google operators over store listings, surfacing the developer's `social-profile`/store page and a support/homepage `domain`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL and search a developer `name`/`username`, extension name, or company.
2. Use quotes/operators to narrow; read the matching Chrome Web Store listings.
3. On a listing, note the developer name, listed website/support email, and other extensions by the same developer.
4. Pivot: developer site/email → domain and email OSINT; extension ID/developer → their other extensions; permissions/description → capability assessment.

## Inputs → Outputs
- **In:** `name`, `username`, extension/company name
- **Out:** `social-profile` (store/developer pages), `domain` (developer/support sites)
- **Empty/negative result looks like:** no matching listings — the extension may be unlisted/removed or the developer name differs; try the extension ID or Google directly with `site:chrome.google.com`.

## Gotchas & OpSec
- A CSE reflects Google's index — removed/unlisted extensions may not appear; cross-check with the store directly and archives.
- Developer-listed names/sites can be pseudonymous — treat as leads.
- OpSec: passive; safe.

## Overlaps ("do both")
- Pairs with direct `site:chrome.google.com` Google queries and extension-analysis tools — this CSE speeds discovery, while direct search and extension inspectors add coverage and technical detail.

## Trust & verifiability
`trust: community` — a community-built CSE over Google's index of the store; listings are authentic store pages, but developer-provided identity fields still need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | better-chrome-web-store-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
