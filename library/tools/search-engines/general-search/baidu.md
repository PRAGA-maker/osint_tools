---
id: baidu
name: Baidu
description: Use when your subject or clue is Chinese-language or China-based and you want web/image/news coverage Google misses — returns pages, images, and social-profile leads from the Chinese web.
url: https://www.baidu.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: Searching the Chinese-language web (news, forums, Tieba, Baike) for people, companies, and images that Western engines under-index.
input: Keywords, operators (inurl:, intitle:, site:, filetype:), language and time filters
output: Ranked web pages, images, news, knowledge graph, trending queries
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- domain
status: live
pricing: free
costNote: Free web search; no account needed. An API and paid ad products exist but core search is free.
opsec: passive
opsecNote: Passive querying, but Baidu is a Chinese company subject to PRC data/monitoring law; assume queries and IPs are logged and may be visible to authorities. Do not run China-sensitive searches from an attributable IP — use a sock-puppet browser and consider a non-attributable exit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Baidu, China's dominant search engine; results are authentic index data (with PRC content filtering/censorship applied).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- baidu-china
- baidu-com
- baidu-image-search
- baidu-image-search-2
- baidu-images
- baidu-maps
- baidu-translate
- baiduknows-search-engine-china
- baike-baidu-chinese-language
aliases:
- 百度
- baidu.com
tags:
- search-engines
- china
- chinese-language
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Baidu

> China's dominant search engine — the primary way to reach Chinese-language web pages, images, Tieba forums, and Baike entries that Google either under-indexes or cannot see.

## When to use
Your subject is Chinese, based in China, or leaves Chinese-language traces (a Pinyin/Hanzi `name`, a reused `username`, a China-hosted site). Baidu surfaces the Chinese web — news, Tieba (贴吧) forums, Zhihu, Baike, and images — where a Western engine returns little. Use it to find a `social-profile`, corroborating `image`s, or the `domain` of a company or personal site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.baidu.com/ (ideally with a Chinese-capable browser and a translation tool alongside).
2. Search the name in Hanzi if you have it — Pinyin works but Hanzi is far more precise. Add a city, employer, or school to disambiguate common names.
3. Use operators much like Google: `site:`, `intitle:`, `inurl:`, `filetype:`; switch tabs for 图片 (images), 资讯/新闻 (news), and 贴吧 (forums).
4. Read/translate hits; note reused handles and linked profiles. Pivot: run an image through `[[baidu-image-search]]` (Baidu's reverse-image works better than Google's on Chinese content), map a place with `[[baidu-maps]]`, or translate with `[[baidu-translate]]`.

## Inputs → Outputs
- **In:** `name` (Hanzi/Pinyin) or `username`
- **Out:** `social-profile` (Tieba/Zhihu/Weibo mentions), `image`, `domain` (personal/company sites)
- **Empty/negative result looks like:** only SEO-spam and shopping results, or nothing beyond generic Baike stubs — the person may have no Chinese-web footprint, or the term is censored/filtered.

## Gotchas & OpSec
- Human-in-the-loop: none, though heavy querying can trigger a slider CAPTCHA.
- OpSec: **passive but sensitive** — Baidu is PRC-jurisdiction; assume logging and possible state visibility. Never search politically sensitive China topics from an attributable IP; use a sock puppet.
- Censorship/filtering shapes results: absence of a result is not proof of absence. Cross-check with Bing (which China-indexes) and Weibo search.

## Overlaps ("do both")
- Pairs with its own suite — `[[baidu-image-search]]`, `[[baidu-maps]]`, `[[baike-baidu-chinese-language]]`, `[[baidu-translate]]` — and with Weibo/Zhihu people search; Baidu finds the mention, the sibling tools enrich the image, place, and language around it.

## Trust & verifiability
`trust: trusted` — it is the genuine Baidu index (authoritative for the Chinese web), but results are subject to PRC censorship and SEO manipulation, so verify individual claims at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, image, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
