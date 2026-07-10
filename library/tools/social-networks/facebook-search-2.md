---
id: facebook-search-2
name: Facebook Search (SowSearch)
description: Use when you have a `name`, `employer-org`, school or city and want to run structured people/post/photo searches on Facebook after Graph Search was killed — returns `social-profile` links and public posts.
url: https://www.sowsearch.info/
category: social-networks
path:
- social-networks
bestFor: Rebuilding Facebook Graph-Search-style queries (people by employer/school/city, posts, photos, places) through a form that emits real Facebook search URLs.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source front-end. No account with SowSearch is needed, but you must be logged into your own Facebook account for the generated search URLs to return results.
opsec: active
opsecNote: SowSearch itself just builds URLs, but clicking through executes the search inside your logged-in Facebook session, so results and clicks are tied to whatever account you use. Use a sock-puppet Facebook account and browser profile, never your real one — Facebook logs searches and profile visits.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community tool by sowdust (open-source, github.com/sowdust). It only constructs Facebook search URLs — the data comes from Facebook itself, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SowSearch
- sowsearch.info
- Facebook Graph Search replacement
tags:
- facebook
- social-networks
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Facebook Search (SowSearch)

> A form-driven rebuild of Facebook's dead Graph Search: fill in fields, and it emits the real Facebook search URLs Facebook no longer exposes in its own UI.

## When to use
You have a `name`, or partial identity attributes (an `employer-org`, a school, a home city, an interest), and want to enumerate a subject's Facebook presence or find public posts/photos matching structured criteria. This is the go-to when Facebook's own search box won't let you filter by "people who work at X and live in Y," which Graph Search used to do.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** Facebook account in a clean browser profile (the generated links only work while authenticated to Facebook).
2. Open https://www.sowsearch.info/ and pick a search category (people, posts, photos, pages, places, videos, events).
3. Fill in the fields you have — name, city, employer, school, keywords, date range — and submit. SowSearch builds a Facebook search URL and opens it in your session.
4. Read the results on Facebook itself: matching profiles (`social-profile`), public posts, tagged photos.
5. Pivot: a confirmed profile feeds face/photo tools and friend-graph mapping; a public post can geolocate or timestamp the subject.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `address` (city/school), keywords
- **Out:** `social-profile` (Facebook profiles), public posts, photos, events
- **Empty/negative result looks like:** Facebook returns "We couldn't find anything" or a generic keyword page. Because Facebook constantly changes its search internals, some query types silently return nothing even when matches exist — treat empty as "this query shape is broken today," not "subject absent."

## Gotchas & OpSec
- Human-in-the-loop: you must be logged into Facebook for the links to resolve; SowSearch cannot search anonymously.
- Facebook has repeatedly broken these query patterns (the underlying SearchBook extension stopped working in 2019); expect some categories to be dead. Try several query shapes.
- OpSec: **active** — every generated search runs in your Facebook session and every profile you open is a logged visit. Use a puppet account and never your real identity.

## Overlaps ("do both")
- Pairs with `[[graph-tips]]`-style Facebook ID/search helpers and any Facebook numeric-ID lookup — one builds queries, the other resolves profiles to stable IDs.
- Feed confirmed profiles into reverse-image/face tools to corroborate identity.

## Trust & verifiability
`trust: community` — open-source and widely used in OSINT training, but it is a query-builder, not an authority: verify every hit on Facebook directly, since the results are Facebook's, not SowSearch's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-search-2 |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org, address → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
