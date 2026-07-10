---
id: name-chk
name: Namechk (namechk.com)
description: Use when you have a `username` and want a quick presence/availability sweep across many social sites and domains — returns which platforms the handle is taken on.
url: https://namechk.com/
category: username
path:
- username
bestFor: Fast web-based check of a username (and domain) across hundreds of social platforms to see where it's registered.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- domain
status: live
pricing: free
costNote: Free to check usernames and domains; it's a branding-availability service, but "taken" results double as account-existence signals for OSINT.
opsec: passive
opsecNote: Checks run on Namechk's servers, so target sites don't see your IP and the subject isn't notified. You disclose the handle of interest to Namechk; nothing else sensitive is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known availability checker; results are branding-oriented ("taken/available") and can be cached or incomplete, so read "taken" as a lead to verify, not proof of your subject.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- namecheckerr-com
aliases:
- namechk.com
- Name Chk
tags:
- username-check
- username-availability
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Namechk (namechk.com)

> The hosted username/domain availability checker — enter a handle and it shows, across hundreds of platforms, where the name is taken (i.e. an account exists) versus available.

## When to use
You have a `username` and want a quick, broad read on where it's registered. Namechk is marketed for brand-name availability, but investigators invert it: a platform marked "taken/unavailable" means an account with that handle exists there and is worth inspecting. It's a fast first-pass discovery step across social sites and domains; follow with a signature enumerator for accuracy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://namechk.com/ and enter the `username`.
2. Scan the grid: platforms shown **unavailable/taken** are the accounts to check; note domain availability too.
3. Open each "taken" platform's profile URL directly and confirm whether it's your subject.
4. Try handle variants (underscores, numbers) to catch related accounts.
5. Pivot: confirmed handles go to `[[whatsmyname-web]]` for thorough enumeration and to per-site enrichment.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-platform availability → `social-profile` sites where the handle exists, plus `domain` registration status
- **Empty/negative result looks like:** the handle shows "available" everywhere — no one registered it, so nothing to pivot to.

## Gotchas & OpSec
- "Taken" ≠ your target — common handles are held by many unrelated people; always verify the actual profile.
- Availability data can be **cached/stale or incomplete** vs. live sites; corroborate with a maintained enumerator.
- Distinct from the archived `ha71/namechk` CLI and from `[[namecheckerr-com]]` — this is the hosted namechk.com service.
- OpSec: passive; checks run server-side.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` (more accurate signature checks) and overlaps with `[[namecheckerr-com]]` — use Namechk for a quick sweep, then a thorough enumerator to close gaps.

## Trust & verifiability
`trust: community` — a popular availability tool, reliable enough for a first pass but branding-oriented; confirm every "taken" on the real platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | name-chk |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
