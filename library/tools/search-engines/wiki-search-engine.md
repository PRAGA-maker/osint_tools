---
id: wiki-search-engine
name: Wiki.com
description: Use when you have a `name`, `username`, or topic keyword and want to search across many wiki-format sites at once — returns `social-profile` / biographical mentions buried in community wikis.
url: http://www.wiki.com
category: search-engines
path:
- search-engines
bestFor: Sweeping wiki-format sites (fandom/community/reference wikis) in one query for people, handles, or niche topics that never surface on mainstream search.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: Free to search; the site also offers paid/free wiki hosting. Some navigation links funnel to a generic contact/host page, so search depth is limited.
opsec: passive
opsecNote: A search front-end — your query goes to Wiki.com and whatever wiki backends it queries. Nothing is sent to the subject. Use a clean browser if you want the lookup anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running but thinly maintained wiki search/host portal; index freshness and coverage are uneven, and some links redirect to a hosting-signup page.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- searchall-net
aliases:
- Wiki Search Engine
tags:
- toddington
- search-engines
- wiki-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Wiki.com

> A keyword search across wiki-format sites — the place to look when your subject only shows up in a fandom, gaming, hobby, or community wiki rather than the open web.

## When to use
You have a `name`, `username`, or a distinctive niche term and mainstream engines are dry. People active in fandoms, games, esports, hobby communities, or small-group projects often have biographical detail, handles, and cross-links recorded in wikis that Google ranks poorly. Wiki.com lets you probe that layer in one pass.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.wiki.com.
2. Enter your query — a `name` in quotes, a `username`, or the niche topic your subject is tied to.
3. Scan the returned wiki pages for biographical detail, linked handles, edit history, or user pages.
4. On any hit, open the source wiki directly and check the page's "user" / contributor namespace — a wiki username is a strong pivot.
5. Pivot: wiki `username` → username-search tools; a linked external profile → the relevant social/email tool.

## Inputs → Outputs
- **In:** `name`, `username`, or topic keyword
- **Out:** `social-profile` links and biographical mentions inside community/reference wikis
- **Empty/negative result looks like:** no wiki pages returned, or the search bounces you to the wiki-hosting signup page — treat as "no wiki footprint found here," and try a direct search on the specific fandom/wiki platform instead.

## Gotchas & OpSec
- The portal is thinly maintained: some links redirect to a hosting/contact page rather than results, so don't rely on it as your only wiki search.
- Wiki content is user-editable and often unverified — corroborate any claim before treating it as fact.
- Passive; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[searchall-net]]` — the metasearch launcher can push the same query at Fandom/Wikipedia and general engines, catching wikis Wiki.com's index misses.

## Trust & verifiability
`trust: community` — an aging, uneven wiki portal indexing user-generated content. Useful as a lead source only; always verify on the underlying wiki and a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiki-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
