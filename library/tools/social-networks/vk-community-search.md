---
id: vk-community-search
name: VK Community Search
description: Use when you have a keyword, place or interest (`name`) and want to find VKontakte groups/communities a subject may belong to — returns social-profile communities and associate members.
url: http://vk.com/communities
category: social-networks
path:
- social-networks
bestFor: Searching VKontakte communities/groups by keyword to find the groups tied to a person, place, event or interest and their members.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to use; VK increasingly requires a logged-in account to search and view communities fully.
opsec: active
opsecNote: Browsing communities from a logged-in VK account can leave a footprint (VK logs activity, and joining a group is visible). Use a sock-puppet VK account with a burner number; do not join or interact with target communities from an attributable profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party VKontakte functionality (the platform's own community search); the community data is authoritative platform data, though members' identities are self-asserted.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: false
aliases:
- VK groups search
- VKontakte communities
- vk.com/communities
tags:
- vkontakte
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- community-search
- get-user-info
- item
- people-search-results-vk
- vk
- vk-com
- vk-com-2
- vk-people-search
---

# VK Community Search

> VKontakte's own community/group search — find the groups tied to a place, employer, school, event or interest, and mine their membership to locate or contextualise a subject.

## When to use
You're investigating someone with a Russian / former-Soviet-space connection and want to find communities they're likely part of: their town, university, workplace, hobby, or a specific event. VK is the dominant Russian social network, and its groups are a rich source — membership lists surface `associate`s, and a niche local group can reveal a subject's affiliations even when their personal profile is locked. Start from a keyword (`name` of a place/org/interest) and enumerate matching communities (`social-profile`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet VK account, then go to https://vk.com/communities (or use VK's global search filtered to "Communities").
2. Search by keyword — a town, school, employer, event, hashtag or interest tied to the subject.
3. Sort/filter results and open promising groups; browse posts and, where visible, the member list.
4. Cross-reference members against your subject's `name`/`username`, or use a known community to find the subject among its members.
5. Pivot: member profiles become `associate` leads; a group's location/topic corroborates the subject's ties; a subject's own listed groups (from their profile) map their affiliations.

## Inputs → Outputs
- **In:** keyword — a place/org/interest (`name`), or a `username` to locate within groups
- **Out:** `social-profile` (matching communities and their pages), `associate` (visible members)
- **Empty/negative result looks like:** no relevant communities, or groups whose membership is hidden — VK privacy settings and closed groups limit member visibility, so absence is not conclusive.

## Gotchas & OpSec
- **Login increasingly required:** VK gates more search/community features behind an account; use a puppet.
- Member lists are often hidden for closed/private groups; you may see the group but not who's in it.
- **Active:** joining or interacting is visible to admins/members — browse, don't join, from a puppet.

## Overlaps ("do both")
- Pairs with VK profile/people search and `[[findclone]]` (face → VK profile) — use community search to map affiliations and members, then face/profile tools to pin a specific individual.

## Trust & verifiability
`trust: trusted` — it is VK's first-party community search, so the group data is authoritative; individual members' claimed identities still need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk-community-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
