---
id: irbis-by-espy
name: IRBIS by Espy
description: Use when you have a `name`, `email`, `phone`, `username`, or `image` and want an aggregated digital-identity profile — returns linked social accounts, contacts and identity signals.
url: https://espysys.com/irbis/
category: search-engines
path:
- search-engines
bestFor: A multi-selector people-search/enrichment engine that maps one identifier to a subject's cross-platform digital footprint.
selectorsIn:
- name
- email
- phone
- username
- image
selectorsOut:
- social-profile
- name
- email
- phone
- face
status: live
pricing: freemium
costNote: Free trial credits (no card required) for limited searches; sustained/bulk use and the API are paid. A paid OSINT platform with a usable free tier for testing.
opsec: active
opsecNote: IRBIS queries many third-party sources for the selector you enter; it aggregates rather than contacting the subject, but you are entrusting the target's identifiers to a commercial platform that logs your account activity. Use a dedicated account and lawful basis.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial aggregator (ESPY Systems); results are compiled from many sources of varying reliability and must be corroborated. Not an authoritative record.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- espysys-com
tags:
- toddington
- curated-directory
- specialty-search
- people-search
- enrichment
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# IRBIS by Espy

> A commercial digital-identity search engine that takes almost any selector — name, email, phone, username, or photo — and returns an aggregated profile of linked accounts and contacts across 200+ platforms.

## When to use
You have one identifier for a subject and want a fast, broad enrichment: which social accounts, emails, phones, and identity signals connect to it. Useful early in an investigation to generate a map of a person's online presence, including a facial-recognition search from a photo. Treat its output as leads to verify, not fact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account (free trial credits, no card) at the IRBIS portal (irbis.espysys.com).
2. Choose a search type: name (optionally + city/company), email, phone (reverse), username, or photo (facial recognition).
3. Enter the selector and run the search.
4. Review the aggregated profile: linked `social-profile`s, associated `email`/`phone`, and identity signals.
5. Spend free credits carefully; sustained or bulk use requires a paid plan or the API.
6. Pivot: each returned account/contact → verify at its source; a photo `face` match → corroborate with independent reverse-image tools before trusting.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `username`, or `image` (photo)
- **Out:** aggregated `social-profile`s, `name`, `email`, `phone`, and facial-recognition `face` matches
- **Empty/negative result looks like:** thin or no profile, or matches that don't actually correspond to your subject — aggregators over-link on common names and weak signals. A hit is a hypothesis to confirm, not a conclusion.

## Gotchas & OpSec
- Freemium with a hard cap: free credits run out fast; the useful volume is paid.
- Aggregated, unverified data with real false-positive risk, especially facial recognition and common names — corroborate every hit independently.
- Legal/ethical: facial recognition and bulk identity aggregation carry jurisdictional restrictions; ensure a lawful basis.
- OpSec: **active** in the sense that you hand a commercial platform the target's identifiers; use a dedicated account.

## Overlaps ("do both")
- Complements free username/email enumeration tools and independent reverse-image search — use those to verify IRBIS's aggregated links rather than trusting the single platform.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with no authoritative guarantee; treat results as leads and confirm each against a primary source, taking special care with facial-recognition matches.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | irbis-by-espy |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, phone, username, image → social-profile, name, email, phone, face |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
