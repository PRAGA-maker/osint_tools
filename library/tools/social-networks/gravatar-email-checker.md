---
id: gravatar-email-checker
name: Gravatar Email Checker
description: Use when you have an `email` and want to know if it has a Gravatar profile/avatar — returns a linked avatar image, public profile, and reused-identity leads.
url: https://en.gravatar.com/site/check/
category: social-networks
path:
- social-networks
bestFor: Turning an email into a face (avatar) and a public Gravatar profile that often links other accounts.
selectorsIn:
- email
selectorsOut:
- image
- social-profile
- name
status: live
pricing: free
costNote: Free; no account needed to check an address. Gravatar is operated by Automattic (WordPress.com).
opsec: passive
opsecNote: Gravatar is keyed on the MD5/SHA-256 hash of the lowercased email; checking is a passive read against Gravatar's public API and never contacts the subject. Nothing is sent to the email owner. Standard sock-puppet browsing is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Automattic service; a returned avatar/profile is authentic to the address, though the profile fields are self-entered by the user.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- Gravatar
- Gravatar Email Checker
tags:
- bellingcat-toolkit
- other-platforms
- email-to-image
source: bellingcat-toolkit
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- gravatar
---

# Gravatar Email Checker

> Feed it an email and it may hand back the person's face — Gravatar links an avatar (and often a public profile with other accounts) to any address someone registered.

## When to use
You have an `email` and want to attach an identity to it. Gravatar (the avatar service behind WordPress and thousands of blogs/forums) maps an email hash to a globally-reused avatar. A hit gives you a photo (`image`) to reverse-search and frequently a public Gravatar profile page listing the person's name, location, and links to their other social accounts — one of the cleanest email→person pivots available.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://en.gravatar.com/site/check/` and enter the `email`.
2. If an avatar returns, the address has a Gravatar — open the associated profile at `gravatar.com/<username-or-hash>`.
3. Read the profile: display name, bio, location, and "Accounts"/links the person added (their other platforms).
4. Save the avatar for reverse-image search.
5. Pivot: the avatar → `[[yandex-images]]`; linked accounts → their profiles; the name → people-search. (Programmatically: `gravatar.com/avatar/<hash>` and the profile JSON at `gravatar.com/<hash>.json`.)

## Inputs → Outputs
- **In:** `email`
- **Out:** `image` (avatar), `social-profile` (Gravatar profile + linked accounts), `name`
- **Empty/negative result looks like:** the default/mystery-person avatar and no profile — the address has no Gravatar. That's not proof the person doesn't exist, only that this email isn't registered with Gravatar.

## Gotchas & OpSec
- Gravatar is email-hash based, so it works even from just the address — but only if the person ever set one up (common among bloggers/developers, rarer for the general public).
- Profile fields are self-entered; the avatar is the most reliable output, the linked-accounts list the most valuable.
- OpSec: fully **passive** — hashed lookup, no contact with the subject.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` and email-permutation/verification tools — the permutator/verifier finds the real address, Gravatar turns that address into a face and a profile, reverse-image spreads the face across the web.

## Trust & verifiability
`trust: trusted` — first-party Automattic service, so an avatar/profile genuinely belongs to that address's registration; treat the self-entered profile text as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gravatar-email-checker |
| category | social-networks |
| selectorsIn → selectorsOut | email → image, social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
