---
id: instaloader-2
name: Instaloader
description: Use when you have an Instagram `username` and want to bulk-download that profile's posts, captions, geotags and metadata for offline analysis — returns image, geolocation, metadata-exif and social-profile data.
url: https://pypi.org/project/instaloader/
category: social-networks
path:
- social-networks
bestFor: Archiving an Instagram profile's public posts, stories, captions, comments and geotags locally via a Python CLI/library.
selectorsIn:
- username
selectorsOut:
- image
- geolocation
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT); install via pip. No paid tier or API key.
opsec: active
opsecNote: Instaloader hits Instagram's servers from your IP. Anonymous scraping of public profiles is possible but rate-limited and can trip anti-bot blocks; logging in with an account (needed for private profiles/stories) ties the scraping to that account and risks temporary or permanent bans and, for private targets, notifying them via a follow. Use a dedicated sock-puppet Instagram account and a throwaway IP, and throttle requests.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Popular, actively maintained open-source project with a large user base and public source on GitHub; unofficial and not endorsed by Instagram/Meta.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- instaloader
- instaloader python
tags:
- instagram
- scraper
- downloader
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Instaloader

> A command-line/Python tool that downloads an Instagram profile's posts, stories, captions, comments, geotags and metadata to disk — turning a live account into an offline, searchable evidence set.

## When to use
You have a target Instagram `username` and need more than a browser tab: a durable local archive you can grep, hash, and re-analyse, complete with post `metadata`, captions, comment threads, and geotags (`geolocation`). Ideal for preserving content before it's deleted, for building a timeline from post dates, and for extracting location tags that place the subject somewhere at a time. Login enables private profiles and stories; public profiles can be pulled anonymously.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install instaloader`.
2. Download a public profile: `instaloader profile <username>` — this pulls posts, images/videos, captions, comments, geotags and the profile picture into a `<username>/` folder.
3. For private profiles or stories, log in with a **sock-puppet** account: `instaloader --login=<puppet> profile <username>` (a session cookie is cached for reuse).
4. Update an existing archive incrementally with `--fast-update`.
5. Analyse locally: read `.json.xz` metadata for timestamps and geotags (`geolocation`), inspect media, and mine captions/comments for `associate` handles.
6. Pivot: geotags feed mapping/geolocation work; tagged/commenting handles feed further profile enumeration.

## Inputs → Outputs
- **In:** Instagram `username` (public; or private with an authorised puppet login)
- **Out:** `image` (photos/videos + profile pic), `geolocation` (post geotags), `metadata` (timestamps, captions, comments, likes counts), `social-profile` (the target's Instagram identity + tagged accounts)
- **Empty/negative result looks like:** a private profile you can't access without following, a 401/403, or a rate-limit/`Too Many Requests` block — none of which mean the profile is empty.

## Gotchas & OpSec
- **Ban risk:** aggressive scraping, especially while logged in, can get the account (and IP) rate-limited or banned. Throttle, and never use your real Instagram account.
- Instagram frequently changes internal endpoints; keep Instaloader updated (`pip install -U instaloader`) or expect breakage.
- Following a private target to gain access is an **active** step that alerts them — weigh before doing it.
- OpSec: this touches Instagram directly from your IP; use a puppet account + clean IP and keep request rates low.

## Overlaps ("do both")
- Pairs with Instagram viewer/anonymous-frontend tools for quick single-post checks, and with EXIF/metadata tools for downloaded media — Instaloader gives you the bulk archive; those give you fast look-ups and deeper per-image analysis.

## Trust & verifiability
`trust: community` — mature, widely used open-source project with transparent source; unofficial, so its behaviour depends on Instagram's ever-changing platform. Verify extracted geotags/timestamps against the live post when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instaloader-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, geolocation, metadata-exif, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (account-login) |
