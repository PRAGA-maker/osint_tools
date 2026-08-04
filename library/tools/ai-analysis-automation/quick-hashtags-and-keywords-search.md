---
id: quick-hashtags-and-keywords-search
name: Quick hashtags and keywords search
description: Use when you have a `username`, hashtag or keyword and want to sweep it across ~89 social platforms at once — returns direct search links per platform to find matching posts/profiles.
url: https://cipher387.github.io/hashtags_and_keywords_social_media_quick_search/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-box fan-out of a keyword/username/hashtag into search links across ~89 platforms.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source, hosted on GitHub Pages; no account. It only builds links — you run each search.
opsec: passive
opsecNote: The page is static client-side and doesn't phone home, but each link you click runs a search on that platform from your own browser, exposing your IP/session to it. Use a sock-puppet browser for platforms where that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known open-source launcher by OSINT tool-maker cipher387; it generates search URLs and holds no data of its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cipher387 hashtags search
- social media quick search
tags:
- My Projects
- social-search
- keyword-search
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Quick hashtags and keywords search

> A single-box search launcher: type a keyword, hashtag or username once and it hands you ready-made search links for ~89 social/video/blog/music platforms.

## When to use
You have a `username`, hashtag or keyword and want to check it everywhere fast — where a handle appears, who's using a tag, which platforms carry a term — without retyping the query into 89 sites. It's a time-saver for the broad "cast a wide net" phase of username/keyword investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page (URL above).
2. Type your query once into the search box.
3. Browse the categorized buttons (video/streaming, blogs, music, photos, business, regional platforms, etc.).
4. Click each relevant platform button — it opens that site's search results for your query in a new tab.
5. Triage the hits: note which platforms carry the handle/keyword. Pivot: confirmed `social-profile`s feed dedicated username/profile tools; a used handle on one platform is a lead to check others.

## Inputs → Outputs
- **In:** `username` / `name` / hashtag / keyword
- **Out:** per-platform search-result pages → candidate `social-profile`s and posts
- **Empty/negative result looks like:** a platform's search returns nothing for the term — meaning no indexed match there, not that the handle is unused elsewhere; check multiple platforms before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none in the tool; you open and read each search yourself.
- OpSec: **passive** — the launcher sends nothing, but each search runs from your browser against that platform; some may require login or throw CAPTCHAs. Use a puppet session where needed.
- It's a link builder: results depend entirely on each platform's own search, and its site list ages as platforms come and go.

## Overlaps ("do both")
- Complements dedicated cross-platform username checkers (Sherlock, WhatsMyName) — those probe profile existence programmatically; this hands you human-readable search pages, catching keyword/post matches those miss.

## Trust & verifiability
`trust: community` — an open-source launcher by a reputable OSINT author; it holds no data, so trust rests on each platform's search results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quick-hashtags-and-keywords-search |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
