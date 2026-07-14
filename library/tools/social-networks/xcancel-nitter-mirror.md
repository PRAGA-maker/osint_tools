---
id: xcancel-nitter-mirror
name: XCancel (Nitter mirror)
description: Use when you have an X/Twitter `username` and want to read their tweets, replies, and media without logging in — returns the public timeline as a social-profile via a Nitter front-end.
url: https://xcancel.com/
category: social-networks
path:
- social-networks
bestFor: Reading and searching an X account's public timeline, media, and replies with no account and no JavaScript tracking.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free public Nitter instance; no account, no ads.
opsec: passive
opsecNote: You view X content through a third-party Nitter mirror instead of x.com, so X does not tie the view to your identity and the target gets no notification. The mirror operator sees your IP/queries; use a sock-puppet browser or route through Tor. Nitter instances come and go — have backup mirrors ready.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of the surviving public Nitter mirrors after X's API lockdown. Community-run; reliability fluctuates as X blocks instances.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- truthnest
- twitter-advanced-search
aliases:
- XCancel
- Nitter
tags:
- twitter
- x
- nitter
- mirror
- no-login
source: inteltechniques-tools
lastVerified: '2026-07-14'
enrichment: full
---

# XCancel (Nitter mirror)

> A login-free Nitter front-end for X/Twitter: read a user's tweets, replies, and media without an account or client-side tracking.

## When to use
You have an X/Twitter `username` and want to review their public activity — timeline, replies, media gallery — without logging into X (which increasingly gates content behind an account) and without your view being attributable. Ideal early-recon read of a target's posts, and for pulling media URLs to reverse-image or geolocate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://xcancel.com/<username>` in a sock-puppet browser (or via Tor).
2. Browse tabs: **Tweets**, **Tweets & replies**, **Media**. Use the search box for keyword/date filtering within the account.
3. Right-click media to grab original image/video URLs for downstream analysis.
4. Pivot: run media through reverse-image/geolocation; for keyword+date search across all of X (not just one account) use `[[twitter-advanced-search]]`; for behavioural analytics use `[[truthnest]]`.

## Inputs → Outputs
- **In:** `username` (X handle)
- **Out:** `social-profile` (public timeline, replies, bio, follower counts), `image` (media)
- **Empty/negative result looks like:** "Instance has been rate limited" / error page, or an empty timeline — the mirror is blocked or the account is protected/suspended; switch to another Nitter instance before concluding the account is empty.

## Gotchas & OpSec
- Human-in-the-loop: none, but expect instance flakiness — keep a list of alternate Nitter mirrors.
- OpSec: **passive** and low-attribution — that's the whole point; still, the mirror operator sees your IP, so sock-puppet or Tor it.
- Protected/private accounts are not visible here.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` (cross-account keyword/date search on x.com) and `[[truthnest]]` (behavioural analytics) — XCancel is the anonymous reader; those add reach and depth.

## Trust & verifiability
`trust: community` — a volunteer-run Nitter mirror. Content is authentic X data proxied verbatim, but availability is unstable; verify anything critical against a second mirror or the live site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xcancel-nitter-mirror |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
