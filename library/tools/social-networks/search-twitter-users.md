---
id: search-twitter-users
name: Pushshift Twitter User Search
description: Use when you follow an old Pushshift Twitter-user-search link — the endpoint is gone (404) and Pushshift no longer serves public Twitter data, so treat as defunct.
url: https://pushshift.io/twitter-user-search/
category: social-networks
path:
- social-networks
bestFor: (Defunct) bulk Twitter user/tweet search via Pushshift; the Twitter endpoints have been removed.
selectorsIn: []
selectorsOut: []
status: down
pricing: free
costNote: Was a free research search over archived Twitter data; the Twitter-user-search page now returns 404 and Pushshift has retired public Twitter access.
opsec: passive
opsecNote: Moot — the service is gone. When it operated it queried an archive, not Twitter live, so it was passive toward the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Pushshift was a respected academic-adjacent data archive, but after platform-API changes it wound down public Twitter search and now focuses on gated Reddit data; the Twitter user-search URL is dead.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pushshift twitter search
tags:
- twitter
- defunct
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- files-pushshift-io-reddit
- pushshift-api
---

# Pushshift Twitter User Search

> A former free search over archived Twitter data — the endpoint now returns 404 and Pushshift no longer offers public Twitter access.

## When to use
Do not rely on this. Pushshift's Twitter user-search page (`pushshift.io/twitter-user-search/`) returns **404**; after Twitter/X locked down its API, Pushshift retired its public Twitter tooling and now concentrates on Reddit data behind access controls. This entry is retained so an agent recognises the name and does not waste time on a dead endpoint.

## How to use it (`bestInteractionPattern`: web-manual)
1. (Not usable.) The URL 404s.
2. Instead, for historical tweets use the Wayback Machine and archive.today on known profile URLs; for live X search use X's own advanced search or current third-party X search tools.

## Inputs → Outputs
- **In:** (formerly) `username` / keyword over archived tweets
- **Out:** (formerly) matching users/tweets from the archive
- **Empty/negative result looks like:** an HTTP 404 page — there is no working search surface.

## Gotchas & OpSec
- Status: **down** — the Twitter side of Pushshift is discontinued; do not confuse it with Pushshift's (separate, gated) Reddit data.
- Any mirror claiming to be "Pushshift Twitter search" is unofficial — treat with suspicion.

## Overlaps ("do both")
- Substitute Wayback Machine / archive.today for historical tweet capture and X advanced search for live queries.

## Trust & verifiability
`trust: community` — Pushshift itself was reputable, but this specific capability is defunct; no Twitter data is obtainable from it now.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-twitter-users |
| category | social-networks |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
