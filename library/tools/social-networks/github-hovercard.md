---
id: github-hovercard
name: GitHub Hovercard
description: Use when you're triaging GitHub `username`s/repos and want at-a-glance detail — hovering shows the user's or repo's key info without opening each page.
url: https://chromewebstore.google.com/detail/github-hovercard/mmoahbbnojgkclgceahhakhnccimnplk
category: social-networks
path:
- social-networks
bestFor: Previewing GitHub user and repo details on hover to speed up scanning search results and contributor lists.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free browser extension (Chrome/Firefox); open-source.
opsec: passive
opsecNote: It reads GitHub's public data via GitHub's API to render previews — you're already browsing GitHub, and hovering doesn't notify anyone. The extension needs permissions on github.com; install it in your investigation browser/profile, not a personal one, and be aware it uses GitHub API calls tied to your session/IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A popular open-source extension; it surfaces genuine GitHub API data, so previews are accurate — the trust caveat is granting a browser extension access to github.com, so use a reputable build.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- GitHub Hovercard extension
tags:
- github
- browser-extension
- productivity
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# GitHub Hovercard

> A browser extension that pops a detail card when you hover over any GitHub user or repo link — the same public info, without a click, so scanning contributors and search results is far faster.

## When to use
You're doing GitHub OSINT — vetting a `username`, scanning a repo's contributors, or wading through search results — and want the key facts (a user's join date, bio, location, followers, top repos; or a repo's stars, language, README snippet) without opening each page in turn. It's a productivity multiplier for GitHub reconnaissance, not a data source of its own.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install GitHub Hovercard from the Chrome Web Store (or Firefox add-ons) into your investigation browser profile.
2. Browse GitHub as normal — search users/repos, open a contributors list, read an issue thread.
3. Hover over any user or repo link; read the popup card: user bio/location/followers/join date, or repo stats/description.
4. Pivot: a user's stated location/bio/linked site becomes a new selector; contributor cards quickly reveal `associate`s (co-committers) worth mapping.

## Inputs → Outputs
- **In:** GitHub `username`/repo links you hover over (while browsing GitHub)
- **Out:** an inline preview of the user's `social-profile` (bio, location, followers, repos) or repo details
- **Empty/negative result looks like:** a sparse card — the user filled in little public info, or the profile is an org/bot; the extension only shows what GitHub's API exposes publicly.

## Gotchas & OpSec
- It **adds no new data** — everything shown is public GitHub API data; it just saves clicks. Don't treat it as a separate intelligence source.
- A browser extension gets access to your GitHub browsing; install a reputable build in a dedicated investigation profile.
- Heavy hovering makes many GitHub API calls; occasional rate-limiting can blank the cards.
- OpSec: passive — public data, no notifications.

## Overlaps ("do both")
- Pairs with GitHub user/commit OSINT tools and the GitHub API directly — Hovercard speeds *manual* triage; scripted tools do bulk extraction (emails from commits, repo history) it doesn't.

## Trust & verifiability
`trust: community` — a well-used open-source extension surfacing authentic GitHub API data, so previews are accurate. The only caution is the general one about granting extensions access to a site; the underlying facts are GitHub's own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-hovercard |
