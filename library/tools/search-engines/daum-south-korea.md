---
id: daum-south-korea
name: Daum (South Korea)
description: Use when you have a name, username, or term tied to South Korea and want Korean-language web/news/cafe results a Western engine misses — returns social-profile and name leads from Korean sources.
url: https://www.daum.net/
category: search-engines
path:
- search-engines
bestFor: Searching Korean-language web, news, blogs, and Cafe communities for a South Korea-linked subject.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to search; a Kakao/Daum account is only needed to view certain Cafe communities, not for general search.
opsec: passive
opsecNote: General search is passive. Daum/Kakao logs queries and may serve differently by region — use a sock-puppet session; logging into a Kakao account to read a private Cafe is an active, attributable step.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Daum is a major, long-established South Korean web portal (now part of Kakao); an authoritative window into the Korean-language web.
missingPersonsRelevance: low
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- daum-search-engine-south-korea
aliases:
- Daum
- 다음
- Kakao Daum
tags:
- main-national-search-engines
- korea
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Daum (South Korea)

> A major South Korean web portal and search engine — reach Korean-language news, blogs, and Cafe communities that Google under-indexes.

## When to use
Your subject is South Korean or has a Korea nexus, and you need Korean-language coverage: local news, blog posts, and especially **Daum Cafe** community discussions that Western engines miss. Search a `name` (ideally in Hangul), a `username`, or a phrase to surface Korean-source mentions and profiles. It's a regional search front door, best paired with Korean-language input.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.daum.net/ and search the `name`/`username`/term — use Hangul for far better recall.
2. Work the verticals: **뉴스** (news), **블로그** (blog), **카페** (Cafe communities), **이미지** (images).
3. For Cafe threads, note that some communities require a Kakao login to read fully (`account-login`).
4. Translate results (e.g. [[systran-translate]] or Papago) and extract `name`s, `social-profile` links, and dates.
5. Pivot: a Korean `social-profile`/handle → KakaoTalk/Naver cross-checks; a real name → Korean registries/news archives.

## Inputs → Outputs
- **In:** a `name` (Hangul preferred), `username`, or phrase tied to South Korea.
- **Out:** Korean-language web/news/blog/Cafe results — `name`s, `social-profile` links, and community mentions.
- **Empty/negative result looks like:** few/no hits — often because you searched a romanized name; retry in Hangul, or the subject simply has a thin Korean-web footprint.

## Gotchas & OpSec
- Recall depends heavily on Hangul input; romanized queries badly under-return.
- Some Cafe content is gated behind a Kakao account — logging in is attributable, so use a persona if you must.
- Results and ranking can differ by region/IP; a Korea-based egress gives the most representative view.

## Overlaps ("do both")
- Pairs with Naver (the other dominant Korean portal) and [[systran-translate]]: run the query on both engines for coverage, and translate to work the results.

## Trust & verifiability
`trust: trusted` — Daum is a first-party major Korean portal (Kakao); results are authentic search output, though individual pages are unverified third-party content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | daum-south-korea |
