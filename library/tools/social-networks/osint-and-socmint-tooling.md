---
id: osint-and-socmint-tooling
name: OSINT & SOCMINT Tooling (osint.support)
description: Use when you have logged-in sessions on major social platforms and want browser-extension tooling to extract data from them — returns friend lists, profile data, and social-profiles.
url: https://osint.support/chrome-extensions/2019/09/29/osint-socmint-tooling.html
category: social-networks
path:
- social-networks
bestFor: A consolidated Chrome extension (plus companion extensions) that adds SOCMINT extraction features across Facebook, Instagram, Twitter, TikTok, and LinkedIn.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
- email
status: degraded
pricing: free
costNote: Free download; last updated Feb 2021 (v1.2.1). Age means some platform integrations may have broken as the sites changed.
opsec: active
opsecNote: The extension operates through YOUR active, logged-in sessions on each platform — so all activity is attributed to whatever accounts you're signed into. Use dedicated sock-puppet accounts, never your real ones. The code is obfuscated (which trips antivirus and means you cannot easily audit what it sends) — run it in an isolated browser profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Community-built by "OSINT Support"; the flagship extension's code is obfuscated, so behavior can't be readily verified — treat as unverified and sandbox it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- seemutualfriendsonfacebook-com
- linkedin-email-reverse-lookup
- facebook-email-reverse-lookup
- facebook-entity-id-parser
- facebook-friends-list-generator
- facebook-profile-id-grabber
aliases:
- OSINT Support tooling
- osint.support Chrome extensions
tags:
- socmint
- browser-extension
- chrome-extension
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# OSINT & SOCMINT Tooling (osint.support)

> A bundled Chrome extension that bolts SOCMINT extraction onto your logged-in Facebook, Instagram, Twitter, TikTok, and LinkedIn sessions — powerful, but obfuscated and dated.

## When to use
You're doing social-media intelligence with sock-puppet accounts already logged into the major platforms, and you want in-browser extraction (e.g. pulling a Facebook friends list, harvesting profile data) rather than manual scraping. The osint.support suite packages several such tools, including a "Facebook Friends List Generator" and a "LinkedIn Email Reverse Lookup."

## How to use it (`bestInteractionPattern`: browser-extension)
1. From an isolated browser profile signed into **sock-puppet** accounts, download the extension from the osint.support page (verify the MD5 it provides).
2. Install it in Chrome; grant it access only in that sandboxed profile.
3. With active sessions on the target platforms (Facebook, Instagram, Twitter, TikTok, LinkedIn), invoke the relevant feature — e.g. generate a Facebook friends list for a public profile, or reverse-lookup a LinkedIn email.
4. Export the extracted data (friend lists, profile fields).
5. Pivot: an exported friends list feeds `[[seemutualfriendsonfacebook-com]]` for mutual-connection analysis; harvested emails feed email-OSINT.

## Inputs → Outputs
- **In:** a target `username`/`name`/`social-profile` on a supported platform (you must be logged in).
- **Out:** extracted `social-profile` data, friend/connection lists (`associate`s), and in some tools `email`s.
- **Empty/negative result looks like:** the feature fails or returns nothing — most often because the platform changed its markup since 2021 and the extension is out of date, or the target content is non-public. Do not read a failure as "no data exists."

## Gotchas & OpSec
- It runs through your logged-in sessions, so everything is attributed to those accounts — mandatory sock puppets, isolated browser profile, expect platform rate-limiting or account bans for aggressive extraction.
- The code is **obfuscated**: you cannot easily see what it does with your session or where data goes, and it may trigger antivirus. This is a real trust cost — sandbox it and assume it could exfiltrate.
- Dated (v1.2.1, 2021): several integrations may simply not work against current site versions.

## Overlaps ("do both")
- Pairs with `[[seemutualfriendsonfacebook-com]]` — use this to generate the raw friend lists, then that tool to intersect them. Its LinkedIn email lookup overlaps with dedicated `[[linkedin-email-reverse-lookup]]` tooling.

## Trust & verifiability
`trust: unverified` — community-built and obfuscated, so its behavior can't be audited. Use only sock-puppet accounts in a sandboxed profile, and verify every extracted datum against the platform directly before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-and-socmint-tooling |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, associate, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes |
