---
id: reddit-persona
name: Reddit Persona
description: Use when you have a Reddit `username` and want an at-a-glance behavioural profile — returns inferred interests, active subreddits, and geolocation/timezone hints built from that user's post/comment history.
url: https://github.com/n2itn/reddit_persona
category: social-networks
path:
- social-networks
bestFor: Building a persona (interests, communities, activity patterns) from a Reddit user's public history.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, open-source Python script. Uses Reddit's API (PRAW), so you supply free Reddit API credentials (client id/secret).
opsec: passive
opsecNote: Reads the target's public Reddit posts/comments via the API; the user is not notified and cannot see who queried them. Your Reddit API credentials/IP are visible to Reddit. Do not upvote/comment/DM from the account you use — keep it read-only to stay passive.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small open-source project; the value is in aggregating public Reddit data, and every inference should be verified against the raw posts it cites.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- reddit-user-analyser
- redective
- reddit-investigator
aliases:
- n2itn/reddit_persona
tags:
- reddit
- persona
- python
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Reddit Persona

> An open-source script that ingests a Reddit user's public post/comment history and summarizes it into a persona — their interests, the communities they frequent, and any location/timezone clues they've dropped.

## When to use
You have a Reddit `username` and want to understand the person behind it fast, without reading hundreds of comments by hand. Redditors routinely reveal their city, job, age, relationships, and daily routine across scattered posts; this tool aggregates that history so you can spot the identifying details and the subreddits that hint at where they live, what they do, and who they interact with.

## How to use it (`bestInteractionPattern`: cli)
1. Register a free Reddit "script" app (reddit.com/prefs/apps) to get a client id/secret, then clone `https://github.com/n2itn/reddit_persona`.
2. Install dependencies (Python + PRAW) and add your Reddit API credentials to the config.
3. Run the script against the target `username`; it pulls their recent posts/comments and outputs a summary of top subreddits, interests, and activity timing.
4. Read the active-subreddit list for `geolocation` leads (city/regional subs, local sports/venues) and the activity timestamps for a likely timezone.
5. Pivot: reused `username` → username-search tools; a named city/employer in the history → people-search; corroborate every inferred fact against the actual linked comment.

## Inputs → Outputs
- **In:** `username` (Reddit handle)
- **Out:** `social-profile` (interests, top subreddits, activity summary), `geolocation` (location/timezone hints inferred from subs and post times)
- **Empty/negative result looks like:** a thin or empty profile — a new, low-activity, or deleted/suspended account, or a user who scrubbed their history. Sparse output means little public data, not that the account is fake.

## Gotchas & OpSec
- Reddit's API only returns a limited window of recent history (roughly the last ~1000 items); older revealing posts may be out of reach — check the profile page directly for anything the script misses.
- Inferences (location, age, job) are guesses from scattered text; always click through to the source comment before treating a detail as fact.
- Human-in-the-loop: you must supply your own Reddit API key. OpSec: **passive** if you keep the account read-only — never interact with the target from it.

## Overlaps ("do both")
- Pairs with `[[reddit-user-analyser]]` and `[[redective]]` — different tools window and summarize the history differently, so run more than one and merge the subreddit/interest signals before drawing conclusions.

## Trust & verifiability
`trust: community` — a small open-source project that only surfaces public Reddit data; treat its persona summary as a lead index into the raw posts, which are the actual verifiable source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-persona |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
