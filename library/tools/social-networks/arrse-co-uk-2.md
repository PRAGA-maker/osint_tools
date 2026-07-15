---
id: arrse-co-uk-2
name: arrse.co.uk (Army Rumour Service)
description: Use when you have a `username` or `name` and want to find a subject's profile on the UK's main British-Army community forum — returns their forum social-profile, post history and self-disclosed details.
url: https://www.arrse.co.uk/community/members/
category: social-networks
path:
- social-networks
bestFor: Locating a subject's account and post history on ARRSE, the large UK British-Army/military community forum.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- employer-org
status: live
pricing: free
costNote: Free to read; a registered account is generally needed to view the member directory and search members.
opsec: passive
opsecNote: Reading public threads is passive. Viewing the members list and profiles typically requires logging in, which exposes your account to the platform (and your profile becomes visible to others) — use a sock-puppet forum account, never a personal one. Do not message or interact with the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established, real UK military community forum; content is user-generated and pseudonymous, so identity and service claims are self-asserted, not verified.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
aliases:
- ARRSE
- Army Rumour Service
- arrse.co.uk
tags:
- uksocialmedia
- UK Social Media Sites
- military-forum
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# arrse.co.uk (Army Rumour Service)

> ARRSE — the large, long-running UK British-Army community forum: find a subject's pseudonymous account, read their post history, and mine self-disclosed military/personal detail.

## When to use
You have a `username` or `name` and suspect the subject has (or had) a British-Army/military connection. ARRSE members frequently reveal unit, postings, locations, timeframes, and personal circumstances in threads. Locating their account gives you a `social-profile` plus a body of posts to mine for `employer-org` (regiment/unit), locations, and reused handles — valuable in a UK missing-person or military-linked investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.arrse.co.uk/. Browsing public threads needs no login, but the member directory (https://www.arrse.co.uk/community/members/) and member search generally require a registered account.
2. Register a sock-puppet account (do not use personal details) to access member search, then look up the `username`/`name`.
3. Open the profile: note join date, post count, signature, and — most useful — click through to their post history for unit references, place names, dates, and other handles.
4. Corroborate: forum claims are self-asserted; treat "served in X regiment" as a lead, not proof.
5. Pivot: reused `username` feeds cross-platform username search; unit/location detail feeds records and mapping; other handles they mention feed direct account checks.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (forum account), `name`, `employer-org` (unit/regiment references), self-disclosed locations/timeframes
- **Empty/negative result looks like:** no member matches the handle, or a matched account with near-zero posts — an existing-but-dormant account places the person nowhere and reveals nothing.

## Gotchas & OpSec
- Human-in-the-loop: viewing members/searching needs a login; use a compartmentalized sock-puppet account.
- OpSec: reading is passive, but logging in and viewing profiles can make your presence visible; never interact with or contact the subject.
- Pseudonymous, user-generated content: unit and identity claims are unverified and sometimes bravado — corroborate before relying.

## Overlaps ("do both")
- Pairs with general username tooling and other UK-forum sources, since a military-adjacent subject often reuses the same handle across forums that ARRSE alone won't cover.

## Trust & verifiability
`trust: community` — ARRSE is a genuine, established community forum, but posts are pseudonymous and self-reported, so its value is as a rich lead source to corroborate, not as an authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arrse-co-uk-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
