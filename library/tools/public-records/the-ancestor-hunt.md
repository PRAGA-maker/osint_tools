---
id: the-ancestor-hunt
name: The Ancestor Hunt
description: Use when you have a `name` and want to find historical/genealogical records — newspapers, obituaries, cemetery, vital and yearbook records — via a large curated free-resource directory; returns name, dob, and associate (family) leads.
url: http://www.theancestorhunt.com
category: public-records
path:
- public-records
bestFor: A curated launchpad to thousands of free genealogy/newspaper/obituary databases for reconstructing a person's history and family links.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
- address
status: live
pricing: freemium
costNote: The core value — huge curated lists of links to free online newspaper, obituary, cemetery and vital-record databases, plus ~10 free tools (relationship calculator, nickname finder) — is free. Some field guides, bundles and courses ($9.95–$20) and an academy are paid.
opsec: passive
opsecNote: You browse a directory and follow out to third-party archives; nothing touches the subject. Normal browsing hygiene applies. The linked databases have their own logging, so use a clean session for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known, long-running (since 2008) genealogy resource by Kenneth R. Marks, widely cited in the family-history community. It's a curated pointer directory, so quality depends on the underlying archives it links to.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- familysearch
- newspapers-com
aliases:
- theancestorhunt.com
- Ancestor Hunt
tags:
- genealogy
- family
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# The Ancestor Hunt

> A veteran genealogy portal: not a database itself, but the best-organised set of doorways into free newspaper, obituary, cemetery and vital-record archives for building out a person's past and family tree.

## When to use
You have a `name` (ideally with an approximate era or US locality) and need historical depth — birth/death dates, maiden names, relatives, addresses, school yearbooks, obituaries. This is the right starting point when a subject predates the social-media era, or when you're working a cold/missing-persons case that hinges on family connections (`associate`s), a `dob`, or confirming a death.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.theancestorhunt.com.
2. Pick the record type from the menus — Newspapers, Obituaries, Cemetery, Vital Records, Yearbooks, Immigration, etc.
3. Follow the curated state/country links to the relevant free archive and search the `name` there.
4. Use the free on-site tools (nickname finder, relationship calculator) to widen name variants and map relatives.
5. Pivot: an obituary yields surviving family (`associate`s) and dates; a maiden name feeds further record searches and people-aggregators.

## Inputs → Outputs
- **In:** `name` (plus era/locality helps enormously)
- **Out:** `dob`/death date, `associate` (relatives), `name` variants, historical `address`
- **Empty/negative result looks like:** the directory always lists resources; an "empty" result means the downstream archive had no match — try a different state list, a nickname, or a spelling variant before giving up.

## Gotchas & OpSec
- It's a **directory**, not a search box — expect to click out to many third-party sites and search each.
- Coverage is strongest for the US/UK/Canada; thinner elsewhere.
- OpSec: passive; the subject cannot see genealogy lookups.

## Overlaps ("do both")
- Pairs with FamilySearch and dedicated newspaper archives — this points you to them and to free alternatives the big paid sites bury.
- Combine with an obituary search (e.g. `[[funeralnet]]`) to cross-confirm death dates and relatives.

## Trust & verifiability
`trust: community` — a respected, long-lived curator; the directory itself is reliable, but always verify a specific fact against the primary record it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-ancestor-hunt |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
