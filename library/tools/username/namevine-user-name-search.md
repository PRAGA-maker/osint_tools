---
id: namevine-user-name-search
name: NameVine (User Name Search)
description: Use when you have a `username` and want an instant, type-as-you-go availability check across major social handles and domains — returns which platforms/domains the handle is taken on (i.e. where the person likely has a `social-profile`).
url: https://namevine.com
category: username
path:
- username
bestFor: Fast, real-time checking of one handle across social networks and domain extensions to spot where it's registered.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to use; a member sign-in exists for enhanced features, but the core cross-platform/domain check works without an account.
opsec: active
opsecNote: NameVine checks handle availability by querying each platform/registrar, so those services see the lookups (from NameVine's infrastructure). It doesn't notify the target. Treat "taken" as a presence signal, not confirmation the same person owns it; use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing handle/domain availability checker; fast and convenient, but availability checks yield false positives (namesakes) and false negatives (site markup changes).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NameVine
- namevine username search
tags:
- username
- handle-availability
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# NameVine (User Name Search)

> Type a handle and watch it check, in real time, across the big social platforms and domain extensions — a quick way to see where a username is already taken.

## When to use
You have a `username` and want an instant read on which major platforms (Instagram, Facebook, X, TikTok, YouTube, LinkedIn, GitHub, Threads, Bluesky) and domains (.com/.io/.ai/.net…) the handle is registered on. Great as a fast first pass to spot a subject's likely accounts and any personal domain before running a deeper multi-site enumerator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://namevine.com in a sock-puppet browser.
2. Start typing the target `username`; it checks availability across social handles and domain TLDs as you type.
3. Note where the handle is **taken** (a presence signal) versus available.
4. Open each "taken" platform to confirm it's your subject (not a namesake).
5. Pivot: registered domains → WHOIS for owner/registration data; confirmed profiles → deeper per-platform OSINT; run the same handle through `[[whatsmyname-python]]`/`[[spy]]` for wider coverage.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-platform/domain taken-vs-available status → `social-profile` presence leads and registered domains
- **Empty/negative result looks like:** the handle is available everywhere — the person may use a different handle, or NameVine's check for a site is stale/broken. "Available" isn't proof of no presence; cross-check with a dedicated enumerator.

## Gotchas & OpSec
- Availability ≠ ownership — "taken" on a platform may be a different person; always open and verify.
- Covers major platforms/domains only; use a broader enumerator for long-tail sites.
- Checks are active toward each service (from NameVine's side); confirm hits on the live profile.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-python]]` and `[[spy]]` (deeper multi-site username enumeration) and WHOIS — NameVine is the instant surface check plus domain signal; the enumerators go wide, WHOIS unmasks any personal domain.

## Trust & verifiability
`trust: community` — a convenient availability checker; treat every "taken" result as an unverified presence lead to confirm on the actual platform.
