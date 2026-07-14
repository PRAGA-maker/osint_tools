---
id: tweetbeaver
name: TweetBeaver
description: Use when you want Twitter/X account tools (username↔ID, common followers, timeline dumps) — but the domain is now hijacked to an unrelated site, so treat it as down.
url: https://tweetbeaver.com/
category: social-networks
path:
- social-networks
bestFor: (Historically) bulk Twitter/X account utilities — ID conversion, common-follower analysis, data export.
selectorsIn:
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was a free Twitter-tools site. The domain no longer serves it — tweetbeaver.com now 301-redirects to an unrelated third-party (gambling) site, indicating the service is defunct or the domain was lost.
opsec: passive
opsecNote: Do NOT visit or submit anything to the current URL — it redirects off-host to an unrelated commercial/gambling domain. There is no safe live endpoint; entering a handle would only reach whoever now controls the domain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The tool this record described is no longer reachable at its URL; the domain now points to unrelated content, so nothing here can be verified against a live service.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tweetbeaver.com
tags:
- twitter
- defunct
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# TweetBeaver

> A once-excellent set of Twitter/X account utilities — now dead: the domain redirects to an unrelated site, so this is documented as down, not usable.

## When to use
Do not use it in a live investigation — it's recorded so an agent recognizes the name and moves on. Historically it was invaluable: convert a Twitter `username` to its numeric ID and back, find followers two accounts have in common, bulk-check friendships, and download timelines/favorites. Twitter/X's API lockdown already gutted such tools, and the domain has since been lost.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognize the status: `tweetbeaver.com` now 301-redirects to an unrelated off-host (gambling) domain — the service is gone.
2. Do not enter any handle or data on the redirected site.
3. Substitute current methods: for username↔ID use `[[find-my-facebook-id-3]]`-style resolvers on the right platform, and for cross-platform handle mapping use `[[maigret]]` and `[[social-profiles-finder]]`.

## Inputs → Outputs
- **In:** Twitter/X `username` (historically)
- **Out:** account utilities (ID conversion, common followers, exports) — currently nothing usable
- **Empty/negative result looks like:** not applicable — there is no working endpoint; anything served at the old URL is an unrelated site, not a result.

## Gotchas & OpSec
- Classic lapsed-domain trap: an OSINT domain re-registered by a third party. Never submit a selector to it.
- If a future check shows the genuine service restored, flip `status` back to live and re-author from the real page rather than assuming its old behavior.

## Overlaps ("do both")
- Superseded by `[[maigret]]` and `[[social-profiles-finder]]` for identity/handle mapping; Twitter/X's own API changes mean no free tool replicates TweetBeaver's old bulk features today.

## Trust & verifiability
`trust: unverified` — no live tool to verify; the URL resolves to unrelated content, so this record exists only to mark it down.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweetbeaver |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
