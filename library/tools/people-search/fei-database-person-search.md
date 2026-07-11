---
id: fei-database-person-search
name: FEI Database Person Search
description: Use when you have a `name` linked to equestrian sport and want to confirm their role and nationality in the international federation — returns FEI ID, discipline, and national federation.
url: https://data.fei.org/Person/Search.aspx
category: people-search
path:
- people-search
bestFor: Confirming a person's registration in international equestrian sport (rider, owner, groom, official) and their nationality/FEI ID.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public search of the FEI database; no account required.
opsec: passive
opsecNote: A public sports-governing-body database; searching does not notify the person and exposes only the sporting record they registered under the FEI. No sock puppet needed; treat it as a niche corroboration source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official database of the Fédération Équestre Internationale (FEI), the world governing body for equestrian sport; authoritative for FEI registration, discipline, and nationality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- FEI Database
- Fédération Équestre Internationale
tags:
- Universal Contact Search and Leaks Search
- equestrian
- sport
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# FEI Database Person Search

> The official database of the international equestrian federation — a niche but authoritative check to confirm that a subject connected to horse sport is a registered FEI athlete, owner, groom, or official, and to pull their nationality and FEI ID.

## When to use
Your subject is tied (by claim or lead) to equestrian sport — a rider, horse owner, groom, trainer, or official — and you want to confirm it and anchor identity. An FEI record corroborates the person, gives a stable FEI ID (`document-id`), their discipline(s), and their national federation (`employer-org`), and links to competition results that place them at specific events and dates. Reach for it when the equestrian angle is plausible; it's a strong corroborator in an otherwise thin profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.fei.org/Person/Search.aspx.
2. Search the subject's `name` (try surname first; add nationality if known to narrow).
3. Open the matching person record: FEI ID, registered role, discipline(s), and national federation.
4. Follow linked results/horses to place the person at competitions (dates/locations) and associated owners/riders.
5. Pivot: national federation and results → `associate`s and event `geolocation`; FEI ID → a durable identifier to cross-reference other equestrian records.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, `employer-org` (national federation / role), `document-id` (FEI ID), plus discipline and competition history
- **Empty/negative result looks like:** no match — the subject isn't FEI-registered (recreational riders and non-international competitors won't appear), or is registered under a variant/native-script name. Absence doesn't rule out horse involvement; try name variants and national-federation databases.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Scope is **international-level FEI registration** — grassroots/national-only participants are absent. It confirms sporting identity, not home address or contact details.
- OpSec: passive; the person is not notified.

## Overlaps ("do both")
- Pairs with national equestrian federation databases and general people-search — FEI confirms the international sporting identity; national bodies and people-search add contact/location the FEI record won't.

## Trust & verifiability
`trust: trusted` — the sport's official world governing body database; authoritative for FEI registration, ID, discipline, and results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fei-database-person-search |
| category | people-search |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
