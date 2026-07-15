---
id: viewing-bitmoji-changes
name: Viewing Bitmoji Changes (Snapchat technique)
description: Use when you have a Snapchat `username` and want a passive activity/liveness signal — watch the account's Bitmoji avatar for changes to infer the person is active, returning avatar `image` and a behavioural signal.
url: https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/
category: image-video-face
path:
- image-video-face
bestFor: Monitoring a Snapchat user's Bitmoji avatar over time as a low-noise signal that the account (and person) is active.
selectorsIn:
- username
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free technique described on the hatless1der OSINT blog; no tool to buy — you pull the public Bitmoji image via a known URL/endpoint and compare over time.
opsec: passive
opsecNote: You fetch a publicly-served Bitmoji image by the account's Snapchat identifier — you do not add, message, or interact with the target, so no notification is generated. Never add the account or view Stories from an attributable account; that would alert them.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Documented by Griffin (hatless1der), a well-known OSINT practitioner; it's a real, community-shared technique, though Snapchat can change how Bitmojis are served at any time.
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
tags:
- profileimages
- Profile Images
- snapchat
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Viewing Bitmoji Changes (Snapchat technique)

> A passive liveness trick for Snapchat — a user's Bitmoji avatar updates when they interact with the app, so watching it change tells you the person is active without ever touching their account.

## When to use
You have a Snapchat `username` (or Snapchat ID) for a subject and, critically, cannot safely add or message them, but you need to know whether the account — and by extension the person — is still active. Snapchat serves a user's Bitmoji as a public image tied to their identifier; because the Bitmoji reflects the user's current avatar (outfit, pose, seasonal changes it applies as they use the app), capturing it periodically and comparing gives a **behavioural signal**: a change strongly implies the person opened/used Snapchat between captures. For a missing-person case where you have a Snapchat handle but no other live signal, this is a rare fully-passive way to establish the account is being used.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the technique at https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/ for the current Bitmoji URL/endpoint pattern (Snapchat changes these, so follow the live method).
2. Resolve the subject's Snapchat username to the identifier the Bitmoji endpoint needs.
3. Fetch and save the current Bitmoji `image`.
4. Re-fetch on a schedule (e.g. daily) and diff the images — note any change in the avatar.
5. Interpret: a changed Bitmoji indicates recent app activity; pair with other signals to build a pattern-of-life. Pivot the account into wider Snapchat/social investigation.

## Inputs → Outputs
- **In:** Snapchat `username`/ID
- **Out:** the account's Bitmoji `image` (an avatar, not a real face) and, over time, an activity/liveness signal for the `social-profile`
- **Empty/negative result looks like:** no Bitmoji served (the user has none, or the endpoint changed), or an avatar that never changes — a static Bitmoji is inconclusive (could be inactive *or* simply unchanged), so treat only a *change* as positive evidence of activity.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — you must capture and compare images and judge what a change means; it's a signal, not proof.
- OpSec: **passive** done correctly — fetch the public image only; do **not** add the account, view Stories, or interact from an attributable identity, as those actions notify the target.
- Fragile: Snapchat frequently changes how Bitmojis are addressed/served, so the exact endpoint may break — rely on the blog's current method, and note a Bitmoji is a cartoon avatar, useless for face recognition.

## Overlaps ("do both")
- Pairs with `[[snapchat]]` — use core Snapchat OSINT (Snap Map, username/QR checks) to establish and enrich the account, and this Bitmoji-diff technique as the passive activity monitor layered on top.

## Trust & verifiability
`trust: community` — a documented technique from a respected OSINT blogger, not a vendor product. The Bitmoji image itself is authoritative (served by Snapchat), but the *inference* (activity from change) is probabilistic — corroborate with other liveness signals before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | viewing-bitmoji-changes |
| category | image-video-face |
| selectorsIn → selectorsOut | username → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
