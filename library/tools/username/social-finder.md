---
id: social-finder
name: Social Finder
description: Use when you have a `username`/`name` and want to check an opt-in directory where people self-publish all their handles — returns a person's linked social profiles when they've claimed a page.
url: https://socialfinder.app
category: username
path:
- username
bestFor: Finding a person's cluster of self-declared social handles via an opt-in directory (only works if the subject published a profile).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free; users create one profile listing all their handles. No account needed to browse.
opsec: passive
opsecNote: Browsing is passive and notifies no one. Because entries are self-published, a hit reflects what the subject chose to reveal — reliable as their own declaration, but coverage is small since it only contains people who opted in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small opt-in social-directory service; data is self-reported by users, so it is honest-but-partial — useful when present, absent for most targets.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- socialfinder.app
tags:
- username-search
- multi-platform
- opt-in-directory
source: osintambition-social
lastVerified: '2026-07-11'
enrichment: full
---

# Social Finder

> An opt-in directory where people publish all their social handles on one page — a jackpot when your subject has claimed a profile, empty for everyone who hasn't.

## When to use
You have a `username` or `name` and want to see if the subject has voluntarily linked their accounts together. Unlike a username *hunter* (which probes every platform for a handle), Social Finder is a directory of self-published profiles: users claim a page and list their Telegram, Discord, gaming, creator and other handles, plus their intent (friends/dating/networking). Reach for it as a quick, high-value check — but expect it to be empty for most targets, since only opted-in people appear.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://socialfinder.app.
2. Search/browse for the `username` or `name`, or browse by platform/interest/intent.
3. If the subject has a claimed page, read the full list of handles they've published.
4. Treat the handles as the subject's own declaration — then verify each on its native platform.
5. Pivot: each declared handle feeds platform-specific tools and `[[sherlock]]`-style hunts for handles they *didn't* declare.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** a self-published set of linked `social-profile`s / `username`s (only if the subject opted in)
- **Empty/negative result looks like:** no profile — the overwhelmingly common case; absence means the person simply hasn't used the directory, NOT that they lack social accounts.

## Gotchas & OpSec
- Opt-in only: tiny coverage — this finds people who chose to be found, so it's a bonus check, not a primary tool.
- Self-reported: handles are as accurate (or as curated/misleading) as the subject made them; verify each.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`-style username hunters — Social Finder shows declared handles; hunters probe for undeclared ones across platforms.
- Pairs with `[[commentpicker-com]]`/`[[toutatis]]` once a real handle is confirmed, to resolve IDs and hidden data.

## Trust & verifiability
`trust: community` — a small self-reported directory; a present profile is a reliable statement of the subject's own handles, but the near-total absence of most people limits it to an opportunistic check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-finder |
