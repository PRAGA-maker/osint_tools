---
id: bitmoji-avatar-history-enumerator
name: Bitmoji / Snapchat Avatar History Enumerator
description: Use when you have a Snapchat `username`/`social-profile` and want the linked Bitmoji avatar and its historical versions — returns `image` avatars and physical-description cues.
url: https://webbreacher.github.io/osinttools/
category: social-networks
path:
- social-networks
bestFor: Pulling a Snapchat user's Bitmoji avatar and prior avatar versions to read appearance/style changes and confirm activity.
selectorsIn:
- username
- social-profile
selectorsOut:
- image
- physical-description
status: live
pricing: free
costNote: Free browser-based tool; no account needed. Uses Snapchat/Bitmoji's own public avatar endpoints.
opsec: passive
opsecNote: The tool resolves public Bitmoji avatar URLs; it does not friend, follow or message the target, so it does not alert them. Run from a clean/sock-puppet browser. Do not escalate to adding the account on Snapchat, which is active and visible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community OSINT utility (WebBreacher / My OSINT Training) that queries public Bitmoji avatar endpoints; reliability depends on Snapchat not changing those endpoints.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Backmoji
- Bitmoji history
- Snapchat Bitmoji enumerator
tags:
- snapchat
- bitmoji
- avatar
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Bitmoji / Snapchat Avatar History Enumerator

> Turns a Snapchat handle into its Bitmoji avatar — and, crucially, the avatar's *past* versions — a lightweight way to read appearance/style changes and confirm an account is real and active.

## When to use
You have a Snapchat `username` (or a `social-profile` you've tied to one) and want more than a static profile. A user's Bitmoji is a personalised cartoon of themselves; the enumerator pulls the current avatar and historical versions (as the user restyled hair, clothing, accessories over time). Those changes are soft `physical-description`/lifestyle cues, and the mere existence of a resolvable, evolving avatar corroborates that the account is genuine and in use — useful when validating a Snapchat identity for a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool (the WebBreacher OSINT tools page; it now redirects to the My OSINT Training tools site — use the current host if the GitHub page moves) and find the Snapchat/Bitmoji history utility.
2. Enter the Snapchat `username` (or the Bitmoji avatar ID if you already have it).
3. The tool resolves the avatar and returns the current image plus prior versions where the endpoints expose them.
4. Read the avatars: hair colour/style, glasses, clothing, accessories, apparent changes over time. Pivot: save the `image`s for reference; combine with other Snapchat-OSINT (map, story availability) and reverse-image on any real photos.

## Inputs → Outputs
- **In:** Snapchat `username` (or Bitmoji avatar ID)
- **Out:** `image` (current + historical Bitmoji avatars), soft `physical-description`/style cues, account-real/active signal
- **Empty/negative result looks like:** no avatar resolves — the handle doesn't exist, the user has no Bitmoji linked, or Snapchat changed the endpoint the tool relies on (tools in this class break when Snapchat updates).

## Gotchas & OpSec
- Bitmoji is a stylised self-caricature, not a photo — treat physical cues as loose indicators, never identification.
- Endpoint-dependent: these tools periodically break when Snapchat changes its avatar URLs; if it fails, the tool may be stale rather than the account absent.
- Passive — it does not friend/follow the target; do NOT escalate to adding them on Snapchat.

## Overlaps ("do both")
- Pairs with other Snapchat OSINT (Snap Map location, story/username checks) and reverse-image tools — the Bitmoji confirms the account and hints at appearance; those add location and real imagery.

## Trust & verifiability
`trust: community` — a community-maintained utility over Snapchat's public avatar endpoints; results are only as current as those endpoints, so verify against other Snapchat signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitmoji-avatar-history-enumerator |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → image, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
