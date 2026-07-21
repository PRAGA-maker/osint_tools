---
id: new-york-post
name: New York Post
description: Use when you have a `name` linked to New York or a tabloid-worthy event and want fast, name-heavy coverage — returns `associate`, `address` and event context from published articles.
url: https://nypost.com
category: communities-forums
path:
- communities-forums
bestFor: Finding NYC-area and national tabloid coverage that names people, neighborhoods and case details.
selectorsIn:
- name
selectorsOut:
- associate
- address
status: live
pricing: free
costNote: Free to read and search; ad-supported, no hard paywall on most articles.
opsec: passive
opsecNote: Searching and reading a public news site transmits nothing about your subject. Fully passive; a private window avoids personalisation cookies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running US tabloid daily (News Corp). Reports quickly and names people/locations freely, but is sensational — treat specifics as leads to verify against primary records.
missingPersonsRelevance: medium
coverage:
- us
aliases:
- NY Post
- nypost.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# New York Post

> A fast, tabloid-style US daily strongest on New York — it names names, neighborhoods, and case details other outlets soften or omit.

## When to use
Your subject is tied to the New York metro area, or to a crime, court case, accident, or scandal that a tabloid would cover. The Post is useful precisely because it publishes quickly and includes specifics — full names, ages, neighborhoods/streets, employers, and the people around a subject (family, victims, witnesses) — that can seed a search. Also good for national "true-crime"-style stories.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nypost.com and use site search, or run: `site:nypost.com "Full Name"`.
2. Read matching articles for the person's age, neighborhood/address, employer, and named associates.
3. Note the date and any court/precinct details for follow-up in official records.
4. Because it is sensational, verify every hard fact (charges, addresses, relationships) against a primary source before relying on it.
5. Pivot: named associates feed people-search; a neighborhood/street narrows address searches; a case detail feeds court-record lookups.

## Inputs → Outputs
- **In:** `name` (NY-area or notable event)
- **Out:** `associate` (people named alongside the subject), `address`/neighborhood, event & date context
- **Empty/negative result looks like:** no article matches — the person wasn't covered here; try local NY outlets and national news before concluding no coverage.

## Gotchas & OpSec
- Tabloid: sensational framing and occasional inaccuracy — corroborate specifics against primary records.
- NY-weighted; strongest for metro-area subjects.
- Fully passive — searching leaks nothing.

## Overlaps ("do both")
- Pairs with more measured outlets and court-record tools — the Post surfaces names and vivid detail fast, while primary records confirm the facts it asserts.

## Trust & verifiability
`trust: community` — an established but sensational tabloid; reliable that a story ran and roughly who was named, but verify hard facts (charges, addresses, ages) against authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-post |
| category | communities-forums |
| selectorsIn → selectorsOut | name → associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
