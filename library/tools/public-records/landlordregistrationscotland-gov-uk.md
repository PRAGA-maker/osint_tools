---
id: landlordregistrationscotland-gov-uk
name: Landlord Registration Scotland
description: Use when you have a Scottish rental property `address` (postcode) or a landlord registration number and want to confirm who is the registered landlord/agent — returns landlord/agent `name`, managing agent, and local authority.
url: https://www.landlordregistrationscotland.gov.uk/search
category: public-records
path:
- public-records
bestFor: Tying a Scottish rental property to its registered landlord and managing agent via the statutory register.
selectorsIn:
- address
- document-id
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public register under the Open Government Licence; no account needed.
opsec: passive
opsecNote: Public statutory register queried by postcode/registration number; the subject is not notified. No login, so nothing is tied to you beyond a normal web request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Scottish Government register maintained by local authorities; authoritative for who is legally registered to let a property.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scottish Landlord Register
- landlordregistrationscotland.gov.uk
tags:
- propertysites
- Property Related Sites
- landlord
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Landlord Registration Scotland

> Scotland's statutory landlord register — search a rental property's postcode (or a registration number) to learn who the registered landlord and managing agent are.

## When to use
You have a Scottish rental `address` and need the person or company legally responsible for letting it, or you have a landlord registration number and want the associated details. Useful for placing a subject at a property they own/let, identifying a managing agent (`employer-org`), and confirming a local authority for follow-up FOI/records requests. Note the search is keyed on postcode or registration number, not a free-text landlord name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.landlordregistrationscotland.gov.uk/search.
2. Enter the property **postcode** (or a known landlord **registration number**).
3. Select the specific property from the results.
4. Read the record: registered landlord `name`, managing agent (`employer-org`), registration status, and the local authority the property is registered in.
5. Pivot: the landlord name feeds people-search and Companies House; the local authority feeds council/FOI routes; a confirmed agent feeds a business lookup.

## Inputs → Outputs
- **In:** `address` (postcode) or `document-id` (registration number)
- **Out:** registered landlord `name`, managing agent (`employer-org`), local authority, registration status
- **Empty/negative result looks like:** no registered landlord for the postcode — either not a registered let, an exempt property, or non-compliance; absence is not proof no one lets it.

## Gotchas & OpSec
- Search is by postcode/registration number, not landlord name — you need the property first.
- Registers only *registered* landlords; unregistered/illegal lets won't appear.
- A managing agent may be listed instead of the beneficial owner — dig further for the true owner (Registers of Scotland/Land Register).

## Overlaps ("do both")
- Pairs with Registers of Scotland (title/ownership) and Companies House when the landlord is a company — this gives the letting registration, those give legal ownership.

## Trust & verifiability
`trust: trusted` — an official Scottish Government statutory register; the registration data is authoritative, though it reflects the registered party, which may differ from the true owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landlordregistrationscotland-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | address, document-id → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
