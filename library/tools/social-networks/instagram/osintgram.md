---
id: osintgram
name: Osintgram
description: Use when you have an Instagram `username` and want to bulk-extract a public account's posts, followers, tagged users and metadata — returns social-profile intelligence and associate lists.
url: https://github.com/Datalux/Osintgram
category: social-networks
path:
- social-networks
- instagram
bestFor: Interactive CLI reconnaissance of a single public Instagram account (posts, captions, comments, followers/following, tagged users).
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- image
- metadata-exif
status: degraded
pricing: free
costNote: Free and open-source (GPL-3.0). Requires either a real Instagram login or a HikerAPI token (first 100 requests free) to authenticate against Instagram.
opsec: active
opsecNote: Every command hits Instagram's private endpoints while authenticated. Instagram rate-limits and can flag or ban the account you log in with, and the target may not be notified but Instagram sees the traffic. Use a burner/sock-puppet Instagram account and a clean IP, never your own login.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Well-known community project (Datalux) with thousands of GitHub stars; last stable release v1.3 (May 2021) with a v2 beta branch, so expect breakage as Instagram changes its API.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools:
- instaloader-3
- instagram-search-engine
aliases:
- Datalux/Osintgram
tags:
- instagram
- cli
- social-media
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Osintgram

> A local Python CLI that logs into Instagram and interactively dumps a public target account's posts, network and metadata — reconnaissance-in-a-shell for a single handle.

## When to use
You have an Instagram `username` (or the numeric ID) for a public account and want more than the web UI shows: full follower/following lists, everyone who tagged or was tagged, comment authors, captions, hashtags, and downloadable media/profile pics. It is the right tool when you need structured, exportable output for one account rather than a broad cross-platform sweep.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/Datalux/Osintgram && cd Osintgram`, create a venv, `pip install -r requirements.txt` (or use the provided Docker image).
2. Put a **sock-puppet** Instagram login (or a HikerAPI token) in `config/credentials.ini` — never your own account.
3. Run `python3 main.py <target_username>` to enter the interactive shell, or `python3 main.py <target_username> --command <cmd>` for one-shot.
4. Useful commands: `followers`, `followings`, `tagged`, `wtagged` (who tagged target), `photos`, `captions`, `comments`, `info`, `propic`. Output lands in the `output/` folder.
5. Pivot: feed extracted follower/tag `associate` handles into username tooling, and run downloaded `image` files through reverse-image and EXIF checks.

## Inputs → Outputs
- **In:** `username` (public account)
- **Out:** `social-profile` detail, `associate` lists (followers/following/taggers), `image` media, and `metadata-exif` from posts/captions
- **Empty/negative result looks like:** login challenge/checkpoint, `429`/rate-limit errors, or empty lists for a private account — none of which mean the target has no data, only that access was blocked.

## Gotchas & OpSec
- Human-in-the-loop: Instagram frequently throws login checkpoints/2FA; you must clear them manually, and heavy use gets the sock account rate-limited or banned.
- OpSec: **active** — you are an authenticated client hitting Instagram's private API. Isolate the burner account and IP; assume Instagram logs the reconnaissance.
- Maintenance: last stable release is 2021; commands break as Instagram shifts. If it fails, fall back to `[[instaloader-3]]`.

## Overlaps ("do both")
- Pairs with `[[instaloader-3]]` — Instaloader is more robust for bulk media/metadata download, while Osintgram's shell is faster for network/tag pivots. Run both when one breaks against Instagram's current API.
- `[[instagram-search-engine]]` helps you *find* the handle before Osintgram enriches it.

## Trust & verifiability
`trust: community` — a widely used, open-source project, but not first-party; verify anything critical against the live Instagram page, since scraped counts can lag or error.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintgram |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
</content>
