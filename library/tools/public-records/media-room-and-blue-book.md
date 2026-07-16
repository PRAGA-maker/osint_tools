---
id: media-room-and-blue-book
name: Media Room & Blue Book (U of T)
description: Use when you have a subject affiliated with the University of Toronto and want their expert profile and media contact — returns faculty affiliation and contact details.
url: https://media.utoronto.ca/
category: public-records
path:
- public-records
bestFor: Finding University of Toronto experts/faculty and their topics and media-contact details via the U of T media room ("Blue Book").
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- email
status: live
pricing: free
costNote: Free, public university media site. No account (some journalist services route through media relations).
opsec: passive
opsecNote: Browsing a public university directory is passive; nothing about the subject is submitted. Emailing media relations to ask about a person would be active and identifying — avoid unless appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official University of Toronto media/communications site; affiliations and contacts are authoritative for U of T personnel.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- U of T Media Room
- UToronto Blue Book
tags:
- university
- expert-directory
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Media Room & Blue Book (U of T)

> The University of Toronto's media room and expert "Blue Book" — a directory of 1000+ faculty experts with their topics and, for many, direct or media-relations contact details.

## When to use
Your subject is (or claims to be) University of Toronto faculty, staff, or a subject-matter expert, and you want to confirm the affiliation and find their department, expertise, and a contact route. Also useful in reverse: identifying which U of T expert commented on a topic/event. It's an institution-specific directory — low general relevance, high value only when U of T is in scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the U of T media site and use the expert finder / search for the subject `name` or a topic.
2. Read the expert profile: department/faculty (`employer-org`), areas of expertise, and any listed contact (`email`) or media-relations routing.
3. Cross-reference the affiliation against the person's other online claims (LinkedIn, papers).
4. Pivot: a confirmed department feeds academic-search (publications, co-authors as `associate`s); a contact route enables (careful) outreach.

## Inputs → Outputs
- **In:** `name` or topic (tied to `employer-org` = U of T)
- **Out:** faculty `employer-org`/department affiliation, expertise, and contact `email`/media-relations details
- **Empty/negative result looks like:** no profile — the person isn't a listed U of T expert (they may still be affiliated but not in the expert directory); check the general U of T directory.

## Gotchas & OpSec
- Scope is one institution — irrelevant unless the subject ties to U of T.
- The expert directory is curated (media-facing experts), so many affiliated staff won't appear.
- OpSec: passive to browse; contacting media relations is active and identifying.

## Overlaps ("do both")
- Pairs with academic-publication search and general people-search — this confirms the U of T affiliation; publication databases reveal the subject's work and collaborators.

## Trust & verifiability
`trust: trusted` — official university source; affiliations are authoritative for U of T, though the directory only covers designated experts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | media-room-and-blue-book |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
