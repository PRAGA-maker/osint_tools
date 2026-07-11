---
id: gmc-uk-org
name: gmc-uk.org (GMC Medical Register)
description: Use when you have a doctor's `name` (or GMC number) and want to verify UK medical registration/licence — returns employer-org context, registration status, and document-id (GMC number).
url: https://www.gmc-uk.org
category: public-records
path:
- public-records
bestFor: Verifying whether a doctor is registered and licensed to practise medicine in the UK via the GMC's public medical register (LRMP).
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public search of the List of Registered Medical Practitioners (LRMP); no account needed.
opsec: passive
opsecNote: Official regulator's public register — searching does not notify the doctor and reveals only your IP to the GMC. Fully passive records lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK regulator (General Medical Council); the authoritative register of who may practise medicine in the UK.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ifa-org-uk
- myewc-wales-2
aliases:
- GMC
- General Medical Council
- medical register LRMP
tags:
- professionlicensing
- Profession & Licensing Sites
- regulator-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# gmc-uk.org (GMC Medical Register)

> The General Medical Council's public register — confirm whether a named doctor is registered and licensed to practise medicine in the UK, and read their registration history.

## When to use
You have a `name` for someone who claims to be (or is described as) a UK doctor, and you want to verify the credential. The GMC's List of Registered Medical Practitioners (LRMP) is the authoritative source: it confirms registration status, licence to practise, GMC reference number (`document-id`), primary medical qualification, and any published fitness-to-practise history/conditions. Strong for confirming an occupation claim, corroborating identity, or checking a professional's standing in a trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gmc-uk.org and open the medical register / "check the register" search.
2. Search by doctor's name or GMC reference number (add specialty/location to disambiguate common names).
3. Read the entry: registration status, whether they hold a licence to practise, GMC number (`document-id`), year and place of primary qualification, and any published sanctions/conditions.
4. Absence means not GMC-registered — they may practise a different profession or in another country; it does not by itself prove impersonation.
5. Pivot: GMC number is a stable identifier; qualification place/year anchors a timeline; a linked employer/practice feeds people/property searches.

## Inputs → Outputs
- **In:** doctor's `name` or GMC number
- **Out:** registration/licence status, GMC reference (`document-id`), qualification details, fitness-to-practise history (`employer-org`/practice context where shown)
- **Empty/negative result looks like:** no match — not a GMC-registered doctor (could be another regulator: NMC for nurses, GDC for dentists, or a non-UK practitioner); disambiguate before concluding.

## Gotchas & OpSec
- Scope is **medical doctors** regulated by the GMC — nurses (NMC), dentists (GDC), pharmacists (GPhC) etc. are on separate registers.
- A registered doctor without a *licence to practise* is registered but not currently permitted to practise — read that field carefully.
- OpSec: passive — an official public register with no notification.

## Overlaps ("do both")
- Pairs with other UK professional registers like [[ifa-org-uk]] (accountants) and [[myewc-wales-2]] (education workforce) — pick the register matching the claimed profession; GMC is specifically for doctors.

## Trust & verifiability
`trust: trusted` — first-party GMC data; the authoritative UK medical register. A match is a verified regulatory fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gmc-uk-org |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
