---
id: telegram
name: Telegram
description: Use when you have a `username`, `phone` or channel link and want Telegram intelligence — returns `social-profile`, `associate` links and public channel/group content.
url: https://telegram.org/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Resolving Telegram usernames/phone numbers to accounts and mining public channels and groups for a subject and their network.
selectorsIn:
- username
- phone
- name
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Free app and API. A phone number is required to create the account you investigate from; the Bot API needs a free token.
opsec: active
opsecNote: Two footprints to manage. (1) Viewing PUBLIC channels/usernames via t.me web preview is passive. (2) Anything from an account — resolving a phone by importing it to contacts, joining a group, viewing a profile — happens as YOUR account and can expose it (Telegram shows "last seen", contacts see you). Always operate from a dedicated sock-puppet account on a burner number, lock down your own privacy settings first, and never use your real account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: The platform is genuine; the content is user-generated and often anonymous/disinfo-heavy. Treat channel claims and profile fields as unverified leads.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- Telegram
- t.me
tags:
- instant-messaging
- Social Media
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Telegram

> A massive messaging platform with sprawling public channels and groups — a top-tier OSINT source for username/phone resolution, network mapping, and monitoring communities a subject frequents.

## When to use
Your subject has a `username`, a `phone` number, or is linked to a Telegram channel/group. Telegram is central to many investigations because: public channels and groups are openly readable; usernames resolve via `t.me/username`; a phone number in your contacts can reveal the linked account/username; and group membership/message history maps a person's associates and interests. Especially relevant for CIS-region subjects, activism, crime, and crypto communities.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Passive first:** open `https://t.me/<username>` or `https://t.me/s/<channel>` in a browser to preview a public profile/channel with no account.
2. From a **sock-puppet account on a burner number** (privacy settings hardened): resolve a `phone` by adding it to contacts — if an account exists, Telegram shows the username/name.
3. Join relevant public groups/channels to read history and enumerate members and their handles; note who the subject interacts with.
4. For scale, use the Bot API (free token) or established Telegram-OSINT tools to search/collect public channel data.
5. Pivot: a resolved username feeds `[[sherlock]]`/`[[whatsmyname]]`; a profile photo feeds reverse-image; associates and channels feed further mapping.

## Inputs → Outputs
- **In:** `username` / `phone` / `name` / channel link
- **Out:** `social-profile` (account), `username`, `associate` (group members, interactions), public channel/group content and media
- **Empty/negative result looks like:** `t.me/username` shows "user not found"; a phone import reveals no account — the person may not use Telegram, uses a username-only privacy setting, or blocks contact discovery. Absence is not proof.

## Gotchas & OpSec
- **Active risk:** account-side actions (phone resolution, joining, profile views) expose your sock puppet — harden its privacy, use a burner number, never your real account.
- Content is user-generated and heavy with anonymity/disinfo — corroborate everything; channel admins can edit/delete history.
- Phone→username discovery depends on the target's "who can find me by number" setting and can fail silently.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/`[[whatsmyname]]` (spread a resolved username) and phone-OSINT tools — Telegram links a phone to a live handle and a network, those extend the identity across platforms.

## Trust & verifiability
`trust: unverified` — an authentic platform carrying unverified, frequently anonymous content; account/username resolution is reliable signal, but channel and profile *claims* must be independently corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, phone, name → social-profile, username, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
