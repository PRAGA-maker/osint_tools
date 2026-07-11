---
id: reddit-old-reddit-search
name: Reddit (old.reddit search)
description: Use when you have a Reddit `username` or keyword/`name` and want to read a user's full post/comment history or find mentions — returns their social-profile activity, interests, associates and location/timing signals.
url: https://old.reddit.com/
category: communities-forums
path:
- communities-forums
bestFor: Reading a Reddit user's submissions/comments and searching keyword/domain mentions via the old, operator-friendly interface.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
- geolocation
status: live
pricing: free
costNote: Free; no account required to read public profiles or search. Logged out avoids personalisation.
opsec: passive
opsecNote: Reading public profiles and searching is passive and does not notify the user. Do NOT upvote, comment, follow or message from a real account — that is active and visible. Use a logged-out session or a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: old.reddit.com is Reddit's own legacy interface — first-party and reliable for what users publicly posted; the caveat is user self-reporting (people post inaccurate or deliberately misleading personal details).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- old.reddit
- old reddit search
tags:
- reddit
- forum
- user-history
source: inteltechniques-tools
lastVerified: '2026-07-11'
enrichment: full
---

# Reddit (old.reddit search)

> Reddit's legacy web interface — cleaner for investigators than new Reddit, with straightforward URLs for reading a user's entire public post/comment history and running keyword/subreddit/domain searches.

## When to use
You have a Reddit `username` and want to mine their public activity — a person's Reddit history is often a rich, candid trove of location, routine, relationships, employer, interests and even photos. Or you have a `name`/keyword and want to find where a subject (or a topic/domain) is discussed. A high-yield source when a subject is a Reddit user.

## How to use it (`bestInteractionPattern`: web-manual)
1. For a known user, go to `https://old.reddit.com/user/<username>` — read Overview, Submitted, Comments tabs for their full public history.
2. Sort comments by New/Top and skim for self-disclosures (city, job, relationships, "my [relative]…").
3. To search, use `https://old.reddit.com/search?q=<terms>` or scope to a subreddit; use operators like `subreddit:`, `author:`, `url:`, `title:` to narrow.
4. Stay logged out (or use a sock puppet) — read only, never interact.
5. Pivot: subreddits reveal interests/location (city/hobby subs); replies map `associate` links; disclosed details feed people-search and other platforms; usernames feed cross-platform enumeration (`[[aliens-eye]]`).

## Inputs → Outputs
- **In:** Reddit `username`, or `name`/keyword/domain query
- **Out:** the user's `social-profile` activity (submissions/comments), `associate` interactions, and `geolocation`/routine signals from self-disclosures and subreddit choices
- **Empty/negative result looks like:** a shadow/empty profile (no visible posts), a suspended/deleted account, or search returning nothing — the person may not use Reddit under that handle, or posts were removed. Note Reddit's native search is weaker for old content; a keyword miss isn't conclusive.

## Gotchas & OpSec
- **Self-reported = unreliable:** people lie, exaggerate, or roleplay on Reddit — corroborate any "fact" before trusting it.
- Native search misses/ranks old content poorly; for historical or deleted posts, consider archive/Pushshift-style tools.
- OpSec: **strictly read-only.** Any vote/comment/DM/follow exposes you; use logged-out or sock-puppet sessions.

## Overlaps ("do both")
- Pairs with archive tools for deleted/edited posts and with cross-platform username enumeration (`[[aliens-eye]]`) — old.reddit reads the live history; those recover what's gone and find the handle elsewhere.

## Trust & verifiability
`trust: community` — first-party Reddit interface, so the activity shown is authentic to what the user posted; the reliability limit is the user's own truthfulness, so verify self-disclosed details independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-old-reddit-search |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
