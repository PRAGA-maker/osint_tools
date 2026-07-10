---
id: yasni
name: Yasni
description: Use when you have a `name` and want an aggregated view of that person's web presence and professional mentions — returns `social-profile` links, `employer-org` and associated web references.
url: https://www.yasni.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: Name-based people search that aggregates web mentions, professional profiles, and nicknames — strongest for German/European professional names.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to search; an account is only needed to create/claim your own profile ("Exposé"). No payment for lookups.
opsec: passive
opsecNote: Aggregate name search; the subject is not notified. Queries go to a third party that may log them — use a puppet browser/IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running (German-origin) people-search aggregator. It compiles existing web references/profiles rather than authoritative records; coverage is dated and uneven, best for European professional identities.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- yasni.com
- yasni.de
tags:
- people-search
- name-search
- web-presence
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Yasni

> A name-centric people-search that pulls together a person's scattered web mentions, professional profiles, and nicknames — historically strongest in the German/European market.

## When to use
You have a `name` and want a consolidated view of that person's public web footprint — professional profiles, company mentions, articles, and associated nicknames — without running a dozen searches yourself. Yasni is most useful for European (especially German) professional identities, where it has the deepest history. Reach for it as an aggregation shortcut to surface leads you then verify at the source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.yasni.com/ (or the .de site) and enter the `name`; add a location, profession, company, or skill to disambiguate.
2. Read the aggregated result: linked `social-profile`s, `employer-org`/company mentions, articles, and nickname variants.
3. Follow each reference to its source to confirm it's your subject (aggregators mix namesakes).
4. Use nickname/alias variants it surfaces to broaden other searches.
5. Pivot: company mentions → corporate registries; profiles → per-platform deep dive; aliases → username enumeration.

## Inputs → Outputs
- **In:** `name` (+ optional location/profession/company)
- **Out:** `social-profile` links, `employer-org` mentions, web references, nickname/alias variants
- **Empty/negative result looks like:** few/no references — a low web profile, a non-European subject (thinner coverage), or a common name drowning the target. A sparse result reflects Yasni's dated index, not necessarily absence.

## Gotchas & OpSec
- **Dated/uneven index:** it aggregates existing references and can be stale; treat hits as leads and verify at the source.
- Namesake mixing is common for popular names — disambiguate with a second attribute.
- Coverage skews European/German; weaker elsewhere.
- OpSec: **passive** — no subject notification.

## Overlaps ("do both")
- Pairs with general web/name search (Google dorking) and other people-search aggregators; for German records specifically, combine with national directories.

## Trust & verifiability
`trust: unverified` — an aggregator of third-party web references, not an authoritative source; every reference should be confirmed at its origin before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yasni |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
