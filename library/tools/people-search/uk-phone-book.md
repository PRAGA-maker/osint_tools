---
id: uk-phone-book
name: UK Phone Book
description: Use when you have a `name` (+ UK area) or a landline `phone` and want a directory listing — returns address and phone, with reverse lookups behind a small paywall.
url: https://www.ukphonebook.com/
category: people-search
path:
- people-search
bestFor: UK landline directory lookup — name→address/number and reverse number→name/address.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- address
- phone
status: live
pricing: freemium
costNote: Basic name/area searches return teaser results free; full address details and reverse-number lookups are pay-per-view or subscription (credits).
opsec: passive
opsecNote: Reads published UK directory and electoral-derived data; the subject is not notified. You disclose the searched name/number to the site.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running UK directory service (part of the 192.com/UKChanged data ecosystem); covers listed landlines and electoral-roll–derived entries, so mobile-only and opted-out people are missing.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- 192-com
- infobel
aliases:
- ukphonebook.com
tags:
- people-investigations
- uk-directory
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# UK Phone Book

> A UK directory-lookup service — resolves a name (with area) to an address/landline and does reverse number lookups, drawing on published phone directories and electoral-roll data.

## When to use
You have a UK subject's `name` (ideally with a town/postcode area) or a landline `phone` number and want a current or historical address and number. Its reverse-number lookup is the standout: turn an unknown UK landline into a name and address. Best for older/settled subjects with listed landlines; weak for mobile-only people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ukphonebook.com/.
2. Search the person's name and narrow by town/postcode; or enter a landline number for a reverse lookup.
3. Read the free teaser (name, partial area); full address/number details and reverse results require buying credits.
4. Cross-check the area against what you already know before paying to reveal.
5. Pivot: an address feeds UK electoral-roll/property tools; a confirmed number feeds caller-ID checks.

## Inputs → Outputs
- **In:** `name` (+area), `phone` (landline), or `address`
- **Out:** `name`, `address`, `phone`
- **Empty/negative result looks like:** no listing — very common for mobile-only, ex-directory, or opted-out subjects. Absence is weak evidence in the UK, where landline listing has declined.

## Gotchas & OpSec
- Human-in-the-loop: full details/reverse lookups are pay-per-view.
- OpSec: **passive**; subject not notified.
- Coverage bias: listed landlines and electoral-derived entries only; mobiles and opt-outs are missing, and data can be years old.

## Overlaps ("do both")
- Pairs with `[[192-com]]` — sibling UK directory/electoral-roll service with overlapping but not identical coverage; run both.
- Pairs with `[[infobel]]` — broader international directory to catch UK entries and extend beyond the UK.

## Trust & verifiability
`trust: community` — an established UK directory built on published/electoral data; reliable for listed landlines but incomplete for mobiles and opt-outs, so treat a no-match as inconclusive and corroborate hits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-phone-book |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → name, address, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
