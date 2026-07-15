---
id: google-com-45
name: google.com (site:qzone.qq.com dork)
description: Use when you have a `name`/`username` for a Chinese subject and want their Qzone (Tencent QQ) profile or posts — returns social-profile links and name hints via a Google site: dork.
url: https://www.google.com/search?q=site%3Aqzone.qq.com&ie=utf-8&oe=utf-8&client=firefox-b-ab
category: social-networks
path:
- social-networks
bestFor: Surfacing public Qzone (QQ空间) pages for a Chinese subject via a Google site: operator.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Google search is free; no QQ/Qzone account to view whatever Google has indexed publicly.
opsec: passive
opsecNote: You query Google, not Qzone or the subject — passive, with no signal to Tencent. Opening an indexed Qzone page is an anonymous pageview; most Qzone content requires a QQ login to view fully, so clicking through may hit a wall rather than the profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's index over Qzone's own pages — both first-party. The dork technique is sound; however Google indexes Chinese platforms poorly, so recall is low, not a data-quality problem.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Qzone search
- site:qzone.qq.com
- QQ空间
tags:
- gsocialmedia
- General Social Media Sites
- google-dork
- qzone
- china
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com (site:qzone.qq.com dork)

> A Google `site:` operator aimed at Qzone (QQ空间) — Tencent's long-running social network — to surface a Chinese subject's profile or posts that Chinese-platform search wouldn't hand you.

## When to use
You have a `username` (often a QQ number) or `name` for someone with a Chinese footprint and want their Qzone presence: profile page, public posts, photos, or self-disclosed details. Qzone is one of China's largest social platforms, so it can carry a subject's history when Western networks are empty — though, be warned, indexing and access are both limited.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run `site:qzone.qq.com "handle or QQ number"` or `site:qzone.qq.com "Name"`.
2. Try the QQ-number pattern directly — Qzone URLs are keyed on QQ IDs (`user.qzone.qq.com/<QQ number>`), so a known QQ number is your strongest selector.
3. Open any indexed page; expect many to prompt a QQ login for full content.
4. Pivot: a QQ number cross-references QQ/WeChat and Chinese people-search; a readable profile yields name, city and photos.

## Inputs → Outputs
- **In:** `username` (QQ number/handle) / `name`
- **Out:** `social-profile` (Qzone URL), `name`/identity hints
- **Empty/negative result looks like:** few or no Google hits — the common case. Google indexes Chinese platforms sparsely and much of Qzone is login-gated, so absence here says little; use a native Chinese search engine (Baidu/Sogou) and a direct QQ-number URL before concluding.

## Gotchas & OpSec
- **Low recall:** Google barely indexes Qzone; a blank result is usually a coverage limit, not proof of absence — this is why `status` is marked degraded.
- **Login walls:** most Qzone content needs a QQ account to view; have a sock-puppet QQ ready.
- Quote exact terms and prefer the QQ-number URL pattern to cut noise.
- OpSec: the Google search is passive; viewing behind a QQ login is a separate, account-attributable step.

## Overlaps ("do both")
- Pairs with Baidu/Sogou `site:` searches and QQ-number lookup tools — native Chinese engines index Qzone far better than Google, and a QQ number often resolves the profile directly.

## Trust & verifiability
`trust: trusted` — the method (Google over Qzone's own pages) is reliable where it returns anything; the limitation is recall, not accuracy. Confirm any hit on the live Qzone page (via a sock-puppet QQ login).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-45 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
