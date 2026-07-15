---
id: google-com-61
name: google.com (site:people.bayt.com dork)
description: Use when you have a `name` or `username` and want to find a subject's public Bayt.com professional profile — returns social-profile links, employer/job history and a real name.
url: https://www.google.com/search?q=site%3Apeople.bayt.com&ie=utf-8&oe=utf-8&client=firefox-b-ab
category: social-networks
path:
- social-networks
bestFor: Surfacing public Bayt.com (Middle East / Gulf job site) CV-style profiles via a Google site: dork.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- name
- employer-org
- address
status: live
pricing: free
costNote: Google web search is free; no Bayt.com account needed to view profiles indexed publicly.
opsec: passive
opsecNote: You query Google, not Bayt or the subject, so this is passive — Bayt gets no signal that you looked. Clicking through to a profile is a normal pageview; use a sock-puppet browser if you want to avoid any account-linked personalization.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's index over Bayt.com's own public profile pages — both first-party sources; the technique (a site: operator) is authoritative, though individual profiles are self-reported.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bayt profile search
- site:people.bayt.com
tags:
- linkedin
- LinkedIn & Similar Sites
- google-dork
- bayt
- middle-east
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com (site:people.bayt.com dork)

> A Google `site:` operator aimed at Bayt.com — the largest jobs/CV network in the Middle East and Gulf — to pull public professional profiles LinkedIn won't show.

## When to use
You have a `name`, `username`, or `employer-org` for someone with a Gulf/Middle East / North Africa footprint and want their public CV-style profile: current and past employers, job titles, city, and sometimes a photo. Bayt.com is to the Arab world roughly what LinkedIn is to the West, so this fills a gap where LinkedIn coverage is thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run `site:people.bayt.com "Full Name"` (add city or employer to disambiguate: `site:people.bayt.com "Full Name" Dubai`).
2. To search by handle instead, try `site:people.bayt.com "username"`.
3. Read the results: each hit is a public Bayt profile page — open it for job history, location, skills and any linked contact.
4. Pivot: employer + title feeds corporate/LinkedIn cross-checks; a profile photo feeds reverse-image/face tools; a city feeds local records.

## Inputs → Outputs
- **In:** `name` / `username` / `employer-org`
- **Out:** `social-profile` (Bayt URL), confirmed `name`, `employer-org` / job history, city-level `address`
- **Empty/negative result looks like:** zero Google hits, or only generic Bayt landing/search pages rather than a personal `/people/` profile. Absence here only means Google hasn't indexed a matching public Bayt profile — not that the person has none.

## Gotchas & OpSec
- Profiles are **self-reported** — treat employers/titles as claims to corroborate.
- Google may return stale cached copies; open the live Bayt page to confirm it still exists.
- Quote the exact name and add a discriminator (city/employer) — common Arabic-transliterated names produce heavy noise.
- OpSec: passive; you touch Google, not the subject.

## Overlaps ("do both")
- Pairs with [[google-com-43]] and other `site:` dorks — each targets a different regional network (Bayt for the Gulf, Nairaland for Nigeria), so run the one matching the subject's region.

## Trust & verifiability
`trust: trusted` — the *method* (Google indexing Bayt's own public pages) is reliable and reproducible. The *content* of any profile is user-submitted, so verify specific claims against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-61 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
