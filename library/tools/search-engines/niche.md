---
id: niche
name: Niche
description: Use when you have a school/college `employer-org` or a `geolocation` and want profile data — returns rankings, stats, and reviews for schools and neighborhoods.
url: https://www.niche.com/
category: search-engines
path:
- search-engines
bestFor: Researching a US school, college, or neighborhood — rankings, demographics, and user reviews.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free to browse school/college/place profiles and reviews; a free account unlocks some tools (its student-facing features and scholarships).
opsec: passive
opsecNote: You browse institution/area profiles — no subject is queried or notified. Reviews are pseudonymous; nothing you read here signals your interest to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial rankings/reviews platform; stats are compiled from public education/census data (broadly reliable) while reviews are anonymous, self-selected, and unverifiable.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- niche.com
tags:
- toddington
- curated-directory
- schools
- neighborhoods
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Niche

> A US rankings-and-reviews site for schools, colleges, and neighborhoods — supporting context when a subject's institution or area matters, not a people finder.

## When to use
A low-relevance context tool: you have a US school/college (`employer-org`) or a `geolocation`/neighborhood and want a quick profile — enrollment, demographics, cost, rankings, and pseudonymous student/resident reviews. Useful for characterising where someone studied or lives, or sanity-checking that an institution exists and its size/type. It won't identify individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.niche.com/ and search a school/college name or a place/zip.
2. Open the profile: rankings, stats (enrollment, demographics, test scores, cost), and the reviews section.
3. Read reviews for qualitative colour, treating them as anonymous and self-selected.
4. Pivot: institution stats corroborate a subject's stated school/area; a confirmed school feeds its official directory/alumni sources.

## Inputs → Outputs
- **In:** a school/college `employer-org` or a `geolocation`/neighborhood
- **Out:** rankings, demographic/stat profile, pseudonymous reviews
- **Empty/negative result looks like:** no profile — a very small, new, or non-US institution/place may be absent; and reviews may be sparse or missing.

## Gotchas & OpSec
- **US-focused** and institution/area-level only — no individual data; don't expect to find a person here.
- Reviews are anonymous and self-selected — treat as impressions, not facts; the hard stats derive from public education/census data.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with official school/college directories, NCES (for authoritative US education stats), and census/neighborhood tools — Niche is the quick overview; those are the systems of record.

## Trust & verifiability
`trust: community` — a commercial aggregator. Its statistics come from reliable public data, but rankings are proprietary and reviews are unverifiable, so use it for orientation and confirm specifics against authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | niche |
