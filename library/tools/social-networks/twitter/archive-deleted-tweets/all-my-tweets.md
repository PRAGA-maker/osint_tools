---
id: all-my-tweets
name: All My Tweets
description: Use when you have a Twitter/X `username` and want that account's recent public tweets on one scrollable page for fast review/export — returns `social-profile` post history (up to ~3,200 tweets).
url: https://www.allmytweets.net/
category: social-networks
path:
- social-networks
- twitter
- archive-deleted-tweets
bestFor: Rendering an X account's recent tweets on a single page for quick keyword/date review and export.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: degraded
pricing: free
costNote: Free, but now requires signing in with an X account and is being wound down ("AllMyTweets is now part of Twilert; will soon stop functioning"). Subject to X API rate limits.
opsec: active
opsecNote: You must authorize the app with an X login — use a sock-puppet X account, never your real one, since the OAuth grant ties your account to the lookups. It reads the target's public tweets, not private ones.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party service dependent on the X API; being merged into Twilert and slated to stop, so reliability is declining.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- allmytweets
- All My Tweets viewer
tags:
- twitter
- x
- tweet-history
- archive
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- allmytweets
---

# All My Tweets

> A single-page renderer for an X account's recent tweets — historically great for skimming and exporting a timeline, now login-gated and being sunset.

## When to use
You have a Twitter/X `username` and want to review or export its recent public tweets quickly, all on one page, to keyword/date-search a timeline rather than infinite-scrolling X. Useful for building a subject's activity timeline and catching mentions of places, people and events — but note the service is degraded (login required, ~3,200-tweet cap, and slated to shut down).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.allmytweets.net/ and sign in with a **sock-puppet** X account (OAuth is now required).
2. Enter the target's X `username`.
3. It renders up to ~3,200 of the account's most recent public tweets on one page.
4. Use browser find (Ctrl-F), the site's keyword/date filters, or export to .txt/.csv.
5. Pivot: pull mentioned locations/handles/dates into mapping, enumeration and timeline work.

## Inputs → Outputs
- **In:** `username` (X handle)
- **Out:** `social-profile` timeline (recent tweets), `metadata-exif`-style timestamps; .txt/.csv export
- **Empty/negative result looks like:** nothing loads or an API-limit/error notice — the account is private/suspended, you hit X rate limits, or the service is down; verify on X directly.

## Gotchas & OpSec
- **Being retired** — merged into Twilert with a notice it will stop functioning; treat as short-lived.
- Login (OAuth) is now mandatory — only ever authorize a sock-puppet account.
- Hard cap of ~3,200 tweets (X API limit) — it is not a full archive; older tweets need the Wayback Machine or archives.

## Overlaps ("do both")
- Pairs with X advanced search and the Wayback Machine — this gives a fast recent-timeline view, those reach older/deleted content it can't.

## Trust & verifiability
`trust: unverified` — a third-party viewer wholly dependent on the X API and now being wound down; content it shows is genuine (straight from X), but coverage is capped and reliability is falling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | all-my-tweets |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
