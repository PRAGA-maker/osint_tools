---
id: genealogybank-ssdi
name: GenealogyBank (SSDI & Obituaries)
description: Use when you have a `name` (and maybe `dob`) and want to confirm a death or find an obituary — returns Social Security Death Index and obituary records yielding `dob`, death date and last `address`.
url: https://www.genealogybank.com/
category: public-records
path:
- public-records
bestFor: Checking the Social Security Death Index and a large historical newspaper/obituary archive to determine whether a US person is deceased.
selectorsIn:
- name
- dob
selectorsOut:
- name
- dob
- address
status: live
pricing: freemium
costNote: The SSDI lookup is free to search; the full obituary/newspaper archive is behind a paid subscription (free trial available). Registration required for most record views.
opsec: passive
opsecNote: Searching genealogical/death records reveals nothing about your subject and alerts no one. Passive. (Registration/subscription ties usage to an account — use a research account.)
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: The SSDI is a US government-derived death index (authoritative for deaths reported to the SSA); the surrounding newspaper/obituary content is a commercial archive of primary sources.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- genealogy-bank
aliases:
- SSDI
- Social Security Death Index
- GenealogyBank
tags:
- ssdi
- genealogy
- death-records
- obituaries
source: inteltechniques-tools
lastVerified: '2026-07-16'
enrichment: full
---

# GenealogyBank (SSDI & Obituaries)

> A US death-and-obituary resource combining the Social Security Death Index with a large historical newspaper archive — a primary way to answer "is this person deceased?"

## When to use
You have a `name` (ideally with a `dob` or approximate age and US location) and need to determine whether the person has died. The free SSDI search confirms deaths reported to the Social Security Administration (with dates and last-residence clues); the obituary/newspaper archive can add cause, family and biographical detail. Directly relevant when a missing-person trail may end in an unrecorded death.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.genealogybank.com/ and open the SSDI search (free).
2. Enter the `name`; narrow with birth year/`dob` and state.
3. Read the SSDI output: matching records with birth date, death date, and last-residence (often ZIP/state → approximate `address`).
4. For richer detail, search the obituary/newspaper archive (subscription/free-trial) for the same name.
5. Pivot: take the death date and location into Find A Grave, state vital records, and obituary searches; use family names from obituaries as `associate` leads.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/location)
- **Out:** `name`, `dob`, death date, and last-residence `address` (SSDI), plus obituary detail
- **Empty/negative result looks like:** no SSDI match — the person may be alive, may have died without an SSA-reported death, or the death is too recent/pre-dates coverage; not proof of being alive.

## Gotchas & OpSec
- SSDI covers deaths *reported to the SSA* (strongest ~1962 onward) — gaps exist, and recent deaths are withheld for a few years, so absence is inconclusive.
- The SSDI search is free, but full obituary/newspaper records are paywalled (partial paywall / trial).
- Common names need `dob`/location to disambiguate.
- OpSec: passive; searching records signals nothing.

## Overlaps ("do both")
- Pairs with `[[genealogy-bank]]` (same provider) and `[[find-a-grave]]` — the SSDI gives the authoritative death fact and date; Find A Grave adds burial location, photos and linked family.

## Trust & verifiability
`trust: community` — the SSDI is a government-derived index (authoritative for reported deaths), wrapped in a commercial archive. Corroborate a specific death against a state vital record when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogybank-ssdi |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → name, dob, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
