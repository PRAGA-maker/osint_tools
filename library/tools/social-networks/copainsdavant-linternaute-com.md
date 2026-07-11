---
id: copainsdavant-linternaute-com
name: Copains d'avant
description: Use when you have a `name` and a French school/town and want to place a subject via their old-classmates profile — returns social-profile, schools/employers, and location.
url: https://copainsdavant.linternaute.com/
category: social-networks
path:
- social-networks
bestFor: Finding a French subject through a classmates/alumni network keyed on schools, towns, and employers.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
- geolocation
- name
status: live
pricing: free
costNote: Free to search; a free registration (identity + schools attended) is required to view full member profile details.
opsec: passive
opsecNote: Name search is passive. Viewing full profiles requires an account, which makes you a logged-in member — use a sock-puppet registration, never your real identity, and avoid any "get in touch" action that would notify the member.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established French network run by CCM Benchmark; profile data is self-reported by members and unverified.
missingPersonsRelevance: high
coverage:
- fr
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Copains d'avant
- copainsdavant.linternaute.com
tags:
- esocialmedia
- European Social Media Sites
- france
- alumni-network
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Copains d'avant

> France's answer to Classmates/Friends Reunited — millions of French profiles indexed by the schools people attended and the towns and firms they worked in.

## When to use
You have a `name` for a French subject and want to anchor them to a place and a life-timeline: which primary/middle/high school and university they attended, what town, and which employers. For a French missing-person or background case, Copains d'avant often has a profile where Facebook/LinkedIn do not, and its school/location anchors are strong disambiguators for a common name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://copainsdavant.linternaute.com/` and search the `name` (you can filter by town/school).
2. Scan the result list; open candidate profiles.
3. To see full details you must be logged in — register a **sock-puppet** account (it asks for an identity and schools). Then read: schools with years, town, employers (`employer-org`), photos.
4. Cross-reference the school/year and town against other sources to confirm you have the right person.
5. Pivot: an employer or school + year feeds people-search and alumni corroboration; the town feeds address/records searches (`geolocation`).

## Inputs → Outputs
- **In:** `name` (best with a town or school)
- **Out:** `social-profile`, `employer-org`, `geolocation` (town/school), `name`
- **Empty/negative result looks like:** no matching members, or matches with no schools/town filled in — the network has no usable profile for that name. Common French names return many candidates; use school/town to narrow.

## Gotchas & OpSec
- Human-in-the-loop: full profiles need a login — register a burner, never your real account.
- The audience skews older/2000s-era, so a young subject may be absent while their parents/relatives are present (still useful for family mapping).
- OpSec: search is **passive**; do not use any "reconnect"/message feature, which alerts the member. Interface is French.

## Overlaps ("do both")
- Pairs with mainstream people-search and `[[copainsdavant-linternaute-com]]`-adjacent European directories — this one's school/employer anchors disambiguate common names that generic search collapses together.

## Trust & verifiability
`trust: community` — a real, established network, but every profile field is self-entered by the member and unverified; treat school/town/employer as strong leads to confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copainsdavant-linternaute-com |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, employer-org, geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
