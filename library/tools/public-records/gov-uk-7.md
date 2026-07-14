---
id: gov-uk-7
name: Immigration Advice Authority Adviser Finder (formerly OISC)
description: Use when you have a `name` or `employer-org` of a UK immigration adviser and want to confirm they are officially regulated — returns the adviser/organisation, authorisation level, and contact details.
url: https://home.oisc.gov.uk/adviser_finder/finder.aspx
category: public-records
path:
- public-records
bestFor: Verifying whether a person/firm is a regulated UK immigration adviser and at what authorisation level.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
status: degraded
pricing: free
costNote: Free official register; no account needed.
opsec: passive
opsecNote: Public regulator register queried by name/location; the subject is not notified and no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK regulator register — the OISC became the Immigration Advice Authority (IAA) on 16 Jan 2025; the current finder lives at portal.immigrationadviceauthority.gov.uk, and the old OISC URL redirects there.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- OISC Adviser Finder
- Immigration Advice Authority Adviser Finder
- IAA register
tags:
- professionlicensing
- Profession & Licensing Sites
- immigration
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Immigration Advice Authority Adviser Finder (formerly OISC)

> The UK regulator's public register of authorised immigration advisers — confirm whether a named person or firm is legally allowed to give immigration advice, and at what level.

## When to use
Your subject claims to be, or is described as, a UK immigration adviser/consultant and you want to confirm that against the statutory regulator: are they registered, under which organisation (`employer-org`), at what authorisation level, and with what contact details? Providing immigration advice while unregulated is illegal in the UK, so absence from this register is itself significant. Marked `degraded` only because the OISC was renamed the Immigration Advice Authority (IAA) in January 2025 — the tool works, but the live URL moved.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Adviser Finder — the old OISC URL (https://home.oisc.gov.uk/adviser_finder/finder.aspx) now routes to the IAA portal at portal.immigrationadviceauthority.gov.uk/s/adviser-finder.
2. Search by adviser/organisation `name` or by location/postcode.
3. Read the record: registered adviser or organisation `name`, authorisation level, website, and contact details.
4. Cross-check the organisation and address against Companies House and the firm's own site.
5. Pivot: a registered firm → business/officer lookups; no record → check other regulators (SRA, CILEx, Law Society of Scotland/NI) before concluding they are unregulated.

## Inputs → Outputs
- **In:** `name` (adviser/firm), `address`/postcode, or `employer-org`
- **Out:** confirmed adviser/organisation `name`, authorisation level, `employer-org`, contact `address`/details
- **Empty/negative result looks like:** no match — the person/firm is not IAA-regulated; check whether they're covered by a different legal regulator before assuming they're operating illegally.

## Gotchas & OpSec
- Rebrand: search the IAA portal, not the legacy OISC page, if the old link fails.
- Solicitors/barristers may give immigration advice under the SRA/Bar rather than the IAA — a blank here isn't the whole picture.
- The register reflects current authorisation; historic lapses may not show.

## Overlaps ("do both")
- Pairs with Companies House and the SRA/CILEx registers — this confirms immigration-advice authorisation, those confirm corporate identity and other legal regulation.

## Trust & verifiability
`trust: trusted` — the UK government's own regulator register; authoritative for regulated status. Just ensure you're querying the current IAA portal after the 2025 rename.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-7 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
