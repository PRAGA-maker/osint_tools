---
id: yellow-co-nz
name: yellow.co.nz
description: Use when you have a business `name`/`phone` in New Zealand and want contact and location details — returns address, phone, and website for NZ businesses (limited for private individuals).
url: https://yellow.co.nz/
category: phone
path:
- phone
bestFor: Looking up New Zealand business listings by name to get phone, address, and website.
selectorsIn:
- name
- phone
selectorsOut:
- name
- address
- phone
status: live
pricing: free
costNote: Free directory search; businesses pay for enhanced listings but lookup is free and needs no account.
opsec: passive
opsecNote: A published business directory — searching it does not notify anyone and reveals only self-published business contact data. Passive. It is not a reverse-lookup for private mobile numbers; expect little on individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official New Zealand Yellow Pages directory (Yellow NZ). Business data is self-submitted and generally reliable; coverage of private individuals is minimal.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- whitepages-nz
aliases:
- Yellow NZ
- Yellow Pages New Zealand
tags:
- mobilephone
- Mobile & Phone Related
- business-directory
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# yellow.co.nz

> New Zealand's official Yellow Pages: find a business's phone, address, and website by name — a business-first directory, not a personal reverse-phone tool.

## When to use
You have a New Zealand business `name` (or a number you suspect is a business line) and want its contact details, physical `address`, and website. Useful when a subject is tied to a NZ business — an employer, a trade, a shopfront — and you need to place that business geographically or find its public contacts. For private individuals it returns little; use a NZ people/white-pages source instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yellow.co.nz/.
2. Search by business name (and region/town to narrow), or by category to enumerate businesses of a type in an area.
3. Read the listing: business name, address, phone, website, sometimes hours and description.
4. Pivot: an address anchors a `geolocation`; a linked person/employer feeds people-search; for a residential number try `[[whitepages-nz]]`.

## Inputs → Outputs
- **In:** business `name` (or `phone` to sanity-check a listed business number)
- **Out:** `name`, `address`, `phone` (business website too)
- **Empty/negative result looks like:** no listing — the business isn't listed, is home-based/unregistered, or the number is a private mobile (not covered); absence doesn't disprove the business exists.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public self-published business data; no notification.
- Scope trap: this is a **business** directory. Do not expect reverse-lookup of personal mobile numbers or private residents here.

## Overlaps ("do both")
- Pairs with `[[whitepages-nz]]` — Yellow covers businesses, White Pages covers residential listings; run both for a NZ subject.

## Trust & verifiability
`trust: trusted` — the official NZ Yellow directory. Business contact data is generally reliable but self-submitted; confirm a critical address on a map or the business's own site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yellow-co-nz |
| category | phone |
| selectorsIn → selectorsOut | name, phone → name, address, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
