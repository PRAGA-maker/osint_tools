---
id: osint-list-of-public-sex-offenders-registers-osintme-com
name: OSINT list of public sex offenders registers – osintme.com
description: Use when you have a subject `name` (and possibly a country) and want to check public sex-offender registers worldwide — returns links to national registers that can confirm an address, photo, or DOB.
url: https://www.osintme.com/index.php/2021/08/31/osint-list-of-public-sex-offenders-registers/
category: public-records
path:
- public-records
bestFor: A curated country-by-country index of publicly accessible sex-offender registers, for checking a named subject against official registries.
selectorsIn:
- name
selectorsOut:
- address
- image
- dob
status: live
pricing: free
costNote: Free blog article; the registers it links to are themselves public and free, though some require captcha or local-language navigation.
opsec: passive
opsecNote: Reading the OSINTme article is passive. The linked registers are official government sites — searching them is generally passive too, but some (e.g. the US NSOPW) log queries and a few require you to accept terms; use a clean browser and avoid entering identifying info about yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Written by OSINTme (Matthias Wilson), a recognized OSINT practitioner; the article is a signpost, and the authority rests with the official government registers it links to.
missingPersonsRelevance: high
coverage:
- global
- us
- kr
- ca
- gb
- ng
- pl
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nsopw
- osintme-com
aliases:
- OSINTme sex offender registers list
- public sex offender registers
tags:
- sex-offender-register
- curated-list
- public-records
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# OSINT list of public sex offenders registers – osintme.com

> A single article that maps where the world's *publicly searchable* sex-offender registers live, so you can check a named subject country by country.

## When to use
You have a subject `name` and a reason to check whether they appear on a public sex-offender register — for example, vetting, safeguarding, or corroborating a criminal history across borders (offenders travel, and destination countries often don't know a visitor's background). This article is the index that tells you which countries actually publish a searchable register and links straight to each.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OSINTme article and scan the country sections.
2. Pick the register(s) for the country/countries relevant to your subject: US (**NSOPW** — the national portal), South Korea, Canada (provincial, e.g. Manitoba), Nigeria (NAPTIP), Poland (public, with photos and birth dates), Maldives (child sex offender registry), plus notes on the UK (no public register — only third-party aggregations of court reporting).
3. Follow the link, then search that register by `name` (and locality where offered).
4. Read the result: a match typically shows a photo, `dob`, and a current or registered `address`/area.
5. Pivot: a register hit confirms identity and location; the photo feeds face/reverse-image search, and the address feeds property/registry lookups.

## Inputs → Outputs
- **In:** subject `name` (+ country to pick the right register).
- **Out:** via the linked registers — offender `image`, `dob`, and registered `address`/locality.
- **Empty/negative result looks like:** the article itself never "fails" (it is a list); a *register* returning no match means the person isn't listed there, which is not proof of no record — many countries have no public register at all, and the UK notably does not.

## Gotchas & OpSec
- This is a signpost, not a search engine — the actual lookups happen on the government sites it links to, whose interfaces, languages, and freshness vary widely.
- The article dates from 2021; individual register URLs may have moved and new registers (e.g. Trinidad & Tobago) may have launched since — treat a dead link as "find the current official page."
- Coverage is patchy globally; absence of a hit reflects the register's scope, not necessarily the subject.

## Overlaps ("do both")
- Pairs with `[[nsopw]]` — use NSOPW directly for the US national search, and this list to reach the equivalent registers in other countries. Also pairs with the broader `[[osintme-com]]` resource hub for related people-search guidance.

## Trust & verifiability
`trust: community` — the article is a well-regarded practitioner's curation, and the underlying data comes from official government registers, which are authoritative. Verify any match on the register's own page (and against a second identifier like DOB) before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-list-of-public-sex-offenders-registers-osintme-com |
| category | public-records |
| selectorsIn → selectorsOut | name → address, image, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
