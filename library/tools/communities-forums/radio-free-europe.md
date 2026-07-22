---
id: radio-free-europe
name: Radio Free Europe / Radio Liberty (RFE/RL)
description: Use when you have a `name` and want reporting from Eastern Europe, Russia, Central Asia, the Caucasus or Iran — returns `social-profile`/mention, event dates and `associate` context.
url: http://www.rferl.org
category: communities-forums
path:
- communities-forums
bestFor: Searching regional reporting on people and events across the former USSR, Eastern Europe, Central Asia and Iran.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read and search; multilingual, no account needed.
opsec: passive
opsecNote: Reading and dorking a public news site is passive and invisible to any subject. Only RFE/RL's servers log your visit; use a clean session in restrictive regions where the site may itself be monitored/blocked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A US-funded international broadcaster with professional newsrooms across the region; well-sourced but a funded outlet — treat as credible journalism, corroborated where possible.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RFE/RL
- Radio Liberty
- rferl.org
tags:
- news-media
- eastern-europe
- central-asia
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Radio Free Europe / Radio Liberty (RFE/RL)

> Deep regional news coverage of Russia, Eastern Europe, the Caucasus, Central Asia and Iran in many languages — often the best English-accessible reporting on people and events there.

## When to use
You have a `name` connected to the former Soviet space, Eastern Europe, the Balkans, Central Asia, the Caucasus or Iran, and want reporting that Western nationals rarely cover. RFE/RL's regional services publish on activists, officials, conflict, sanctions, disappearances and local events — valuable for a date-stamped event, a location, named associates/officials, and quotes establishing a person's role or status in the region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use RFE/RL's on-site search, or Google-dork it: `site:rferl.org "<name>"` (add a country/topic term to cut noise).
2. Check the relevant language service too (e.g. Radio Svoboda, Azattyq) — some coverage exists only in the regional language; use translation.
3. Read matching articles for the exact connection, date, location and named associates/officials.
4. Pivot: named `associate`/officials feed relationship mapping; an event date/location anchors a timeline; regional-language spellings feed further searches.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/mention, named `associate`/officials, event dates, locations and quoted context
- **Empty/negative result looks like:** no English hits — try the regional-language service and transliteration variants before concluding no coverage exists.

## Gotchas & OpSec
- Coverage is region-specific; irrelevant for subjects outside its footprint.
- Name transliteration (Cyrillic/other scripts ↔ Latin) varies — try multiple spellings.
- A US-funded broadcaster; credible but corroborate contested claims with additional sources.

## Overlaps ("do both")
- Pairs with local/regional outlets, Meduza, and general news search — RFE/RL often has the deepest English coverage, but local sources add detail and different framing.

## Trust & verifiability
`trust: trusted` — professional multilingual newsrooms with regional expertise; well-sourced journalism, though a funded outlet, so anchor contested facts to primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radio-free-europe |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
