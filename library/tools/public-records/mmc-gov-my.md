---
id: mmc-gov-my
name: Malaysian Medical Council Register (MeRITS)
description: Use when you have a doctor's `name` in Malaysia and want to verify registration — returns their registration number, qualifying institution, and practice status (employer-org, document-id).
url: https://merits.mmc.gov.my/search/registeredDoctor
category: public-records
path:
- public-records
bestFor: Verifying that a person is a registered medical practitioner in Malaysia and pulling their qualifications and registration status.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public register search; no account needed to search (some advanced features may prompt login).
opsec: passive
opsecNote: Official government register; read-only searches do not notify the practitioner. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Malaysian Medical Council (MeRITS — Medical Register Information and Technical System), the statutory licensing body for doctors in Malaysia.
missingPersonsRelevance: high
coverage:
- my
auth: none
api: false
localInstall: false
registration: false
aliases:
- MMC
- MeRITS
- Malaysian Medical Council
tags:
- professionlicensing
- Profession & Licensing Sites
- medical-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Malaysian Medical Council Register (MeRITS)

> Malaysia's official doctor register: confirm a person is a licensed medical practitioner and pull their registration details.

## When to use
You have a `name` for someone who claims to be — or is reported to be — a doctor in Malaysia, and you want to confirm it and extract identifiers. A licensing register turns a claimed profession into a verified `document-id` (registration number) and a qualifying `employer-org` (institution), which anchors identity and can seed further searches (alma mater, practice location).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://merits.mmc.gov.my/search/registeredDoctor.
2. Search by practitioner `name`; you can also filter by graduating institution, practice location, or registration type (full / provisional).
3. Read results: the doctor's name and qualifying institution show in the list; open "Details" for the registration number and status.
4. Pivot: the registration number (`document-id`) verifies identity; the institution/practice location narrows other people-search work.

## Inputs → Outputs
- **In:** `name` (optionally institution / location / registration type)
- **Out:** registered `name`, qualifying `employer-org` (institution), registration `document-id` and status (full/provisional)
- **Empty/negative result looks like:** no match — meaning not registered under that spelling, or not a Malaysian-registered doctor. A claimed doctor absent from the register is a red flag worth noting.

## Gotchas & OpSec
- Coverage is Malaysia only and doctors only — dentists/pharmacists have separate registers.
- Name transliteration varies (Malay/Chinese/Tamil names); try partial names and alternate spellings before concluding absence.
- OpSec: **passive**, official, read-only.

## Overlaps ("do both")
- Pairs with other national medical/professional registers when a subject may be licensed in more than one country — cross-border practitioners appear in each jurisdiction's register separately.

## Trust & verifiability
`trust: trusted` — the statutory licensing body's own register, so a hit is authoritative confirmation of medical registration in Malaysia.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mmc-gov-my |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
