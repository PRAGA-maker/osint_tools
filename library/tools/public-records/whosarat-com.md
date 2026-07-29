---
id: whosarat-com
name: WhosaRat.com
description: Use when you have a `name` and want to check a crowd-submitted database of alleged informants/cooperating witnesses — returns unverified informant/agent profiles (partial paywall).
url: https://whosarat.com/
category: public-records
path:
- public-records
bestFor: Checking whether a name appears in a user-submitted informant/cooperating-witness database.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: freemium
costNote: Limited free browsing; viewing full profiles, documents and posting requires a paid membership (partial paywall).
opsec: passive
opsecNote: Passive toward the subject, but this is a sensitive, adversarial database — searching or registering ties activity to you. Use a research identity; never create or post content, and treat entries as unproven allegations, not fact.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Crowd-sourced, user-submitted content about individuals; not curated or authenticated. High risk of error, bias and fabrication — corroborate only against court records.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Who's a Rat
- whosarat
tags:
- informants
- court-adjacent
- crowdsourced
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# WhosaRat.com

> A crowd-submitted database of alleged police/government informants and cooperating witnesses — searchable by name, but unverified and largely paywalled.

## When to use
You have a `name` and want to check whether it appears in this user-submitted database of alleged informants, cooperating witnesses, agents or associated attorneys — occasionally a lead when researching a legal-adjacent case. Treat everything here as unproven allegation: the content is anonymous and uncurated, and the real evidentiary source is court records, not this site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whosarat.com/ and search the `name` (limited browsing is free).
2. Note that full profile details, case documents and forums sit behind a paid membership (partial paywall).
3. Read any match as an unverified claim — capture the referenced case number/`document-id` if given.
4. Verify independently: pull the actual court docket/records (PACER, state courts) before believing anything.
5. Pivot: a cited case number feeds authoritative court-record searches, which are the real source of truth.

## Inputs → Outputs
- **In:** `name`
- **Out:** alleged informant/agent profile, sometimes a case `document-id` — all unverified
- **Empty/negative result looks like:** no match — which says nothing either way, given the database is small and crowd-built.

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall gates full profiles/documents (`payment-wall-partial`); registration required for those.
- OpSec: passive but sensitive — use a research identity; do not create/post entries.
- Reliability is low: user-submitted, adversarial content prone to error and defamation. Never treat an entry as established fact.

## Overlaps ("do both")
- Always pair with authoritative court-record sources (PACER, CourtListener, state dockets) — those are the verifiable basis; WhosaRat is at most a pointer to a case to check.

## Trust & verifiability
`trust: unverified` — anonymous crowd-sourced accusations with a paywall; corroborate any claim against primary court records and discard what you can't confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whosarat-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
