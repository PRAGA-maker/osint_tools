---
id: the-bitmoji-avatar-history-enumerator-2
name: BACKMOJI (Bitmoji Avatar History Enumerator)
description: Use when you have a Snapchat user's Bitmoji ID and want their historical avatar/outfit changes — returns image snapshots and physical-description clues over time.
url: https://webbreacher.com/2022/10/24/grabbing-old-bitmoji-outfits-with-BACKMOJI/
category: social-networks
path:
- social-networks
bestFor: Enumerating a Snapchat/Bitmoji user's past avatar outfits and appearance changes by iterating Bitmoji outfit IDs.
selectorsIn:
- username
- social-profile
selectorsOut:
- image
- physical-description
status: live
pricing: free
costNote: Free web tool by Micah Hoffman (WebBreacher), hosted at backmoji.myosint.training. No account. The linked blog post explains the method; the tool itself does the enumeration.
opsec: passive
opsecNote: It requests public Bitmoji avatar images from Snapchat's/Bitmoji's CDN by iterating outfit IDs — the target's Snapchat account is not notified and you never interact with them. Still, do the ID discovery step (viewing their Snapchat/Bitmoji) from a sock-puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built and maintained by Micah Hoffman (WebBreacher / MyOSINT Training), a highly regarded OSINT trainer, building on Griffin's Snapchat research. Reputable and technique-transparent.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- snapchat
- snap-map
aliases:
- BACKMOJI
- Bitmoji Avatar History Enumerator
tags:
- snapchat
- Snapchat
- bitmoji
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# BACKMOJI (Bitmoji Avatar History Enumerator)

> WebBreacher's tool for time-travelling a Snapchat user's Bitmoji: iterate outfit IDs to recover past avatar looks — clothing, hair, accessories — that can corroborate identity, timeframe and appearance.

## When to use
You have a subject's **Bitmoji ID** (obtained from their Snapchat profile/avatar URL) and want their avatar *history*, not just the current look. Historical outfits can place a person in a season/era, reveal appearance changes, or match a Bitmoji seen elsewhere. Valuable in Snapchat-centric investigations where the Bitmoji is one of the few durable, enumerable artifacts.

## How to use it (`bestInteractionPattern`: web-manual)
1. First obtain the target's **Bitmoji ID** — extract it from their Snapchat avatar image URL / profile (do this from a sock-puppet).
2. Go to backmoji.myosint.training (the tool the blog post describes).
3. Enter the Bitmoji ID, set the **Upper value** to the current outfit ID + ~10–20, keep S Value (spacing) and image height at defaults.
4. Run it: the page lays out front/side-view images for each discoverable outfit version, hyperlinked.
5. Read the sequence for appearance/`physical-description` changes over time.
6. Pivot: a distinctive Bitmoji look feeds cross-account matching; the Snapchat account feeds `[[snap-map]]` for location context.

## Inputs → Outputs
- **In:** `social-profile` / `username` resolved to a **Bitmoji ID**
- **Out:** `image` (historical avatar renders), `physical-description` (outfit/hair/appearance evolution)
- **Empty/negative result looks like:** no images render across the ID range — usually a wrong Bitmoji ID or an account with no outfit history; re-derive the ID from the Snapchat avatar URL.

## Gotchas & OpSec
- You must have the **Bitmoji ID first** — the tool doesn't resolve a Snapchat username to an ID; that's a manual precursor step.
- Bitmoji/Snapchat changes to their CDN can break enumeration over time — verify the tool still returns images.
- OpSec: the enumeration itself is passive; keep the upstream Snapchat/Bitmoji viewing behind a sock puppet.

## Overlaps ("do both")
- Pairs with Snap Map and Snapchat username tools — those locate and identify the account; BACKMOJI adds the avatar-history dimension.
- Combine with reverse-image search on a distinctive Bitmoji to find the same avatar reused on other platforms.

## Trust & verifiability
`trust: community` — authored by a respected OSINT trainer and openly documented; the images come straight from Bitmoji's CDN, so they're authentic, but confirm the current outfit ID to anchor the timeline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-bitmoji-avatar-history-enumerator-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → image, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
