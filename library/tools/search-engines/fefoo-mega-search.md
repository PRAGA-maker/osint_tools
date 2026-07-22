---
id: fefoo-mega-search
name: FeFoo Mega Search
description: Use when you have a `name` or `username` and want to fire the same query across many search engines and verticals fast — returns social-profile and web-mention leads.
url: http://fefoo.com
category: search-engines
path:
- search-engines
bestFor: Quickly re-running one query across Google/Bing/Yahoo and specialised verticals (images, video, news, maps, social) from a single launcher.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, no account. It is a query launcher/aggregator, not a paid data service.
opsec: passive
opsecNote: FeFoo hands your query off to third-party engines; the searches run against those engines, not the target, so it is passive against the subject. Your query and IP are exposed to whichever engine you launch into (and to FeFoo). Use a VPN/sock-puppet if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small independent meta-search launcher; it surfaces nothing itself and only redirects to mainstream engines, so result quality is entirely that of the underlying engines. Appears semi-maintained (site content dated ~2022).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fefoo.com
tags:
- toddington
- meta-mega-search-tools
- search-engines
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# FeFoo Mega Search

> A single-box launcher that fires one query across many search engines and verticals — a time-saver for sweeping a `name`/`username` across Google, Bing, images, video, news, and more without retyping.

## When to use
You have a `name` or reused `username` and want to sweep it across many engines and content types quickly, rather than opening each engine by hand. It does not aggregate results into one page; it is a fast way to launch the same query into web, image, video, news, map, and social verticals so you don't miss an engine that surfaces a mention others bury.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://fefoo.com.
2. Pick the category (Web, Images, Videos, News, Maps, and specialised tabs) you want to search.
3. Enter the `name` or `username` (quote exact phrases) and launch — FeFoo opens/queries the chosen engine.
4. Cycle through the categories/engines for the same query and collect any profiles, images, or mentions.
5. Pivot: a surfaced `social-profile`, image, or page feeds username-search, reverse-image, and people-search tools for the real enrichment.

## Inputs → Outputs
- **In:** `name` or `username` (plus chosen engine/vertical)
- **Out:** `social-profile` and web-mention leads (whatever the underlying engine returns)
- **Empty/negative result looks like:** the underlying engine returns nothing — that is an engine result, not a FeFoo result; try another vertical or a dedicated engine.

## Gotchas & OpSec
- It is only a launcher — all data quality, ranking, and coverage come from the third-party engines it hands off to.
- Semi-maintained: some verticals/engines may be stale or dead; verify a given tab still works before relying on it.
- Passive against the subject, but your query is exposed to FeFoo and the target engine.

## Overlaps ("do both")
- Pairs with a purpose-built username tool and reverse-image search — FeFoo casts the wide first net across engines, the dedicated tools do the deep pivot on what it surfaces.

## Trust & verifiability
`trust: unverified` — FeFoo produces no data of its own and is a lightly-maintained independent launcher; trust the underlying engine's results, verify each surfaced item at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fefoo-mega-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
