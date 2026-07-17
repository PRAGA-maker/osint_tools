---
id: google-alerts
name: Google Alerts
description: Use when you have a `name`, `username`, `email`, `phone`, or `domain` and want ongoing notification whenever new pages mentioning it are indexed — returns email alerts with fresh matching URLs.
url: https://www.google.com/alerts
category: search-engines
path:
- search-engines
- search-tools
bestFor: Standing monitoring — get emailed when new web content mentions a selector.
selectorsIn:
- name
- username
- email
- phone
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free Google service. A Google account is only needed to manage alerts in a dashboard; alerts can be created and delivered to any email.
opsec: passive
opsecNote: Alerts monitor Google's public index — you never contact the subject, and they get no signal that they are being watched. Creating alerts ties them to a Google account/email; use a sock-puppet Google account and inbox for investigations you want to keep separate.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google monitoring service; results are Google search index hits, as authoritative as Google search itself.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- talkwalker-alerts
- visualping
aliases:
- google.com/alerts
tags:
- monitoring
- search
- alerts
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Google Alerts

> Google's free standing-query monitor: register a search term once and get emailed every time Google indexes a new page matching it.

## When to use
You have a selector — a `name`, `username`, `email`, `phone`, or `domain` — and the trail has gone cold or you expect new information to surface (a missing person who may resurface online, a new social post, a fresh forum mention, a newly registered site). Instead of re-running the same search daily, a Google Alert watches Google's index for you and pushes new hits to your inbox as they appear. It converts a one-time search into passive, continuous monitoring.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.google.com/alerts (log in with a dedicated sock-puppet Google account to manage/edit alerts).
2. Enter the query. Use quotes and operators for precision: `"Firstname Lastname" -site:linkedin.com`, an `email`, a `phone` in a couple of formats, or `site:example.com`.
3. Open **Show options** to set frequency (as-it-happens / daily / weekly), sources (news, blogs, web, video), region/language, and the delivery email or RSS feed.
4. Save. Google emails new matching URLs on your chosen cadence; use the RSS-feed option to pipe alerts into a reader or automation.
5. Pivot: each alerted URL is a fresh lead — a new `social-profile`, a new `domain`, a mention to run through the rest of your toolkit.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, or `domain` (as a search query)
- **Out:** email/RSS notifications containing new `social-profile` / `domain` / page URLs mentioning the term
- **Empty/negative result looks like:** no emails arrive — nothing new was indexed for that query. Silence is normal for a quiet subject; broaden the query if it's too narrow.

## Gotchas & OpSec
- Alerts only fire on what Google *indexes* — content behind logins, in closed forums, or on the dark web will not trigger them.
- Broad or common-name queries flood the inbox; anchor with quotes, a location, or a domain to cut noise.
- Human-in-the-loop: a Google account login is needed to create/edit alerts from the dashboard; use a puppet account.
- OpSec: **passive** — monitoring the public index never touches or notifies the subject.

## Overlaps ("do both")
- Pairs with `[[talkwalker-alerts]]` and `[[visualping]]` — Talkwalker catches mentions Google misses, and VisualPing watches a specific page for changes rather than the whole index, so combine them for fuller monitoring coverage.

## Trust & verifiability
`trust: trusted` — it is Google's own service and each alert is a real Google-index hit you can click and verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-alerts |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone, domain → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
