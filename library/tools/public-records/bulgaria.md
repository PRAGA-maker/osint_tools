---
id: bulgaria
name: Bulgarian Commercial Register (Registry Agency)
description: Use when you have a `name` or `employer-org` in Bulgaria and want to confirm company officers, ownership and registered addresses — returns employer-org, address, associate, name.
url: https://portal.registryagency.bg/CR/Reports/VerificationPersonOrg
category: public-records
path:
- public-records
bestFor: Linking a Bulgarian individual to the companies they direct or own, and pulling co-officers and registered addresses.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
- name
status: live
pricing: free
costNote: Free public search on the state Commercial Register portal; a paid/registered account is only needed for certified extracts and e-filing, not for read-only lookups.
opsec: passive
opsecNote: You query a government portal; the register is public and searches are not shown to the subject. No login is needed for the verification report, so a clean browser plus a neutral IP keeps the lookup unattributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Bulgarian Registry Agency (Агенция по вписванията) under the Ministry of Justice — the authoritative state source, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- bg
auth: none
api: false
localInstall: false
registration: false
aliases:
- Registry Agency Bulgaria
- registryagency.bg
- Търговски регистър
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Bulgarian Commercial Register (Registry Agency)

> Bulgaria's official Commercial Register: check which companies a person controls and who else sits on the board.

## When to use
You have a subject with a Bulgarian connection — a `name` or a known `employer-org` — and you want their business footprint: companies where they are a manager, owner or authorised representative, the registered seat (`address`) of those companies, and the co-officers (`associate`) filed alongside them. A strong pivot for turning a bare name into a network of business links and physical addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the portal and choose the **Commercial Register and Register of Non-Profit Legal Entities** ("Търговски регистър"). The `VerificationPersonOrg` report is the "check of a person/organisation" screen.
2. Enter the subject's `name` (Cyrillic gives best recall; also try transliteration variants) or a company name / UIC (ЕИК unique identification code).
3. Read the results:
   - A hit lists the company name, UIC, legal form, registered seat (`address`), and the natural persons filed as managers/owners — those co-named people are `associate` leads.
   - Open a company's file to see the full filing history and every officer ever recorded.
4. Pivot: co-officers feed back into another name search here; the registered address feeds property/geolocation work; the UIC lets you pull a certified extract if needed.

## Inputs → Outputs
- **In:** `name` or `employer-org` (company name / UIC)
- **Out:** `employer-org` (linked companies), `address` (registered seat), `associate` (co-officers/owners), `name` (canonical spelling)
- **Empty/negative result looks like:** "no results" for the entered name — meaning no current *or* historical commercial-register entry under that spelling. Retry Cyrillic and transliteration variants before concluding the person has no Bulgarian company ties.

## Gotchas & OpSec
- Name matching is spelling-sensitive; a Latin transliteration will miss Cyrillic filings and vice-versa. Search both.
- The read-only verification report is anonymous; only certified extracts and e-filing require the paid registered account — do not log in for OSINT lookups.
- OpSec: passive and low-risk; the subject is never notified. Still use a clean browser session out of habit.

## Overlaps ("do both")
- Pairs with an EU-wide company aggregator (OpenCorporates-style) — the national register is authoritative and current, while an aggregator cross-borders a person's directorships in one view.

## Trust & verifiability
`trust: trusted` — this is the Bulgarian state Registry Agency's own portal, so officer and ownership data is the primary legal record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bulgaria |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
