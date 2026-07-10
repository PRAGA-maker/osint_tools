---
id: redarcs
name: REDARCS (Reddit Archives)
description: Use when you have a subreddit or Reddit `username` and want bulk downloadable archives of its submissions and comments — including removed/banned content — returns social-profile activity for offline analysis.
url: https://the-eye.eu/redarcs/
category: social-networks
path:
- social-networks
bestFor: Downloading full submission/comment archives of subreddits (including banned/quarantined ones) to recover deleted content and analyse a user's Reddit history offline.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free bulk downloads hosted by the-eye.eu; no account. Cost is bandwidth/disk — archives are large compressed dumps.
opsec: passive
opsecNote: You download static archive files and analyse them locally, never contacting Reddit or the target — fully passive. Downloading via a VPN keeps the retrieval off your attributable IP; the-eye is a third-party mirror, so verify file integrity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-hosted Reddit data dumps on the-eye.eu (Pushshift-era collections); the underlying data is genuine historical Reddit content, but the archive is frozen in time and site availability can be intermittent.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- REDARCS
- Reddit Archives
- the-eye reddit dumps
tags:
- reddit
- archive
- deleted-content
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# REDARCS (Reddit Archives)

> Bulk, downloadable archives of entire subreddits' submissions and comments — including content Reddit later removed — for recovering deleted posts and mining a user's full history offline.

## When to use
You need Reddit content that the live site no longer shows: posts/comments a user deleted, an account that's been suspended, or a whole subreddit that was banned/quarantined. REDARCS provides large compressed dumps of subreddit submissions and comments captured before Reddit locked down its API. Load a dump locally and you can reconstruct a `username`'s complete comment/post history — invaluable when a subject scrubbed their trail or the account is gone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse https://the-eye.eu/redarcs/ and locate the subreddit(s) relevant to your subject (dumps are per-subreddit).
2. Download the submissions and comments archives (compressed NDJSON, e.g. `.zst`).
3. Decompress and search locally (jq/grep/scripts) for the target `username`, keywords, or timeframes.
4. Reconstruct the user's activity — including entries deleted from live Reddit — and note linked usernames, timestamps and any self-disclosed details.
5. Pivot: recovered posts feed timeline and network analysis; mentioned handles/links feed cross-platform enumeration.

## Inputs → Outputs
- **In:** a subreddit name, plus a `username`/`social-profile` to search within the dumps
- **Out:** `social-profile` (a user's full archived posts/comments, including removed ones)
- **Empty/negative result looks like:** the subreddit isn't in the archive, or the user never posted in the archived subs/timeframe — the collection is a snapshot, not all of Reddit, so absence isn't conclusive.

## Gotchas & OpSec
- **Frozen snapshot:** dumps end at the collection date (Pushshift-era); nothing after is captured, and coverage is per-subreddit, not global.
- Large files — plan disk/bandwidth; the-eye availability can be intermittent (mirrors exist).
- OpSec: fully passive; analyse offline.

## Overlaps ("do both")
- Pairs with live Reddit user tools and `[[mostly-harmless]]` — use REDARCS to recover what live Reddit hides, and live tools for anything posted after the archive cutoff.

## Trust & verifiability
`trust: community` — genuine historical Reddit data hosted by a community mirror; content is authentic to its capture date, but verify against any surviving live posts and note the snapshot boundary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redarcs |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
