---
id: sijilat-bh-2
name: Sijilat (Bahrain Commercial Registry)
description: Use when you have a Bahraini business `name`/CR number or an `employer-org` and want official commercial-registration data — returns company existence, status, activities, and registration details.
url: https://www.sijilat.bh/agency-registration/ARSearch/ar-search-1.aspx
category: public-records
path:
- public-records
bestFor: Official Bahrain company/commercial-registration lookups — status, activities, and registration details.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free public commercial-registration search on the government Sijilat portal; some detailed services/certificates may carry fees.
opsec: passive
opsecNote: Public registry lookup — the business/owners are not notified. Anonymous; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sijilat is Bahrain's official commercial registration portal (Ministry of Industry & Commerce) — the authoritative source for Bahraini company records.
missingPersonsRelevance: high
coverage:
- bh
auth: none
api: false
localInstall: false
registration: false
aliases:
- sijilat.bh
- Bahrain commercial registry
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Sijilat (Bahrain Commercial Registry)

> Bahrain's official commercial-registration portal — the authoritative check for whether a Bahraini company exists, its status, and its registered activities.

## When to use
You have a Bahraini business `name` or commercial-registration (CR) number, or an `employer-org` you suspect a subject is tied to, and you want the official record: company existence, status, licensed activities, and registration details. Relevant when an investigation touches Bahrain-based businesses — to confirm a company is real and connect a subject to it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Sijilat commercial-registration search (https://www.sijilat.bh/ → agency registration / AR search).
2. Search by company `name` or CR number (`employer-org`); Arabic and English name searches may both be supported.
3. Read the result: registered company name, CR number, status (active/expired), legal form, and licensed business activities.
4. Note the registered address/activities for context; some detailed certificates may require paid services.
5. Pivot: a confirmed company + activities feeds broader corporate mapping; registration details corroborate a subject's business footprint.

## Inputs → Outputs
- **In:** `employer-org` (company name or CR number), `name`
- **Out:** company existence/status, CR number, legal form, licensed activities, registration `address`
- **Empty/negative result looks like:** no match — the name/CR is wrong, transliterated differently (Arabic vs English), or the registration lapsed; not proof of non-existence.

## Gotchas & OpSec
- Bilingual search: Bahraini names transliterate multiple ways — try Arabic and English spellings.
- Owner/officer detail may be limited on the public search; deeper records can require paid certificates.
- OpSec: passive; the lookup is invisible to the business.

## Overlaps ("do both")
- Pairs with other Gulf/offshore registries and `[[jerseyfsc-org]]`/`[[gov-im]]` when a Bahraini entity links to offshore structures — each authoritative registry confirms its own jurisdiction; aggregators help connect them.

## Trust & verifiability
`trust: trusted` — Bahrain's official government commercial registry; company existence, status, and activities are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sijilat-bh-2 |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
