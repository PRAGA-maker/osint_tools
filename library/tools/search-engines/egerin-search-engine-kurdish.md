---
id: egerin-search-engine-kurdish
name: Egerin Search Engine (Kurdish)
description: Use when you have a `name`, `username`, or keyword in a Kurdish context and want Kurdish-language web/news results — returns regional pages toward `social-profile`, `domain`, `associate`.
url: http://egerin.com
category: search-engines
path:
- search-engines
bestFor: Searching Kurdish-language web, news, and media that mainstream engines index poorly, for subjects in the Kurdish diaspora/region.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free Kurdish search engine and portal; no account required to search.
opsec: passive
opsecNote: Searching is passive. Results link out to Kurdish news and media sites that may log visits; use a sock-puppet/logged-out session when clicking through, especially given the politically sensitive nature of much Kurdish-region content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Egerin (launched 2013–2014) is a recognized first Kurdish-language search engine built on Solr/Scrapy; it is a genuine regional engine, though smaller and less complete than global engines.
missingPersonsRelevance: low
coverage:
- iq
- tr
- ir
- sy
auth: none
api: false
localInstall: false
registration: false
aliases:
- egerin.com
- Kurdish Google
tags:
- toddington
- curated-directory
- search-engines
- kurdish
- regional-search
source: toddington-resources
lastVerified: '2026-07-20'
---

# Egerin Search Engine (Kurdish)

> The first Kurdish-language search engine — reaches Kurdish web, news, and media (Sorani/Kurmanji) that global engines index thinly.

## When to use
You have a subject with a Kurdish-region or diaspora nexus (Iraq, Turkey, Iran, Syria) and want Kurdish-language coverage — news, forums, media — that Google surfaces poorly because it doesn't fully handle Kurdish alphabets and outlets. Egerin recognizes Kurdish scripts and dialects (Sorani, Kurmanji) and indexes Kurdish sites, plus offers a Kurdish news feed and dictionary/translator. It's a general regional engine, not a person finder, so relevance is low but genuinely additive for Kurdish-context subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://egerin.com (the site may block some automated fetchers with a 403 but is reachable in a real browser; there are also Android/iOS apps).
2. Search the subject `name`/`username`, ideally transliterated into Kurdish script for best recall.
3. Use its dictionary/translator to convert Turkish/English terms into Kurdish dialects to broaden queries.
4. Read the Kurdish news feed for outlet coverage; follow links from a clean session.
5. Pivot: Kurdish-script spellings and any `domain`/`social-profile` hits feed further regional and social searches.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword (best in Kurdish script)
- **Out:** Kurdish-language web/news results → `social-profile`, `domain`, `associate` mentions
- **Empty/negative result looks like:** few or no results — the index is regional and modest, so absence is weak evidence; cross-check global engines and correct the transliteration.

## Gotchas & OpSec
- Kurdish-language and regional — you must transliterate names into Kurdish script (and try both Sorani and Kurmanji) to get recall.
- Smaller, less complete index than global engines; treat as a supplement.
- OpSec: politically sensitive content is common; search passively and click through only from a sock-puppet session.

## Overlaps ("do both")
- Pairs with global engines and regional Turkish/Arabic/Persian search — Egerin catches Kurdish-script pages the others miss; run the same subject across all for coverage.

## Trust & verifiability
`trust: community` — a genuine, recognized Kurdish engine, but modest in scale; verify each result at its source outlet before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | egerin-search-engine-kurdish |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
