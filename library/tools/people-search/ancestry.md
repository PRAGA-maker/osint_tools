---
id: ancestry
name: Ancestry
description: Use when you have a name plus a date or place and want genealogical records (census, birth/marriage/death, immigration) to build family connections and a timeline.
url: http://www.ancestry.com
category: people-search
path:
- people-search
bestFor: Building a family tree and timeline from historical records (census, vital records, immigration) starting from a name and approximate date/place.
selectorsIn:
- name
- dob
- geolocation
selectorsOut:
- associate
- dob
- address
- name
status: live
pricing: freemium
costNote: Searching and seeing record hits is free; viewing full record images, building extended trees, and DNA features require a paid subscription (14-day free trial available).
opsec: active
opsecNote: Viewing records and saving them to a tree happens behind an Ancestry login tied to your subscription; activity is logged to your account. Other users can sometimes see that a tree/record was viewed. Use a dedicated research account, not your personal genealogy account.
humanInLoop: true
humanInLoopReason: [account-login, payment-wall-partial]
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Ancestry.com LLC; one of the largest commercial genealogy databases with billions of indexed historical records.
missingPersonsRelevance: high
coverage: [us, uk, ca, global]
auth: account
api: false
localInstall: false
registration: true
aliases:
- Ancestry.com
tags:
- people-investigations
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# Ancestry

> The largest commercial genealogy database — turns a name and rough date/place into census records, vital records, and a web of family relationships.

## When to use
You have a `name` plus a `dob` (even approximate) or a `geolocation`, and you need to establish **family connections** and a **historical timeline**: parents, siblings, spouses, children, prior addresses, immigration. Especially useful for reconstructing relatives and last-known places for older subjects or for confirming kin who might be contacted in a missing-persons search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the URL and sign in (or start the 14-day trial). Use a dedicated research account.
2. Open Search and enter `name`, then add any of: birth year/place, residence, parents'/spouse's names to disambiguate.
3. Review hits across collections (census, BMD, immigration, military). Free tier shows that a match exists and indexed fields; opening the **record image** or saving to a tree needs a subscription.
4. Pivot: extracted relatives become `associate` leads; historical addresses become `address`/`geolocation` leads; confirmed birth years sharpen `dob`. Feed names into general people-search.

## Inputs → Outputs
- **In:** `name`, `dob`, `geolocation`
- **Out:** `associate` (relatives), `dob`, `address`, `name` (maiden/alternate)
- **Empty/negative result looks like:** no collection hits, or only loose soundalike matches. Common-name searches return many false candidates — disambiguate with a second known fact (parent, place, year) before trusting a match.

## Gotchas & OpSec
- Human-in-the-loop: requires an account; full record access is paywalled (free trial then subscription).
- Records are historical — great for relationships and old addresses, weak for *current* whereabouts. Pair with a live people-search for present-day data.
- OpSec: marked `active` because viewing/saving is logged to your account and some tree activity is visible to other members. Use a sock research account; avoid linking to a real family tree.

## Overlaps ("do both")
- Pairs with `[[ancestry-com]]` and `[[ancestry-genealogy-family-trees-and-family-history-records]]` (regional Ancestry portals) for US/UK record coverage.

## Trust & verifiability
`trust: trusted` — operated by Ancestry.com LLC, an established commercial genealogy provider with billions of indexed records. Index transcriptions can contain errors; verify against the original record image where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ancestry |
| category | people-search |
| selectorsIn → selectorsOut | name, dob, geolocation → associate, dob, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
