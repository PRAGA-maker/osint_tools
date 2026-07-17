---
id: justlanded-classified-ads-worldwide
name: Just Landed Classifieds (Worldwide)
description: Use when your subject is an expat/mover and you have a `name`/`username` — Just Landed's per-country classifieds, housing, jobs and community can surface ads, location and contact details.
url: https://classifieds.justlanded.com/en
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding an expatriate subject's small ads, housing/job posts or community presence in a specific country.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free to browse classifieds, housing and jobs. Posting/replying and some community features need a (free) account.
opsec: passive
opsecNote: Browsing ads and listings is passive and anonymous. Replying to an ad or using the community requires an account and may reveal you to the poster — use a sock-puppet account if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Just Landed is a real, long-running (since 2003) expat portal, but individual ads/profiles are user-posted and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- JustLanded
- classifieds.justlanded.com
tags:
- classifieds
- expat
- marketplace
- toddington
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Just Landed Classifieds (Worldwide)

> The classifieds/community side of Just Landed, the expat portal — small ads, housing, jobs and forums organised by country, useful when a subject has moved or lives abroad.

## When to use
Your subject is an expatriate, recent mover, or lives outside their home country, and you have a `name` or reused `username`. Just Landed hosts per-country classifieds (items for sale, language exchange, services), a housing portal, a jobs board, a business directory and an expat community — all rich with location and contact detail. Someone relocating often leaves a trail here: a flat-share ad giving a city/neighbourhood, a "for sale" post before/after a move, a job listing, or a community profile connecting them to other expats (`associate`s). It's a niche source, but strong precisely for the mobile/abroad subjects that mainstream local tools miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://classifieds.justlanded.com/en and choose the relevant country (also check the housing, jobs and community sub-sites).
2. Browse/search the category that fits your subject's situation (housing if they're relocating, jobs if working abroad, classifieds for goods/services).
3. Scan ads for the subject's `name`/`username`, matching phrasing, or contact details; also try `site:justlanded.com "<name/handle>"` in a search engine.
4. On a hit, read the ad for city/`geolocation`, contact method, timing (before/after a move), and any named companions.
5. Pivot: a city/neighbourhood feeds geolocation; a contact email/phone feeds account-existence tools; community connections are `associate` leads.

## Inputs → Outputs
- **In:** `name` or `username` (best combined with a country/city)
- **Out:** classified/housing/job ads, community `social-profile`, `geolocation` (city/country), contact details, `associate`s
- **Empty/negative result looks like:** no ads/profile — most people never post here, and coverage is thin in some countries, so absence is weak evidence. Try other countries they may have lived in and mainstream local classifieds.

## Gotchas & OpSec
- Niche and expat-focused — high value for movers/abroad subjects, low for someone rooted in their home town.
- Ads are user-posted and unverified; treat contact details and claims as leads to confirm.
- Coverage/activity vary a lot by country; a quiet country section isn't proof of absence.
- Browsing is passive; replying/community use needs an account — use a sock puppet.

## Overlaps ("do both")
- Pairs with mainstream local classifieds (Craigslist, country-specific boards) and people-search tools: Just Landed adds the cross-border expat layer they miss, while they anchor identity and fill in home-country detail.

## Trust & verifiability
`trust: unverified` — Just Landed is a genuine, established expat platform, but individual ads and community profiles are self-posted and unverified. Corroborate any location/contact detail before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justlanded-classified-ads-worldwide |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
