---
id: ipo-gov-uk
name: ipo.gov.uk
description: Use when you have a `name`/`employer-org` and want the UK trademarks they own — the UK Intellectual Property Office owner search returns the owner's name, address and their registered/applied trademarks.
url: https://trademarks.ipo.gov.uk/ipo-tmowner
category: public-records
path:
- public-records
bestFor: Finding UK trademarks by owner name to link a person/business to brands and a service address.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free official government search; no account or payment.
opsec: passive
opsecNote: Searching the public trademark register is a passive, anonymous lookup against government records — no notification to the owner. A normal browser session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The UK Intellectual Property Office's own register — an authoritative, first-party government source of trademark ownership.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- UK IPO trademark search
- Intellectual Property Office
- search by owner
tags:
- companysites
- Company Related Sites
- trademark
- uk
- ip
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# ipo.gov.uk

> The UK Intellectual Property Office's trademark **owner** search — put in a person or company name and get the trademarks they hold, plus the name and address recorded against them.

## When to use
You have a `name` or `employer-org` and want to tie them to brands, products, or a business identity. Trademark filings expose the owner's legal name and a correspondence/service `address` (often a home or agent address), and reveal the brands a subject controls — useful for confirming a business, finding an address, or mapping someone's commercial activity in the UK.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trademarks.ipo.gov.uk/ipo-tmowner (the "search by owner" facility).
2. Enter the owner's name or company; submit.
3. Read the results: matched owner(s), the address recorded on the mark, and each trademark (word/logo, status, class, dates).
4. Pivot: the owner address feeds people/property lookups; the company feeds Companies House; a brand name feeds web/social searches. For marks by text rather than owner, use the IPO's trademark-text search instead.

## Inputs → Outputs
- **In:** `name` / `employer-org` (optionally an `address` to disambiguate)
- **Out:** owner `name`, service/correspondence `address`, owned `employer-org`/brands (trademarks)
- **Empty/negative result looks like:** no marks for that owner — meaning they hold no UK trademark (most individuals don't), not that they don't exist. Try name spelling variants and the associated company name.

## Gotchas & OpSec
- Addresses are often the agent/representative's, not the owner's home — verify before treating as a residence.
- Only covers UK/EU-registered-via-UK marks; for EU/international marks use EUIPO/WIPO searches.
- Owner-name matching is literal — try variants (initials, "Ltd" vs full name).
- OpSec: passive government lookup.

## Overlaps ("do both")
- Pairs with Companies House and EUIPO/WIPO trademark databases — Companies House ties the owner to filings and officers; EUIPO/WIPO extend coverage beyond the UK register.

## Trust & verifiability
`trust: trusted` — an authoritative first-party government register. Ownership and marks are reliable; treat the recorded address as "as-filed" and confirm it independently before assuming it's the person's home.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipo-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
