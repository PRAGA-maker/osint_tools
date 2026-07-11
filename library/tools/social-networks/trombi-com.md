---
id: trombi-com
name: trombi.com
description: Use when you have a `name` (including a maiden name) and a French school/era and want to find the person's classmates-network profile and photos — returns a `social-profile`, `name`, and `image`.
url: https://www.trombi.com/
category: social-networks
path:
- social-networks
bestFor: Locating a French subject via their former school, class year, and class photos on a classmates reunion network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: freemium
costNote: Free to register and search; contacting members and some features require a paid ("Premium") membership.
opsec: active
opsecNote: Full search and profile viewing require a logged-in account, and viewing a profile can leave a "visitor" trace to that member. Register and browse only from a sock-puppet account with a plausible French persona; never use an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running French commercial social network (classmates/reunion niche); profiles are user-submitted, so accuracy and freshness vary.
missingPersonsRelevance: high
coverage:
- fr
auth: account
api: false
localInstall: false
registration: true
aliases:
- Trombi
- Copains d'avant competitor
tags:
- esocialmedia
- European Social Media Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# trombi.com

> France's "trombinoscope"/classmates network (~13M members, 280k+ class photos) — a way to place a French subject at a specific school and year, and to surface old photos of them.

## When to use
Your subject is French (or attended a French/francophone school) and you have a `name` — crucially, this network indexes **maiden names** and links people to a school and class year. Useful when other social networks come up empty on an older subject, or when you need a period photograph or a pre-marriage identity for someone who has since changed their name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a sock-puppet account at https://www.trombi.com/ (free; a French persona and email help).
2. Use the member/school search. Search by `name` (try maiden name), or browse to the subject's school via département → town → establishment.
3. Open candidate profiles: note the class year, school, listed `name`, and any `image` (profile or class photo).
4. Confirm identity via corroborating details (school, town, era) — do not assume a name match alone.
5. Pivot: a confirmed maiden name feeds French civil/marriage records and other people-search; a class photo aids `[[pimeyes]]`-style face search.

## Inputs → Outputs
- **In:** `name` (including maiden name) or `username`, ideally plus a school/town/era
- **Out:** `social-profile`, confirmed `name` (incl. maiden name), `image` (profile and class photos)
- **Empty/negative result looks like:** no matching member, or a profile shell with no photo/details — many members registered once and never filled in data, so a thin profile is common and not conclusive.

## Gotchas & OpSec
- Requires login to do anything useful — plan the sock puppet before you start.
- French-language interface; use translation.
- User-submitted data: names and photos can be years stale or aspirational (school listed but never attended).

## Overlaps ("do both")
- Pairs with `[[copainsdavant]]`-style French classmates sites and general people-search — each network has a different member base for the same schools, so a subject missing from one may be on the other.

## Trust & verifiability
`trust: community` — a real, established network, but every data point is member-submitted; treat a hit as a lead requiring corroboration, not a record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trombi-com |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
