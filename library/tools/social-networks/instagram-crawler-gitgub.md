---
id: instagram-crawler-gitgub
name: instagram-crawler (hehpollon)
description: Use when you have an Instagram `username` (or hashtag) and want to bulk-download that account's posts, captions, comments and timestamps for offline analysis — returns image, social-profile, and associate leads.
url: https://github.com/hehpollon/instagram-crawler
category: social-networks
path:
- social-networks
bestFor: Bulk-scraping a public Instagram account's or hashtag's posts, images, captions, and commenters to a local folder for offline review.
selectorsIn:
- username
selectorsOut:
- image
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open-source (Python); no fees. Cost is operational — Instagram's anti-scraping measures increasingly break unauthenticated crawlers.
opsec: passive
opsecNote: You never contact the target, but the tool repeatedly hits Instagram from your IP. Instagram may rate-limit or block that IP/account. Run from a sock-puppet context and a disposable IP; never point it from an account or address tied to your identity.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: unverified
trustNote: Small third-party GitHub project (~86 stars), not widely audited and lightly maintained; verify the code before running and expect breakage as Instagram changes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- instaloader
- osintgram
aliases:
- instagram-crawler
- hehpollon instagram crawler
tags:
- instagram
- open-source
- cli
- scraper
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# instagram-crawler (hehpollon)

> A Python command-line Instagram scraper that pulls a public account's or hashtag's posts — images, captions, comments, timestamps — into a local `./data` folder without the official API.

## When to use
You have a public Instagram `username` (or a hashtag) and want a preserved offline copy of everything that account has posted — the images themselves, caption text, the list of commenters (`associate` leads), and post dates — before the account is deleted or locked. Best when you need bulk capture rather than one-off browsing.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/hehpollon/instagram-crawler` and install its Python requirements.
2. Run against a handle: `python3 crawl.py -q '<username>' -n 100` (or a hashtag with `-q '#tag'`). `-n` sets the post count (default 10,000); add the comments flag to also collect comment text.
3. Output lands in `./data`: downloaded post images plus metadata files with likes, comment counts, captions, comment text, and post dates.
4. Review offline: captions/comments for location and relationship leads; commenter handles as `associate` pivots.
5. Pivot: feed images into reverse-image/face tools and commenter handles into a username search.

## Inputs → Outputs
- **In:** `username` (or hashtag)
- **Out:** `image` (downloaded posts), `social-profile` (the account's public data), `associate` (commenter handles), captions, timestamps
- **Empty/negative result looks like:** an empty `./data`, an immediate block/redirect, or a login wall — Instagram is refusing the unauthenticated scrape, not proof the account is empty.

## Gotchas & OpSec
- **Degraded:** Instagram has aggressively hardened against unauthenticated scraping; expect this to partially or fully break and require code tweaks or a logged-in session.
- Human-in-the-loop: watch for rate-limiting/blocks — throttle `-n`, rotate IPs, and use a burner account/context.
- Third-party code — read it before running; do not run it against a target from an identity-linked machine or account.

## Overlaps ("do both")
- Pairs with `[[instaloader]]` — a far more maintained Instagram scraper; if this crawler breaks, Instaloader is the fallback for the same capture goal. `[[osintgram]]` adds analysis (followers, tagged locations) on top of raw capture.

## Trust & verifiability
`trust: unverified` — a small, lightly-maintained community repo. The approach is sound but the specific tool is not audited; validate output against the live profile and prefer a maintained alternative for anything operational.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-crawler-gitgub |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
