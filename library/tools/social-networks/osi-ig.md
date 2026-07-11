---
id: osi-ig
name: osi.ig
description: Use when you have an Instagram `username` and want to pull the profile's public data — user ID, name, bio, counts, profile photo, and any email/locations in posts — returns name, social-profile, image and email.
url: https://github.com/th3unkn0n/osi.ig
category: social-networks
path:
- social-networks
bestFor: Command-line extraction of an Instagram profile's public metadata and post details.
selectorsIn:
- username
selectorsOut:
- name
- social-profile
- image
- email
status: degraded
pricing: free
costNote: Free, open-source Python CLI. No paid tier, but it now needs a working Instagram session to function.
opsec: active
opsecNote: To work it authenticates with an Instagram account and hits Instagram's endpoints programmatically — Instagram detects automation and may challenge or ban the account used. Use a dedicated sock-puppet Instagram account, never your real one. Fetching public profile data does not directly notify the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source Instagram OSINT script (th3unkn0n); its reliability tracks Instagram's frequent API changes, so verify it still runs before depending on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- osi.ig
- osintgram-style ig tool
tags:
- instagram
- open-source
- cli
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# osi.ig

> A Python CLI that dumps an Instagram profile's public data — IDs, counts, bio, avatar, and any emails/locations surfaced from posts — from just a username.

## When to use
You have an Instagram `username` and want its structured public data at the command line rather than clicking through the app: numeric user ID, full `name`, follower/following/post counts, external URL, profile-picture URL (`image`), and — from post scraping — hashtags, mentions, any `email` in the bio, and post captions/locations/timestamps. Good for quickly profiling an account and extracting pivots in bulk.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/th3unkn0n/osi.ig && cd osi.ig && pip install -r requirements.txt`.
2. Provide a **sock-puppet** Instagram login when prompted (required since Instagram stopped serving JSON to anonymous requests).
3. Run `python3 main.py -u <username>` for profile info, add `-p` to also pull post information (captions, locations, timestamps).
4. Read the output: user ID, name, counts, avatar URL, bio email/links, and post-derived data.
5. Pivot: the numeric ID feeds ID-based Instagram tools; the avatar feeds reverse-image/face; a bio email feeds email-OSINT; post locations feed geolocation.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** `name`, numeric user ID (`social-profile`), profile-pic `image`, `email` from bio, post locations/hashtags/mentions
- **Empty/negative result looks like:** errors or empty fields — usually Instagram blocking the request or the session being invalid; a private account returns only limited public fields.

## Gotchas & OpSec
- **Degraded:** Instagram changed how it responds to non-browser requests, so the tool now requires a logged-in session and breaks periodically. Check the repo before relying on it.
- **Active and account-risking:** the Instagram account you authenticate with can be challenged or banned — use a throwaway.
- Private accounts expose little regardless of the tool.

## Overlaps ("do both")
- Pairs with `[[instagram-user-id]]` (handle→ID resolution when you don't want to run a script) and reverse-image search on the pulled avatar — osi.ig bulk-extracts, those give quick single-value lookups.

## Trust & verifiability
`trust: community` — a well-known open-source script whose accuracy depends on Instagram's shifting endpoints. The data it returns is Instagram's own public data; the risk is breakage and the account you must use to run it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osi-ig |
| category | social-networks |
| selectorsIn → selectorsOut | username → name, social-profile, image, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
