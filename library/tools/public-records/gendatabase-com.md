---
id: gendatabase-com
name: GenDatabase.com
description: Use when you have a `name` of a deceased South African and want genealogy/vital records (birth, death, marriage, estate, voter roll, ID) — returns dob, name, associate, document-id.
url: https://www.gendatabase.com/
category: public-records
path:
- public-records
bestFor: Researching a deceased South African subject's birth/death/marriage/estate records and ID number to anchor identity and surface relatives.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
- document-id
- address
status: live
pricing: freemium
costNote: Some free databases exist, but most searching requires a paid membership (about R110/US$6.99 per day up to R400/US$23.99 per month for unlimited searches).
opsec: passive
opsecNote: Searching transcribed historical/genealogy indexes is passive and does not alert anyone (the platform only covers deceased individuals, not living people). A paid membership ties access to a billing identity — use a dedicated account if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial South African genealogy platform providing transcribed (not original) records; useful as leads and pointers to official documents, but transcriptions can carry errors — verify against source registries.
missingPersonsRelevance: high
coverage:
- za
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Gen Database
- gendatabase
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# GenDatabase.com

> South Africa's largest genealogy research platform — over a billion transcribed birth, death, marriage, estate, voter-roll and ID records for the deceased.

## When to use
You have a `name` for a deceased South African (or an ancestor of a living subject) and want to anchor their identity — date of birth/death, ID number, marriage, estate file — and surface relatives named in those records. Strong for building a family tree around a subject, confirming a death, or extracting an SA ID number as a hard identifier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gendatabase.com/.
2. Search the exact full name and surname, or use `%` wildcards for partial/uncertain spellings.
3. Review previews; full record detail requires a paid membership (daily or monthly).
4. Read the transcribed record: birth/death dates, marriage, estate file, voter-roll entry, ID number, immigration status.
5. Pivot: an SA `document-id` (ID number) is a strong cross-reference; named relatives become `associate`/`name` leads; an estate file points to further official documents.

## Inputs → Outputs
- **In:** `name` (exact or `%` wildcard)
- **Out:** `dob`/death date, `name`, `associate` (relatives), `document-id` (SA ID number), `address` (last residence/estate)
- **Empty/negative result looks like:** no matching transcribed record — meaning the person isn't in these indexes (living people are excluded by design; coverage varies by era), not proof they never existed.

## Gotchas & OpSec
- Deceased only: it deliberately holds no data on living individuals.
- Freemium: most searching/detail is behind a subscription (payment-wall-partial).
- Records are transcriptions, not scans — treat as leads and request official documents to confirm.
- OpSec: passive; only the paid account is attributable.

## Overlaps ("do both")
- Pairs with `[[sadoctorsapp-co-za]]` for living-professional location and with official SA Home Affairs/deeds records — GenDatabase gives the historical/deceased genealogy layer those don't.

## Trust & verifiability
`trust: community` — a real, established commercial genealogy service, but its records are transcribed by the platform, so verify key facts (ID numbers, dates) against source registries before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gendatabase-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate, document-id, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
