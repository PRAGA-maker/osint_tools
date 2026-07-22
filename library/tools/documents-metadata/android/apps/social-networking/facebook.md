---
id: facebook
name: Facebook
description: Use when you have a `name`, `email`, `phone`, or `username` and want a person's social footprint — returns profile, friends/associates, photos, and location clues.
url: https://www.facebook.com/
bestFor: Core social-media reconnaissance — profiles, relationship networks, photos, check-ins, and life events.
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
selectorsIn:
- name
- email
- phone
- username
selectorsOut:
- social-profile
- associate
- image
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to use with a Facebook account; most profile viewing and all search now require being logged in.
opsec: active
opsecNote: Facebook links activity to your logged-in account and surfaces "People You May Know" based on who you view/who views you — viewing a target from a real or contaminated account can expose you to them. Always use a well-aged sock-puppet account on a clean browser, disable contact upload, and never interact (friend, like, message) with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party platform data, so profiles are authentic; but users self-report and privacy settings hide much, and impersonation/fake profiles exist.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- facebook-directory-users-by-name
- facebook-photos-by-id
- facebook-profile-directory
- fb-email-search
- fb-identify-requires-logout
- recover-fb-account
- facebook-live-map
- facebook-ad-s-link
- facebook-com
- facebook-com-2
- facebook-watch
aliases:
- Facebook
- FB
- facebook.com
tags:
- social-networking
- social-media
- profile-recon
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Facebook

> The single largest social-media OSINT surface — the place to turn a `name`, `email`, `phone`, or handle into a profile, a friend/family network, photos, and location breadcrumbs.

## When to use
You have almost any personal selector — a `name`, `email`, `phone`, or reused `username` — and want the subject's social footprint: who they are connected to (`associate`s: family, partners, coworkers), what they look like (`image`s), where they've been (`geolocation` from check-ins, tagged places, photo backgrounds), and life events (employer, school, relationship). For missing-persons work Facebook is often the richest single source of living relatives and recent activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a **sock-puppet** account (aged, no real contacts, clean browser/IP).
2. Search the `name` (add city/school/employer to disambiguate), or find the profile via a known `email`/`phone` (some accounts remain discoverable by these), or by the profile URL/username.
3. Read what's visible: About (work, education, hometown, relationship), Friends list, Photos (and their comments/tags), and recent posts/check-ins.
4. Mine associates and tagged locations; save photos for reverse-image/face search.
5. Do NOT friend, like, or message the target. Pivot: friends become new `name`s; a profile photo feeds face-search; a hometown/check-in narrows `geolocation`; a linked Instagram/handle feeds cross-site tools.

## Inputs → Outputs
- **In:** `name` / `email` / `phone` / `username`
- **Out:** `social-profile`, `associate` network, `image`s, `employer-org`/education, `geolocation` from check-ins & tags
- **Empty/negative result looks like:** no match, or a locked-down profile showing only name and cover photo. A private profile confirms existence but yields little without the account owner loosening settings — do not attempt to bypass privacy.

## Gotchas & OpSec
- **Active and account-linked:** "People You May Know" can reveal your sock-puppet to the target if hygiene slips — never upload contacts, never reuse a puppet across cases.
- Search and most viewing require login; logged-out access is heavily restricted.
- Self-reported data can be stale or false; impersonation profiles exist — corroborate before concluding.

## Overlaps ("do both")
- Pairs with `[[facebook-directory-users-by-name]]`, `[[facebook-photos-by-id]]`, and `[[fb-email-search]]` for structured pivots, and with Instagram plus reverse-image/face tools — Facebook gives the network and life events; those extract photos, confirm the face, and follow the handle elsewhere.

## Trust & verifiability
`trust: trusted` — first-party platform data, so real profiles are authentic; the caveats are privacy settings hiding data, self-reported fields, and fake/impersonation accounts, all of which require corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, email, phone, username → social-profile, associate, image, employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
