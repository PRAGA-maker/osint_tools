---
id: khalil-shreateh-social-applications
name: Khalil Shreateh Social Applications
description: Use when you have a social `username` and want quick enrichment — profile-picture full-view, ID lookup, post/account timestamps, TikTok username→email — returns `image`, sometimes `email`, and account-age/timestamp metadata.
url: https://khalil-shreateh.com/khalil.shtml/social_applications/
category: social-networks
path:
- social-networks
bestFor: A grab-bag of free web utilities for Facebook/Instagram/TikTok/Twitter — profile-pic viewers, ID lookups, timestamp/account-age checkers, downloaders and a TikTok username-to-email tool.
selectorsIn:
- username
selectorsOut:
- image
- email
status: live
pricing: freemium
costNote: Free browser tools (ad-supported). No account for most utilities.
opsec: passive
opsecNote: Passive toward the target — the utilities query public platform data/APIs, not the subject, and viewing a profile picture via a third-party viewer avoids visiting the profile directly. But you are handing the target's handle to a third-party site; assume it may log queries, so avoid entering anything sensitive and don't rely on it for anonymity-critical work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Personal tool site of security researcher Khalil Shreateh; utilities are free and generally functional but unvetted, ad-heavy, and dependent on platform APIs that break — verify outputs elsewhere.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- facebook-applications-khalil-shreateh
aliases:
- Khalil Shreateh social tools
tags:
- Social Media
- Universal
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Khalil Shreateh Social Applications

> A 20+ tool grab-bag of free social-media web utilities — the useful OSINT bits are the profile-picture full-viewers, ID/timestamp lookups, and the TikTok username→email tool.

## When to use
You have a social `username` (Facebook, Instagram, TikTok, or Twitter/X) and want fast, low-friction enrichment without installing anything: pull the full-resolution profile picture, resolve a numeric ID, check when an account was created or a post was published, or try to surface a linked email. Handy for a quick pass before reaching for heavier, more reliable tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the social_applications index and pick the utility for the platform/task (e.g. "Instagram profile picture viewer," "Twitter account creation date," "TikTok username to email").
2. Enter the target `username` (or profile URL/ID as the tool asks).
3. Read the output — full-res profile image, numeric ID, creation/timestamp, or a candidate email.
4. **Verify elsewhere**: confirm any email against `[[account-live-com]]`-style existence checks and reverse-image the profile pic before trusting it.
5. Pivot: a full-res `image` feeds face/reverse-image search; a candidate `email` feeds email OSINT.

## Inputs → Outputs
- **In:** `username` (or profile URL/ID)
- **Out:** profile `image` (full view), sometimes a linked `email`, plus account-age/post timestamps
- **Empty/negative result looks like:** a tool errors, returns nothing, or gives an obviously wrong value — likely a platform API change broke it; treat as unavailable, not as a negative finding.

## Gotchas & OpSec
- **Third-party & unvetted**: you're feeding handles to a personal ad-supported site; assume queries may be logged — don't use for anonymity-critical targets.
- Tools break when platforms change APIs; outputs (especially "username→email") can be stale or wrong — corroborate.
- OpSec: passive toward the subject, but not private toward the tool operator.

## Overlaps ("do both")
- Pairs with `[[facebook-applications-khalil-shreateh]]` (the same author's Facebook-specific set) and with dedicated reverse-image/email tools — use these for a quick grab, then confirm in a trusted tool.

## Trust & verifiability
`trust: unverified` — a hobby/utility site by an individual researcher; convenient but unvetted and API-dependent, so every output is a lead to confirm, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | khalil-shreateh-social-applications |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
