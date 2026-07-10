---
id: soig
name: SoIG
description: Use when you have an Instagram `username` and want profile metadata, hashtags, and post details beyond what the profile page shows — returns social-profile data, geolocation from posts, and image URLs.
url: https://github.com/yezz123/SoIG
category: social-networks
path:
- social-networks
bestFor: Pulling structured Instagram profile + post metadata (locations, hashtags, captions) for one username.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- image
- metadata-exif
status: degraded
pricing: free
costNote: Free, open-source Python tool on GitHub. No account or key to install.
opsec: active
opsecNote: The tool queries Instagram's endpoints for the target profile; scraping without login is rate-limited and may require a session cookie, which ties activity to whatever account you supply. Use a sock-puppet Instagram account and residential/proxy IP, never your real one.
humanInLoop: true
humanInLoopReason:
- rate-limit
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source by GitHub user yezz123. Small project (~41 commits); Instagram's frequent API/anti-scraping changes mean parts may break without notice.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- instaloader
- toutatis
aliases:
- yezz123/SoIG
tags:
- instagram
- social-media-scraper
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# SoIG

> A command-line Instagram OSINT scraper that pulls a target's profile stats, most-used hashtags, and per-post metadata (captions, locations, timestamps, image URLs).

## When to use
You have a subject's Instagram `username` and need more than the profile page shows: follower/following counts, bio, business/verification flags, the hashtags they reuse, and post-level details including tagged **locations** and timestamps. Post locations are the highest-value output for a missing-person case — they place the subject at real geolocations.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/yezz123/SoIG` (needs Python 3, Linux).
2. Create a virtualenv and `pip install -r requirements.txt`.
3. Run `python3 main.py -u <username>` for profile data; add `-p` to scrape posts, `-t` for all hashtags, `-s` to save output to files.
4. Read the output: profile block (counts, bio, flags), then per-post captions/locations/timestamps/image URLs.
5. Pivot: post `geolocation` feeds map/geo analysis; image URLs feed reverse-image and EXIF tools; hashtags reveal communities and alternate handles.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** `social-profile` (bio, counts, flags), `geolocation` (post locations), `image` URLs, post metadata
- **Empty/negative result looks like:** private accounts return only the public header (no posts); a hard error usually means Instagram blocked the request or the scraping path broke — not that the account is empty.

## Gotchas & OpSec
- Human-in-the-loop: Instagram rate-limits and may demand a logged-in session; expect to supply a sock-puppet account cookie and to pace requests.
- OpSec: **active** — requests go to Instagram tied to your IP/session. Never use your real account.
- Fragility: Instagram changes break scrapers constantly; cross-check anything critical against `[[instaloader]]`.

## Overlaps ("do both")
- Pairs with `[[instaloader]]` — a more actively maintained Instagram scraper; run both since one often works when the other breaks.
- Pairs with `[[toutatis]]` — Toutatis extracts obfuscated email/phone tied to an IG account, complementing SoIG's post/location harvest.

## Trust & verifiability
`trust: community` — open source and inspectable, but a small unmaintained project against a hostile, fast-changing target; verify outputs before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soig |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit, account-login) |
