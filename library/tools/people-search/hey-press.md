---
id: hey-press
name: Hey Press
description: Use when you have a `name` or beat and want to find a journalist and what they cover — returns the journalist's outlet, recent articles, and social-profile links (a media-contact database, not general people search).
url: https://www.hey.press
category: people-search
path:
- people-search
bestFor: Identifying journalists by name, outlet, or topic and pulling their recent coverage and contact/social links.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free searches are limited; fuller results and contact detail require a paid plan. Now integrated with JournoFinder.
opsec: passive
opsecNote: Searching a public journalist database is passive and does not alert the person. Registering ties queries to your account — use a research login if you want separation.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial PR/media-contact database (JournoFinder/Hey Press); accurate for journalist–outlet mapping, but a marketing tool, not an investigative record source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- hey.press
- JournoFinder
tags:
- people-search
- journalists
- media
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Hey Press

> A searchable database of journalists and what they write — narrow to media people, but authoritative for tying a name to an outlet and a body of coverage.

## When to use
Your subject is (or claims to be) a journalist/writer, or you need to identify the reporter behind a beat. Given a `name`, Hey Press maps them to their outlet(s) and recent articles, and often to social/contact links. This is a *media-contact* database (built for PR outreach), not a general people finder — use it precisely when the media angle matters: verifying a press credential, finding a byline's full context, or reaching a reporter.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hey.press (it now runs on the JournoFinder platform).
2. Search by journalist `name`, outlet, or topic/beat.
3. Read the profile: associated `employer-org` (publication), recent articles, and linked `social-profile`s; contact detail is typically gated.
4. Hit the paywall for full contact data — decide if the lead warrants it.
5. Pivot: the outlet and bylines corroborate a claimed journalist identity; social links feed username/profile mapping; article topics reveal the subject's areas and locations.

## Inputs → Outputs
- **In:** `name` (or outlet / topic)
- **Out:** `employer-org` (publication), recent article list, `social-profile`/contact links (contact often paywalled)
- **Empty/negative result looks like:** no matching journalist — meaning not in the database, which skews toward English-language and PR-relevant press. Absence is not proof someone isn't a writer; niche/local/foreign-language journalists may be missing.

## Gotchas & OpSec
- Scope is journalists only — do not use it as a general person search; a non-media subject simply won't appear.
- Freemium: profiles are visible but contact detail is gated behind a paid plan.
- OpSec: **passive**; searching doesn't notify anyone.

## Overlaps ("do both")
- Pairs with Muck Rack-style databases and plain byline search (`site:` an outlet + name) — Hey Press structures the journalist→outlet mapping, while raw search catches bylines it hasn't indexed.

## Trust & verifiability
`trust: community` — a commercial media database; reliable for journalist–outlet associations it lists, but confirm any claimed credential against the outlet's own staff page and the actual bylines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hey-press |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
