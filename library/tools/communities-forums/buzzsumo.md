---
id: buzzsumo
name: BuzzSumo
description: Use when you have a `name`, `domain`, or topic and want to find the most-shared content and the authors/influencers behind it — returns articles, engagement metrics, and `social-profile` links.
url: https://buzzsumo.com/
category: communities-forums
path:
- communities-forums
bestFor: Finding what content a person/brand published or that mentions them, plus the social accounts of the authors who wrote it.
selectorsIn:
- name
- domain
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free plan gives ~10 searches/month (1 user, 1 year of data, capped results); unlimited searches and influencer data require paid Pro ($99/mo) and up. A 30-day free trial (no card) is available.
opsec: passive
opsecNote: Queries hit BuzzSumo's index, not the subject's accounts, so nothing reaches the target. Registration is required even for the free tier, so BuzzSumo (and its owner Brandwatch/Cision) logs your searches under your account — use a research-only login, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial content-intelligence platform (Brandwatch/Cision). Data is real and broad but engagement metrics are proprietary estimates; treat author→profile links as leads to confirm.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- appsumo-content-analyzer
- buzz-sumo
aliases:
- Buzz Sumo
tags:
- toddington
- curated-directory
- news-journalism
- content-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# BuzzSumo

> Content-discovery engine over 8B+ articles: find the most-shared content on any topic, domain, or byline — and surface the authors and social accounts behind it.

## When to use
You have a subject's `name`, a `domain` they run, or a topic they're associated with, and you want to find what they published or what was written about them, ranked by social engagement. The Content Analyzer maps articles to their authors, and the influencer search maps a name/topic to social accounts and bios — useful for turning a byline into a `social-profile`, or for finding an active person's public writing footprint. Also handy for establishing a timeline of when someone/something was in the news.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://buzzsumo.com/ (free plan allows ~10 searches/month — use a research account).
2. Content search: enter the subject's `name`, a keyword, or a `domain` into Content Analyzer. Results are articles with share counts, publish dates, and the author's name.
3. Click an author to see other content by them and, where available, their linked social accounts.
4. Influencer/creator search: query a name or topic to find matching accounts with bios and follower data (this feature is largely gated to paid plans).
5. Watch the search quota — the free tier exhausts quickly; batch your queries.
6. Pivot: an author name → their `social-profile` for username/photo pivots; a domain's top content → the people who wrote and shared it.

## Inputs → Outputs
- **In:** `name`, `domain`, or topic/keyword
- **Out:** articles + engagement metrics, author `name`s, author/creator `social-profile` links
- **Empty/negative result looks like:** "No results" or only unrelated content — the subject has little indexed published/shared content; absence here does not mean they have no online presence.

## Gotchas & OpSec
- Human-in-the-loop: an account login is mandatory even for free use, and the free tier is hard-capped at ~10 searches/month, so plan queries carefully.
- Engagement numbers are proprietary estimates, not verified counts.
- Strongest for people who publish or are covered by media (journalists, marketers, execs); weak for private individuals.
- Passive toward the target, but your searches are tied to your BuzzSumo login — use a dedicated research account.

## Overlaps ("do both")
- Pairs with `[[appsumo-content-analyzer]]` and `[[buzz-sumo]]` — overlapping content-analysis angles; run alongside a name-based social search so an author found here can be resolved to full profiles.

## Trust & verifiability
`trust: community` — a mature commercial platform with real, broad data, but engagement metrics are estimates and author→account links should be confirmed on the actual platform before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buzzsumo |
| category | communities-forums |
| selectorsIn → selectorsOut | name, domain → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
