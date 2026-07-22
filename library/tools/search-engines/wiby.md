---
id: wiby
name: Wiby
description: Use when you have a `name` or `username` and want to surface mentions on old, small, independent "classic web" pages that mainstream engines bury — returns social-profile leads.
url: https://wiby.me
category: search-engines
path:
- search-engines
bestFor: Finding a person or handle named on personal homepages, hobby sites, and old-web pages that Google no longer ranks.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, donation-supported search engine; no account or payment needed.
opsec: passive
opsecNote: Queries hit Wiby's own index, not the target and not Google, so this is passive. No login or cookies required. Normal search-engine query logging applies; use a VPN/sock-puppet if you want to avoid tying the search to your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, community-curated project indexing hand-submitted classic-web pages; small and human-maintained rather than an authoritative crawler.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wiby.me
- Wiby classic web search
tags:
- toddington
- specialty-search
- search-engines
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Wiby

> A search engine for the "classic web" — old, small, personal and hobbyist pages — useful for surfacing mentions that modern engines have buried under commercial content.

## When to use
You have a `name`, `username`, or an old-web trail (a hobby, a defunct forum handle, a personal-homepage-era subject) and mainstream search returns only recent commercial noise. Wiby indexes hand-built personal pages, club sites, and niche resources where an older person or a long-dormant identity might still be named — a genealogy page, a model-railway club roster, a 2000s university lab page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wiby.me.
2. Type the `name`, `username`, or subject keyword and search. Combine a name with a hobby/place term to cut noise (e.g. `"John Fettler" amateur radio`).
3. Read the results — each is a link to an indexed classic-web page. Open promising pages and look for the subject named in rosters, guestbooks, staff lists, or bylines.
4. Use the "surprise me" random button only for exploration, not targeted search.
5. Pivot: a page that names the subject can yield an old `email`, `username`, affiliation, or `associate` links to run through people-search and username tools.

## Inputs → Outputs
- **In:** `name` or `username` (optionally plus a hobby/place keyword)
- **Out:** `social-profile` / mention leads on classic-web pages
- **Empty/negative result looks like:** few or zero results — Wiby's index is small and curated, so an empty result means "not in this niche index," not "this person has no web footprint." Fall back to mainstream and specialty engines.

## Gotchas & OpSec
- The index is deliberately small and skewed toward retro/indie content; treat it as a supplement, not a primary crawler.
- No login or CAPTCHA in normal use; fully passive against the target.
- Results skew older, which is exactly the point for a long-cold trail but useless for someone with only a recent footprint.

## Overlaps ("do both")
- Pairs with a mainstream engine and targeted dork-style queries — Wiby finds the small old pages those miss, while they cover the current, indexed web.

## Trust & verifiability
`trust: community` — Wiby is an independent, donation-funded project built on hand-submitted pages, so coverage is idiosyncratic but every result is a real link you can open and verify yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiby |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
