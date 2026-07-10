---
id: peoplesmart-us
name: PeopleSmart
description: Use when you have a `name`, `email`, `phone`, or LinkedIn (`social-profile`) and want a business/contact-data lookup — returns name, email, phone, employer-org, and address.
url: https://www.peoplesmart.com
category: people-search
path:
- people-search
bestFor: Reverse contact lookup (email/phone/LinkedIn → person) via a B2B contact database.
selectorsIn:
- name
- email
- phone
- social-profile
selectorsOut:
- name
- email
- phone
- employer-org
- address
status: live
pricing: freemium
costNote: Positioned as a B2B lead/contact database; searching may show teasers but revealing full contact details requires a paid plan/credits.
opsec: passive
opsecNote: A commercial contact-data broker; the subject is not notified. You disclose the searched selector and your account/payment to the vendor. The vendor states data may not be fully accurate and that it is not a consumer reporting agency (no FCRA uses).
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Rebuilt as a B2B lead-generation service (distinct from the consumer PeopleSmart that closed in 2016); marketing/aggregated data with a self-declared accuracy disclaimer.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- rocketreach
- beenverified-com
aliases:
- peoplesmart.com
- PeopleSmart US
tags:
- people-search
- b2b-contact-data
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# PeopleSmart

> A B2B contact-data service (the rebuilt PeopleSmart) that reverse-resolves an email, phone, or LinkedIn profile into a person's name, work contact details, and employer.

## When to use
You have an `email`, `phone`, or LinkedIn (`social-profile`) and want to attach a name, employer, and additional contact points — or you have a name and want their professional contact data. Its reverse lookups (email→person, phone→person) are the useful angle when other people-search tools only go name-first. Skews to working professionals and business contacts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peoplesmart.com and choose a search: by name, or reverse by email/phone/LinkedIn URL.
2. Read the teaser (name, employer, partial contact); full details require a paid plan/credits.
3. Filter by job title/industry/location to disambiguate common names.
4. Treat results as leads — the vendor itself disclaims full accuracy.
5. Pivot: an employer feeds LinkedIn/company OSINT; a revealed email/phone feeds contact-OSINT and messaging-app checks.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, or `social-profile` (LinkedIn)
- **Out:** `name`, `email`, `phone`, `employer-org`, `address`
- **Empty/negative result looks like:** no match — common for non-professionals, privacy opt-outs, or people outside its B2B-skewed corpus. Absence is weak evidence; use consumer people-search instead.

## Gotchas & OpSec
- Human-in-the-loop: full contact reveal is behind a paid plan/credits.
- OpSec: **passive** toward the subject; you disclose selectors + account to the broker.
- Not the old PeopleSmart: this is a rebuilt B2B service; don't expect the 2016-era consumer report format. No FCRA-permissible uses.

## Overlaps ("do both")
- Pairs with `[[rocketreach]]` — comparable B2B contact-enrichment source; cross-check since corpora differ.
- Pairs with `[[beenverified-com]]` — consumer broker for the non-professional / residential data PeopleSmart lacks.

## Trust & verifiability
`trust: unverified` — a commercial B2B data broker with a self-declared accuracy disclaimer; useful for professional-contact leads but every field needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peoplesmart-us |
| category | people-search |
| selectorsIn → selectorsOut | name, email, phone, social-profile → name, email, phone, employer-org, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
