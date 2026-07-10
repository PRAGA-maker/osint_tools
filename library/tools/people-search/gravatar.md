---
id: gravatar
name: Gravatar
description: Use when you have an `email` (or its MD5 hash) or a Gravatar `username` and want the linked public avatar and profile — returns a profile photo, display name, and any linked social/websites the person published.
url: https://en.gravatar.com
category: people-search
path:
- people-search
bestFor: Turning an email into a public avatar photo, display name, and self-listed links via its Gravatar profile.
selectorsIn:
- email
- username
selectorsOut:
- image
- social-profile
- name
status: live
pricing: free
costNote: Free public service (owned by Automattic/WordPress.com); no account needed to view a profile.
opsec: passive
opsecNote: Passive — you look up a hash/handle against Gravatar's public API, never contacting the subject. Querying the profile URL or `/avatar/<md5>` leaks nothing to the account owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Automattic; the avatar/profile is authentic Gravatar data, though profile fields (links, name) are self-published by the user and only as complete as they chose.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Globally Recognized Avatar
- gravatar.com
tags:
- people-search
- avatar
- email-osint
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Gravatar

> The avatar service behind WordPress and countless comment systems — an `email` (hashed) or Gravatar handle resolves to a public profile photo, display name, and whatever links the person chose to publish.

## When to use
You have an `email` and want to put a face and name to it. Because millions of sites use Gravatar for comment/forum avatars, a target's email often has a Gravatar profile exposing a photo (for face search), a display `name`, and self-listed social/website links. It's one of the quickest, most passive email→identity pivots available.

## How to use it (`bestInteractionPattern`: web-manual)
1. Compute the lowercase-trimmed MD5 (or SHA-256) hash of the target `email`.
2. View the profile: open `https://en.gravatar.com/<hash>` (append `.json` or `.vcf` for structured data), or just try a known Gravatar `username` at `gravatar.com/<username>`.
3. Fetch the avatar directly at `https://www.gravatar.com/avatar/<hash>?d=404` — a 404 means no Gravatar; an image means one exists.
4. Read the profile: photo (`image`), display `name`, bio, and any linked accounts/websites (`social-profile`).
5. Pivot: run the avatar through face/reverse-image search (`[[pimeyes]]`); follow the self-listed links to other platforms.

## Inputs → Outputs
- **In:** `email` (as MD5/SHA-256 hash) or Gravatar `username`
- **Out:** profile `image` (avatar), display `name`, bio, linked `social-profile`s/websites
- **Empty/negative result looks like:** `avatar/<hash>?d=404` returns 404 and the profile page 404s — the email has no Gravatar. That's common; absence just means they never set one up.

## Gotchas & OpSec
- Profile fields are self-published — links and name may be old, aliased, or absent even when an avatar exists.
- The hash is one-way but trivially brute-forceable for common addresses; you must know/guess the exact email to look it up (Gravatar doesn't reverse hash→email for you).
- A default/identicon avatar (mystery-person, retro pattern) means no real photo was set — not a usable face.
- Fully passive; the lookup never touches the subject.

## Overlaps ("do both")
- Pairs with `[[google-account-finder-epieos]]` and `[[account-live-com]]` — each turns an email into a different provider's profile/photo; run all three.
- Feed the avatar into `[[pimeyes]]`/`[[face-recognition]]`; feed listed handles into `[[snoop]]`/`[[gaddr]]`.

## Trust & verifiability
`trust: trusted` — the avatar and profile are authentic first-party Gravatar data from Automattic. The caveat is completeness: profile text/links are user-supplied, so treat those as leads while the existence of the avatar itself is reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gravatar |
| category | people-search |
| selectorsIn → selectorsOut | email, username → image, social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
