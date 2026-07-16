---
id: twitch-tools-lolarchiver-com
name: twitch-tools.lolarchiver.com
description: Use when you have a Twitch `username` and want its historical name changes and account history — returns prior usernames and profile leads, though this endpoint has moved and now requires the LoLArchiver suite.
url: https://twitch-tools.lolarchiver.com/username_changelog
category: social-networks
path:
- social-networks
bestFor: Recovering a Twitch account's past username(s) to widen handle/identity pivots.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: degraded
pricing: freemium
costNote: LoLArchiver offers some free lookups but gates full history/results behind a paid subscription. The original `twitch-tools.lolarchiver.com/username_changelog` URL now returns HTTP 410 Gone / 301s to `t-tools.lolarchiver.com`; the username-changelog feature lives inside the current Twitch Tools suite there.
opsec: passive
opsecNote: Queries LoLArchiver's own archive, not Twitch's live API against the target, so it is passive toward the subject. Note this is a grey-area aggregator — use a sock-puppet account/browser and do not enter your own identifiers.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A niche, paid grey-area archive; data is scraped and not independently auditable, so confirm any prior-username claim before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- LoLArchiver Twitch Tools
- t-tools.lolarchiver.com
- Twitch username changelog
tags:
- twitch
- Twitch Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- osint-lolarchiver-com
- osint-lolarchiver-com-2
- twitter-lolarchiver-com
---

# twitch-tools.lolarchiver.com

> LoLArchiver's Twitch tools archive account changes — most usefully, the username changelog that recovers a streamer's past handles — now served from the `t-tools.lolarchiver.com` suite.

## When to use
You have a Twitch `username` and need its **history** — prior handles, username/broadcaster-type changes, and account traces — to reconnect a renamed account to older activity or to a wider identity graph. Twitch name-change history is a strong pivot: an old handle often maps to accounts on other platforms that the current handle hides.

## How to use it (`bestInteractionPattern`: web-manual)
1. The direct link `twitch-tools.lolarchiver.com/username_changelog` now 410s/redirects — go to the current suite at `t-tools.lolarchiver.com` and open the username-changelog (name-history) tool. Related tools there cover broadcaster-type changes, timeout/chat history, and moderator-of lookups.
2. Enter the target Twitch `username`.
3. Read the changelog: previous usernames and the dates they changed. Expect free lookups to be limited/teased and full history to require a subscription.
4. Pivot: each recovered prior `username` feeds `[[social-profiles-finder]]`, `[[user-sherlock]]`, and username-variant expansion (`[[username-generation-guide]]`) to find the same person's accounts elsewhere.

## Inputs → Outputs
- **In:** Twitch `username`
- **Out:** prior `username`(s)/name-change history, `social-profile` (the Twitch account) and cross-platform leads
- **Empty/negative result looks like:** no recorded changes (the handle may never have changed, or isn't in LoLArchiver's archive), or a paywall standing between you and the full history — absence is not proof the account never renamed.

## Gotchas & OpSec
- Endpoint moved: bookmark the current `t-tools.lolarchiver.com` suite, not the dead direct URL.
- Grey-area, paid, unaudited: treat prior-username claims as leads to confirm (e.g., cross-check the old handle against archived streams/social accounts) rather than proof.
- Registration/subscription gates the useful depth — budget for that or stop at the free teaser.

## Overlaps ("do both")
- Pairs with `[[social-profiles-finder]]` and `[[user-sherlock]]`: this recovers *historical* Twitch handles that current-state namecheckers can't see, and those tools then resolve each recovered handle to profiles on other networks.

## Trust & verifiability
`trust: unverified` — a niche commercial grey-area archive with no auditable sourcing; confirm any recovered prior username against an independent record before attributing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-tools-lolarchiver-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
