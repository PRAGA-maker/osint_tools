---
id: sn0int-framework-module-for-pornhub
name: sn0int module for Pornhub
description: Use when you have a Pornhub `username`/profile and want its linked identities — returns the display `name`, linked `social-profile`s (Instagram, Twitter, Snapchat, ModelHub, FanCentro) and online status, via the sn0int OSINT framework.
url: https://sn0int.com/r/kpcyrd/pornhub
category: social-networks
path:
- social-networks
bestFor: Pivoting a Pornhub profile to its linked mainstream social accounts inside the sn0int framework.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free, open-source (GPL-3.0) module for the free sn0int framework; you self-host sn0int.
opsec: passive
opsecNote: The module fetches the target's PUBLIC Pornhub profile from YOUR IP with no login; the account owner is not notified. Requests originate from you, so run sn0int behind a VPN/sock-puppet, especially given the sensitive platform.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community module in kpcyrd's well-regarded open-source sn0int framework; it parses public profile HTML, so it breaks if Pornhub changes its page structure.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- sn0int pornhub module
- kpcyrd/pornhub
tags:
- Social Media
- Pornhub
- sn0int
- username-pivot
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# sn0int module for Pornhub

> A sn0int module that turns a Pornhub username into a cross-platform identity map — pulling the profile's display name and the mainstream social accounts it links out to.

## When to use
You have a Pornhub `username` (or you've found one during an investigation) and need to connect it to the person's other identities. Adult-platform profiles frequently link to the same person's Instagram, Twitter/X, Snapchat, ModelHub or FanCentro — a strong pivot from a pseudonymous handle toward mainstream, often real-name accounts. This module automates that extraction inside the sn0int framework so results land in sn0int's linked-entity database.

## How to use it (`bestInteractionPattern`: cli)
1. Install the sn0int framework (kpcyrd's OSINT framework) and add this module: `sn0int add kpcyrd/pornhub`.
2. Seed the target `username`/profile as input in sn0int's database.
3. Run the module against it; it fetches the public profile and parses:
   - the display `name`,
   - linked `social-profile`s (Instagram, Twitter, Snapchat, ModelHub, FanCentro),
   - online status and last-seen, storing them as linked entities.
4. Read sn0int's database for the newly linked accounts.
5. Pivot: each linked social handle feeds username-enumeration and platform-specific OSINT — often the fastest route from a pseudonymous adult handle to a real identity.

## Inputs → Outputs
- **In:** `username` / Pornhub profile URL
- **Out:** display `name`, linked `social-profile`s, online/last-seen status
- **Empty/negative result looks like:** the profile has no linked socials (many don't), is private/removed, or the module errors because Pornhub changed its markup — check for an updated module version.

## Gotchas & OpSec
- Parses **public profile HTML**, so it's brittle: a site redesign can break it until the community updates the module.
- Only surfaces links the user *chose* to publish on their profile; absence of links isn't proof of none elsewhere.
- OpSec: **passive** but requests come from **your** IP against a sensitive platform — always use a VPN/sock-puppet.

## Overlaps ("do both")
- Pairs with username-enumeration tools (Sherlock/Maigret-style) — this extracts the *declared* links; enumeration tests the handle across many other platforms the profile doesn't mention.

## Trust & verifiability
`trust: community` — a community module in the reputable open-source sn0int framework. It reports exactly what the public profile links to, so verify each surfaced account is genuinely the same person before merging identities.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sn0int-framework-module-for-pornhub |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
