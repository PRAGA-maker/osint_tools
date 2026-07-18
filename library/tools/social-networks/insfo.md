---
id: insfo
name: InsFo (Export Instagram Followers)
description: Use when you have an Instagram `username` and want its social graph — a Chrome extension that exports an account's followers/following (and comments/tags/locations) to a table.
url: https://chrome.google.com/webstore/detail/insfo-export-instagram-fo/bckleejkdhlponanidmjfjdigpahlado/related
category: social-networks
path:
- social-networks
bestFor: Exporting an Instagram account's followers/following list to a spreadsheet for network analysis.
selectorsIn:
- username
selectorsOut:
- username
- associate
status: live
pricing: freemium
costNote: Free tier exports the first ~500 records; unlimited export requires a premium upgrade. Requires installing the extension and logging into Instagram.
opsec: active
opsecNote: The extension runs inside YOUR logged-in Instagram session and pages through the target's follower lists, which is detectable API activity against your account. Use a sock-puppet Instagram account and browser profile, never your real one, and expect rate limits/anti-scraping.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension (~10k users) that reads Instagram data through your session; not affiliated with Instagram, and such tools risk account action and change/break with Instagram updates.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- InsFo
- Export Instagram Followers
tags:
- Social Media
- Instagram
- follower-export
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# InsFo (Export Instagram Followers)

> A Chrome extension that dumps an Instagram account's followers/following — and its commenters, taggers and locations — into a table for offline social-network analysis.

## When to use
You have a target Instagram `username` and want its social graph as data: who follows it and who it follows, to find close ties, mutual connections, alt accounts, and `associate` leads. Exporting to a table lets you sort, dedupe, and compare follower sets across accounts (e.g. to link two profiles by shared followers) — far more tractable than scrolling the lists by hand.

## How to use it (`bestInteractionPattern`: browser-extension)
1. In a sock-puppet browser profile logged into a sock-puppet Instagram account, install InsFo from the Chrome Web Store.
2. Navigate to the target's Instagram profile and open the extension.
3. Export the desired dataset — Followers, Following, Commenters, Tags, or Locations — to a table/CSV (free tier caps at ~500 records; premium removes the cap).
4. Pivot: compare follower/following sets across accounts to link identities; treat notable handles as `associate`/`username` leads and enrich them with profile tools.

## Inputs → Outputs
- **In:** an Instagram `username` (a public/accessible profile)
- **Out:** exported `username` lists (followers/following) and `associate` links, plus comment/tag/location data
- **Empty/negative result looks like:** an empty or truncated export, or a rate-limit/error — Instagram throttled the session, the profile is private/inaccessible, or the free cap was hit; back off rather than hammering the account.

## Gotchas & OpSec
- **Active & account-risking:** it operates through your Instagram login and pages the target's lists — Instagram may rate-limit, shadow-flag, or ban the account. Always use a throwaway account, never a real or important one.
- Private accounts you don't follow won't export; large accounts hit the free 500-record cap and heavier rate limits.
- Third-party and fragile: Instagram's frequent changes break such extensions; verify it still works and cross-check exported handles on the live profile.

## Overlaps ("do both")
- Pairs with other Instagram OSINT tools and cross-platform username checkers — InsFo captures the follower graph, while profile-enrichment and username tools turn the surfaced handles into identities.

## Trust & verifiability
`trust: unverified` — an unofficial extension acting through your session; treat exports as leads, confirm key handles on the live profile, and weigh the account-safety risk before every run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insfo |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
