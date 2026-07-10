---
id: hitta-se-2
name: Hitta.se
description: Use when you have a `name` (or `phone`/`address`) in Sweden and want official-directory people/business data — returns `address`, `phone`, age and household `associate`s.
url: http://hitta.se
category: people-search
path:
- people-search
bestFor: Swedish people and business directory — name/phone/address lookups returning current address, phone, approximate age, and household members, drawing on Sweden's open population data.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
status: live
pricing: freemium
costNote: Free to search names, numbers, addresses, and view maps; some detailed/background reports are paid partner services. No account needed for basic lookups.
opsec: passive
opsecNote: Sweden's population registration data is legally public, so this lookup is routine and doesn't notify the subject. Queries go to a commercial directory that may log them — use a puppet browser/IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, established Swedish directory built on official population and business registry data — reliable for Swedish residents; less useful outside Sweden.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- hitta.se
- Swedish directory
tags:
- people-search
- sweden
- directory
- reverse-lookup
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Hitta.se

> Sweden's big people-and-business directory — thanks to Sweden's open population data, a name gets you a current address, phone, age, and who lives in the household.

## When to use
You have a `name`, `phone`, or `address` for someone in Sweden and want to locate them. Because Swedish population-registration (folkbokföring) data is legally public, Hitta.se can return a genuinely current home `address`, landline/mobile `phone`, approximate age, and household members — unusually complete compared with most countries. This is a primary locating tool for any Swedish-nexus missing-person or skip-trace case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hitta.se/ (Swedish interface; a translator helps).
2. Search by `name` (person or company), or use reverse lookup on a `phone` or `address`.
3. Read the result: current `address` with map, `phone` number(s), approximate age/birth year, and other people registered at the address (`associate`/household).
4. For deeper background, note the paid partner-report links; the free directory fields are usually the locating gold.
5. Pivot: household members → family graph; address → neighbours and property; phone → other reverse tools; cross-check on Eniro/Ratsit (other Swedish directories).

## Inputs → Outputs
- **In:** `name`, `phone`, or `address` (Sweden)
- **Out:** `address` (current, mapped), `phone`, `associate` (household/registered co-residents), approximate age
- **Empty/negative result looks like:** no match — the person may have a protected identity (skyddad identitet), be non-Swedish, recently moved, or spelled differently (å/ä/ö matter). A protected identity deliberately hides the record; that's a meaningful signal, not a tool error.

## Gotchas & OpSec
- **Swedish characters** (å, ä, ö) and name order affect matching — try variants.
- Some individuals have protected/secret identities and won't appear.
- Deeper "background" reports are paid; basic directory data is free.
- OpSec: **passive** — public data by Swedish law; no notification.

## Overlaps ("do both")
- Pairs with Eniro.se, Ratsit.se, and Merinfo.se — Sweden's other directories, each with slightly different data; cross-check for completeness. Use `[[forebears]]` first if unsure the subject is even Swedish.

## Trust & verifiability
`trust: community` — a major directory built on official Swedish registry data, so core address/phone fields are reliable for residents. Confirm against a second Swedish directory for anything decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hitta-se-2 |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
