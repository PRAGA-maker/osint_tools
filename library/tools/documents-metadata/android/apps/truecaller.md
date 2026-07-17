---
id: truecaller
name: Truecaller
description: Use when you have a `phone` number and want a crowd-sourced caller-ID name — returns the name/label others have saved for that number plus carrier/region and spam reports.
url: https://www.truecaller.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
bestFor: Resolving an unknown phone number to a crowd-sourced name and spam reputation.
selectorsIn:
- phone
selectorsOut:
- name
status: live
pricing: freemium
costNote: Free tier (with account) allows limited lookups; heavier use, name-search, and "who searched me" features push Premium. Web/search access is gated behind login.
opsec: active
opsecNote: Truecaller is account-bound and can be intrusive - searches are tied to your Truecaller identity, the person you look up may (with some settings/premium) be able to see they were searched, and installing the app uploads your address book. Use a dedicated sock-puppet account and a burner device/number; never log in with your real identity or contacts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Caller-ID data is crowd-sourced from users' address books and community spam tags — often right, but the "name" is whatever contacts saved, so it can be a nickname, a business, or wrong. Corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- true-caller
- truecaller-com
aliases:
- True Caller
tags:
- phone
- caller-id
- spam
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Truecaller

> The big crowd-sourced caller-ID database — put in a number, get back the name the crowd has saved for it. Powerful for `phone`→`name`, but account-bound and intrusive.

## When to use
You have a `phone` number and no name. Truecaller aggregates hundreds of millions of users' address books plus community spam tags, so a lookup frequently returns the name (or business) that contacts have saved for that number, the carrier/region, and whether it's been flagged as spam/scam. High-value for identifying an unknown number in a missing-persons or fraud context.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Set up a **sock-puppet** Truecaller account on a burner device/number — never your real phone or contacts (the app harvests your address book).
2. Search the target `phone` number in the app (or the login-gated web search).
3. Read the result: the crowd-sourced `name`/label, carrier and region, and any spam reports/tags.
4. Treat the name as a lead — it's whatever contacts saved, which may be a nickname, a relative's label, a business, or stale. Corroborate before relying on it.
5. Pivot: the recovered `name` → people-search and social tools; carrier/region → narrows geography; spam tags → context on how the number is used.

## Inputs → Outputs
- **In:** `phone` number
- **Out:** crowd-sourced `name`/label, carrier + region, spam reputation
- **Empty/negative result looks like:** "no name found" / only a spam score — the number isn't in enough address books, or has privacy protections. Absence of a name doesn't mean the number is unused or invalid.

## Gotchas & OpSec
- **Active and identity-bound:** lookups tie to your Truecaller account; some settings/premium let the searched party learn they were searched. Use a burner identity, always.
- Installing the app **uploads your contacts** — only ever run it on a clean device with no real address book.
- The name is crowd-sourced, not authoritative: it can be wrong, outdated, a business, or a mislabel. Never treat a single Truecaller name as identity confirmation.

## Overlaps ("do both")
- Do both with other phone-intel tools (carrier/HLR lookups, `[[account-live-com]]`-style existence checks, messaging-app profile lookups) and a people-search once you have a name. Truecaller gives the crowd's label; the others verify and enrich it.

## Trust & verifiability
`trust: community` — the data is user-contributed caller ID and community spam tagging; the aggregate spam signal is strong, but any individual name is unverified and must be corroborated against an independent source before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truecaller |
| category | documents-metadata |
| selectorsIn → selectorsOut | phone → name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
