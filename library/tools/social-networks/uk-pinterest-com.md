---
id: uk-pinterest-com
name: Pinterest (UK)
description: Use when you have a `username` or `name` and want a subject's Pinterest boards/pins — returns a `social-profile` whose boards leak interests, plans, locations and saved `image`s.
url: https://uk.pinterest.com/
category: social-networks
path:
- social-networks
bestFor: Reading a person's Pinterest boards to infer interests, life plans (weddings, homes, travel), locations and reused imagery.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- name
status: live
pricing: free
costNote: Public profiles and pins are viewable free; Pinterest increasingly nudges toward login, and some browsing is gated behind a free account.
opsec: passive
opsecNote: Viewing public boards is passive. Do not follow, message, or react from an attributable account — that alerts the subject. If login is required, use a sock-puppet account, never your own; avoid the "related pins" personalisation tying activity to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: uk.pinterest.com is the UK locale of the first-party Pinterest platform; board content is user-generated but the platform reliably reflects what the account saved.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pinterest
- pinterest-trends
aliases:
- uk.pinterest.com
- Pinterest UK
tags:
- pinterest
- Pinterest Related Sites
- interests
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Pinterest (UK)

> The UK locale of Pinterest — a board of saved pins is an unusually candid window into a person's interests, plans and aesthetic, often under a reused handle.

## When to use
You have a `username` or `name` and want soft-intelligence about a subject: hobbies, upcoming life events (wedding, house move, baby, travel), aesthetic and brand affinities, and sometimes location cues from local businesses or venues they pin. Pinterest users curate openly and rarely think of it as revealing, so boards frequently corroborate or extend what other platforms show.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://uk.pinterest.com/<username>/` for a known handle, or use search for a `name`.
2. Browse their boards and pins; board titles and pin clusters signal current preoccupations and plans.
3. Note self-saved photos and local/venue pins — reverse-image the photos and geolocate the venues.
4. Pivot: the avatar/photos feed reverse-image search; a reused handle feeds cross-platform username enumeration; life-event boards inform timeline and associate leads.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`, saved `image`s, confirmed `name`, and inferred interests/plans/locations
- **Empty/negative result looks like:** the profile 404s, is set to secret/private boards only, or search returns no matching person — Pinterest presence is optional and often sparse, so absence is weak evidence.

## Gotchas & OpSec
- Boards can be "secret" (owner-only) — you'll see only public ones; a thin public profile may hide a rich private one.
- Handles aren't identity-verified; corroborate before attributing a board to your subject.
- OpSec: passive while browsing; Pinterest pushes login and personalises — use a sock-puppet and don't interact.

## Overlaps ("do both")
- Pairs with reverse-image search and cross-platform username tools — Pinterest supplies saved imagery and interest signals that image search and handle enumeration then extend to other surfaces.

## Trust & verifiability
`trust: trusted` — a first-party platform reliably showing what the account saved; identity attribution rests on corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-pinterest-com |
