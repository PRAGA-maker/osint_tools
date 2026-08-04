---
id: clubhouse-database
name: Clubhouse Database
description: Use when you have a `username`/`name` on the Clubhouse audio app and want their profile stats, bio and club memberships — returns `social-profile` details.
url: https://clubhousedb.com/
category: social-networks
path:
- social-networks
bestFor: Looking up a Clubhouse user's follower stats, bio, registration date and clubs from a public third-party index.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free community analytics site ("first free Clubhouse analytics tool"); no login stated.
opsec: passive
opsecNote: This is a third-party index, so you query clubhousedb.com rather than the Clubhouse app itself — the subject is not notified and never sees your lookup. Fully passive; still use a sock-puppet browser as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, unaffiliated with Clubhouse/Alpha Exploration Co. Data is scraped/cached, so it can be stale — Clubhouse's own decline since 2021 means freshness is not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- clubhousedb.com
- ClubhouseDB
tags:
- social-networks
- clubhouse
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Clubhouse Database

> A third-party analytics index of Clubhouse (the audio social app) — look up a user or club without touching the app.

## When to use
You have a `username` or `name` you suspect is on Clubhouse and want profile context: follower/following counts, bio text, registration date, and which clubs they belong to. Because Clubhouse itself is invite-history-heavy and app-gated, this external index lets you check a handle and read bio/affiliation data passively. Bio text and club memberships are the useful bits — they can yield real names, locations, employers, or links to other platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://clubhousedb.com/.
2. Search for the `username` or `name`; you can also browse "Most Followed Users" and "Most Popular Clubs" for context.
3. Open the matching profile and read the details: follower/following counts, bio, registration date, club memberships.
4. Mine the bio and club list for pivotable selectors — a real `name`, a city, an employer, or a linked handle.
5. Pivot: run any recovered handle/name through cross-platform username search; feed a stated location/employer into the relevant people-search tools.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (follower stats, bio, registration date, club memberships) and any real `name` disclosed in the bio
- **Empty/negative result looks like:** no matching user in the index, or a sparse/stale record. Absence here means "not indexed," not "not on Clubhouse" — the index is a cached subset, not the full platform.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you never touch the Clubhouse app or alert the subject.
- **Staleness is the main risk:** Clubhouse peaked in 2020–2021 and has declined sharply; cached figures and profiles may be years out of date. Treat data as historical unless corroborated.

## Overlaps ("do both")
- Pairs with cross-platform username-search tools — Clubhouse Database gives the in-app profile/club context that generic username sweeps miss, while those confirm the same handle across other networks.

## Trust & verifiability
`trust: community` — an independent, unaffiliated project working from scraped data. Useful as a lead source, but verify anything material (name, location, affiliation) against a live, primary source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clubhouse-database |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
