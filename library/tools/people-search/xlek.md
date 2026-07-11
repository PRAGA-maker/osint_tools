---
id: xlek
name: Xlek
description: Use when you have a `name` (+ US location) and want free public-records data — returns `address`, `phone`, `email`, `associate` plus voter/property/corporate records.
url: https://xlek.com/
category: people-search
path:
- people-search
bestFor: Free US people-search across property, voter, corporate and contact records (formerly Cubib).
selectorsIn:
- name
- address
selectorsOut:
- address
- phone
- email
- associate
status: live
pricing: freemium
costNote: Core public-data search is free (no paywall for basic records); the site monetizes via ads and upsell links to paid background-check partners.
opsec: passive
opsecNote: Aggregator of public records; searching is passive and the subject isn't notified. No login for basic search. Avoid clicking through to partner background-check upsells with real details — those are paid third parties that log you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free public-data aggregator (formerly Cubib); data is real public records but can be outdated, so treat hits as leads to confirm.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cubib
- Xlek Free Public Data Search
tags:
- people-search
- public-records
- address
- voter-records
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Xlek

> A free US public-data aggregator (the former Cubib): search a name and pull addresses, phones, emails, plus voter, property, corporate and campaign-finance records in one place.

## When to use
You have a US subject's `name` (ideally with a state/city to disambiguate) and want a fast, free sweep of public records: current/past `address`, `phone`, `email`, likely relatives/`associate`, and structured records (voter registration, property ownership, corporate registrations, campaign contributions, financial cases). Good early breadth pass before paying for a background check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xlek.com/ and search by name (add location to narrow).
2. Open a matching person record: addresses, phones, emails, relatives/associates, and links to underlying record types.
3. Drill into specific record categories (property, voter, corporate, campaign finance) for corroborating detail.
4. Note that some data is stale — cross-check the freshest-looking address/phone elsewhere.
5. Pivot: feed `email`/`phone` into existence/breach checks, `associate` names back into people-search, `address` into mapping and property records.

## Inputs → Outputs
- **In:** `name` (+ US location)
- **Out:** `address`, `phone`, `email`, `associate` (relatives), plus voter/property/corporate/campaign records
- **Empty/negative result looks like:** no record or only unrelated same-name hits — the subject may have opted out (Xlek honors 30-day opt-out removals), be non-US, or use a name variant; absence isn't proof of no footprint.

## Gotchas & OpSec
- US-only; no coverage outside the States.
- Data can be **outdated** — verify the most-recent-looking contact details against a second source.
- People can opt out, so a clean result may just mean removal, not absence.
- The upsell links go to paid third-party background-check vendors — don't feed them real case details.

## Overlaps ("do both")
- Pairs with other free people-search aggregators (FastPeopleSearch, TruePeopleSearch) — each indexes public records differently, so cross-run to fill gaps and catch stale entries.

## Trust & verifiability
`trust: community` — a free aggregator of genuine public records; the data is real but not curated for freshness, so confirm any actionable detail before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xlek |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, phone, email, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
