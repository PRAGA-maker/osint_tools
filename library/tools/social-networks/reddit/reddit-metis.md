---
id: reddit-metis
name: Reddit Metis
description: Use when you have a Reddit `username` and want a behavioral profile of that account — returns activity stats, subreddit/topic distribution, active hours/timezone hints, and personality/interest summaries.
url: https://redditmetis.com/
category: social-networks
path:
- social-networks
- reddit
bestFor: Profiling a Reddit account's habits, interests, timezone, and likely location/personality from its public comment/post history.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free web tool; no account required. Rate-limited by Reddit's API, so heavy accounts can take a while or occasionally fail.
opsec: passive
opsecNote: Reads only public Reddit data via the API — the target is not notified and never sees you. No login. Standard browser hygiene; the request comes from Reddit Metis's servers, not your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community successor to snoopsnoo-style profilers; stats are computed directly from public history, but the inferred "personality"/attributes are heuristic guesses, not facts.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Reddit Metis
- redditmetis
tags:
- reddit
- Reddit Related Sites
- account-profiling
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Reddit Metis

> Feed it a Reddit handle and it summarizes the account's behavior — top subreddits, active hours, topics, and heuristic guesses at personality, interests, and location.

## When to use
You have a Reddit `username` and want a fast behavioral read on that account without scrolling months of history: which communities they inhabit, what times of day they post (a strong timezone/geolocation hint), recurring topics, and inferred interests. Excellent for building a pattern-of-life and location hypothesis around a subject's Reddit identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://redditmetis.com/.
2. Enter the target Reddit username and submit.
3. Wait while it pulls and analyzes the public post/comment history (large accounts take longer).
4. Read the report: subreddit distribution, activity heatmap by hour/day (timezone signal), top words/topics, and heuristic personality/interest/location guesses.
5. Pivot: active-hours → likely timezone/region; named places/teams/dialect in top words → geolocation leads; distinctive interests → cross-platform username/interest search.

## Inputs → Outputs
- **In:** Reddit `username`
- **Out:** activity stats, subreddit/topic distribution, active-hours heatmap (`geolocation`/timezone hint), heuristic interest/personality/location inferences
- **Empty/negative result looks like:** "not enough data"/very sparse output for low-activity or brand-new accounts, or a failure on deleted/suspended users. Thin history = thin profile, not a tool error.

## Gotchas & OpSec
- Inferred personality/location are heuristic guesses — treat as leads to corroborate, never as fact.
- Deleted comments/removed accounts limit or break analysis.
- Passive; the pull is server-side, so your IP isn't exposed to Reddit.

## Overlaps ("do both")
- Pairs with direct Reddit history review and `[[reddit-user-analyser]]`-style tools — Metis summarizes and infers, a raw history read confirms the specifics its heuristics flagged.

## Trust & verifiability
`trust: community` — computed from public Reddit data (reliable stats) plus heuristic inferences (unreliable). Verify any location/identity guess against the actual comments it drew from.
