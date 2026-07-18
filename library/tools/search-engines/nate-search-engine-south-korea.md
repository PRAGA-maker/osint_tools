---
id: nate-search-engine-south-korea
name: Nate Search Engine (South Korea)
description: Use when you have a `name`, `username`, or `phone` on a South Korean subject and want Korean-language web/news results Google misses — returns `social-profile`, news mentions.
url: https://www.nate.com/
category: search-engines
path:
- search-engines
bestFor: Regional Korean-language search (web, news, community) for subjects with a Korea footprint.
selectorsIn:
- name
- username
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free portal search; no account needed to run queries.
opsec: passive
opsecNote: A standard portal search; the subject isn't contacted. Nate logs queries server-side like any search engine, so use a sock-puppet/clean session and avoid logging into Nate services while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Nate is a major, established South Korean web portal (operated by SK Communications); the portal is legitimate though its integrated search partly draws on third-party indexes.
missingPersonsRelevance: medium
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- yam-search-engine-taiwan
aliases:
- Nate
- nate.com
- 네이트
tags:
- search-engines
- korea
- regional
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Nate Search Engine (South Korea)

> One of Korea's mega-portals — reach for its integrated search when a subject's life is in Korean-language space that Western engines index poorly.

## When to use
Your subject has a South Korea connection (Korean `name`, a handle used on Korean platforms, a KR `phone`, or Korean-language content) and Google/Bing return thin results. Nate's 통합검색 (integrated search) surfaces Korean web pages, news, and community (Pann) discussion, giving regional coverage — including Korean news mentions and forum posts — that non-Korean engines routinely miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nate.com/.
2. Enter the query in the integrated search box — try the name in Hangul (한글) as well as romanized, since Korean sources index the Hangul form.
3. Switch across the result tabs: web (웹), news (뉴스), and community/Pann for discussion mentions.
4. Read results as leads to a `social-profile`, a news article, or a forum thread naming the subject.
5. Pivot: run the same query on other Korean portals (Naver, Daum) to triangulate; a Korean news mention can anchor a timeline/location.

## Inputs → Outputs
- **In:** `name` (prefer Hangul), `username`, or `phone`
- **Out:** Korean-language web/news results, community mentions, links to a `social-profile`
- **Empty/negative result looks like:** no Korean-language hits — the subject may have little Korean online presence, or you need the Hangul spelling of the name rather than a romanization.

## Gotchas & OpSec
- Human-in-the-loop: none; open search, though the interface is entirely in Korean — use browser translation to navigate.
- Romanized names often miss; get the Hangul form for real coverage.
- Nate is a full portal (mail, shopping, games) — don't sign into any of it from your investigative session.
- OpSec: passive; standard search-engine query logging applies.

## Overlaps ("do both")
- Pairs with [[yam-search-engine-taiwan]] — the same "use the regional portal, not Google" tactic for a different market; pick the one matching your subject's region, or run both for cross-border subjects.

## Trust & verifiability
`trust: community` — Nate is a legitimate, long-established Korean portal, but treat it as an index/starting point: confirm any claim from the underlying source page, not the search snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nate-search-engine-south-korea |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
