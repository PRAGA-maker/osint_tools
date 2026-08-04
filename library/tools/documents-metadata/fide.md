---
id: fide
name: FIDE
description: Use when you have a `name` (or FIDE ID) of a competitive chess player and want to confirm identity and country — returns rating, federation, title, birth year and FIDE ID.
url: https://ratings.fide.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Confirming a competitive chess player's identity, federation and birth year via the official FIDE database.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
status: live
pricing: free
costNote: Free public database run by the International Chess Federation; no account needed to search or view profiles.
opsec: passive
opsecNote: You query FIDE's public ratings site, never the subject. Standard passive web research; no notification to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official governing body's ratings database (FIDE); the authoritative source for rated-player identity data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ratings.fide.com
- International Chess Federation ratings
tags:
- chess
- people-search
- sports-records
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# FIDE

> The International Chess Federation's official ratings database — search a player's name and get their federation, rating, title, birth year and unique FIDE ID.

## When to use
Your subject is (or claims to be) a competitive chess player, or you have a `name` that might match a rated player. FIDE's database is an authoritative people-search for that niche: it confirms the person exists in the rating system, pins their country (federation) and birth year, and gives a stable `document-id` (FIDE ID) to disambiguate people who share a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ratings.fide.com/ and use "Search FIDE database" (advanced search lets you filter).
2. Enter the player's `name` (try surname first; use alternate transliterations for non-Latin names).
3. Open the matching profile — read federation, standard/rapid/blitz ratings, FIDE title, birth year and the numeric FIDE ID.
4. Use the FIDE ID to disambiguate namesakes and to pull rating history.
5. Pivot: the confirmed federation + birth year narrows other people-searches; the name+country feeds national records or tournament databases (e.g. chess-results.com).

## Inputs → Outputs
- **In:** `name` (or FIDE `document-id`)
- **Out:** confirmed `name`, `dob` (birth year), federation/country, rating, title, FIDE ID
- **Empty/negative result looks like:** no matching player — meaning the subject isn't FIDE-rated (most casual players aren't), not that they don't play chess.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — fully public data; nothing reaches the subject.
- Only covers *rated* players; birth data is year-only, and common names return many hits — always confirm via the FIDE ID and corroborating detail.

## Overlaps ("do both")
- Pair with tournament databases (chess-results.com, national federation sites) — FIDE confirms identity/rating; those add event history, locations and photos.

## Trust & verifiability
`trust: trusted` — the sport's official governing body; the authoritative record for rated-player identity, so data quality is high within its scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fide |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, document-id → name, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
