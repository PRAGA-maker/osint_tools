---
id: ico-org-uk
name: ICO Data Protection Register (ico.org.uk)
description: Use when you have an organisation/sole-trader `name` and want to confirm UK data-protection registration and its contact details — returns registered name, address, and employer-org registration.
url: https://ico.org.uk/ESDWebPages/Search
category: public-records
path:
- public-records
bestFor: Confirming a UK business/sole trader is registered with the ICO and pulling its registered name, address, and registration number.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free official UK register maintained by the Information Commissioner's Office; no account.
opsec: passive
opsecNote: A public register lookup; the registrant is not notified. Nothing is sent to the subject. Note that sole traders who register may have their home address published here — handle personal addresses responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Information Commissioner's Office (the UK data-protection regulator); the authoritative register of fee-paying data controllers.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- ICO register
- Data Protection Register
- ICO ESD register
tags:
- companysites
- Company Related Sites
- uk
- data-protection
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ICO Data Protection Register (ico.org.uk)

> The UK regulator's public register of organisations (and sole traders) that pay the data-protection fee — search a name to get the registered entity, address, and registration number.

## When to use
You have a UK organisation or trader `name` (or `employer-org`) and want to confirm it's a registered data controller and pull its official registration details. Because sole traders and small businesses register too, this can tie a *person* to a trading name and a registered address — useful when someone operates under a business, and a corroborating address/registration for the entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ICO register search (ico.org.uk/ESDWebPages/Search).
2. Enter the organisation/trading `name` (or registration number if known).
3. Open the matching entry: registered name, registered `address`, registration number, registration/renewal dates, and (for some) the public contact/DPO.
4. Pivot: the registered address feeds property/company checks; the trading name feeds Companies House; a person's trading name confirms a business link.

## Inputs → Outputs
- **In:** organisation/trader `name` (or `employer-org`), or ICO registration number
- **Out:** registered `name`, registered `address`, registration `document-id`/number, dates, sometimes a public contact
- **Empty/negative result looks like:** no match — the entity isn't registered (many small/exempt operations aren't required to), or the name differs from how it registered. Absence doesn't imply the business doesn't exist.

## Gotchas & OpSec
- It's a data-protection fee register, not a general company register — not every business appears; cross-check Companies House.
- Sole-trader entries can expose a home address; treat personal data with care.
- OpSec: passive public-register lookup; no notification.

## Overlaps ("do both")
- Pairs with Companies House (UK company officers/filings) and property registers — the ICO entry confirms a trading identity and address, Companies House gives directors/ownership, and property records tie the address to people.

## Trust & verifiability
`trust: trusted` — first-party ICO data; authoritative for who is registered as a UK data controller. It reflects what the registrant filed, so verify the underlying entity via Companies House where identity matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ico-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
