---
id: zaba-search
name: zaba search
description: Use when you have a US `name` (or phone) and want free current/past addresses and phone numbers — returns address, phone, age and links to fuller records.
url: https://zabasearch.com
category: people-search
path:
- people-search
bestFor: Fast free first-pass US people lookup — surfacing addresses, phone numbers and age range from a name.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- dob
- associate
status: live
pricing: freemium
costNote: Basic results (name, address, partial phone, age range) are free with no registration; full reports, background details and unmasked data are gated behind a paid partner (BeenVerified/Intelius-style, ~$25/mo). Author-tier value is entirely in the free layer.
opsec: passive
opsecNote: Passive against the target — data comes from aggregated public records, not the subject's infrastructure, so no notification is sent. ZabaSearch/its ad partners log your searches and IP; use a clean browser and don't sign in. Beware "upsell" buttons that hand you off to paid partner sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running US data broker (one of the oldest free people-search engines). Reliable enough for lead generation but records are stale/merged; always corroborate before acting on any single hit.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- australia-lookup
aliases:
- ZabaSearch
- Zaba Search
tags:
- people-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# zaba search

> One of the oldest free US people-search engines — a name in, addresses and phone numbers out, no signup.

## When to use
You have a `name` (US person) and want a quick, free baseline of where they've lived and what phone numbers are tied to them, plus an age range to disambiguate common names. Good as an early, throwaway lookup before spending on paid brokers — it often surfaces enough to seed reverse-address and phone pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://zabasearch.com in a clean browser.
2. Enter first + last name and optionally a state to cut down matches (reverse phone lookup is also offered).
3. Scan the free result cards: full name, current/prior `address`, age range (`dob` proxy), and partial phone numbers.
4. Ignore the "view full report / background check" buttons — those hand off to a paid partner. Stay on the free layer.
5. Pivot: an address feeds reverse-address/neighbor lookups and county property records; the age range disambiguates namesakes; phones feed phone-OSINT.

## Inputs → Outputs
- **In:** `name` (or `phone` for reverse lookup)
- **Out:** `address` (current + historical), partial `phone`, age range (`dob`), sometimes `associate`/relatives
- **Empty/negative result looks like:** no cards or only unrelated ages/states — treat as "not indexed here," not as proof the person doesn't exist; brokers miss younger people and those with common names.

## Gotchas & OpSec
- Records are aggregated and often stale or merged across namesakes — the "age" and address history are the best disambiguators.
- The free tier deliberately masks part of each phone to drive paid upgrades; don't pay ZabaSearch for what free tools (TrueCaller-style, county records) may give you.
- OpSec: **passive**; no contact with the subject. Just don't log in or pay from an attributable identity.

## Overlaps ("do both")
- Run alongside other US free brokers (TruePeopleSearch/FastPeopleSearch-style) — each broker buys different data feeds, so one surfaces addresses/relatives the other misses. For non-US subjects, pair with a country-specific finder like `[[australia-lookup]]`.

## Trust & verifiability
`trust: community` — a well-known commercial data broker, not an authoritative record. Good for leads; verify any address/phone against a primary source (property records, direct contact) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zaba-search |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, dob, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
