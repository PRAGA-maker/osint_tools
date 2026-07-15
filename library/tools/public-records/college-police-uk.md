---
id: college-police-uk
name: college.police.uk (Police Barred List)
description: Use when you have a `name` and want to check whether a UK police officer/special was dismissed for misconduct — returns the barred person's `name`, former force (`employer-org`) and dismissal details.
url: https://www.college.police.uk/ethics/barred-list/search-the-barred-list
category: public-records
path:
- public-records
bestFor: Checking the public Police Barred List to see if a named individual was dismissed from UK policing for gross misconduct.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public search operated by the College of Policing; no account required.
opsec: passive
opsecNote: Reading a public register does not notify the individual. Only the College of Policing site sees the query; use a sock puppet only if the wider investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the College of Policing, the professional body for UK policing — the authoritative first-party source for the statutory Police Barred List.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- mpts-uk-org-2
aliases:
- Police Barred List
- College of Policing Barred List
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# college.police.uk (Police Barred List)

> The public register of UK police officers dismissed for gross misconduct — confirm, by name, whether someone was barred from policing and which force they left.

## When to use
Your subject is, or claims to be, a current or former UK police officer/special constable, and you want to test that against the misconduct record. The College of Policing's **Barred List** is publicly searchable by `name` and shows officers dismissed after conduct/performance proceedings, their former force (`employer-org`), and the basis for barring. It's useful for vetting an identity or authority claim, for background on a person who worked in policing, and for spotting a name that left a force under a cloud. (The related **Advisory List** — those who resigned/retired mid-investigation — is *not* public.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.college.police.uk/ethics/barred-list/search-the-barred-list (the older `What-we-do/…/Search.aspx` path has been retired).
2. Enter the subject's `name`.
3. Read any match: barred individual's name, former force, and the dismissal details/date shown.
4. Note the five-year rule — entries are removed five years after publication — so an absence may mean "never barred" *or* "barred more than five years ago."
5. Pivot: a former-force name feeds force-specific and local-news OSINT; confirming ex-police status can corroborate or debunk claims elsewhere in the investigation.

## Inputs → Outputs
- **In:** `name` (optionally cross-referenced with a claimed `employer-org`/force)
- **Out:** barred person's `name`, former force (`employer-org`), dismissal basis/date
- **Empty/negative result looks like:** no match for the name — the person hasn't been publicly barred (or was barred >5 years ago and aged off, or is police *staff*/PCSO, who are excluded from the public list). Not proof of a clean record on its own.

## Gotchas & OpSec
- Human-in-the-loop: none; a simple name search.
- OpSec: **passive** — public register, no subject notification.
- Scope: **officers and specials only** — police staff and PCSOs do not appear on the public list; only conduct/performance *dismissals* are shown, and entries drop off after five years. Same-name collisions are possible; corroborate with the force and dates.

## Overlaps ("do both")
- Pairs with `[[mpts-uk-org-2]]` — both are UK professional-conduct registers; where MPTS covers struck-off doctors, the Barred List covers dismissed police, and the same background-check workflow (name → profession register → force/employer) applies.

## Trust & verifiability
`trust: trusted` — the official College of Policing register, authoritative for public barrings. Caveats are scope and the five-year removal rule, not data quality; verify a match against the named force before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | college-police-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
