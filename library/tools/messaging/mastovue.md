---
id: mastovue
name: MastoVue
description: Use when you have a hashtag or topic and want to browse matching Mastodon accounts/posts across the fediverse without an account — returns `social-profile`, `username`.
url: https://mastovue.glitch.me/#/
category: messaging
path:
- messaging
bestFor: Discovering Mastodon accounts and posts by hashtag/interest across fediverse instances.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free browser-based viewer; no account or login required.
opsec: passive
opsecNote: It reads public Mastodon timelines/hashtags via public APIs, so browsing is passive and anonymous. You are not logged in, so nothing ties the viewing to you — but the instances you query see the requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small community-built viewer hosted on Glitch; it surfaces authentic public Mastodon data but is a hobby tool that could go offline.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fedifinder
aliases:
- Masto Vue
tags:
- Social Media
- Mastodon
- fediverse
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# MastoVue

> A no-login browser viewer for Mastodon — search a hashtag or interest and browse matching accounts and posts across the fediverse.

## When to use
Your subject may be active on Mastodon / the fediverse (common among tech, infosec, activist, and privacy-minded communities), and you want to explore by hashtag or topic without creating an account or being tied to one instance. MastoVue reads public timelines and hashtag feeds, so you can find accounts posting on a given subject, then pivot to a specific `username`. It's a discovery/browsing aid for a decentralized network where there's no single search box; low general relevance but useful when the subject fits the fediverse demographic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mastovue.glitch.me/#/.
2. Enter a hashtag, an instance, or an account of interest to load its public feed.
3. Browse the matching posts/accounts; note handles in the `user@instance` form.
4. Read the output: candidate `social-profile`s and `username`s posting on your topic.
5. Pivot: take a `user@instance` handle to that account's profile directly, and reuse the username on cross-platform username tools and `[[fedifinder]]` to bridge to other networks.

## Inputs → Outputs
- **In:** `username`, hashtag, or instance/topic
- **Out:** `social-profile` (Mastodon accounts), `username` (fediverse handles)
- **Empty/negative result looks like:** no posts/accounts for the hashtag or the instance not loading — the topic is quiet on the queried instance or the tool/instance is down; try a different/larger instance.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and login-free; the queried instances see the requests but not your identity — still use a sock-puppet network setup for sensitive work.
- It's a Glitch-hosted hobby tool and the fediverse is fragmented — coverage depends on which instances federate; absence is not proof.

## Overlaps ("do both")
- Pairs with `[[fedifinder]]` and cross-platform username tools — MastoVue browses by topic/hashtag, fedifinder maps a known person's fediverse accounts, and username tools bridge to other networks. Do both to go from topic → account → cross-platform identity.

## Trust & verifiability
`trust: community` — a small community viewer over authentic public Mastodon APIs; the data is real, but confirm any account on its home instance and don't rely on the tool's continued uptime.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastovue |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
