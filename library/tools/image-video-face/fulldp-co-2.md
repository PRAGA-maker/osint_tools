---
id: fulldp-co-2
name: fulldp.co
description: Use when you have a TikTok username/profile and need the full-resolution profile picture (TikTok serves a thumbnail) — returns a downloadable full-size avatar image.
url: https://fulldp.co/tiktok-full-size-profile-picture/
category: image-video-face
path:
- image-video-face
bestFor: Fetching the full-size TikTok profile picture from a username instead of the cropped thumbnail.
selectorsIn:
- username
- social-profile
selectorsOut:
- image
- face
status: unknown
pricing: free
costNote: Free ad-supported web utility; no account.
opsec: passive
opsecNote: You query fulldp.co (a third party) with the target's public username; the subject is not contacted. The third-party site sees what handle you looked up.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party avatar-grabber site; relies on TikTok's public CDN. Functionality and uptime vary; not officially affiliated with TikTok.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FullDP TikTok
tags:
- profileimages
- Profile Images
- tiktok
source: uk-osint
lastVerified: ''
enrichment: full
---

# fulldp.co (TikTok)

> A web utility that pulls the full-resolution TikTok profile picture from a username, bypassing the small in-app thumbnail.

## When to use
You have a TikTok `username` or `social-profile` for a missing person or associate and need the largest available avatar to run reverse-image / face search. Tie-in: input `username`, output a full-size `image`/`face`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fulldp.co/tiktok-full-size-profile-picture/.
2. Enter the TikTok `username` (handle) and submit.
3. The page renders the full-size avatar — right-click to save the `image`.
4. Pivot: run the saved avatar through reverse-image / face search ([[google-com-66]], PimEyes-class tools) to find the same face elsewhere.

## Inputs → Outputs
- **In:** `username` / `social-profile` (TikTok handle)
- **Out:** `image`, `face` (full-size avatar)
- **Empty/negative result looks like:** Error, a placeholder/default avatar, or no image — the handle is wrong, private, or the CDN endpoint changed.

## Gotchas & OpSec
- Human-in-the-loop: ad-supported pages may show interstitials/CAPTCHA.
- The image is only the avatar — quality depends on what the user uploaded; many avatars are too small or stylized for reliable face matching.
- OpSec: passive — the subject is not notified, but fulldp.co logs your lookups.

## Overlaps ("do both")
- Sibling pages [[fulldp-co-3]] (VK), [[fulldp-co-5]] (YouTube), and the [[fulldp-co-4]] hub cover other platforms; pick by where the target's profile lives.

## Trust & verifiability
`trust: unverified` — unaffiliated third-party grabber dependent on TikTok's CDN; uptime and behavior not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fulldp-co-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | username, social-profile → image, face |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
