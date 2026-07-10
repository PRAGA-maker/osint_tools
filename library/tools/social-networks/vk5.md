---
id: vk5
name: VK5 (city4me VK viewer)
description: Use when you have a VKontakte profile (`social-profile` id/URL) and want to surface hidden friends, activity, likes, and photos — returns associates, images, and activity metadata.
url: http://vk5.city4me.com
category: social-networks
path:
- social-networks
bestFor: Extracting hidden friends, likes, online activity, and photos from a VK profile.
selectorsIn:
- social-profile
- username
selectorsOut:
- associate
- image
- social-profile
status: live
pricing: free
costNote: Free web service; most features unlock only after you authorize it against your own VK account (OAuth).
opsec: active
opsecNote: This is a third-party Russian VK-surveillance service. Authorizing it grants a foreign tool access to your VK account and exposes your queries; the account you use is attributable. Use a dedicated sock-puppet VK account, never a personal one, and assume the service logs everything. VK also applies flood-control that can throttle or flag automated viewing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party VK scraper of unknown operator; requires handing it VK OAuth. Treat as untrusted infrastructure — useful signal, real operational risk.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- vk-com
- 220vk
aliases:
- vk5.city4me.com
- city4me
tags:
- vkontakte
- vk-analytics
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# VK5 (city4me VK viewer)

> A third-party VKontakte profile analyzer that surfaces hidden friends, likes, online-activity history, group memberships, and photos for a target VK account.

## When to use
You have a subject's VK profile (id or URL) and want intelligence the profile page hides: mutual/"hidden" friends (associates), what they like and when they are online (activity pattern), group memberships, and downloadable photos. High value for Russian-speaking/CIS subjects where VK is the dominant network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://vk5.city4me.com in a sock-puppet browser session.
2. Enter the target VK user ID or profile URL.
3. To unlock most features, authorize the tool against a **throwaway** VK account via OAuth (never your real one).
4. Read the output: hidden/derived friend lists, likes on avatars/posts, online-status history, groups, and photo galleries.
5. Pivot: derived friends feed an associate map; online-activity patterns hint at timezone/routine; photos feed reverse-image and face search.

## Inputs → Outputs
- **In:** `social-profile` (VK id/URL), or `username`
- **Out:** `associate` (hidden friends), `image` (photos), `social-profile` (activity, groups, likes)
- **Empty/negative result looks like:** blank or minimal data usually means a well-locked profile, VK flood-control throttling, or that you didn't authorize — not that the account is inactive.

## Gotchas & OpSec
- Human-in-the-loop: OAuth authorization with a VK account is needed for most features.
- OpSec: **active and risky** — you grant a foreign, unknown-operator tool access to a VK account and disclose your targets. Sock-puppet only; assume full logging.
- VK flood-control limits automated viewing; pace requests.

## Overlaps ("do both")
- Pairs with `[[vk-com]]` — verify anything VK5 infers against the real VK profile to avoid acting on scraper artifacts.
- Pairs with `[[220vk]]` — a comparable VK-analytics service; cross-check hidden-friend/activity claims since methods differ.

## Trust & verifiability
`trust: unverified` — anonymous third-party scraper requiring VK OAuth; the signals can be valuable but the operator is unknown, so corroborate on VK directly and never use a real account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk5 |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → associate, image, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
