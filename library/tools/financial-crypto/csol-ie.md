---
id: csol-ie
name: csol.ie Bankruptcy Search
description: Use when you have a `name` and want to check Ireland's public bankruptcy register — returns bankruptcy status, address and adjudication details for a matched person.
url: https://www.csol.ie/ccms/bankruptcy.html#/search
category: financial-crypto
path:
- financial-crypto
bestFor: Checking whether a named person appears on Ireland's official bankruptcy register.
selectorsIn:
- name
selectorsOut:
- address
- dob
status: live
pricing: free
costNote: Free public search on Courts Service Online (Ireland). No account or payment to search the bankruptcy register.
opsec: passive
opsecNote: You query the Irish Courts Service register, not the subject — nobody is notified. Standard web access to a government public-records portal; use a VPN if you want to keep the query itself private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Courts Service Online (csol.ie) is the official Irish Courts Service system; bankruptcy adjudications listed here are authoritative public records.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Courts Service Online bankruptcy
- Irish bankruptcy register
- CSOL
tags:
- creditdebt
- Credit & Debtor Information
- bankruptcy
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# csol.ie Bankruptcy Search

> Ireland's official Courts Service bankruptcy register — a free name search that confirms whether someone has been adjudicated bankrupt and gives the address and dates on record.

## When to use
You have a `name` for an Irish subject and want an authoritative check of whether they appear on the bankruptcy register. A hit confirms a bankruptcy adjudication and typically surfaces the debtor's address, occupation, and key dates — useful for financial background, corroborating an address/locale, and understanding a subject's circumstances in a missing-persons or due-diligence context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.csol.ie/ccms/bankruptcy.html#/search .
2. Enter the subject's `name` (surname/first name) in the search form.
3. Read the matches: each record shows the bankrupt's name, `address`, often occupation, and the adjudication/discharge dates.
4. Pivot: the address anchors a locale for people/property searches; the dates and occupation corroborate other timeline evidence.

## Inputs → Outputs
- **In:** `name`
- **Out:** bankruptcy record — `address`, occupation, adjudication/discharge dates (and enough detail to disambiguate, sometimes an approximate `dob`/age)
- **Empty/negative result looks like:** "no results" — the person has not been adjudicated bankrupt in Ireland (or the name is spelled differently). Absence is meaningful here (it's a complete official register) but check name variants first.

## Gotchas & OpSec
- Register scope is **Ireland only** and covers formal bankruptcy adjudications — it won't show informal debt, other insolvency arrangements, or activity in other jurisdictions.
- Common names can produce multiple matches; use the address/occupation/dates to disambiguate before attributing a record to your subject.
- OpSec: fully passive — querying a government register, nothing is disclosed to the subject.

## Overlaps ("do both")
- Pair with the Irish Companies Registration Office and a general people-search — bankruptcy shows financial adjudication, company records show directorships, and people-search ties the address to current contact details.

## Trust & verifiability
`trust: trusted` — csol.ie is the official Irish Courts Service portal, so a listed adjudication is an authoritative public record; the only care needed is disambiguating common names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | csol-ie |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → address, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
