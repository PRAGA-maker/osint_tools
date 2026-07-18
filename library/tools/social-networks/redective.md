---
id: redective
name: Redective
description: Use when you have a Reddit `username` (or subreddit/keyword) and want a fast activity profile — returns their subreddits, most-used words, active hours and posts as a `social-profile` summary.
url: https://www.redective.com/
category: social-networks
path:
- social-networks
bestFor: Rapidly profiling a Reddit user's behaviour — favourite subreddits, active hours, vocabulary — from their public history.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free web tool; real-time queries against Reddit's public data, no account needed.
opsec: passive
opsecNote: Redective queries Reddit's public API in real time and stores nothing, so it doesn't touch the target directly — but Reddit sees Redective's requests, not yours, keeping you at arm's length. Analysing timing/subreddits is passive OSINT; drawing conclusions (e.g. timezone) is inference, not fact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party Reddit analytics tool; it summarises genuine public Reddit activity, but its stats depend on Reddit's API returning full history (older/removed content may be missing).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Redective the Reddit Search Detective
- redective.com
tags:
- reddit
- social-media
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Redective

> "The Reddit Search Detective" — paste a Reddit username and get an instant behavioural profile: which subreddits they haunt, when they're active, and the words they use most.

## When to use
You have a Reddit `username` and want to understand the person behind it quickly. Redective aggregates a user's public post/comment history into a profile: their most-frequented **subreddits** (interests, location clues, affiliations), **active hours** (a rough timezone/lifestyle signal), and **most-used words/phrases** (topics, jargon, possible identifying detail). It's a fast triage step before manually reading their comment history, and it also searches subreddits and keywords.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.redective.com/.
2. Enter the Reddit `username` (or search a subreddit/keyword instead).
3. Read the generated profile:
   - **Top subreddits** — interests, communities, and sometimes location/employer hints (e.g. a city or team subreddit).
   - **Activity by hour/day** — infer an approximate timezone and routine.
   - **Most-used words** — topics and vocabulary that may leak identifying detail.
4. Then read the actual comments the tool surfaces for context and quoted specifics.
5. Pivot: subreddit membership and self-disclosures feed geolocation and identity work; the handle feeds cross-platform username searches.

## Inputs → Outputs
- **In:** Reddit `username` (or subreddit/keyword)
- **Out:** `social-profile` summary — subreddits, active hours, word frequencies, posts — plus location/timezone inferences (`geolocation`)
- **Empty/negative result looks like:** no data / very thin profile — the account is new, deleted, suspended, shadowbanned, or has almost no public activity; or Reddit's API returned limited history. Not proof of nothing.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — Redective queries Reddit on your behalf and keeps no data, so you stay a step removed from the target.
- Active-hours → timezone is an **inference**, easily thrown off by shift work, travel, or scheduling; treat it as a hypothesis to corroborate.
- History depth depends on Reddit's API; deleted/removed content and very old posts may be missing, so the profile can under-represent activity.

## Overlaps ("do both")
- Do both with a manual read of the user's Reddit profile and with cross-platform username tools — Redective gives the fast statistical overview, the manual read and username sweep give the identifying specifics.

## Trust & verifiability
`trust: community` — a third-party analytics front-end over genuine public Reddit data; the raw activity is real (verify by reading the linked posts), but the derived stats are only as complete as Reddit's API allows.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redective |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
