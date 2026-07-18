---
id: yam-search-engine-taiwan
name: Yam Search Engine (Taiwan)
description: Use when you have a `name` or `username` on a Taiwan-linked subject and want Traditional-Chinese web/news/blog results — returns `social-profile`, news and blog mentions.
url: https://www.yam.com/
category: search-engines
path:
- search-engines
bestFor: Regional Traditional-Chinese (Taiwan) search across news, blogs, and web content.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free portal/search; no account needed.
opsec: passive
opsecNote: Ordinary portal search; the subject isn't contacted. Query logging applies as with any search engine — use a clean/sock-puppet session and don't sign into Yam services while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Yam (蕃薯藤) is a long-established Taiwanese media/content portal (operated by Tian Kong Media); legitimate, though now more media hub than pure search and its search leans on partner indexes.
missingPersonsRelevance: medium
coverage:
- tw
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- nate-search-engine-south-korea
aliases:
- Yam
- yam.com
- 蕃薯藤
tags:
- search-engines
- taiwan
- regional
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Yam Search Engine (Taiwan)

> Taiwan's veteran 蕃薯藤 portal — use it for Traditional-Chinese news, blog, and web content that Western engines under-index.

## When to use
Your subject has a Taiwan connection (a Traditional-Chinese `name`, a handle on Taiwanese platforms, or Taiwan-language content) and mainstream engines return little. Yam aggregates Taiwanese news (蕃新聞), lifestyle/blog content, and web search geared to a Taiwanese audience, giving regional mentions — news write-ups, blog posts, community content — that Google may bury or miss for local-language subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.yam.com/ and use the search (搜尋) function.
2. Enter the query in Traditional Chinese where possible, since local sources index that form.
3. Scan across the portal's news and content sections as well as raw search results.
4. Read hits as leads to a `social-profile`, a Taiwanese news article, or a blog naming the subject.
5. Pivot: cross-check on other Taiwan/Chinese-language engines; a dated local news mention can anchor location/timeline.

## Inputs → Outputs
- **In:** `name` (prefer Traditional Chinese) or `username`
- **Out:** Taiwan-focused web/news/blog results and links to a `social-profile`
- **Empty/negative result looks like:** no Traditional-Chinese hits — the subject may have little Taiwan online presence, or you need the Chinese-character form of the name rather than a romanization.

## Gotchas & OpSec
- Human-in-the-loop: none; open search, but the interface is in Traditional Chinese — lean on browser translation.
- Yam has shifted toward being a media hub, so its search may route through partner indexes and skew toward its own news/content — treat it as one regional lens, not exhaustive.
- Romanized names underperform; get the Chinese-character spelling for real coverage.
- OpSec: passive; standard search-log exposure only.

## Overlaps ("do both")
- Pairs with [[nate-search-engine-south-korea]] — the same regional-portal tactic for a different market; choose by your subject's region, or run both for East-Asia-spanning subjects.

## Trust & verifiability
`trust: community` — a legitimate, long-running Taiwanese portal, but use it as a discovery index: verify any finding against the underlying source page rather than the result snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yam-search-engine-taiwan |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
