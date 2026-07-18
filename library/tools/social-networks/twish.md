---
id: twish
name: Twish
description: Use when you want to build an advanced Twitter/X search query (by user, keyword, date, engagement) from a `name`/`username` without memorising operators — returns `social-profile`.
url: https://chromewebstore.google.com/detail/twish/afpegchfbaddfmenhkajjggbnjfjejeh
category: social-networks
path:
- social-networks
bestFor: Quickly constructing precise Twitter/X advanced-search queries from a simple form.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free Chrome extension; no account or payment. (X's own advanced search still requires being logged in to view many results.)
opsec: passive
opsecNote: The extension only builds a twitter.com/x.com search URL locally; the actual searching happens on X, which sees the request. Do it from a sock-puppet X session, not your personal login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A small third-party Chrome extension (cyb-detective-sourced); it just assembles query strings, but as a legacy extension its behaviour may lag X's frequent search changes — verify results on X.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Twish Chrome extension
tags:
- Social Media
- Twitter
- advanced-search
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Twish

> A Chrome extension that turns a simple form into a precise Twitter/X advanced-search query — so you can filter a subject's posts by keyword, date, and engagement without hand-writing operators.

## When to use
You're searching Twitter/X for a subject's activity and want tight control — a specific `username`'s posts in a date window, mentions of a `name`, tweets above an engagement threshold — but don't want to memorise X's `from:`, `since:`, `min_faves:` operators. Twish gives you a builder UI and hands you the ready query. It's a convenience layer over X search, so its value is speed and precision on a platform you're already working; low standalone relevance.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Twish from the Chrome Web Store (https://chromewebstore.google.com/detail/twish/afpegchfbaddfmenhkajjggbnjfjejeh).
2. Open the extension and fill the fields: from-user (`username`), keywords (`name`/terms), date range, min engagement, etc.
3. Run it — it opens the assembled advanced-search query on Twitter/X.
4. Be logged into a sock-puppet X account (most search results require an authenticated session on X now).
5. Read the output: the filtered tweet set (`social-profile` activity). Pivot: reuse the handle on cross-platform username tools; save useful queries.

## Inputs → Outputs
- **In:** `name` / `username` plus filter criteria (dates, engagement)
- **Out:** `social-profile` — a filtered view of a subject's Twitter/X posts
- **Empty/negative result looks like:** X returns no tweets for the query — the account is protected/suspended/inactive, the date window is wrong, or you're not logged in; check each before concluding.

## Gotchas & OpSec
- Human-in-the-loop: X now gates most search behind a login — use a sock-puppet account, never your personal one.
- OpSec: passive locally, but the search runs on X, which logs it against whatever session you use.
- Status degraded: X changes its search behaviour often; a legacy query-builder can produce queries X no longer honours — always sanity-check results against X directly.

## Overlaps ("do both")
- Redundant with X's native advanced-search page and other query-builder extensions — Twish just speeds up query construction; the results and their limits are X's.

## Trust & verifiability
`trust: unverified` — a small third-party extension that only assembles query strings; trust the tweets you see on X itself, and treat the builder as a convenience whose operators may drift out of date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twish |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
