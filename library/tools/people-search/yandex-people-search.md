---
id: yandex-people-search
name: Yandex People Search
description: Use when you have a `name` (or `username`) and want to find matching social-media profiles across many networks in one query — returns social-profile links, strongest for Russian/CIS and European subjects.
url: https://yandex.ru/people
category: people-search
path:
- people-search
bestFor: Aggregated cross-network people search by name/username, with unusually strong coverage of Russian/CIS and European social platforms.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search; no account required.
opsec: passive
opsecNote: You query Yandex, not the subject — the target gets no signal. But Yandex is a Russia-based provider that logs queries; run from a sock-puppet browser/clean IP and never from an attributable identity.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Yandex's own people-search aggregator over public social profiles; results are as reliable as the indexed public data, and coverage skews to Russian/CIS/European networks Western engines index poorly.
missingPersonsRelevance: high
coverage:
- global
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yandex-images
- yandex-mail
- google-com-3
aliases:
- Yandex People
- yandex.ru/people
tags:
- people-search
- social-search
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Yandex People Search

> Yandex's cross-network people finder: one name query surfaces matching social profiles across many platforms — and it sees the Russian/CIS and European networks Google barely indexes.

## When to use
You have a `name` or `username` and want a fast sweep for matching social-media profiles, especially when the subject has a Russian, CIS, or European footprint. Yandex indexes VK, OK (Odnoklassniki), and other regional networks far better than Western engines, so it's the go-to people aggregator when a Google/Bing name search comes up thin on someone from that region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yandex.ru/people in a sock-puppet browser.
2. Enter the subject's `name` (try native-script spellings too, e.g. Cyrillic) or a `username`.
3. Optionally filter by network/region where offered.
4. Read the results: candidate profiles across multiple social networks with names and thumbnails; solve any CAPTCHA manually.
5. Pivot: open promising profiles, and cross-check the profile photo via [[yandex-images]] reverse search; feed usernames into username-enumeration tools.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` candidate matches across multiple networks (name, thumbnail, network)
- **Empty/negative result looks like:** few or no matches — common for people with a purely Western footprint (use Google/Bing/dedicated tools there) or a well-locked-down presence. CAPTCHA walls can also suppress results; retry from a clean session.

## Gotchas & OpSec
- Try **native-script** name spellings — Cyrillic queries surface CIS profiles that transliterations miss.
- Yandex CAPTCHAs anonymous/repeated queries; go by hand and space them out.
- OpSec: passive toward the subject, but Yandex (Russia-based) logs your queries — always use a sock puppet and clean IP.

## Overlaps ("do both")
- Pairs with [[yandex-images]] (reverse-image/face — the strongest reason to be in the Yandex ecosystem) and with Western name search — the two index different halves of the world, so run both on any cross-region subject.

## Trust & verifiability
`trust: community` — an aggregator over public profiles; matches are leads to open and confirm, and its real edge is coverage of regional networks Western engines under-index, not any authority over the data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yandex-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
