---
id: interment
name: Interment
url: http://www.interment.net/data/search.htm
category: public-records
path:
- public-records
description: Use when you have a `name` of a possibly-deceased person and want burial/cemetery records — returns death dates, cemetery location, and related-family names.
bestFor: Confirming a death and locating the cemetery/interment record for a named person, especially in the US.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- dob
- associate
- address
status: live
pricing: free
costNote: Free online library of cemetery transcriptions; no account or payment required to search.
opsec: passive
opsecNote: Passive read of a public genealogy archive. You are not contacting the subject or any live account, so nothing is disclosed to a target. Standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running single-sourced (not crowd-sourced) transcription project; records come from cemetery offices, churches and archives rather than volunteer edits, so entries are relatively reliable but coverage is patchy.
missingPersonsRelevance: high
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- interment.net
- Interment.net Cemetery Records
tags:
- genealogy
- family
- burial-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Interment

> A free, single-sourced cemetery-transcription library used to confirm a death and pin down the cemetery, burial date and family links for a named person.

## When to use
You have a `name` (optionally a US state/region as rough `geolocation`) for someone who may be deceased, and you need to confirm the death and find the interment record. A hit gives you a death year, cemetery and often adjacent family plots — which turns a cold "is this person even alive?" question into dated, place-anchored facts you can pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.interment.net/data/search.htm in a clean browser.
2. Enter the subject's surname (and given name if common), optionally narrowing by US state or country from the region lists.
3. Use search operators when a name is common: quote `"john smith"` for an exact phrase, or add a state name to constrain results.
4. Read the transcription: name, birth/death dates, cemetery name and location, and sometimes headstone-adjacent relatives.
5. Pivot: a confirmed cemetery + death date feeds obituary and probate searches; adjacent plot names feed `[[deceasedonline-com]]` (UK) or general genealogy for next-of-kin.

## Inputs → Outputs
- **In:** `name` (+ optional `geolocation` / state)
- **Out:** `name`, `dob` (birth/death dates), cemetery `address`/location, `associate` (family buried nearby)
- **Empty/negative result looks like:** no matching transcription rows — this means the record hasn't been transcribed here, NOT that the person is alive or never died. Coverage is uneven, so confirm elsewhere before concluding.

## Gotchas & OpSec
- Coverage is single-sourced and incomplete: an absent record proves nothing. Treat a miss as "unknown," not "no death."
- Transcriptions can contain reading errors from worn headstones; verify dates against a second source.
- OpSec: fully passive archive read — no login, no target contact, no notification risk.

## Overlaps ("do both")
- Pairs with `[[deceasedonline-com]]` — Interment is strongest for US cemeteries while DeceasedOnline covers UK burial/cremation registers; run both when the subject's country is uncertain.

## Trust & verifiability
`trust: community` — a stable, decades-old transcription library sourced from official cemetery/church records rather than open crowd edits, so individual entries are fairly trustworthy even though overall coverage is spotty.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | interment |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → name, dob, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
