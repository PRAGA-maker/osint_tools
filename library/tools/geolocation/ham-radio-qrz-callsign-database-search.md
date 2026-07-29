---
id: ham-radio-qrz-callsign-database-search
name: Ham Radio QRZ Callsign Database Search
description: Use when you have an amateur-radio callsign (a `document-id`) or a licensee `name` and want the operator's identity and registered location — returns `name`, `address`, and grid-square `geolocation`.
url: https://www.qrz.com/lookup
category: geolocation
path:
- geolocation
bestFor: Resolving a ham-radio callsign to the licensed operator's name and registered address/location.
selectorsIn:
- document-id
- name
selectorsOut:
- name
- address
- geolocation
status: live
pricing: freemium
costNote: Basic callsign lookups are free; advanced/bulk search and some detail fields require a (free or paid) logged-in QRZ account.
opsec: passive
opsecNote: You query QRZ's database, not the operator — the subject is not contacted. Note that logged-in lookups are tied to your QRZ account; use a research account, not a personal one, if attribution matters.
humanInLoop: false
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: QRZ mirrors official government amateur-radio license registries (e.g. the US FCC ULS), which are public record; identity data is authoritative for licensed operators.
missingPersonsRelevance: low
coverage:
- global
- us
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- QRZ
- QRZ callsign lookup
tags:
- amateur-radio
- callsign
- public-records
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Ham Radio QRZ Callsign Database Search

> The amateur-radio identity oracle: a callsign resolves to a licensed operator's real name and government-registered address — public record for licensed hams.

## When to use
Your subject is (or is suspected to be) a licensed amateur-radio operator, and you have a callsign — spotted in a bio, a QSL card, a vehicle plate frame, a forum handle, or radio logs — or a name you want to check against the licensee registry. For US and many other operators, the license is public record, so a callsign can hand you a verified `name` and `address`, and a Maidenhead grid square gives an approximate `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.qrz.com/lookup.
2. Search **by Callsign** (wildcards supported) or **by Name/Addr** to find a licensee.
3. Read the callsign page: licensed operator `name`, registered `address`, grid square (→ `geolocation`), license class/date, and any bio the operator wrote.
4. Log in (free account) for advanced/name searches and fuller detail; some fields are gated.
5. Pivot: the registered `address`/`name` feeds people-search and public-records tools; the grid square narrows a search area.

## Inputs → Outputs
- **In:** callsign (`document-id`) or `name`
- **Out:** `name`, registered `address`, grid-square `geolocation`, license class/dates, operator bio
- **Empty/negative result looks like:** "Not found" / no license record — the callsign is unissued, expired and purged, or from a country QRZ doesn't index; not proof the person isn't a ham.

## Gotchas & OpSec
- Login gates name/advanced searches; use a dedicated research account.
- Registered address may be a P.O. box, a club address, or years out of date — treat as a lead, corroborate.
- Coverage/detail is strongest for US (FCC) and other open registries; some countries restrict or omit operator addresses.

## Overlaps ("do both")
- Pairs with people-search and public-records tools — QRZ gives an authoritative name+address anchor from the callsign, which those tools then expand into current contact/associates.

## Trust & verifiability
`trust: trusted` — QRZ reflects official government license registries (US FCC ULS and others), so for licensed operators the name/address is authoritative public record; verify against the source registry when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ham-radio-qrz-callsign-database-search |
| category | geolocation |
| selectorsIn → selectorsOut | document-id, name → name, address, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
