---
id: locate-family
name: Locate Family
description: Use when you have a `name` and want a scraped public-directory listing of address/phone and household members — returns name, address, and associate leads.
url: https://www.locatefamily.com
category: public-records
path:
- public-records
bestFor: A free, scraped worldwide directory of names with street addresses and phone numbers — useful for household/associate leads, with heavy accuracy caveats.
selectorsIn:
- name
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free to browse/search; no account. Monetized via ads. Listings are aggregated/scraped from public sources without consent (it offers an opt-out removal page).
opsec: passive
opsecNote: Searching the directory does not notify anyone; only LocateFamily sees your IP (use a VPN/sock-puppet browser). Ethical/legal caution: the site is widely criticized for publishing personal data without consent and is restricted in some jurisdictions — treat findings as unverified leads and handle personal data responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Scraped aggregator with no authoritative sourcing and known-stale data; entries are lead-quality only and must be corroborated at a reliable source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- inteltechniques-people-search-tools
- spydialer
aliases:
- LocateFamily
- locatefamily.com
tags:
- genealogy
- family
- people-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Locate Family

> A free, ad-supported directory that scrapes names, street addresses, and phone numbers worldwide — cheap leads on where someone lived and who shared the household, but low reliability.

## When to use
You have a `name` and want quick, free leads on a possible address, phone, or household members (`associate`s living at the same address) — especially outside the US, where LocateFamily has broader (if patchy) coverage than many US-centric brokers. Use it as an early lead generator, never as a source of truth: data is scraped, often years out of date, and unverified.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.locatefamily.com and browse/search by name (the site is organized alphabetically by country and surname).
2. Locate the entry and read the listed street `address` and phone number, plus other names at the same address (`associate`/household leads).
3. Treat every field as a hypothesis — cross-check the address/phone against a reliable source before acting.
4. Pivot: run the phone through [[spydialer]]; run the name+address through a broader launcher like [[inteltechniques-people-search-tools]] to corroborate.

## Inputs → Outputs
- **In:** `name`
- **Out:** listed `address`, phone, and co-listed household `name`s (`associate` leads)
- **Empty/negative result looks like:** no listing — the person may never have been scraped, opted out, or the data predates their current life; absence proves nothing.

## Gotchas & OpSec
- **Low trust:** data is scraped and frequently stale/incorrect — do not rely on a LocateFamily address/phone without independent confirmation.
- Ethics/legality: the site publishes personal data without consent and is contested in several jurisdictions; use findings responsibly and lawfully, and note subjects can opt out (which also means gaps).
- OpSec: passive — no notification to the subject; only your IP is exposed to the site.

## Overlaps ("do both")
- Pairs with [[inteltechniques-people-search-tools]] (broader multi-broker sweep) and [[spydialer]] (phone confirmation) — LocateFamily is one weak signal; corroborate across several before trusting an address.

## Trust & verifiability
`trust: unverified` — a scraped aggregator with no authoritative sourcing and known accuracy problems. Everything it returns is a lead to verify elsewhere, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | locate-family |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
