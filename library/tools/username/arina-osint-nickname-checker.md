---
id: arina-osint-nickname-checker
name: Arina OSINT nickname checker
description: Use when you have a `username`/nickname and want to enumerate matching accounts across 40+ platforms — returns candidate `social-profile` links to check.
url: https://github.com/AlexC-ux/Arina-OSINT-nickname-checker-
category: username
path:
- username
bestFor: Checking one nickname across 40+ sites (GitHub, VK, Telegram, Reddit, TikTok, Steam, etc.) to find associated accounts.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open source (MIT). Requires the .NET Core 3.1 runtime; pre-built binaries are on the releases page or you can compile the C# source.
opsec: passive
opsecNote: The tool sends requests to each platform from YOUR IP to test whether the username exists — passive toward the subject, but it fans out many outbound requests. Run behind a VPN if you don't want those checks tied to you, and treat hits as unconfirmed until you open them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community project (~22 stars, MIT, last release v2.3 in 2022) by AlexC-ux; low adoption and unmaintained-leaning, so expect some site checks to be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- arina
tags:
- username
- nickname
- account-discovery
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# Arina OSINT nickname checker

> A small C#/.NET username enumerator: feed it a nickname, it probes 40+ platforms for that handle and reports where it exists.

## When to use
You have a `username`/nickname (from an email prefix, a chat handle, a gamertag) and want a fast first sweep of where else that exact handle appears — GitHub, VKontakte, Pinterest, YouTube, Telegram, Facebook, Reddit, Twitch, TikTok, Spotify, Steam, Wikipedia, and more. Use it to seed a username investigation, then verify and enrich the hits by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install the .NET Core 3.1 runtime.
2. Grab a pre-built binary from the GitHub releases page, or `git clone` and compile the C# source.
3. Run the tool and supply the target `username`/nickname when prompted.
4. Read the output: a list of platforms where the handle resolves to an account, with links.
5. Open each hit — confirm it's the same person (avatar, bio, activity), then pivot: `social-profile` → posts, `associate`s, a real `name`, or a linked `email`.

## Inputs → Outputs
- **In:** `username` / nickname
- **Out:** candidate `social-profile` URLs across 40+ sites for that handle
- **Empty/negative result looks like:** few or no hits — either the handle is rare, or (given the project's age) some site checks have broken and silently miss real accounts. Cross-check with a more actively maintained enumerator before concluding absence.

## Gotchas & OpSec
- Username checkers throw false positives (parked/placeholder pages) and false negatives (broken checks). Never treat a raw hit as identity — open and confirm.
- It queries many sites from your IP; use a VPN/sock IP to avoid attributing the sweep to you.
- Low-maintenance project (last release 2022): expect some platforms' detection logic to be outdated. Corroborate with a current tool.

## Overlaps ("do both")
- Do both with a mainstream, actively maintained enumerator (Sherlock/Maigret-class tools). Run several — each covers a different site list and detection method, so together they catch accounts any single checker misses.

## Trust & verifiability
`trust: community` — open-source and inspectable, but small and aging; reliability of individual site checks varies, so use it as one input among several rather than an authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arina-osint-nickname-checker |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
