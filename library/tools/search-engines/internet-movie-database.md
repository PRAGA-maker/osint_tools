---
id: internet-movie-database
name: IMDb
description: Use when you have a `name` (or username/handle) connected to film/TV work and want a biography, filmography, and linked identity details — returns name confirmation, associates, and biographical hints.
url: https://www.imdb.com
category: search-engines
path:
- search-engines
bestFor: Profiling anyone tied to film/TV/entertainment — cast, crew, extras — with biography and collaborator links.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: freemium
costNote: Free to browse and search; IMDbPro (paid) adds contact/representation details and industry data. Public profiles need no account.
opsec: passive
opsecNote: Browsing public profiles is read-only and invisible to the subject. IMDb sees your IP; use a clean session. Nothing you view is reported to the person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The dominant film/TV reference database; core credits are well-verified, though user-editable bio fields can contain errors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- wikipedia
aliases:
- imdb.com
- Internet Movie Database
tags:
- entertainment
- biography
- film
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# IMDb

> The reference database for film and television and the people who make it; if a subject has any entertainment-industry connection, IMDb often carries a biography, birth date, real-name/AKA, and a network of collaborators.

## When to use
Your subject is (or claims to be) an actor, filmmaker, crew member, or extra, and you have a `name` or stage name to check. IMDb can confirm the real name behind a stage name (and vice versa), give a birth date and birthplace, list every credited project (placing the person in specific times and cities of production), and expose frequent collaborators as `associate` links. It's also a fast credibility check on someone's claimed industry résumé.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.imdb.com and search the `name` (or use web search `site:imdb.com "<name>"`).
2. Open the person's page: read the **bio** (birth name, DOB, birthplace, height, family), the **filmography** (dates/locations of work), and the **"known for" / frequent collaborators**.
3. Cross-check a stage name against the listed birth name; note birthplace and DOB as identity anchors.
4. Use production credits to place the subject geographically and temporally (a shoot in a given city/year).
5. Pivot: real name → people-search; collaborators → `associate` mapping; birthplace/DOB → public-records lookups.

## Inputs → Outputs
- **In:** `name` (real or stage name)
- **Out:** `name` (real/AKA confirmation), `dob` and birthplace, `associate` (collaborators/family), filmography timeline
- **Empty/negative result looks like:** no matching person, or a name-only entry with a single uncredited role and no bio — the person has minimal industry footprint; not proof they never worked in film.

## Gotchas & OpSec
- Biographical fields (family, trivia) are partly user-contributed and can be wrong or vandalized — corroborate DOB/real-name before relying on them.
- Common names produce many matches; disambiguate via a specific credit you already know.
- Contact/representation data is IMDbPro-only (paid); the free profile won't give you an agent's email.
- OpSec: **passive** and read-only.

## Overlaps ("do both")
- Pairs with `[[wikipedia]]` (fuller prose biography and sourced facts for notable people) — IMDb has the credits/DOB, Wikipedia often has citations and life details, so use both to confirm identity facts.

## Trust & verifiability
`trust: trusted` — credits are well-maintained and widely cross-referenced; treat the editable bio fields as leads to verify rather than settled fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internet-movie-database |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
