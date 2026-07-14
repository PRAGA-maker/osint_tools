---
id: nigeria-sexual-offenders-registers
name: Nigeria Sexual Offenders Database (NAPTIP)
description: Use when you have a `name` and want to check whether a person appears in Nigeria's national sexual-offenders database as reported, arraigned, or convicted — returns offence status and case details.
url: https://nsod.naptip.gov.ng/
category: public-records
path:
- public-records
bestFor: Background-checking a name against Nigeria's national register of reported/convicted sexual offenders.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- physical-description
status: live
pricing: free
costNote: Convicted-offender records are free to view online; non-convicted categories (reported/arraigned but not convicted) are released on demand rather than shown publicly.
opsec: passive
opsecNote: Searching a public government register is passive and anonymous; the listed individual is not notified. Handle results carefully — these are sensitive criminal-status records; corroborate before acting and respect the presumption of innocence for non-convicted entries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NAPTIP (National Agency for the Prohibition of Trafficking in Persons), a Nigerian federal agency; authoritative for the records it publishes.
missingPersonsRelevance: high
coverage:
- ng
auth: none
api: false
localInstall: false
registration: false
aliases:
- NAPTIP NSOD
- Nigeria National Sexual Offenders Database
tags:
- offenders
- background-check
- nigeria
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Nigeria Sexual Offenders Database (NAPTIP)

> Nigeria's official national sexual-offenders database: check whether a name has been reported, arraigned, or convicted for sexual offences.

## When to use
You have a `name` with a Nigerian nexus and need a criminal-background signal — for safeguarding checks, vetting, or corroborating an investigation. Convicted offenders are searchable directly on the site; the database also tracks cases in court and under investigation (accessible on demand). A match provides case details and, in some records, a `physical-description` and photo useful for identity confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nsod.naptip.gov.ng/ and go to the offender/case listing (the "view cases" section — reach it from the homepage nav if a direct link 404s).
2. Search or browse by the subject's `name`.
3. Read the record: offence status (reported / arraigned / convicted), case reference (`document-id`), and any published description or photo.
4. Pivot: a convicted record with a photo/description feeds face/image search and corroborates identity; the case reference can support formal follow-up with NAPTIP.

## Inputs → Outputs
- **In:** `name`
- **Out:** offence status, case `document-id`, offender `name`, and where published a `physical-description`/photo
- **Empty/negative result looks like:** no match — the person may not be in the database, may be in a non-convicted category not shown publicly, or the name may be spelled/transliterated differently. Absence is not proof of a clean record.

## Gotchas & OpSec
- Distinguish **convicted** entries (shown publicly) from **reported/arraigned/under-investigation** entries (released on demand) — the latter are allegations, not findings; respect the presumption of innocence.
- These are highly sensitive records; verify identity carefully before attaching a status to a real person, and mind local data/defamation law.
- OpSec: passive; the individual is not notified.

## Overlaps ("do both")
- Do both with face/reverse-image tools (on any published offender photo) and with Nigerian court/news sources to corroborate a case before relying on it.

## Trust & verifiability
`trust: trusted` — first-party data from NAPTIP, the Nigerian federal agency responsible for the register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nigeria-sexual-offenders-registers |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
