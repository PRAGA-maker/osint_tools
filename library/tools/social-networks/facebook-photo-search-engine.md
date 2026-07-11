---
id: facebook-photo-search-engine
name: Facebook Photo Search Engine (Google CSE)
description: Use when you have a `name` or keyword and want to find Facebook-hosted photos/pages indexed by Google — returns Facebook links (profiles, photos) matching your terms.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:jyvyp2ppxma
category: social-networks
path:
- social-networks
bestFor: Keyword/name search scoped to publicly indexed Facebook photos and pages via a Google Custom Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free to use — it is a hosted Google Custom Search Engine; no account required.
opsec: passive
opsecNote: Queries go to Google, not to Facebook, so the target is not touched or notified. Standard search-engine hygiene (sock-puppet browser) is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Google Custom Search Engine with a fixed configuration; coverage is only what Google has indexed of Facebook and degrades as the CSE config ages and Facebook restricts indexing.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Facebook photo CSE
tags:
- facebook
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Facebook Photo Search Engine (Google CSE)

> A pre-built Google Custom Search Engine scoped to Facebook photos/pages — a keyword-to-Facebook shortcut that leans on Google's index rather than Facebook's own (crippled) search.

## When to use
You have a `name`, `username`, or descriptive keyword and want to find publicly indexed Facebook photos or pages associated with it — a way around Facebook's own limited search. Useful for surfacing a subject's public Facebook presence or images when you only have a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL in a sock-puppet browser.
2. Enter the subject's `name`/`username` or keywords (add a location or distinguishing term to cut noise).
3. Read the results: Google-indexed Facebook links — profiles, photo pages, public posts.
4. Because it only sees what Google has indexed of Facebook (a shrinking set), treat hits as a starting point and open them directly.
5. Pivot: a found profile feeds `[[facebook-friend-list-scraper]]` and photo/face search; an image feeds reverse-image tools.

## Inputs → Outputs
- **In:** `name`, `username`, or keywords
- **Out:** Facebook `social-profile`/photo links, `image` results
- **Empty/negative result looks like:** few/no results — Facebook increasingly blocks indexing, so a miss often reflects the index, not the person's absence from Facebook. Confirm with on-platform search from a sock puppet.

## Gotchas & OpSec
- Index-limited: only publicly Google-indexed Facebook content appears; much of Facebook is invisible to it, and coverage decays over time (`status: degraded`).
- Stale CSE: the search-engine configuration is fixed by whoever built it and may not reflect current Facebook URL patterns.
- OpSec: passive — queries hit Google, not Facebook; nothing reaches the target.

## Overlaps ("do both")
- Pairs with direct Facebook graph/photo search and with general `site:facebook.com` Google dorks — the CSE is one pre-tuned lens; run raw dorks too, since each surfaces different indexed pages.

## Trust & verifiability
`trust: unverified` — a third-party CSE whose coverage depends entirely on Google's Facebook index and the config's freshness; verify every hit on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-photo-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
