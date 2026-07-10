---
id: twitch-tools-rootonline-de
name: twitch-tools.rootonline.de
description: Use when you have a Twitch `username` and want to enumerate its followers — returns the follower list with follow dates and account-age filters, exposing associated accounts.
url: https://twitch-tools.rootonline.de/followerlist_viewer.php
category: social-networks
path:
- social-networks
bestFor: Pulling and filtering the follower list of any Twitch channel to find associated accounts and follow timing.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free web tool; an optional sign-up/verification adds benefits but the follower viewer is usable without it.
opsec: passive
opsecNote: The tool queries Twitch's public follower data server-side — you do not follow, message, or otherwise touch the target channel, so no notification reaches it. You disclose the channel name to a third-party site; use a sock-puppet browser. Large channels' follower lists may be truncated or rate-limited by Twitch.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist third-party Twitch utility (rootonline.de), not affiliated with Twitch; depends on Twitch's public API and can break or truncate when Twitch changes access.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Twitch follower list viewer
- twitch-tools rootonline
tags:
- twitch
- Twitch Related Sites
- follower-enumeration
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# twitch-tools.rootonline.de

> A Twitch follower-list viewer: enumerate who follows a channel, filter by follow date and account age, and surface associated accounts.

## When to use
You have a Twitch `username`/channel and want to map its social orbit — who follows it, when they followed, and which follower accounts are freshly created (a signal for alts/sockpuppets or coordinated activity). Follower enumeration turns one Twitch identity into a list of associated accounts (`associate`s) to investigate, and the follow-date/account-age filters help spot the interesting ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twitch-tools.rootonline.de/followerlist_viewer.php in a sock-puppet browser.
2. Enter the target Twitch channel `username`.
3. Load the follower list and apply filters: follow date, account creation date, the gap between account creation and following, or username substring.
4. Read the results: follower usernames (`social-profile` links to their Twitch), with the timing metadata. Sort to find accounts created just before following (possible alts) or long-time followers (likely genuine associates).
5. Pivot: each follower username feeds `[[user-searcher]]` and cross-platform username tools; follow-timing clusters can indicate a linked network.

## Inputs → Outputs
- **In:** Twitch channel `username`
- **Out:** follower list (`social-profile`/`associate` usernames) with follow dates and account-creation dates
- **Empty/negative result looks like:** empty list, error, or an obviously truncated result — the channel has no/hidden followers, the name is wrong, or Twitch is rate-limiting/capping large lists. Absence is not proof of no followers.

## Gotchas & OpSec
- Large channels: follower lists can be huge and Twitch may truncate or throttle; expect partial data on popular streamers.
- Third-party reliability: it rides Twitch's public API and can break when Twitch changes access — treat failures as tool-side.
- OpSec: **passive** — no follow/message is sent to the target; still use a sock puppet since you query a third-party site.

## Overlaps ("do both")
- Pairs with `[[user-searcher]]` and other username tools — this produces the follower usernames; those resolve each username across other platforms. Do both to turn a Twitch follower list into cross-platform identities.

## Trust & verifiability
`trust: unverified` — an independent hobbyist utility, not Twitch. The follower data originates from Twitch's public API (reliable when it loads), but coverage can be truncated and the tool can break, so corroborate key accounts directly on Twitch.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-tools-rootonline-de |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
