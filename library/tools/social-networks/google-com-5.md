---
id: google-com-5
name: google.com
description: Use when you have a `name` or `username` and want to find profiles on Draugiem.lv (the dominant Latvian social network) via a Google site-search dork — returns `social-profile` links.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Adraugiem.lv
category: social-networks
path:
- social-networks
bestFor: Google-dorking Draugiem.lv, Latvia's main social network, for a specific person.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Uses only Google search; free, no account.
opsec: passive
opsecNote: Query hits Google, not Draugiem, so the subject is not alerted and you avoid registering on the platform. Search signed out / in a sock browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A Google `site:` dork, not a third-party tool; reliability equals Google's index of public Draugiem.lv pages.
missingPersonsRelevance: high
coverage:
- lv
auth: none
api: false
localInstall: false
registration: false
aliases:
- 'site:draugiem.lv dork'
- Draugiem Google search
tags:
- esocialmedia
- European Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com

> A Google `site:draugiem.lv` dork that pulls public profiles out of Draugiem.lv — Latvia's dominant homegrown social network — without registering on the platform.

## When to use
Your subject has a Latvian footprint and you want to check a national network that cross-platform username tools rarely cover. Draugiem.lv is deeply embedded in Latvia (used well beyond social chat — for logins and services), so a hit strongly corroborates identity, and profiles can expose friends (`associate`), workplace, and photos.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start from `site:draugiem.lv` and append the subject's name or username in quotes, e.g. `site:draugiem.lv "Vārds Uzvārds"`.
2. Run it in Google (signed out / sock browser); add a town or school to disambiguate.
3. Read results — public Draugiem profile and content pages Google has indexed.
4. Pivot: a profile yields associates and place/employer detail; feed those into people-search and other social lookups.

## Inputs → Outputs
- **In:** `name` or `username` (quoted), optionally + location
- **Out:** links to public Draugiem.lv `social-profile` pages; `name`/associate corroboration
- **Empty/negative result looks like:** no indexed pages — Draugiem gates most content behind login, so Google's view is shallow; absence is weak evidence, not proof.

## Gotchas & OpSec
- OpSec: **passive** — you query Google, not Draugiem; no account, no notification.
- Draugiem shows little to logged-out visitors, so the indexable surface is thin; treat null as inconclusive.
- Latvia-specific: near-zero relevance for subjects with no Latvian connection.

## Overlaps ("do both")
- Pairs with `[[google-com-3]]` (Trombi/France) and `[[here-8]]` (Facebook) — run the family of national-network dorks so a subject absent on global platforms still surfaces regionally.

## Trust & verifiability
`trust: trusted` — no intermediary; results are Google's index of public Draugiem pages. Confirm the profile is your subject before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-5 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
