---
id: chatter
name: chatter
description: Use when you want automated keyword/phrase monitoring across Twitter, Reddit, and 4chan with alerts to Telegram — returns matching public posts. NOTE archived abandonware; Twitter portion broken by API lockdown.
url: https://github.com/visualbasic6/chatter
category: social-networks
path:
- social-networks
bestFor: (Historical) a self-hosted bot that crawls Twitter/Reddit/4chan for keywords and pushes matches to a Telegram group.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Free and open-source, but the repo was archived in April 2023 as abandonware and its author called it "very unstable." Written in Visual Basic 6 (Windows-only) and may trip antivirus.
opsec: passive
opsecNote: Monitoring reads public posts via APIs, so it doesn't touch the target — but it needs a Telegram bot token and API keys, and the queried platforms log the API traffic from your keys. Use dedicated credentials, not personal accounts.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An archived proof-of-concept OSINT monitor; conceptually useful but unmaintained, unstable, and partly broken by Twitter's API changes — review the code and treat as a reference design.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- chatter monitor
- visualbasic6 chatter
tags:
- monitoring
- twitter
- reddit
- 4chan
- keyword-alerts
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# chatter

> A self-hosted keyword monitor that crawled Twitter/Reddit/4chan and alerted a Telegram group — now archived abandonware, with its Twitter half broken by API lockdown. Kept as a reference pattern.

## When to use
The use-case is standing keyword/phrase surveillance: watch Twitter, Reddit, and 4chan for a subject's name, handle, phrase, or a case-specific term, and get near-real-time Telegram alerts on matches. In practice, verify before relying on it — the project is archived and the Twitter path is effectively dead post-API-lockdown; treat this entry as the technique plus a pointer to maintained alternatives.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/visualbasic6/chatter (note: archived, VB6, Windows). Review the code first (uncommon language can trip AV).
2. Configure a Telegram bot token + group chat ID, and populate keyword/phrase and subreddit lists.
3. Run it on a Windows host; it periodically crawls the sources and posts matches to your Telegram group, storing seen URLs as `.txt` to avoid duplicates.
4. Expect the Reddit/4chan crawlers to work better than Twitter (which now requires paid API).
5. Pivot: for a maintained setup, replicate the pattern with current tooling (e.g. Reddit/4chan APIs + a monitoring framework) rather than this abandonware.

## Inputs → Outputs
- **In:** keyword/phrase and source lists (subreddits, terms) — plus `name`/`username` as watch terms
- **Out:** matching public posts (`social-profile` content) delivered to Telegram
- **Empty/negative result looks like:** no alerts — either nothing matched, or (commonly now) the Twitter crawler is failing on API errors. Silence is not proof of no chatter; confirm each source is actually working.

## Gotchas & OpSec
- **Down/abandoned:** archived April 2023, unstable, Windows/VB6-only, Twitter portion broken — do not treat as production-ready.
- Needs API keys and a Telegram bot; use dedicated credentials.
- Passive toward targets; your API keys are what's exposed to the platforms.

## Overlaps ("do both")
- Pairs with maintained monitoring stacks and platform-native alerts — use those for live coverage; keep chatter only as a design reference for a multi-source keyword monitor.

## Trust & verifiability
`trust: community` — an archived proof-of-concept. Its outputs (when it runs) are real public posts, but its reliability is poor; prefer a maintained equivalent for any real investigation.
