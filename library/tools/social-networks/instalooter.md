---
id: instalooter
name: InstaLooter
description: Use when you have a public Instagram `username`, hashtag, or location and want to bulk-download its media without login or the API — returns saved `image`s/videos with `metadata-exif`.
url: https://pypi.org/project/instalooter/
category: social-networks
path:
- social-networks
bestFor: Programmatic bulk download of a public Instagram profile/hashtag/location's media without an account or the official API.
selectorsIn:
- username
- social-profile
selectorsOut:
- image
- metadata-exif
status: degraded
pricing: free
costNote: Free, open-source Python package/CLI. No cost, but Instagram's frequent front-end changes routinely break unauthenticated scrapers like this — expect breakage and check the project's issue tracker before relying on it.
opsec: passive
opsecNote: InstaLooter fetches public media from your own host/IP, so Instagram sees the request pattern (bursty scraping can trigger blocks). It does not log into or notify the target account when used unauthenticated. Run behind a proxy/VPN from a sock-puppet environment; never supply your real Instagram credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Established open-source tool (PyPI/GitHub), but Instagram's anti-scraping changes mean it is frequently partially or fully broken; reliability depends on the current release matching Instagram's live behaviour.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- instaloader-2
- toutatis-2
aliases:
- instalooter
- InstaLooter
tags:
- instagram
- downloader
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# InstaLooter

> A Python scraper/CLI that bulk-downloads a public Instagram profile, hashtag, or location's media without an account or the official API — for evidence preservation and offline analysis.

## When to use
You have a public Instagram `username` (or a hashtag/location) and want to archive its media in bulk — preserving posts before they can be deleted and enabling offline reverse-image and detail analysis without repeatedly loading the account in a browser. It complements a browser-based approach when you need many images at once, programmatically.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install instalooter`.
2. Download a profile: `instalooter user <username> ./out/` (or `hashtag <tag>` / `post <shortcode>`).
3. Add filters (date ranges, number of posts) and a proxy/VPN for OpSec; run unauthenticated to avoid credential exposure.
4. If it errors or returns nothing, check the project's issue tracker — Instagram changes often break the current release; consider `[[instaloader-2]]` as an alternative.
5. Pivot: run downloaded frames through reverse-image search; read on-image detail for `geolocation`/`address` clues; feed the profile into `[[toutatis-2]]` for account metadata.

## Inputs → Outputs
- **In:** public Instagram `username`, hashtag, or location
- **Out:** saved `image`s/videos and available `metadata-exif`/post metadata
- **Empty/negative result looks like:** errors, empty output, or partial downloads — with unauthenticated scrapers this usually means Instagram changed something or rate-limited you, not that the account is empty.

## Gotchas & OpSec
- Status is **degraded**: unauthenticated Instagram scrapers break often; verify the tool works today before depending on it.
- Only public content is reachable without login; private accounts are out of scope.
- Bursty scraping from one IP invites blocks — use a proxy/VPN and pace requests.
- OpSec: passive toward the target when unauthenticated; never enter real credentials, and mask your IP.

## Overlaps ("do both")
- Overlaps with `[[instaloader-2]]` — a more actively maintained equivalent; if InstaLooter is broken, switch to it. Pair with `[[toutatis-2]]` for profile-level metadata beyond the media.

## Trust & verifiability
`trust: community` — a legitimate, known open-source tool, but its reliability tracks Instagram's ever-changing anti-scraping measures. Treat successful downloads as authentic media; treat failures as tooling/rate-limit issues, not evidence about the account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instalooter |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
