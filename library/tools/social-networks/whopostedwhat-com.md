---
id: whopostedwhat-com
name: whopostedwhat.com
description: Use when you have a `name`/keyword and a date and want Facebook posts from that exact day/range — returns social-profile and post leads around a key date.
url: https://whopostedwhat.com/
category: social-networks
path:
- social-networks
bestFor: Searching Facebook for posts containing a keyword/name on a specific day, month, year, or date range — activity that native Facebook search won't surface by date.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to use (donation-supported). Some features (e.g. resolving a profile to its numeric ID, or running certain searches) work best when you are logged into your own Facebook account in the same browser.
opsec: active
opsecNote: The site builds Facebook search URLs that you then open inside YOUR Facebook session — Facebook logs the viewing account and it can surface you to the target via "people you may know". Always run the resulting searches from a sock-puppet Facebook account, never an attributable one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Widely used, well-regarded journalist/OSINT tool (conceived by Henk van Ess); it constructs Facebook's own search queries, so results come from Facebook itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- facebook-search-tool-2
- social-searcher
aliases:
- who posted what
- whopostedwhat
tags:
- facebook
- search
source: gh-topic-osint-resources
lastVerified: '2026-07-11'
enrichment: full
---

# whopostedwhat.com

> A Facebook keyword-by-date search built for journalists and researchers — find posts mentioning a name/term on an exact day or range, which native Facebook search can't do.

## When to use
You have a `name`, phrase, or keyword and a **date that matters** — the day someone went missing, an event, a claimed alibi — and you want Facebook posts from that specific day/month/year/range. Native Facebook search has no reliable date filter; whopostedwhat reconstructs the query so you can pin activity to a time window. Especially valuable in missing-persons work for locating public Facebook activity around a disappearance date.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whopostedwhat.com/.
2. Enter your keyword/name and the target date or date range; optionally scope to a profile, page, place, or Instagram location (using numeric IDs where required — the site also helps resolve a profile URL to its numeric ID).
3. Launch the search; it opens Facebook's results for that keyword+date. Be signed into a **sock-puppet** Facebook account so results render.
4. Read the matching posts (with timestamps) and the profiles behind them.
5. Pivot: profiles feed [[facebook-search-tool-2]] for graph queries; broaden across networks with [[social-searcher]].

## Inputs → Outputs
- **In:** `name`/keyword + a date or range (optionally a profile/place ID)
- **Out:** Facebook posts matching the term on that date, and the `social-profile`s that posted them
- **Empty/negative result looks like:** no posts returned — the content may be non-public, deleted, or Facebook's search may be throttling the query; a blank is not proof nothing was posted.

## Gotchas & OpSec
- Facebook periodically breaks these search URLs; if a query returns nothing, the syntax may need adjusting rather than the content being absent.
- Human-in-the-loop: results depend on being logged into Facebook — use a burner account, never your own.
- OpSec: **active** once you open the search inside Facebook; Facebook logs the viewing account.

## Overlaps ("do both")
- Pairs with [[facebook-search-tool-2]] (graph/connection queries by numeric ID) and [[social-searcher]] (cross-network breadth) — whopostedwhat owns the date dimension the others lack.

## Trust & verifiability
`trust: trusted` — a well-known, respected OSINT/journalism tool that builds Facebook's own queries. Results are served by Facebook, so they're verifiable on-platform; the tool adds no data of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whopostedwhat-com |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
