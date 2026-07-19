---
id: kirbstr-s-mastodon-search
name: Kirbstr's Mastodon search
description: Use when you have a `name`, `username` or keyword and want to search across popular Mastodon instances at once — returns matching posts and `social-profile`s.
url: https://cse.google.com/cse?cx=e57e14c971ef34e61
category: messaging
path:
- messaging
bestFor: Full-text searching many large, open Mastodon instances in a single query via a purpose-built Google Programmable Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom/Programmable Search Engine; no account. Coverage is limited to instances Google has indexed and the CSE owner included.
opsec: passive
opsecNote: This is a Google search restricted to Mastodon domains — the query goes to Google, not to any Mastodon user, so no one is alerted. Standard search-privacy hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained Google CSE; it depends on Google's index and the owner keeping the engine live, so coverage and availability are not guaranteed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Mastodon Google CSE
- Kirbstr Mastodon search
tags:
- Social Media
- Mastodon
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Kirbstr's Mastodon search

> A Google Programmable Search Engine scoped to the biggest open Mastodon instances — one box to full-text search fediverse posts that Mastodon's own search won't surface.

## When to use
Mastodon deliberately limits full-text search, so finding a `name`, `username`, phrase or link across the fediverse is hard. This CSE searches Google's index of major open instances at once, making it a fast way to find public posts mentioning your subject or a distinctive term, and the accounts behind them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search engine at https://cse.google.com/cse?cx=e57e14c971ef34e61.
2. Enter the `name`, handle, phrase, URL or keyword (quote exact phrases; try the `@user` form).
3. Review results — each links to a public Mastodon post/profile page on an indexed instance.
4. Pivot: open the account, note its `@user@instance` handle and bio links, and run the handle through fediverse discovery ([[fediverse-explorer]]) and username-search.

## Inputs → Outputs
- **In:** `name`, `username`, phrase, or keyword
- **Out:** matching Mastodon posts and `social-profile`s on indexed instances
- **Empty/negative result looks like:** no hits — the content is on an instance Google/this CSE doesn't index, is too new to be crawled, or the user restricts indexing. Absence is weak; also search individual instances and other fediverse tools.

## Gotchas & OpSec
- **Only indexed, open instances** are covered; many instances block search-engine crawling, so this misses them and lags on fresh posts.
- It's a hosted CSE that the owner could remove at any time — if it 404s, rebuild the same idea with a `site:` Google search over major instances.
- OpSec: passive; it's a Google query, not contact with the user.

## Overlaps ("do both")
- Pairs with [[fediverse-explorer]] (account discovery) — this finds the post/mention, the explorer helps enumerate and map the account.

## Trust & verifiability
`trust: community` — a community-built search shortcut over Google's index. Treat hits as leads; open the actual Mastodon post to confirm content and authorship rather than trusting the search snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kirbstr-s-mastodon-search |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
