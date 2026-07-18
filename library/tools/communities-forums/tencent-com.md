---
id: tencent-com
name: QQ.com (Tencent)
description: Use when you have a Chinese-language `name`/keyword and want mainland coverage — Tencent's QQ.com news portal and gateway to the QQ/Qzone ecosystem for searching Chinese media and profiles.
url: https://www.qq.com
category: communities-forums
path:
- communities-forums
bestFor: Searching Chinese-language news/media coverage and entering the QQ/Qzone social ecosystem.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read news; QQ/Qzone social features require a Tencent/QQ account.
opsec: passive
opsecNote: Reading QQ.com news is passive. Anything deeper (QQ/Qzone profiles) needs a QQ account and a Chinese phone number — use a sock-puppet identity, and be aware Tencent platforms are heavily monitored and geofenced.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Tencent's flagship portal — a major, live Chinese media property; state-influenced editorial context applies, so treat coverage accordingly.
missingPersonsRelevance: medium
coverage:
- cn
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- qzone
- qzone-china
- tencent-maps
- tencent-qq-mail
aliases:
- QQ.com
- Tencent
- qq.com
tags:
- toddington
- curated-directory
- news-journalism
- china
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# QQ.com (Tencent)

> Tencent's flagship Chinese portal — a huge news/media site and the front door to the QQ and Qzone social ecosystem, useful for mainland-Chinese coverage and profile pivots.

## When to use
Your subject has a China connection and you need Chinese-language sources: news coverage, regional life-service info, or an entry point into Tencent's QQ/Qzone social platforms where many mainland users have profiles. QQ.com surfaces Chinese media that Western search engines under-index, and its ecosystem links (`[[qzone]]`, QQ) are where a Chinese `name`/handle may resolve to a `social-profile`. It's a broad portal/media source rather than a targeted search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.qq.com and use its search / news sections for the subject's Chinese-language `name` or keywords (a translation tool helps).
2. Read coverage for names, affiliations, locations and dates; note any linked QQ/Qzone handles.
3. To pivot into social profiles, move to `[[qzone]]`/QQ (which need a QQ account) rather than the portal itself.
4. Pivot: Chinese-language mentions feed name/associate research; a QQ number/handle feeds messaging and social-profile tools in the Tencent ecosystem.

## Inputs → Outputs
- **In:** `name`/keyword (ideally in Chinese)
- **Out:** Chinese-language news/media coverage and links toward `social-profile`s in the QQ/Qzone ecosystem
- **Empty/negative result looks like:** no relevant coverage — the subject may have no Chinese-media footprint, or your query needs the correct Chinese characters; romanized names often miss, so try the native script.

## Gotchas & OpSec
- Human-in-the-loop: none to read news; QQ/Qzone social access needs a QQ account (Chinese phone number) — a real hurdle.
- Language: effective use needs Chinese-language queries and translation; romanized searches under-return.
- Context: Tencent is a state-influenced platform in a censored information space — weigh editorial slant and expect some content to be geofenced or removed.

## Overlaps ("do both")
- Pairs with `[[qzone]]`, `[[tencent-qq-mail]]` and Weibo/Baidu-oriented tools — QQ.com is the news gateway, while the social/mail tools resolve handles to profiles; a thorough China workup uses several.

## Trust & verifiability
`trust: community` — a major but state-influenced media portal; corroborate any claim across additional Chinese and non-Chinese sources rather than relying on a single QQ.com article.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tencent-com |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
