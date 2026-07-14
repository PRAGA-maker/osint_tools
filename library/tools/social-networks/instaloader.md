---
id: instaloader
name: Instaloader
description: Use when you have an Instagram `username` and want to bulk-download their public posts, stories highlights, captions, and metadata — returns `image`s, `metadata-exif`/timestamps, and profile data for offline analysis.
url: https://github.com/instaloader/instaloader
category: social-networks
path:
- social-networks
bestFor: Archiving a public Instagram profile's media, captions, and metadata to a local folder for analysis.
selectorsIn:
- username
selectorsOut:
- image
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python). You run it yourself; no paid service.
opsec: active
opsecNote: Downloading hits Instagram's servers and is rate-limited; heavy use or logging in raises ban risk for the account/IP used. Prefer anonymous (no-login) mode where possible, run behind a proxy/sock-puppet, and throttle. Logging in with a sock-puppet is sometimes needed but ties requests to that account.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: trusted
trustNote: Long-established, widely used open-source Instagram tool with an active community; the data is straight from Instagram, though IG changes can require updates.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- instaloader.py
tags:
- instagram
- media-download
- python
- scraper
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Instaloader

> The standard open-source Instagram downloader — pull a public profile's photos, videos, captions, and metadata to disk so you can analyse a subject's activity offline and preserve it before it disappears.

## When to use
You have an Instagram `username` and need more than the web UI shows: a complete local archive of their public posts with captions, timestamps, likes/comments counts, tagged users, and any location tags — plus the profile picture and bio. Essential for timeline reconstruction, pattern-of-life, and evidence preservation (posts get deleted). Captions and timestamps frequently place a person in time and space; occasional geotags and tagged accounts surface locations and `associate`s.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install instaloader`.
2. Basic archive: `instaloader <username>` (downloads posts, captions as .txt/.json, profile pic).
3. Add `--no-login` where possible for anonymous mode; for more (stories/highlights) you may need `--login <sockpuppet>` — accept the added ban risk.
4. Throttle and use a proxy/sock-puppet IP to avoid rate-limit blocks; space out large jobs.
5. Analyse the JSON metadata (timestamps, tagged users, locations); pivot tagged accounts → their profiles, geotags → geolocation, faces/media → reverse-image.

## Inputs → Outputs
- **In:** `username`
- **Out:** `image`s/videos, captions, `metadata-exif`/timestamps, tagged users, location tags, `social-profile` (bio, counts, profile pic)
- **Empty/negative result looks like:** a private account (no public posts downloadable), an empty profile, or a rate-limit/login error — the last is a tool/access problem, not proof of inactivity.

## Gotchas & OpSec
- Rate-limiting and bans are real; logging in ties activity to that account and increases risk — use a disposable sock puppet and go slow.
- Private accounts require following (active, detectable) — usually out of scope for passive work.
- Instagram changes break scrapers periodically; keep Instaloader updated.

## Overlaps ("do both")
- Pairs with manual profile review (context/stories) and reverse-image/geolocation tools (this supplies the media/metadata they consume); check the Wayback Machine for deleted content.

## Trust & verifiability
`trust: trusted` — a mature, widely-audited open-source tool pulling data directly from Instagram; the media/metadata are authentic. Verify inferred locations/associations before treating them as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instaloader |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, metadata-exif, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
