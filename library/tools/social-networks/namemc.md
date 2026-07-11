---
id: namemc
name: NameMC
description: Use when you have a Minecraft `username` (or account UUID) and want its name-change history, skins, and profile — returns prior usernames and social-profile leads.
url: https://namemc.com/
category: social-networks
path:
- social-networks
bestFor: Looking up a Minecraft account's username history, skins/capes, and profile — and checking username availability.
selectorsIn:
- username
- name
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free to search; no account needed for name history, skins, and profile lookups.
opsec: passive
opsecNote: NameMC indexes public Mojang/Minecraft account data; searching does not notify the account owner. Only NameMC (and your network) sees your query and IP. Note NameMC profiles have public comment/friend features — do NOT log in or interact from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known community Minecraft-identity site; name-history data derives from Mojang's public profile API and is broadly reliable, though NameMC is third-party.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- steamosint
- username-search-2
aliases:
- name mc
- namemc minecraft
tags:
- bellingcat-toolkit
- other-platforms
- minecraft
- gaming
source: bellingcat-toolkit
lastVerified: '2026-07-11'
enrichment: full
---

# NameMC

> The go-to public lookup for Minecraft identities — name-change history, skins/capes, and profile — plus username-availability checks.

## When to use
You have a Minecraft `username` (or an account UUID) and want to (a) recover the account's **previous usernames** — a rich pivot, since a person you found under one Minecraft handle may have used others for years — and (b) fingerprint them by skin/cape and profile. Gaming handles frequently reuse across platforms, so a Minecraft name history often unlocks other accounts elsewhere. Recommended in the Bellingcat toolkit for exactly this cross-platform pivoting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://namemc.com/ and search the target's Minecraft `username` (or paste a UUID).
2. On the profile page read:
   - **Name history** — the list of prior usernames and the dates they changed.
   - **Skins/capes** — visual fingerprint; a distinctive custom skin can tie accounts together.
   - **Profile** — UUID and any public NameMC social features (friends/comments).
3. Use the search box to check whether a specific username is currently available/taken (timing a handle's release).
4. Pivot: feed each prior username into cross-platform tools ([[username-search-2]], Sherlock-style checks); tie a shared handle to other gaming accounts like Steam via [[steamosint]].

## Inputs → Outputs
- **In:** `username` (Minecraft handle) or account UUID
- **Out:** prior `username`s (name history), UUID, skin/cape fingerprint, `social-profile` (NameMC profile + links)
- **Empty/negative result looks like:** "no results" / an unclaimed name — the handle may be free, or Mojang's name-history endpoint has limited older data (Microsoft-migrated accounts changed how history is exposed); absence isn't proof.

## Gotchas & OpSec
- Since the Mojang→Microsoft account migration, full name-history availability changed for some accounts; older changes may not always show.
- Same-handle ≠ same-person across platforms — confirm via skin/profile/behavioral overlap before merging identities.
- OpSec: passive — the owner isn't notified. Don't authenticate to NameMC or use its comment/friend features from a real account.

## Overlaps ("do both")
- Pairs with [[steamosint]] (other major gaming identity) and [[username-search-2]] — NameMC resolves Minecraft-specific history; those spread the discovered handles across the wider web.

## Trust & verifiability
`trust: community` — a widely used third-party built on Mojang's public profile data. Name-history and UUID are reliable pointers; verify identity links with corroborating signals rather than the handle alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namemc |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
