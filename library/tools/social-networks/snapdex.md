---
id: snapdex
name: Snapdex
description: Use when you have a `username` or `name` and want to find a Snapchat account — returns a wiki-style directory profile with the handle, snapcode, snaps, and related accounts.
url: https://snapdex.com/
category: social-networks
path:
- social-networks
bestFor: Discovering and confirming a Snapchat handle via a user-built, wiki-style directory of Snapchat profiles.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Free to browse/search; content is user-generated, no account needed to view.
opsec: passive
opsecNote: Browsing a public directory of self/community-listed handles is passive; the listed person isn't told you looked. No login to view. Adding someone on Snapchat would be active — stay at the lookup stage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wiki-like, 100% user-generated directory (by Boot Ventures, Brussels); not affiliated with Snapchat and entries are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ghostcodes-addmesnaps-directories
- snapchat
- snap-map
aliases:
- Snapdex
- snapdex.com
tags:
- snapchat
- username-directory
- social-media
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Snapdex

> A wiki-style directory of Snapchat users — a "Pokédex for Snapchat" where community-added profiles list handles, snapcodes, and related accounts, helping you find or confirm a Snapchat account.

## When to use
Snapchat has no built-in public profile search, so finding someone's account is hard. Snapdex is a user-built index of Snapchat profiles — search it by `username` or `name` to see if a subject (often a creator or notable user) is listed, with their handle, snapcode, sample snaps, and linked/related accounts. Useful for confirming an account exists and grabbing the exact handle plus association leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://snapdex.com/ and search a name/handle, or browse the indexed lists.
2. Open a profile: note the Snapchat username, snapcode, any snaps, and "related accounts."
3. Because it's wiki-style and user-edited, treat entries as leads — confirm via corroborating signals (matching handle/photos/links elsewhere).
4. Follow "related accounts" to map connections.
5. Pivot: a confirmed handle → check activity on `[[snapchat]]`; public geotagged content → `[[snap-map]]`; also check `[[ghostcodes-addmesnaps-directories]]` for the same person.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** Snapchat `username`/`social-profile`, snapcode, related accounts (`associate`)
- **Empty/negative result looks like:** no listing — the person was never added to Snapdex (most users aren't), so a null is weak evidence they have no Snapchat.

## Gotchas & OpSec
- Skews toward creators/notable users and is far from comprehensive — absence proves little.
- 100% user-generated and unverified — anyone can add/edit an entry, so confirm identity independently.
- Passive to browse; don't cross into adding/messaging the subject.

## Overlaps ("do both")
- Pairs with `[[ghostcodes-addmesnaps-directories]]` — another Snapchat handle directory; different user bases, so check both.
- Pairs with `[[snap-map]]` (public content by location) and `[[snapchat]]` (verify a live account).

## Trust & verifiability
`trust: community` — an unaffiliated, wiki-style directory with no vetting. A listing indicates a handle was posted, not that it's your subject's; verify via cross-platform corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapdex |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
