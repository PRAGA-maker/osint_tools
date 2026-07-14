---
id: xquik
name: Xquik
description: Use when you have a `username` or keyword and want to search public X (Twitter) posts and export an account's follower list — returns `social-profile` links, post content, and `associate` connections.
url: https://xquik.com
category: social-networks
path:
- social-networks
bestFor: Searching public X/Twitter posts by keyword/account/operator and exporting an account's followers to map connections, via a dashboard or API.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
- name
status: live
pricing: freemium
costNote: Third-party X-access platform with a dashboard, REST API and MCP server. A free tier exists for basic use; higher-volume search and follower export sit behind paid plans and require account signup / OAuth.
opsec: active
opsecNote: You connect an X account (OAuth 2.1) to use it, so activity is attributable to that account — use a research/sock-puppet X login, never a personal one. Follower exports and keyword monitoring generate real API traffic against X.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third party, explicitly not affiliated with X Corp. Data reflects X's public API; treat coverage as best-effort and verify anything load-bearing directly on X.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- xquik.com
tags:
- twitter
- x
- follower-export
- api
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Xquik

> A third-party X (Twitter) toolkit — dashboard plus REST API and MCP server — whose OSINT-useful pieces are public-post search and bulk follower export.

## When to use
You have an X `username` (or a keyword/name) and want either the subject's public posting history filtered by term/operator, or their follower/following graph exported for associate mapping. Xquik packages both behind a dashboard and API, which is faster than scraping X manually when you need paginated bulk output.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at xquik.com and connect a research X account via OAuth.
2. In the dashboard, use post search to query by keyword, account, or operator expression; or use the follower-export tool against a target handle.
3. Let the export paginate through the follower list; download the results.
4. For automation, drive the same functions through the REST API / MCP server documented on the site.
5. Pivot: exported followers are candidate `associate` links to enrich individually; post content can surface locations, dates and other handles.

## Inputs → Outputs
- **In:** `username` / `name` / keyword or operator query
- **Out:** `social-profile` and post content, plus `associate` lists (followers/following) and display `name`
- **Empty/negative result looks like:** search returns no posts (account is private, suspended, or the term genuinely never appears), or an export truncates at a plan/rate limit — check whether you hit a paywall before concluding the data isn't there.

## Gotchas & OpSec
- Human-in-the-loop: requires signup and an OAuth-connected X account; the free tier caps volume, and large follower exports need a paid plan.
- OpSec: **active** and attributable — everything runs through the X account you connect. Use a dedicated sock-puppet, expect X-side rate limits, and don't authorize a personal login.

## Overlaps ("do both")
- Pairs with native X search and other Twitter-OSINT tooling — Xquik wins on bulk follower export and API access, while direct X viewing wins on freshness and avoiding a third party in the loop.

## Trust & verifiability
`trust: community` — an unaffiliated third-party service surfacing X's public data; useful for scale but verify any critical finding against X directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xquik |
