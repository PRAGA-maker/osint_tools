---
id: vk-watch
name: VK.watch
description: Use when you have a VKontakte `social-profile`/`username` and want the profile's change history — former names, deleted avatars, added/removed friends and groups — returns historical `social-profile` snapshots plus `associate` links.
url: https://vk.watch/
category: social-networks
path:
- social-networks
bestFor: Reconstructing how a VKontakte profile looked in the past — prior display names, deleted avatars, and friends/groups later hidden or removed.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- name
- image
- associate
status: live
pricing: freemium
costNote: Free tier is the @VKHistoryRobot Telegram bot, which returns basic historical dumps (old profile page, avatars, bio) for a VK ID. Continuous monitoring and deeper friend/group change history on vk.watch itself require a paid subscription.
opsec: passive
opsecNote: You query a third-party archive, not VK, so the target is not notified and nothing touches their account. Risk is that you hand the target's VK ID to a Russian-operated service — use a sock-puppet Telegram account for the bot and keep operationally sensitive selectors off it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Widely cited in VK-OSINT tradecraft guides. Independent third party, not affiliated with VK; historical depth depends on when VK.watch first crawled the target.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- vk.watch
- VKHistoryRobot
tags:
- vkontakte
- profile-history
- social-media
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# VK.watch

> A VKontakte profile-history archive: what this account used to be called, which avatars it deleted, and who it used to be friends with.

## When to use
You have a VKontakte `social-profile` or numeric VK ID and the current page is thin, cleaned-up, or recently edited. VK.watch reconstructs the past: a former display name can re-open a stalled search, a deleted avatar feeds reverse-image/face search, and friends or groups later removed can surface `associate` links the subject tried to bury. Especially valuable in Russian/Eastern-European missing-person and identity cases where the live profile has been sanitized.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get the target's VK ID or profile URL (e.g. `vk.com/id12345` or a vanity name).
2. Free path: in Telegram, message `@VKHistoryRobot` with the VK ID/username; it returns archived dumps — old profile page, previous avatars, bio snapshots dating back years.
3. Full path: open https://vk.watch/, register, submit the profile to see continuous change history (name changes, friend adds/removes, group joins/leaves) and to put it under ongoing monitoring.
4. Read the output: each snapshot is a point-in-time copy — compare consecutive snapshots to see what changed and when.
5. Pivot: old avatars → reverse image / face search; former display names → re-run name searches; removed friends → `associate` mapping.

## Inputs → Outputs
- **In:** `social-profile` / `username` (VK ID or vanity URL)
- **Out:** historical `social-profile` snapshots, previous `name`(s), old avatar `image`s, added/removed friends and groups (`associate`)
- **Empty/negative result looks like:** "no history for this ID" — VK.watch only holds data from profiles it began crawling; never-indexed accounts return nothing, which is not proof the account is new.

## Gotchas & OpSec
- Human-in-the-loop: the paid site needs an account; the free bot needs a Telegram account — use a sock puppet for both.
- Coverage is retroactive only from VK.watch's first crawl of that profile; it cannot show changes it never captured.
- OpSec: **passive** toward the target (no alert), but you are trusting a Russian-run third party with the ID you are investigating — keep sensitive context off it.

## Overlaps ("do both")
- Pairs with `[[search4faces]]` and other VK reverse-face tools — VK.watch supplies the *old* avatars and names those searches then resolve against current accounts.

## Trust & verifiability
`trust: community` — heavily referenced in VK OSINT guides, but it is an unofficial archive; treat each snapshot as a lead to corroborate, and remember gaps in history are gaps in *their* crawl, not proof of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk-watch |
