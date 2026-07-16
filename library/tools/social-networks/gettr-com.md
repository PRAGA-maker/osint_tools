---
id: gettr-com
name: GETTR
description: Use when you have a `username` or `name` and want to find the subject on GETTR (a Twitter/X alternative) — returns `social-profile`, posts, `name`.
url: https://gettr.com/
category: social-networks
path:
- social-networks
bestFor: Locating and reading a subject's public posts on GETTR, a right-leaning microblogging platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to view public posts/profiles; no account needed for basic browsing (deeper features may prompt sign-up).
opsec: passive
opsecNote: Viewing public posts is passive; the target isn't notified. Creating an account to follow/interact ties a (sock-puppet) identity to your activity — keep to logged-out reading where possible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real, operating platform; profile content is authoritative for that account, but anyone can register a handle, so identity attribution needs corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gettr
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
- microblog
- twitter-alternative
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- gettr-search
---

# GETTR

> A Twitter/X-style microblogging platform popular with a right-leaning audience: a place to find a subject's public posts when they've left or supplement mainstream socials.

## When to use
You have a `username` or `name` and want to check whether the subject is active on GETTR — especially relevant when the target's politics or the case context points to alt-tech platforms, or when they've gone quiet on X/Facebook. Public posts here can surface locations, associates, opinions, media and timelines the mainstream platforms don't.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://gettr.com/user/<username>` or use the site search for a `name`/handle.
2. Read the public profile: bio, posts, reposts, following/followers where shown.
3. Capture posts and media (screenshots + saved images) for evidence and reverse-image work.
4. Note mentioned locations, dates, and other handles.
5. Pivot: enumerate the handle on other platforms, reverse-image any avatar/media, and correlate posting times/content with the subject's X/Facebook.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (posts, bio, network), `name`
- **Empty/negative result looks like:** no profile/handle — the subject isn't on GETTR, or uses a different handle here than elsewhere; absence doesn't imply anything about other platforms.

## Gotchas & OpSec
- Handles are self-chosen and may differ from the subject's usual username — try variants and match on content/avatar, not name alone.
- Some browsing depth prompts sign-up; use a sock-puppet if you must register.
- Content moderation differs from mainstream platforms — expect more unfiltered material.

## Overlaps ("do both")
- Pairs with X/Twitter tooling and other alt-tech platforms (Truth Social, Parler archives) — cross-check because a subject often mirrors or migrates content between them.

## Trust & verifiability
`trust: community` — a genuine operating platform; account content is authoritative for that handle, but confirm the handle actually belongs to your subject via corroborating content before asserting identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gettr-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
