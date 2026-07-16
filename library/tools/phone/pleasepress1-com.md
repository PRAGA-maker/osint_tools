---
id: pleasepress1-com
name: Please Press 1
description: Use when you have a customer-service `phone` number and want to attribute it to a company and see its call-menu structure — returns employer-org.
url: https://www.pleasepress1.com
category: phone
path:
- phone
bestFor: Attributing a UK/US customer-service phone number to the company it belongs to via a crowd-built IVR-menu directory.
selectorsIn:
- phone
- employer-org
selectorsOut:
- employer-org
- phone
status: live
pricing: free
costNote: Free public directory; no account or payment required to search company customer-service numbers and menu maps.
opsec: passive
opsecNote: You are searching a static third-party directory, not dialling the number — nothing is leaked to the company. Calling the number itself would be active; this lookup is not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/editorially maintained UK directory of company call-centre menus; numbers are user-submitted and curated, not an official carrier database.
missingPersonsRelevance: high
coverage:
- uk
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- pleasepress1.com
- Please Press 1
tags:
- mobilephone
- Mobile & Phone Related
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Please Press 1

> A free directory of company customer-service phone menus — useful in reverse for saying "which company owns this 0800/1-800 number?"

## When to use
You have a `phone` number that looks like a business customer-service line (an 0800/0345/1-800 style number appearing in breach data, an ad, or a scam report) and you want to attribute it to an `employer-org`. Or you have a company and need its published customer-service number. This is a niche attribution aid, not a personal-phone lookup — it will not resolve a mobile to an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `pleasepress1.com` and use the search bar (accepts company name, sector, or a phone number).
2. Enter the `phone` number (or `employer-org` name).
3. Read the results:
   - A hit shows the company, its customer-service number(s), a map of the IVR menu ("press 1 for…"), and a star rating for menu quality — confirming the number belongs to that business.
   - Browsing by sector lists organisations and their published numbers.
4. Pivot: a confirmed company attribution feeds corporate-registry and domain research; rule the number *out* as a personal line if it maps to a call centre.

## Inputs → Outputs
- **In:** `phone` (business customer-service number) or `employer-org`
- **Out:** `employer-org` (owning company), `phone` (its other published lines)
- **Empty/negative result looks like:** no match — meaning the number isn't a catalogued business line (it may be a personal/mobile number, or simply not submitted). Absence is not proof of anything.

## Gotchas & OpSec
- Coverage is strongest for UK consumer brands, with a growing US section; obscure or overseas numbers may be missing.
- This is a directory of *business* lines only — never expect a personal mobile or landline to resolve here.
- OpSec: fully passive; you never contact the subject or the company.

## Overlaps ("do both")
- Pairs with a formatting/carrier lookup (e.g. a libphonenumber-style tool) — carrier lookup tells you the line type and region, this tells you the owning organisation for known business numbers.

## Trust & verifiability
`trust: community` — user-submitted and editorially curated; treat an attribution as a strong lead and confirm against the company's own website before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pleasepress1-com |
| category | phone |
| selectorsIn → selectorsOut | phone, employer-org → employer-org, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
