---
id: google-com-3
name: google.com
description: Use when you have a `name` or `username` and want to find profiles on Trombi.com (French classmates network) via a Google site-search dork — returns `social-profile` links.
url: https://www.google.com/search?q=site%3Atrombi.com&ie=utf-8&oe=utf-8&client=firefox-b-ab
category: social-networks
path:
- social-networks
bestFor: Google-dorking the French social/classmates network Trombi.com for a specific person.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Uses only Google search; free, no account needed.
opsec: passive
opsecNote: Query hits Google, not Trombi, so the subject is not alerted and you avoid creating a Trombi account. Search signed out / in a sock browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A Google `site:` dork, not a third-party tool; reliability equals Google's index of public Trombi.com pages.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: false
localInstall: false
registration: false
aliases:
- 'site:trombi.com dork'
- Trombi Google search
tags:
- esocialmedia
- European Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com

> A Google `site:trombi.com` dork that pulls public profiles out of Trombi.com — a French classmates/reunion network in the Copains d'avant vein — without registering on the platform itself.

## When to use
Your subject has a French footprint (lived, studied, or worked in France) and you want to check a regional social network that most cross-platform username tools ignore. Trombi.com connects people by school, promotion year, and workplace, so a hit can confirm a school, a graduation year, and old classmates (`associate`) — strong corroboration for identity resolution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start from the template `site:trombi.com` query and append the subject's name or username in quotes, e.g. `site:trombi.com "Prénom Nom"`.
2. Run it in Google (signed out / sock browser). Add a school name, town, or promotion year to disambiguate common names.
3. Read results — public Trombi profile and listing pages that Google has indexed.
4. Pivot: a profile yields school/employer history and classmate names; feed those into people-search and other social lookups.

## Inputs → Outputs
- **In:** `name` or `username` (quoted), optionally + school/town
- **Out:** links to public Trombi.com `social-profile` pages; school/year and `name` corroboration
- **Empty/negative result looks like:** no indexed pages — Trombi gates most profile detail behind login, so absence here is weak evidence; it may only mean the profile isn't publicly crawlable.

## Gotchas & OpSec
- OpSec: **passive** — you query Google, not Trombi; no account, no notification to the subject.
- Trombi shows limited data to logged-out visitors, so Google's index of it is shallow; treat a null result as inconclusive.
- French-market tool: relevance drops sharply for subjects with no France connection.

## Overlaps ("do both")
- Pairs with `[[here-8]]` (the same dork technique aimed at Facebook) and `[[google-com-85]]` — run the family of Google dorks together so a subject who's absent on one network still surfaces on another.

## Trust & verifiability
`trust: trusted` — no intermediary; results are Google's index of public Trombi pages. Confirm the profile matches your subject before relying on the school/year details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-3 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
