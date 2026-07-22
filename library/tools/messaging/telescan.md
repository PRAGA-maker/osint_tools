---
id: telescan
name: Telescan
description: Use when you have a Telegram `username`, user ID, or a `phone` already in your contacts and want to discover which shared groups a user is in (and enumerate members) — returns social-profile, associate.
url: https://github.com/pielco11/telescan
category: messaging
path:
- messaging
bestFor: Mapping which Telegram groups a known user shares with you and enumerating members of groups you're in.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free, open-source (MIT); requires your own free Telegram API credentials from my.telegram.org.
opsec: active
opsecNote: This runs under YOUR Telegram account and can only see groups you are a member of — so joining a target's group to scan it is an active, potentially observable act (admins see joins/members). Run it from a dedicated sock-puppet Telegram account and number, never your real identity, and be aware phone-based lookup only works if the number is already in that account's contacts.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source Python tool by pielco11 (~240 stars, MIT); results come directly from Telegram's API via your session, so accuracy is Telegram's own.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- telescan
tags:
- telegram
- messengers
- group-enumeration
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Telescan

> A Python CLI that leverages your own Telegram session to answer "which of my shared groups is this user in?" and to enumerate members of groups you belong to.

## When to use
You have a Telegram `username` or user ID (or a `phone` that's already saved in the scanning account's contacts) and want to place that person socially on Telegram — which groups you share with them, or who else is in a group you can see. Useful for building an `associate` graph around a subject who is active on Telegram.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/pielco11/telescan` and install the Python requirements.
2. Get free API credentials at https://my.telegram.org and put `api_id`/`api_hash` into `api_creds.ini` — ideally under a dedicated sock-puppet account.
3. Run the tool against a target `username`/ID; it checks the groups your account is in and reports shared membership, or enumerates members of a specified group.
4. Read the output: shared groups for a user, or member lists (usernames/IDs) for a group — a `social-profile` and `associate` map.
5. Pivot: discovered usernames feed username-OSINT; shared-group topics hint at the subject's interests/location.

## Inputs → Outputs
- **In:** `username` or Telegram user ID; `phone` only if it's already in the account's contacts
- **Out:** `social-profile` (Telegram presence/shared groups), `associate` (co-members)
- **Empty/negative result looks like:** no shared groups (you don't co-belong to any group with the target) — a hard limit, not proof they're inactive; you can't see groups you haven't joined, and channel members are invisible unless you're an admin.

## Gotchas & OpSec
- Fundamental constraint: **"to know if a user is in a group, you have to be in that group too."** Joining a target's group to scan it is observable.
- Phone lookup requires the number to already be a contact — it does not resolve arbitrary phone numbers to accounts.
- Human-in-the-loop: Telegram login + API keys required.
- OpSec: **active** — everything runs as your logged-in account; use a burner account/number and expect group admins to see your presence.

## Overlaps ("do both")
- Pairs with other Telegram OSINT tools that resolve usernames/IDs to profile metadata — Telescan adds the group-membership/social layer those don't cover, provided you share groups with the target.

## Trust & verifiability
`trust: community` — an open-source MIT tool, but the data is Telegram's own (pulled through your session), so results are as authoritative as Telegram's API; the tool merely orchestrates the queries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telescan |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
