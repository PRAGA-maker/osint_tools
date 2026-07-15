---
id: onli-vk-ru
name: onli-vk.ru
description: Use when you have a VKontakte profile ID/name and want hidden friends, friend-list changes and derived profile data — returns associate links, social-profile insights and DOB/age.
url: https://onli-vk.ru/pivatfriends.php?id=12345
category: social-networks
path:
- social-networks
bestFor: Revealing a VK user's hidden friends and tracking friend-list changes to map their real social network.
selectorsIn:
- username
- name
selectorsOut:
- associate
- social-profile
- dob
status: live
pricing: free
costNote: Free third-party VK analysis tool (redirects to onli-vk.com); no account needed to run a lookup. Some deeper tracking features may prompt for registration.
opsec: passive
opsecNote: You submit only a public VK ID to a third-party site; the VK user is not notified. This is NOT an official VKontakte site — it derives "hidden friends" by cross-referencing public connection data, so treat its inferences as leads. onli-vk logs the IDs you query; use a clean session and don't log into your own VK there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent Russian-language VK OSINT site of unknown ownership; the "hidden friends" output is inferred, not authoritative, so corroborate any key connection against VK directly.
missingPersonsRelevance: high
coverage:
- ru
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- onli-vk.com
- VK hidden friends
tags:
- russiansocialmedia
- Russian Social Media Sites
- vk
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# onli-vk.ru

> A Russian VK analysis tool that infers a user's **hidden friends** and tracks friend-list changes — a way to reconstruct a VKontakte target's real social network.

## When to use
Your subject has a VKontakte presence and either hides their friend list or you need to map who they're actually connected to. onli-vk cross-references public VK data to surface **hidden friends**, people who hide their own lists, recently added/removed connections, and derived facts (account age, frequent photo-likers, zodiac). Strong for `associate` mapping when a VK profile is deliberately locked down.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get the target's VK ID or profile URL (e.g. `https://vk.com/id110922108`).
2. Open onli-vk (https://onli-vk.ru/ → onli-vk.com) and enter the ID/name.
3. Read the outputs: hidden/likely friends, friend-list changes over time, and derived profile data (age/creation date, frequent likers).
4. Treat inferred connections as leads and confirm each on VK itself.
5. Pivot: revealed `associate`s feed further VK/username lookups; account-creation date and frequent-liker patterns help disambiguate or corroborate identity.

## Inputs → Outputs
- **In:** VK profile ID or `name`/`username`
- **Out:** `associate` links (hidden friends, changes), `social-profile` insights, `dob`/age estimate
- **Empty/negative result looks like:** no hidden friends surfaced or an error — the profile may be genuinely sparse, fully private, or the tool may be rate-limited; absence isn't proof of no connections.

## Gotchas & OpSec
- Inferential: "hidden friends" are *derived*, not confirmed — verify each against VK before relying on it.
- Russian-language interface; primarily useful for CIS-region subjects, though VK is used globally.
- OpSec: **passive** — the subject isn't notified; just don't sign into your own VK on a third-party site.

## Overlaps ("do both")
- Pair with direct VK profile review and username-search tools — onli-vk *infers hidden connections*, while manual VK checking confirms them and pulls posts/photos the tool doesn't show.

## Trust & verifiability
`trust: unverified` — an unofficial third-party VK tool. Its derived-connection data is a lead generator, not authoritative; corroborate every important link on VKontakte itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onli-vk-ru |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → associate, social-profile, dob |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
