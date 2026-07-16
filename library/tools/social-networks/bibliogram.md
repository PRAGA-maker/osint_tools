---
id: bibliogram
name: Bibliogram
description: Use when you have an Instagram `username` and want to view a profile/posts without an Instagram login — but note this front-end is defunct; returns `social-profile` content only on rare surviving instances.
url: https://bib.actionsack.com/
category: social-networks
path:
- social-networks
bestFor: Historically, viewing public Instagram profiles and posts anonymously (no login, no JS) via a privacy front-end — now largely non-functional.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: down
pricing: free
costNote: Free and open-source when it worked; no account required. Value today is near zero because the project is discontinued.
opsec: passive
opsecNote: The design intent was passive/anonymous Instagram viewing (no account, no JS, no Instagram cookies). If you find a live mirror, it still proxies through a third party you do not control — assume the operator can log your queries; use a puppet IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by cadence (sr.ht/~cadence/bibliogram). Officially discontinued in September 2022; most public instances, including bib.actionsack.com, are down or block profile views.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
deprecated: true
aliases:
- Bibliogram Instagram frontend
- bib.actionsack.com
tags:
- instagram
- social-networks
- alternative-frontend
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- send
- youtube-dl
---

# Bibliogram

> A discontinued open-source Instagram front-end that once let you read public profiles anonymously — mostly dead now, catalogued so agents don't waste time on dead instances.

## When to use
You have an Instagram `username` and want to view the profile/posts without logging into Instagram or triggering its rate limits. **Reach for this only as a fallback and expect failure**: the project was discontinued in September 2022 after Instagram repeatedly changed its data format, and the reference instance `bib.actionsack.com` (like most) no longer serves profiles. If you need a working alternative, jump straight to a current Instagram viewer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try opening `https://bib.actionsack.com/u/<username>` (the `/u/` path is the profile route).
2. If it 403s, times out, or shows "profile viewing is disabled," the instance is dead — do not retry other Bibliogram instances one by one; they share the same breakage.
3. On the rare working mirror, read the profile bio, post grid, and images (`social-profile`, `image`) and download media directly.
4. Pivot: because uptime is unreliable, go to a maintained viewer (Imginn, Picuki-style services) or an authenticated puppet Instagram account for anything time-sensitive.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** `social-profile` (bio, post list), `image` (post media) — only if an instance is alive
- **Empty/negative result looks like:** HTTP 403/404, a "this instance is closed" notice, or an infinite spinner. That is the *expected* state today, not a sign the account is private.

## Gotchas & OpSec
- **Defunct:** the single biggest gotcha — assume it does not work and have a fallback ready.
- Self-hosting the open-source code no longer helps much because Instagram broke the scraping paths it relied on.
- OpSec: passive by design, but any surviving public instance is a third party proxying your request; treat queries as logged.

## Overlaps ("do both")
- Superseded in practice by maintained Instagram viewers and by direct puppet-account viewing — use those for coverage.
- Pairs conceptually with other alternative front-ends (Nitter for Twitter/X, Invidious for YouTube), which faced the same platform-blocking pressures.

## Trust & verifiability
`trust: community` — legitimate, well-known open-source project, but functionally deprecated. Any data you do retrieve is proxied Instagram content; verify against the live platform where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bibliogram |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
