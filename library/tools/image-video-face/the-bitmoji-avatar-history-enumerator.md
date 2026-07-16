---
id: the-bitmoji-avatar-history-enumerator
name: Backmoji (Bitmoji Avatar History Enumerator)
description: Use when you have a Snapchat `username` and want to enumerate the history of Bitmoji avatars that account has used — returns `image` avatars and `physical-description` / appearance cues.
url: https://backmoji.myosint.training/
category: image-video-face
path:
- image-video-face
bestFor: Pulling the historical Bitmoji avatar images tied to a Snapchat account to observe appearance/style changes and corroborate identity.
selectorsIn:
- username
selectorsOut:
- image
- physical-description
status: live
pricing: free
costNote: Free web tool hosted by MyOSINT Training; no account or payment.
opsec: passive
opsecNote: The tool reads publicly exposed Bitmoji avatar assets keyed to a Snapchat account; it does not add the target or notify them on Snapchat. Run from a sock-puppet browser for hygiene. It reveals only Bitmoji cartoons the user chose, not real photos.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built and hosted by MyOSINT Training (a recognized OSINT training provider); it relies on Snapchat's public Bitmoji asset URLs, which can change if Snapchat alters that surface.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Backmoji
- Bitmoji avatar history
- Snapchat Bitmoji history
tags:
- profileimages
- Profile Images
- snapchat
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- my-osint-training-tools
- myosint-training
---

# Backmoji (Bitmoji Avatar History Enumerator)

> A MyOSINT Training tool that enumerates the historical Bitmoji avatars a Snapchat account has used — a cartoon breadcrumb trail that still carries identity and appearance signals.

## When to use
You have a Snapchat `username` and want more than the single current avatar. Snapchat exposes Bitmoji avatar assets publicly, and Backmoji walks the account's avatar history — surfacing past Bitmoji designs (hairstyle, clothing, accessories, expressions). Useful for corroborating that an account belongs to a subject, spotting appearance/style changes over time, and enriching a thin Snapchat lead where no real photo is available.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool (backmoji.myosint.training, now served via tools.myosint.training) in a sock-puppet browser.
2. Enter the target Snapchat `username`.
3. Run it: the tool resolves and displays the sequence of Bitmoji avatar `image`s associated with the account.
4. Read the avatars for `physical-description` cues (styling choices, accessories) and changes across the history.
5. Pivot: a confirmed Snapchat account feeds other Snapchat OSINT (Snapmap, story presence); avatar styling can weakly corroborate a real-photo identity found elsewhere.

## Inputs → Outputs
- **In:** Snapchat `username`
- **Out:** historical Bitmoji avatar `image`s, `physical-description` styling cues, account-existence confirmation
- **Empty/negative result looks like:** no avatars returned — the username doesn't resolve to a Snapchat account, the account has no Bitmoji, or Snapchat changed the asset surface. Absence isn't proof the person has no Snapchat.

## Gotchas & OpSec
- Bitmoji are user-designed cartoons, not photographs — treat styling as a soft corroborating signal, not identification.
- Depends on Snapchat's public Bitmoji asset URLs; if Snapchat locks that down, results thin out.
- OpSec: passive — no friending or notifying the target. Still run from a sock puppet.

## Overlaps ("do both")
- Pairs with other Snapchat OSINT (username/account checks, Snapmap) and reverse-image search — Backmoji confirms the account and its avatar history, while those place the account in space/time or tie it to real photos.

## Trust & verifiability
`trust: community` — a purpose-built tool from a known OSINT training provider, riding Snapchat's public Bitmoji surface. Confirm account ownership with a second Snapchat signal; never treat a cartoon avatar as identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-bitmoji-avatar-history-enumerator |
| category | image-video-face |
| selectorsIn → selectorsOut | username → image, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
