---
id: gogettr
name: GoGettr
description: Use when you have a GETTR `username`, hashtag or post and want to archive its data — a Python client pulling posts, comments, followers and profiles from GETTR.
url: https://pypi.org/project/gogettr/
category: public-records
path:
- public-records
bestFor: Bulk-collecting a GETTR user's posts, comments, followers/following and profile, or trending posts/hashtags, for archival and analysis.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open-source (Stanford Internet Observatory); no API key needed — it uses GETTR's public endpoints.
opsec: active
opsecNote: The client makes requests to GETTR's servers to pull data. It needs no login and names no third-party service, but heavy pulling is high-volume traffic against GETTR from your IP — run from attributable-safe infrastructure and rate-limit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Built by the Stanford Internet Observatory for research; well-regarded but SIO wound down in 2024, so maintenance is uncertain and it may break if GETTR changes its API.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- stanfordio/gogettr
- GETTR API client
tags:
- gettr
- social-scraper
- python
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# GoGettr

> A Python client from the Stanford Internet Observatory for pulling public GETTR data — posts, comments, followers, profiles, trends — in bulk for archival and analysis.

## When to use
Your subject (or an entity of interest) is active on GETTR and you need to collect their footprint at scale: all their posts and comments, who they follow and who follows them (`associate`), and profile details — or you want platform-level trending posts/hashtags. GoGettr automates what would be impractical to gather by hand.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install gogettr` (needs Python 3.8+).
2. Use the Python API (or CLI) to call the relevant method — e.g. pull a user's posts/comments, their followers/following, or profile info by `username`.
3. It requires no authentication; data comes from GETTR's public endpoints.
4. Export the results (JSON) for analysis/archival; rate-limit heavy pulls.
5. Pivot: follower/following lists build an `associate` network; profile links and reused handles feed cross-platform username enumeration.

## Inputs → Outputs
- **In:** GETTR `username` (or hashtag/post id)
- **Out:** `social-profile` (posts, comments, profile), followers/following as `associate`s
- **Empty/negative result looks like:** errors or empty pulls — often because GETTR changed its endpoints or the account is gone, not necessarily a true negative; verify the account exists in a browser.

## Gotchas & OpSec
- **Maintenance risk:** SIO wound down in 2024; if GETTR alters its API the client can break. Test on a known account first.
- OpSec: **active** — bulk requests hit GETTR from your IP; use safe infrastructure and throttle.
- Collect only what your authorisation and the platform's terms permit.

## Overlaps ("do both")
- Overlaps with other social-network scrapers (for cross-platform coverage) and with manual GETTR browsing when you only need a few items rather than a bulk archive.

## Trust & verifiability
`trust: community` — reputable research origin and open-source/auditable, but its age means results should be spot-checked and functionality re-verified before a run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gogettr |
