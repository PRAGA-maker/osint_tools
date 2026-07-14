---
id: izuum
name: Izuum
description: Use when you have an Instagram `username` and want to view/enlarge their (public) profile picture — returns image, social-profile. Now largely a bio/quote blog; treat the DP-viewer as degraded.
url: http://izuum.com/
category: social-networks
path:
- social-networks
bestFor: Enlarging a public Instagram profile picture from a username (instadp-style viewer).
selectorsIn:
- username
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free, ad-supported. No account needed for the viewer when it works.
opsec: passive
opsecNote: Third-party viewers render Instagram's own CDN image; the target is not notified. But you are trusting an unaffiliated ad-supported site with your query — use a sock-puppet browser and never enter your own IG credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Unaffiliated third party (explicitly "not affiliated with Instagram"). On last check the domain served mostly bio/quote/blog content and the profile-picture-viewer function could not be confirmed working — hence degraded.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Izuum instadp
- Instagram DP viewer
tags:
- toddington
- curated-directory
- social-media
- instagram
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Izuum

> An instadp-style Instagram profile-picture viewer — enter a handle, see the full-size DP — but the live domain has drifted toward a bio/quote blog, so treat it as degraded and keep a backup viewer ready.

## When to use
You have an Instagram `username` and need the subject's full-resolution profile picture — Instagram serves DPs at a small crop in-app, and a viewer pulls the original for reverse-image search or face comparison. Useful when the target's IG is otherwise private (the DP is usually still public).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://izuum.com/ in a clean/sock-puppet browser.
2. If a profile-picture/instadp search box is present, enter the Instagram `username` and submit.
3. Save the full-size image it renders (right-click / save), then push it into reverse-image and face-search tools.
4. If the site only shows bio/quote/blog content and no working viewer (its current degraded state), abandon it and use an alternative instadp-style viewer.
5. Pivot: the saved `image` feeds [[pimeyes-com]] / reverse-image engines; a confirmed live IG account feeds username enumeration.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** `image` (full-size profile picture), `social-profile` (confirmation the handle exists)
- **Empty/negative result looks like:** no image control on the page, an error, or only marketing/quote articles — meaning the viewer is down, not that the DP doesn't exist.

## Gotchas & OpSec
- Degraded: the domain now largely serves bio/quote blog content; the DP-viewer may not function. Have a second instadp-style tool ready.
- Third-party and unaffiliated — never enter your own Instagram login; it only needs the public handle.
- OpSec: passive (image comes from IG's CDN), but the site logs your query; use a throwaway browser.

## Overlaps ("do both")
- Pairs with any other instadp/Instagram-DP viewer for redundancy, and with [[pimeyes-com]] / reverse-image tools that consume the DP you extract.

## Trust & verifiability
`trust: unverified` — an anonymous, ad-supported third party that explicitly disclaims Instagram affiliation and whose core function was not confirmed live; use only for public DP extraction and verify the image independently.
