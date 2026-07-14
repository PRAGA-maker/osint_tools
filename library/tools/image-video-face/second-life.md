---
id: second-life
name: Second Life
description: Use when you have a `username` (Second Life resident name) or `name` and want to find a subject's virtual-world avatar profile — returns social-profile and image (avatar) leads.
url: https://secondlife.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's Second Life resident/avatar profile and picking up avatar images and in-world social connections.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to create an account and view resident profiles; land/goods cost in-world currency but are irrelevant to profile lookups.
opsec: passive
opsecNote: Viewing profiles is passive, but joining Second Life to search in-world means creating an avatar and logging in. Use a sock-puppet resident account; never contact or teleport to the target avatar.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A genuine Linden Lab virtual world, but identities are pseudonymous avatars with a deliberately weak link to real-world identity; treat any match as a soft lead.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- gravatar
- username-search
aliases:
- SecondLife
- SL resident search
tags:
- virtual-world
- avatar
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Second Life

> Linden Lab's long-running virtual world — a niche corner where a subject may maintain a pseudonymous avatar identity, community ties, and a reused username.

## When to use
Your subject is (or was) active in Second Life, or you're chasing a distinctive `username` they might have reused there. SL residents have profiles, group memberships, and avatars. If a handle from elsewhere turns up as an SL resident name, it can corroborate a persona and surface an avatar image and community connections. This is a supplementary, weak-signal source — SL deliberately separates avatar from real identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Check the web profile directly if you have a resident name (historically `secondlife.com/resident/<name>` / my.secondlife.com profiles).
2. For in-world search, create a sock-puppet SL account, log into the viewer, and use in-world Search → People for the `username`/`name`.
3. Read the profile: avatar image (`image`), "About" text, groups, and picks — often the richest real-world leakage is in the free-text bio.
4. Do NOT message, friend, or teleport to the avatar — that's visible and active.
5. Pivot: a reused resident `username` feeds username enumeration; bio text often leaks other handles or a real name.

## Inputs → Outputs
- **In:** `username` (resident name) or `name`
- **Out:** `social-profile` (resident profile), `image` (avatar), groups, bio text
- **Empty/negative result looks like:** no resident by that name, or a bare avatar with no bio — SL names are unique but reveal little unless the user chose to write real-world details.

## Gotchas & OpSec
- Human-in-the-loop: in-world search needs an **account + viewer login** — use a burner avatar.
- Avatar identity is intentionally decoupled from real identity; a match is a lead, not proof.
- The bio/"picks" free text is where real-world leakage happens — read it closely.

## Overlaps ("do both")
- Pairs with `[[username-search]]` (does the same handle exist elsewhere?) and `[[gravatar]]` (email→avatar) — use these to connect the SL persona to a broader identity graph.

## Trust & verifiability
`trust: unverified` — a legitimate platform, but pseudonymous by design. Any real-world attribution must come from corroborating details the user volunteered, not the avatar itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | second-life |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
