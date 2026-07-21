---
id: kribrum-io
name: Kribrum.io
description: Use when you have a `name`/`username` and want to search public social-media posts by author and time period — returns `social-profile` and post content.
url: https://kribrum.io/search
category: social-networks
path:
- social-networks
bestFor: Searching across multiple social platforms for posts filtered by author and date range (strong Russian-language coverage).
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: Freemium social-listening service; basic search is free but deeper/analytic features and history generally require registration and a paid plan.
opsec: passive
opsecNote: You query Kribrum's own aggregated social-media index, not the target's accounts, so the search does not notify the subject. It is a Russian service — assume queries may be logged on that side; use a sock-puppet identity and avoid entering sensitive terms.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established Russian social-media monitoring platform; index coverage and freshness are opaque, so treat results as a partial view and corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- kribrum
aliases:
- kribrum.io
- Крибрум
tags:
- Social Media
- Universal
- social-monitoring
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Kribrum.io

> A Russian social-media search/monitoring engine that indexes posts across many platforms and lets you filter by **author and time period** — useful for finding what a person said online and when, especially in Russian-language spaces.

## When to use
You have a `name`, `username`, or author handle and want to find their (or others') public posts across social networks, optionally scoped to a date window. This is strongest for Russian-language and RU-region social content that Western tools index poorly, and for building a timeline of when an account was active around a specific event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kribrum.io/search in a sock-puppet browser. **Note:** the service was in a planned maintenance window around 22–23 July 2026 — if it shows "Сервис временно недоступен", retry after that window.
2. Enter your query term (name/keyword) and set the author and time-period filters.
3. Register a (sock-puppet) account if prompted — full search/analytics is gated behind login and likely a paid tier.
4. Read the returned posts: author handle, platform, timestamp, and content are the payload.
5. Pivot: feed a discovered author `username` into a cross-platform username sweep and any linked accounts into platform-specific tools.

## Inputs → Outputs
- **In:** `name`/`username`/keyword + optional author and date filters
- **Out:** matching public posts and their author `social-profile`s (handle, platform, timestamp)
- **Empty/negative result looks like:** no posts for the term/author/date range — either the content isn't in Kribrum's index (coverage is partial) or it's gated behind the paid tier; weak negative evidence.

## Gotchas & OpSec
- **Degraded/maintenance:** may be temporarily unavailable (see the maintenance note); retry rather than assuming it's dead.
- Russian-language interface and service — use machine translation, and assume RU-side logging; keep to a sock puppet.
- Freemium: the most useful depth (analytics, history) is behind registration/payment.

## Overlaps ("do both")
- Pairs with `[[kribrum]]` (same provider) and with Western social-search tools — Kribrum fills RU-language gaps those miss, and vice versa.

## Trust & verifiability
`trust: unverified` — a real, established monitoring platform, but its index scope and freshness are opaque; corroborate any post/attribution on the originating platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kribrum-io |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
