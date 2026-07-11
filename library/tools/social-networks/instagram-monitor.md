---
id: instagram-monitor
name: instagram_monitor
description: Use when you have an Instagram `username` and want to watch it over time — returns real-time alerts on new posts/stories/reels, follower/following changes, and profile edits (`social-profile` + `image` capture).
url: https://github.com/misiektoja/instagram_monitor
category: social-networks
path:
- social-networks
bestFor: Continuously monitoring an Instagram account for new activity and profile changes, with media capture.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free and open-source (Python). No cost; optional features (stories, follower deltas) need you to import a logged-in browser session.
opsec: active
opsecNote: Basic tracking runs in a no-login mode (passive-ish); enabling stories/follower monitoring imports YOUR (ideally sock-puppet) Instagram session, which is ACTIVE — repeated polling and story views can be visible to the target (story view lists) and risk the account. Use a dedicated burner Instagram account, never your real one, and keep polling intervals sane.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source OSINT tool (misiektoja), part of a family of *_monitor tools, ~1k stars and frequent releases. It surfaces Instagram's own data; reliability tracks Instagram's anti-automation measures.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- instagram-com
- osintgram
aliases:
- instagram_monitor
- misiektoja instagram monitor
tags:
- instagram
- monitoring
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# instagram_monitor

> A self-hosted watcher for a single Instagram account: it polls the profile and pings you (email, Discord/webhook) the moment there's a new post, story, follower change, or bio edit — and archives the media.

## When to use
You have a subject's Instagram `username` and need to know about their activity *as it happens* rather than checking manually — new posts/reels/stories, changes in who they follow or who follows them (surfacing `associate`s), profile-picture swaps, and public/private visibility flips. Ideal for a live missing-person watch or building a timeline of a subject's Instagram behaviour, with stories/posts captured before they disappear.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/misiektoja/instagram_monitor and install its Python requirements.
2. Configure the target `username` and your alert channels (email, Discord webhook).
3. For basic public tracking, run in no-login mode; for stories and follower/following deltas, import a **sock-puppet** browser session (Firefox/Chrome/Brave/Chromium).
4. Run the monitor; watch the live CLI/local web UI and receive alerts (with attached media) on each change.
5. Pivot: new followers/followees feed `associate` mapping; captured `image`s feed reverse-image/face search; correlate posting times with `geolocation`/routine.

## Inputs → Outputs
- **In:** Instagram `username` (one account per monitor)
- **Out:** real-time change alerts → new posts/stories/reels, follower/following deltas (`associate`), profile edits, and archived `image` media; CSV logs
- **Empty/negative result looks like:** no alerts firing, or auth/scrape errors — the account may be inactive, went private beyond your access, or Instagram is blocking the session. A silent monitor isn't proof of no activity; check it's still authenticated.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** for the richer features — set up the sock puppet in advance.
- OpSec: **active** once logged in. Viewing stories adds you to the target's story-viewer list; aggressive polling gets accounts rate-limited or banned. Use a burner identity, conservative intervals, and never your real account.
- Instagram actively fights automation; expect breakage and keep the tool updated.

## Overlaps ("do both")
- Pairs with `[[instagram-com]]` (manual review for depth) and `[[osintgram]]` (one-shot enumeration of followers/tags/locations) — instagram_monitor is the *ongoing watch*, Osintgram the *snapshot*, manual browsing the *qualitative read*. Use the monitor to catch changes, the others to analyse a moment in time.

## Trust & verifiability
`trust: community` — an actively maintained, popular open-source tool that reports Instagram's own data. Its completeness depends on session access and Instagram's defences, so treat gaps as access artefacts and verify captured media/changes on-platform when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-monitor |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
