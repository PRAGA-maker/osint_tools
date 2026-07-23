---
id: alltheinternet
name: AllTheInternet
description: Use when you have a `name`/`username`/keyword and want one query fanned across many engines and services — returns a launchpad of results from Google, Bing, socials and more.
url: http://www.alltheinternet.com
category: search-engines
path:
- search-engines
bestFor: A single search box that pushes your query to many search engines and specialised services at once.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free metasearch launcher, no account. Ad-supported.
opsec: passive
opsecNote: AllTheInternet hands your query off to the individual engines (opening tabs / relaying), so those engines still see a search and may see your IP when results load. Nothing touches your subject directly. Use a sock-puppet browser/VPN if you don't want the query tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple metasearch launchpad, not a ranking engine — it just routes your query to other services. Useful for breadth; the quality of any result is the destination engine's, not AllTheInternet's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- alltheinternet-com
aliases:
- All the Internet
- alltheinternet.com
tags:
- meta-search
- search-launcher
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# AllTheInternet

> A metasearch launchpad — type once and it fans your query out across many search engines and specialised services (web, images, video, social, shopping), so you don't miss what a single engine buries.

## When to use
Early in a search on a `name`, `username`, or keyword when you want breadth fast — to see how different engines and verticals surface the same subject, and to catch results Google alone ranks out of view. It's a starting-point sweep, not a deep tool; use it to spot promising leads, then go direct to the strongest source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.alltheinternet.com .
2. Enter the `name`/`username`/keyword and pick a category (web, images, video, social, etc.).
3. It routes the query to the chosen engines/services — review each, noting where the subject appears and where they don't.
4. Because it merely relays, treat it as a launcher: when one engine looks fruitful, continue there directly with proper operators.
5. Pivot: a `social-profile` or `domain` that surfaces feeds dedicated username/social/domain OSINT.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** results routed across multiple engines — surfaced `social-profile`s, `domain`s, media, listings
- **Empty/negative result looks like:** thin or duplicated results across engines — the term is genuinely sparse online, or you need better operators/variants. Not evidence of a definitive "nothing".

## Gotchas & OpSec
- It's a *launcher*, not a search engine — it adds no ranking/dedup intelligence; you still evaluate each destination's results.
- Ad-supported; ignore sponsored placements.
- OpSec: **passive** toward your subject, but the destination engines see your searches — use a clean profile/VPN for sensitive work.

## Overlaps ("do both")
- Complements deliberate single-engine searching (Google/Bing/Yandex with operators) and people-search aggregators — use AllTheInternet for the quick wide net, then the specialised tools for depth.

## Trust & verifiability
`trust: community` — a convenience metasearch launcher. It doesn't vouch for anything; judge each result at its source engine, and corroborate leads independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alltheinternet |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
