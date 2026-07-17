---
id: invidious-instances
name: Invidious Instances
description: Use when you have a YouTube `social-profile`/video and want to view it privately without an account — returns the same `social-profile` content via a tracker-free proxy.
url: https://docs.invidious.io/instances/
category: social-networks
path:
- social-networks
bestFor: Watching and downloading YouTube content anonymously (no Google account, no tracking) through an open-source proxy front-end.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open source; a community-maintained list of public instances (you can also self-host).
opsec: passive
opsecNote: An Invidious instance fetches YouTube on your behalf, so Google sees the instance rather than your IP/account — useful for viewing a subject's channel/videos without leaving a Google-side footprint. Note the instance operator can see your requests; prefer a reputable instance or self-host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable open-source project, but public instances come and go and are sometimes rate-limited/blocked by YouTube; verify an instance works before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Invidious
- invidious.io
tags:
- youtube
- privacy-frontend
- opsec
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Invidious Instances

> An open-source, privacy-respecting front-end to YouTube: view a subject's channel and videos through a proxy instance so Google never ties the viewing to your IP or a logged-in account.

## When to use
You need to watch, browse or download a subject's YouTube content — channel, videos, comments — without signing in and without Google logging your interest against your account/IP. Invidious proxies YouTube through community-run (or self-hosted) instances that strip tracking. The docs page is the maintained directory of currently-working public instances. Reach for it whenever your YouTube OSINT should leave no Google-side footprint tied to you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://docs.invidious.io/instances/ for the current list of public instances and their health/uptime.
2. Pick a healthy instance; open the target channel/video by replacing `youtube.com` with the instance domain, or search within it.
3. Watch/browse the same `social-profile` content (videos, channel, comments) tracker-free; many instances allow direct video/audio download.
4. If an instance is down or rate-limited (common), switch to another from the list — or self-host for reliability.
5. Pivot: combine with `[[youtube-video-upload-time]]` for exact timestamps and thumbnail reverse-search to find original uploads.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube channel/video URL)
- **Out:** the same `social-profile` content (video, channel info, comments) via a private proxy; often downloadable
- **Empty/negative result looks like:** an instance that errors, is rate-limited, or shows "video unavailable" — usually YouTube blocking that instance, not the content being gone. Try another instance or self-host.

## Gotchas & OpSec
- OpSec: **passive** for the target — the instance masks you from Google. But the **instance operator** sees your requests; prefer a trusted instance or run your own.
- Public instances are volatile — YouTube actively blocks them, so uptime is inconsistent (hence `status: degraded`). Always check the list is current.
- Self-hosting gives the strongest privacy and reliability.

## Overlaps ("do both")
- Pairs with `[[youtube-video-upload-time]]` and `[[youtube-comments-downloader]]` — Invidious is the low-footprint viewing layer; those extract timestamps and comment data.

## Trust & verifiability
`trust: community` — a respected open-source project; content is genuine YouTube served through a proxy, so verify anything decisive against the source and re-check that your chosen instance is live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | invidious-instances |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
