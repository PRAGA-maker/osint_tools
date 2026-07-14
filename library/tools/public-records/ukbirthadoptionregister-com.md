---
id: ukbirthadoptionregister-com
name: ukbirthadoptionregister.com
description: Use when you have a `name` and approximate `dob` and are working an adoption-reunion case — searches an adoption contact register to link adopted people with birth parents/siblings; returns name, dob, and associate leads.
url: https://www.ukbirthadoptionregister.com/search.php
category: public-records
path:
- public-records
bestFor: Matching adopted people with birth relatives via a voluntary UK adoption contact/reunion register.
selectorsIn:
- name
- dob
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free to search the register. (Some UK reunion registers charge to register an entry, but searching entries here is free.)
opsec: passive
opsecNote: A voluntary reunion register — entries are self-submitted by people seeking contact. Search is passive, but this is sensitive personal territory; use findings only for legitimate reunification/tracing, never to expose someone who has not sought contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A private/voluntary adoption contact register, not an official government record; entries are self-reported and unverified, so treat matches as leads requiring confirmation.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gro-gov-uk
- freebmd
aliases:
- UK Birth Adoption Register
- ukbirthadoptionregister.com
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- adoption
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ukbirthadoptionregister.com

> A voluntary UK adoption-reunion register: search self-submitted entries to connect adopted people with birth parents and siblings who are also looking.

## When to use
You are working an adoption or family-tracing case and have a `name` and approximate `dob`. This register lets you search two pools — adopted people, and birth parents/siblings — for someone actively seeking contact. Because entries are self-submitted by people who *want* to be found, a match is a strong, consent-backed lead toward a relative (`associate`) and can supply a name, DOB, and reunion contact route.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ukbirthadoptionregister.com/search.php.
2. Choose which database to search — adopted people, or birth parents/siblings.
3. Enter the `name` and `dob` you have; partial dates (year-only, or fields left as "n/a") are allowed to widen the net.
4. **Search both databases** — the matching person may have registered on either side.
5. Read matches: self-reported name, date/place of birth, and the contact/reunion details the registrant provided. Pivot to official records to confirm.

## Inputs → Outputs
- **In:** `name` + approximate `dob`
- **Out:** `name`, `dob`, and `associate` (a birth relative / adopted person seeking contact), plus the registrant's reunion contact route
- **Empty/negative result looks like:** no matching entry — very common, because only people who have proactively registered appear. Absence means "not on this voluntary register," not that the relative can't be found elsewhere.

## Gotchas & OpSec
- **Voluntary and partial** — only self-registered, consenting people appear; most adoptions are not represented.
- Entries are self-reported and unverified — confirm any match against official records before acting.
- **Sensitivity:** adoption reunion is emotionally and legally delicate; use only for legitimate tracing and respect that the other party registered on their own terms.
- OpSec: passive search.

## Overlaps ("do both")
- Pairs with official UK records — the GRO birth index ([[gro-gov-uk]]) and [[freebmd]] — to verify a self-reported match against civil registration, and with the statutory Adoption Contact Register for the government-run equivalent.

## Trust & verifiability
`trust: unverified` — a private voluntary register of self-submitted, unverified entries; matches are consent-backed leads that must be confirmed against official birth/adoption records before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukbirthadoptionregister-com |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → name, dob, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
