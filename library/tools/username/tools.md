---
id: tools
name: Intelligence X Third-Party Search Tools
description: Use when you have a `username` (or email/phone/domain/name/image) and want to fan it out across dozens of people-search and social sites at once — returns links to matching `social-profile`s and person records on each service.
url: https://intelx.io/tools?tab=username
category: username
path:
- username
bestFor: Fanning a single selector out across many people-search and social platforms from one page.
selectorsIn:
- username
- email
- phone
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: The third-party search launcher is free and needs no Intelligence X account; it only builds and opens query links on external sites. Intelligence X's own breach/leak search (a separate product) is the paid part.
opsec: passive
opsecNote: The launcher just constructs URLs on third-party services and opens them — Intelligence X itself does not see your target. Exposure comes from the destination sites: each query hits that platform directly, so some (e.g. the Facebook Graph searcher, which requires you to be logged in) can tie the lookup to your account. Use a sock-puppet where a destination needs login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Intelligence X, a well-known OSINT/search company; the tools page is a transparent link-builder over reputable third-party services, not a scraper of its own.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- facebook-graph-searcher-intelligencex
- intelligence-x
- intelligence-x-2
- intelligence-x-person-tools
- intelligence-x-telegram-search
- intelligencex
- intelligencex-linkedin-search
- intelx-io
aliases:
- Intelligence X Tools
- intelx tools
- IntelX third-party search
tags:
- username
- search-aggregator
- pivot-hub
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Intelligence X Third-Party Search Tools

> Intelligence X's free "Tools" page: pick a selector tab (username, email, phone, domain, IP, name, image, bitcoin…) and it launches your query across a curated set of external services in one place.

## When to use
You have one selector — most often a `username`, but also `email`, `phone`, `domain`, `name`, or an `image` — and you want to sweep it across many people-search and social platforms without hand-typing each site. This page is a pivot hub: enter the value once and it opens pre-built searches on namevine, PeekYou, usersearch, Twitter/X, Facebook, YouTube, Tumblr, Instagram, Gravatar, Tinder, GitHub, and more (for username), with parallel tabs for the other selector types.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intelx.io/tools and select the tab for your selector (e.g. **Username**, **Email**, **Phone number**, **Domain**).
2. Type the value into the input at the top of that tab.
3. Click a service in the list (or "search on" each) — it opens that platform's results for your value in a new tab.
4. Work down the list, noting which services return a real `social-profile` / person record and which come up empty.
5. Watch for per-service notes — e.g. the Facebook Graph searcher requires you to be logged into Facebook.
6. Pivot: a confirmed profile on one platform hands you a new username/real `name`/image to run back through the other tabs.

## Inputs → Outputs
- **In:** `username` (primary), or `email` / `phone` / `domain` / `name` / `image` via the other tabs
- **Out:** links to matching `social-profile`s and person records across the listed services, plus corroborating `name`s
- **Empty/negative result looks like:** each service opens its own "no results" page — the launcher can't tell you a hit exists, only send you to check. Treat it as a dispatcher, not a database.

## Gotchas & OpSec
- It doesn't aggregate results into one view — it opens each service separately, so you interpret each site's page yourself.
- Some destinations require login (Facebook Graph search) or have their own rate limits/captchas.
- OpSec: passive at IntelX (it just builds URLs), but each opened search hits the destination directly — use a sock-puppet browser for any that tie to a logged-in account.

## Overlaps ("do both")
- Do both with a dedicated username-enumeration tool like a Sherlock/WhatsMyName-style checker: this page covers the big consumer platforms and people-search sites by hand, while an enumerator brute-checks hundreds of niche sites automatically. Together they cover breadth and long-tail.

## Trust & verifiability
`trust: trusted` — maintained by Intelligence X, a reputable OSINT vendor; the page is a transparent link-builder over third-party services, so trust each *result* as far as you'd trust that underlying platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tools |
| category | username |
| selectorsIn → selectorsOut | username, email, phone → social-profile, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
