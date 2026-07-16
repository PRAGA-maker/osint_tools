---
id: parler-com
name: parler.com
description: Use when you have a `username`/`name` and suspect the subject is active on the right-leaning social platform Parler — returns their `social-profile`, posts and stated `name`.
url: https://parler.com/
category: social-networks
path:
- social-networks
bestFor: Finding and reading a subject's profile and posts on Parler, an alt-tech / right-leaning social network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to sign up and browse. Relaunched after its 2023 shutdown; some content/profile viewing may require an account.
opsec: active
opsecNote: Parler restricts anonymous browsing, so you likely need to register and log in to view profiles — do this only from a sock-puppet account (burner email/number), never your own. Following or interacting leaks your interest to the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Parler is a real, operating platform (relaunched under new ownership), but it is a partisan alt-tech network with a turbulent history — profiles are user-generated and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- gab-com
- parler-search
aliases:
- Parler
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# parler.com

> An alt-tech, right-leaning social network — a place to look for a subject who has migrated off mainstream platforms; back online after its 2023 shutdown and relaunch.

## When to use
Your subject isn't on (or was deplatformed from) mainstream social media and skews toward alt-tech spaces. Parler is a candidate: if they hold a `username` there you can read their posts, stated `name`, bio, connections, and shared media — a `social-profile` that can corroborate identity, surface associates, and reveal views, locations, and pattern-of-life. Especially relevant when other social checks come up empty for someone in a right-leaning online milieu. Note Parler went dark in April 2023 and has since relaunched, so historical handles may or may not have carried over.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://parler.com/ in a clean/sock-puppet browser.
2. If browsing is gated, register a **sock-puppet** account (burner email; avoid a real phone number if possible) and log in.
3. Search the subject's `username` or `name`; open candidate profiles.
4. Read the profile: bio, posts, media, follows/followers, and any linked handles or locations.
5. Pivot: linked usernames feed cross-platform enumeration; media feeds reverse-image/geolocation; named associates and shared content build the network and timeline.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (posts, bio, media, connections), stated `name`
- **Empty/negative result looks like:** no profile for the handle, or an empty/dormant account — the subject may not use Parler, may have lost the handle in the relaunch, or uses a different name; treat as inconclusive.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** is generally needed to view profiles — set up a sock puppet first.
- OpSec: **active** — you are inside a logged-in session; never use a real identity, and do not follow/interact with the target (that notifies them).
- History: the platform's 2023 shutdown/relaunch means pre-2023 accounts and content may be gone; cross-check with the Parler data from that era via archives if you need historical posts.

## Overlaps ("do both")
- Pairs with `[[gab-com]]` — subjects in this milieu often hold parallel accounts across alt-tech networks; check Gab (and similar) for the same handle to widen coverage and cross-confirm identity.

## Trust & verifiability
`trust: community` — a genuinely operating platform, but partisan and user-generated: profiles are self-asserted and unverified, and the relaunch adds provenance uncertainty. Corroborate any claimed identity or fact against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | parler-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
