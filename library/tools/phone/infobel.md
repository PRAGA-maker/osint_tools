---
id: infobel
name: Infobel
description: Use when you have a `name` or `phone` and want an international white/yellow-pages listing — returns phone, address, and name across many countries.
url: https://www.infobel.com/
category: phone
path:
- phone
bestFor: International phone-directory lookup (name→number/address and reverse) across many countries.
selectorsIn:
- name
- phone
- address
selectorsOut:
- phone
- address
- name
status: live
pricing: free
costNote: Free directory search; Infobel also sells business data (Infobel Pro), but the consumer/business directory search is free.
opsec: passive
opsecNote: Reads published directory listings; the subject is not notified. It only holds people/businesses that appear in public phone directories, which skews to landlines and businesses.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running international directory aggregator (Kapitol/Infobel, Belgium); coverage and freshness vary widely by country, and mobile numbers are largely absent.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truecaller
- whitepages
- thats-them
aliases:
- infobel.com
tags:
- phone-number-research
- directory
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Infobel

> An international white/yellow-pages aggregator — one of the few directory tools that spans dozens of countries, useful for name↔phone↔address lookups outside the US.

## When to use
You have a `name` (with a country) or a landline `phone` for a subject and want a published directory listing: a number and address for a name, or a name/address for a number. Its strength is international breadth — when a subject is in a country your usual US-centric people-search tools don't cover, Infobel often has a directory for it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infobel.com/ and select the country.
2. Search white pages by person name, or do a reverse lookup by phone number; business (yellow pages) search is also available.
3. Read the listing: name, address, and phone as published in that country's directory.
4. Pivot: an address feeds property/people-search for that country; a confirmed number feeds caller-ID/messaging-app checks.

## Inputs → Outputs
- **In:** `name` (+ country) or `phone` / `address`
- **Out:** `phone`, `address`, `name` (directory listing)
- **Empty/negative result looks like:** no listing — very common for mobile-only subjects and ex-directory numbers, since it indexes published landline/business directories. Absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; published data, no alert.
- Coverage bias: landlines and businesses dominate; mobile numbers and unlisted subjects are usually missing, and freshness varies a lot by country.

## Overlaps ("do both")
- Pairs with `[[truecaller]]` — covers mobile numbers that directories omit, complementing Infobel's landline focus.
- Pairs with `[[thats-them]]` and `[[whitepages]]` — stronger US coverage; use Infobel for the non-US countries they miss.

## Trust & verifiability
`trust: community` — a legitimate long-standing aggregator, but coverage and currency vary by country and it misses mobiles; corroborate any hit with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infobel |
| category | phone |
| selectorsIn → selectorsOut | name, phone, address → phone, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
