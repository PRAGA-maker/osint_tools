---
id: thisnumber-com-2
name: thisnumber.com
description: Use when you have a `phone` number (from 200+ countries) and want to identify it — returns country, carrier and line type for any number, plus owner `name`/`address` for US numbers.
url: https://www.thisnumber.com/
category: phone
path:
- phone
bestFor: Free international reverse-phone lookup — country/carrier/line-type worldwide, plus US owner name/address.
selectorsIn:
- phone
selectorsOut:
- name
- address
- social-profile
status: live
pricing: free
costNote: Free; no account required, works for numbers from 200+ countries.
opsec: passive
opsecNote: Read-only lookup against public/carrier reference data; the number's owner is not notified. Not FCRA-compliant — do not use for employment/tenant screening. Use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free reverse-phone aggregator; carrier/country/line-type data is generally reliable, but US "owner name/address" is drawn from public records that can be stale or wrong.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- who-called-me
- open-cnam
- thisnumber-com
aliases:
- ThisNumber
- thisnumber reverse phone
tags:
- mobilephone
- Mobile & Phone Related
- reverse-phone
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# thisnumber.com

> A free, broad international reverse-phone lookup — identify the country, carrier, and line type of almost any number, with owner name/address for US numbers.

## When to use
You have a `phone` number and need to characterise it: which country and carrier it belongs to, whether it's a mobile, landline, VoIP, toll-free, or premium-rate line, and — for US numbers — the owner's `name` and `address` plus any scam/robocall history. Its strength is breadth: it handles numbers from 200+ countries, making it a good first stop when a number's origin is unknown.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thisnumber.com/.
2. Enter the `phone` number in international format (or use the country selector).
3. Read the result:
   - **Any country:** country of origin, carrier, line type, validity.
   - **US numbers:** additionally owner `name`, `address` (from public records), and FTC spam/robocall complaints.
4. Treat US owner data as a lead to corroborate; treat line-type/carrier as reliable.
5. Pivot: a carrier/line-type informs which messaging/app-checks to run; a US name/address feeds people-search; the number feeds `[[who-called-me]]` and `[[open-cnam]]`.

## Inputs → Outputs
- **In:** `phone` (200+ countries)
- **Out:** country, carrier, line type; for US: owner `name`, `address`, scam reports; possible linked `social-profile`
- **Empty/negative result looks like:** only generic country/carrier metadata with no owner (normal for non-US numbers), or "invalid number" — meaning the number is malformed or unassigned. Absence of an owner is expected outside the US.

## Gotchas & OpSec
- Owner name/address is **US-only** and public-records-derived — often stale; verify before relying on it.
- Not FCRA-compliant: do not use for employment/tenant/credit decisions.
- Line-type/carrier is generally trustworthy; owner identity is not.
- OpSec: **passive** — the owner is not alerted.

## Overlaps ("do both")
- Pairs with `[[who-called-me]]` (crowd-sourced caller reports) and `[[open-cnam]]` (caller-ID name) — this gives global carrier/line-type and US owner data; the others add reputation and CNAM detail.

## Trust & verifiability
`trust: unverified` — dependable for carrier/country/line-type, but US owner data comes from public records of variable freshness; corroborate any identity before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thisnumber-com-2 |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
