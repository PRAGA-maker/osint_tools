---
id: search-ch
name: Search.ch
description: Use when you have a `name` in Switzerland and want their phone/address — returns `phone`, `address`, and business listings from the Swiss national directory (2M+ entries).
url: https://www.search.ch
category: search-engines
path:
- search-engines
bestFor: Swiss phone book and business directory lookups — resolve a name to phone/address across Switzerland.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- address
status: live
pricing: free
costNote: Free to search the directory, maps, and timetables; a login (email/Google/Apple/etc.) is optional and only needed for personalised features, not for lookups.
opsec: passive
opsecNote: A public directory lookup — you query search.ch, not the person, so no notification is sent. Standard passive collection; a login is not required for searches, so stay logged out to avoid attributing yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established mainstream Swiss portal (operates the tel.search.ch / local.ch directory data); directory entries are authoritative for listed numbers, though unlisted/mobile-only people won't appear.
missingPersonsRelevance: high
coverage:
- ch
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- search.ch
- tel.search.ch
- Die Schweizer Suchmaschine
tags:
- switzerland
- phone-book
- directory
- international
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Search.ch

> The Swiss search portal — a 2-million-entry phone book and business directory that turns a name into a phone number and address in Switzerland.

## When to use
Your subject is in Switzerland and you have a `name` (or a `phone` to reverse) and need their landline/`phone`, `address`, or business listing. Search.ch is one of the primary Swiss directories, so it's a first stop for Swiss people/business location — alongside maps, routing, and public-transport timetables that help confirm and contextualise an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.search.ch (logged out).
2. Use the Telefonbuch/phone-book search: enter the `name` (add a city/canton to disambiguate), or enter a `phone` for a reverse lookup.
3. Read the entries: full name, `address`, `phone`, and — for businesses — category and hours.
4. Cross-check the address on the built-in Karte/Route (map) to confirm and geolocate it.
5. Pivot: the address/phone feeds further Swiss records and phone OSINT; a business hit feeds company research and `[[account-live-com]]`-style enrichment.

## Inputs → Outputs
- **In:** `name` (or `phone` for reverse lookup), optionally + city/canton
- **Out:** `phone`, `address`, business listing details
- **Empty/negative result looks like:** no directory entry — very common, since mobile-only and unlisted individuals aren't in the phone book; absence is not proof the person isn't in Switzerland.

## Gotchas & OpSec
- Directory coverage skews to listed landlines and businesses; younger/mobile-only subjects often have no entry.
- German-language UI by default (also FR/IT/EN) — switch language if needed.
- Passive and login-free for search; stay logged out.

## Overlaps ("do both")
- Pairs with other Swiss/European directory and people-search tools — search.ch is authoritative for listed Swiss numbers, while broader engines catch the mobile-only and cross-border cases it misses.

## Trust & verifiability
`trust: trusted` — a mainstream Swiss directory operator. Listed entries are reliable; treat a no-match as "unlisted," not "not in Switzerland," and confirm an address via the map view.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-ch |
| category | search-engines |
| selectorsIn → selectorsOut | name, phone → phone, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
