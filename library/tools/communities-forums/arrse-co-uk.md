---
id: arrse-co-uk
name: ARRSE (Army Rumour Service)
description: Use when a subject has a British Army/UK military connection and you have a `username` or `name` — a large UK military forum; returns posts, `social-profile` history, and community leads.
url: https://www.arrse.co.uk/community/forums/
category: communities-forums
path:
- communities-forums
bestFor: Searching a large British-military community forum for a member's posts, handle history, and military/regimental context.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read; registration/login required to post and to see some content.
opsec: passive
opsecNote: Reading public threads is passive. Registering or posting is active and leaves a footprint in a tight-knit, security-aware community — use a sock-puppet account, never engage the subject, and expect members to notice unusual accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, well-known British Army community forum; genuine user content, but pseudonymous, opinionated, and full of in-jokes/rumour — treat posts as leads.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Army Rumour Service
- ARRSE
tags:
- forums
- uk
- military
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ARRSE (Army Rumour Service)

> The big British-Army community forum — mine a member's post history and regimental context for a military-linked subject.

## When to use
Your subject is (or claims to be) connected to the British Army/UK military and you have a `username` or `name`. ARRSE is a large, active forum where members discuss units, deployments, and each other — posts can reveal service history, locations, timelines, relationships, and whether a "veteran" claim holds up (the community actively calls out "Walts"/impostors).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.arrse.co.uk/community/forums/.
2. Use the forum search (or Google `site:arrse.co.uk "<username or name>"`) to find posts and profiles.
3. Read the output: a member's post history, join date, and threads referencing the person/unit. Note self-disclosed details.
4. Pivot: reuse the handle across platforms; corroborate service claims against official/records channels; follow named units/people.

## Inputs → Outputs
- **In:** a `username` or `name` (ideally with a military angle)
- **Out:** the member's `social-profile`/post history and related threads
- **Empty/negative result looks like:** no posts under a handle means it's unused here or content was deleted — try `site:` search and alternate handles.

## Gotchas & OpSec
- Pseudonymous, rumour-heavy content and dark humour — verify anything factual elsewhere.
- Security-aware community: sock-puppet accounts and unusual activity get noticed; reading is safer than engaging.
- Human-in-the-loop: some content needs a logged-in account.

## Overlaps ("do both")
- Do both with username-enumeration and official military-records channels — ARRSE gives community context; those confirm identity and service.

## Trust & verifiability
`trust: community` — genuine but pseudonymous forum; treat posts as leads and verify service claims through authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arrse-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
