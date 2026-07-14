---
id: lithuania
name: Lithuania Register of Legal Entities (JAR)
description: Use when you have a company name, person name or address and want official Lithuanian company records — returns registration code, legal status, address and management/officer names.
url: https://www.registrucentras.lt/jar/p_en/
category: public-records
path:
- public-records
bestFor: Verifying a Lithuanian company and finding the people (directors, managers) legally tied to it.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: free
costNote: Free public search of the Register of Legal Entities, capped at roughly 100 free searches per day; formal certified extracts and deeper filings are paid.
opsec: passive
opsecNote: Querying an official public register is passive — the subject is not notified. The state operator logs standard web access; use a VPN for sensitive lookups. You are searching a government database, so stay within lawful public-record use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the State Enterprise Centre of Registers (Registrų centras) under Lithuania's Ministry of Justice — the authoritative national company register.
missingPersonsRelevance: high
coverage:
- lt
auth: none
api: false
localInstall: false
registration: false
aliases:
- Registru centras
- JAR
- Lithuania company register
- Register of Legal Entities Lithuania
tags:
- companysites
- Company Related Sites
- corporate-registry
- lithuania
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Lithuania Register of Legal Entities (JAR)

> Lithuania's authoritative national company register — search legal entities by name, person or address to confirm a company and surface the officers legally attached to it.

## When to use
You have a Lithuanian `employer-org` (company name or registration code), a `name` of someone you think holds a company role, or an `address` you want to tie to a business. JAR is the first-party record: it confirms whether a company exists, its legal status (active/liquidated), registered address, legal form, and the names of management-body members — which turns a company lead into named people, or a named person into the companies they run.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.registrucentras.lt/jar/p_en/ (the English public-search interface).
2. Search by company `name`/registration code, by a person's `name`, or by `address` — the public search supports all three.
3. Open a matching legal entity to read its registration code, legal form, status, registered `address`, activity field, and listed management-body members.
4. Note the numeric registration code — it is the stable key for cross-referencing other Lithuanian/EU sources (e.g. rekvizitai.lt, EU Business Registers).
5. Pivot: officer `name`s feed people-search and social lookups; the registration code feeds paid certified extracts if you need court-usable proof; the address feeds mapping.

## Inputs → Outputs
- **In:** `employer-org` (name/code), `name` (person), or `address`
- **Out:** `employer-org` details, `address`, officer `name`s (`associate` links to the company), legal status
- **Empty/negative result looks like:** no entity matched, or a hit with limited public fields. Try the Lithuanian-language spelling and the registration code; absence in JAR means no *registered legal entity* under that term, not that a person doesn't exist.

## Gotchas & OpSec
- The English UI is partial — some labels and deeper data appear only in Lithuanian; keep a translator handy.
- Free search is capped (~100/day) and certified extracts / full filing history are paid; the free view is enough for identity/officer confirmation.
- It registers *legal entities*, not private individuals — you find people only via their company roles.
- Passive and lawful public-record use; the register logs access but does not alert the subject.

## Overlaps ("do both")
- Pairs with rekvizitai.lt and EU-wide business-register aggregators to cross-check the same registration code and fill gaps in the free view.
- Officer names feed people-search / social-profile tools to move from a corporate role to a real person.

## Trust & verifiability
`trust: trusted` — this is the official Registrų centras register under the Ministry of Justice, so entity, status and officer data are authoritative; certified paid extracts exist when you need legally-usable proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lithuania |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
