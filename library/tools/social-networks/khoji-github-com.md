---
id: khoji-github-com
name: Khoji
description: Use when you have a Snapchat `username` and want to download that user's full Bitmoji avatar history — returns image artifacts revealing appearance and self-presentation over time.
url: https://github.com/asharbinkhalil/khoji
category: social-networks
path:
- social-networks
bestFor: Enumerating and downloading the historical Bitmoji avatars of a Snapchat username to study appearance and self-presentation changes.
selectorsIn:
- username
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open-source Python tool; a free hosted web version exists at khoji.onrender.com (slow on free hosting).
opsec: active
opsecNote: The tool queries Snapchat's public Bitmoji endpoints for the target username — that traffic originates from your IP/host. It does not friend or message the user, but you are touching Snapchat's infrastructure; run from a sock-puppet context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community OSINT tool (~48 stars) implementing a public technique credited to hatless1der; verify output and expect breakage if Snapchat changes its Bitmoji endpoints.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- the-bitmoji-avatar-history-enumerator-2
- reveye-reverse-image-search
aliases:
- khoji
- Snapchat Bitmoji history
tags:
- snapchat
- bitmoji
- open-source
- cli
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Khoji

> A niche Snapchat tool that downloads a user's entire Bitmoji avatar history — a surprisingly rich window into how a subject depicts themselves (hairstyle, outfits, accessories) over time.

## When to use
You have a Snapchat `username` and want more than the current avatar. Users update their Bitmoji to reflect real changes — new hairstyle, glasses, seasonal outfits, sometimes a new partner in a "friendmoji." Khoji pulls the full history of those avatars, which can corroborate physical description, timeline, and self-image details in a missing-persons or identity case where the person is Snapchat-active.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/asharbinkhalil/khoji and `pip install -r requirements.txt` (or use the web version at khoji.onrender.com).
2. Run: `py script.py -u <snapchat-username>`.
3. It downloads the historical Bitmoji images for that user to disk.
4. Review the sequence for appearance changes, accessories, and any friendmoji (paired avatars → `associate` leads).
5. Pivot: feed distinctive avatars into reverse-image tools; corroborate physical-description details against other photos.

## Inputs → Outputs
- **In:** `username` (Snapchat handle)
- **Out:** `image` (full Bitmoji avatar history)
- **Empty/negative result looks like:** no images / an error — the username may be wrong, the account may not exist or lack a Bitmoji, or Snapchat's endpoint changed and broke the tool.

## Gotchas & OpSec
- **Active:** it queries Snapchat directly — use a sock-puppet host/IP.
- Depends on Snapchat's public Bitmoji endpoints; expect breakage over time.
- A Bitmoji is a stylised self-depiction, not a photo — treat appearance cues as soft corroboration, not proof.

## Overlaps ("do both")
- Pairs with `[[the-bitmoji-avatar-history-enumerator-2]]` (same technique, alternate implementation) and `[[reveye-reverse-image-search]]` (to hunt the same avatar/username elsewhere). Do both if one implementation breaks.

## Trust & verifiability
`trust: community` — a small open-source tool built on a documented public technique. The code is inspectable; reliability rides on Snapchat's endpoints, so verify it still works before relying on a negative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | khoji-github-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
