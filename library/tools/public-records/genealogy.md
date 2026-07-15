---
id: genealogy
name: "Genealogy.com death records"
description: Use when you have a `name` and want to check death records / obituaries to confirm a person is deceased and surface relatives — returns `dob`/death dates, `name` variants and `associate` (family) links.
url: https://www.genealogy.com/lp/death-records
category: public-records
path:
- public-records
bestFor: Starting a death-records / obituary search by name to confirm death and identify family members.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: freemium
costNote: The landing page and basic searching are free, but genealogy.com is an Ancestry-owned funnel — full record images (Social Security Death Index, obituaries, death certificates) typically require an Ancestry subscription.
opsec: passive
opsecNote: Passive records search; the (deceased) subject and living relatives are not notified. Registration/subscription ties searches to an account — use a research account, not personal, if you sign up.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: genealogy.com is a long-running genealogy portal owned by Ancestry; the death-record datasets it draws on (SSDI, obituaries) are legitimate, though full access is a paid upsell.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- genealogy.com
- death records genealogy
tags:
- genealogy
- family
- death-records
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Genealogy.com death records

> An Ancestry-owned genealogy portal's death-records entry point — search a name to check whether a person has died and to surface obituaries and family links. Deceased-status is a fast way to close (or redirect) a missing-person line of inquiry.

## When to use
You have a `name` and need to determine whether the person is deceased, or you want to build the family network around them (parents, spouse, children) via death/obituary records. Confirming a death resolves a search; the associated obituary and index records also name relatives (`associate`) and dates (`dob`/death) that pivot to living family who may know a subject's whereabouts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.genealogy.com/lp/death-records and enter the subject's name (add approximate location/dates to narrow).
2. Review the free result snippets — matching index entries, obituaries, Social Security Death Index hits.
3. To view full record images you'll usually be routed to an Ancestry subscription (payment wall) — decide whether the free snippet already answers your question.
4. Extract dates and named relatives from what's visible.
5. Pivot: relatives feed people-search and social OSINT; a confirmed death with dates feeds official vital-records requests.

## Inputs → Outputs
- **In:** `name` (plus optional place/date)
- **Out:** death/obituary index hits — `name` (incl. maiden/variant), `dob`/death dates, relatives (`associate`)
- **Empty/negative result looks like:** no index match — the person may be living, the record not digitised, or under a different spelling. Absence is not proof of life; corroborate with SSDI-specific and local obituary searches.

## Gotchas & OpSec
- Freemium funnel: the free tier shows teasers; full images push you to a paid Ancestry subscription.
- US-centric (SSDI, US obituaries); weak for deaths abroad.
- Index transcription errors are common in older records — search loosely and cross-check dates.

## Overlaps ("do both")
- Pairs with dedicated obituary aggregators, FindAGrave, and the SSDI — genealogy.com is one funnel into overlapping datasets; use the free specialised sources to avoid the paywall where possible.

## Trust & verifiability
`trust: trusted` — a reputable Ancestry-owned portal over legitimate death datasets; the data is sound but access is monetised, so verify a death against a second free source (obituary, grave record) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogy |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
