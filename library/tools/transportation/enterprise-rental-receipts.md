---
id: enterprise-rental-receipts
name: Enterprise Rental Receipts
description: Use when you (or lawful process) have access to an Enterprise Plus account and need that account's own rental receipts — returns the renter's `name`, `address`, dates and vehicle; NOT a third-party lookup.
url: https://www.enterprise.com/en/reserve/receipts.html
category: transportation
path:
- transportation
bestFor: Retrieving an Enterprise Plus account holder's own past rental receipts (name, billing address, dates, vehicle) — only usable with that account's login.
selectorsIn:
- name
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free to use, but only for the logged-in Enterprise Plus account holder's own rentals; no fee and no public/anonymous lookup.
opsec: active
opsecNote: This requires signing into an Enterprise Plus account. Do NOT log into anyone else's account. It is only appropriate for your own rentals or where you have lawful authority (e.g. subpoena/consent). Accessing another person's account without authorisation is illegal.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Enterprise receipt-retrieval page; the data is first-party and authoritative, but it is scoped strictly to the account holder's own rentals — it is not an OSINT lookup against arbitrary vehicles or people.
missingPersonsRelevance: low
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Enterprise get a receipt
tags:
- vehicle
- rental
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Enterprise Rental Receipts

> Enterprise's official "get a receipt" page — first-party rental receipts, but only for the logged-in account holder's own rentals. It is **not** a way to look up a stranger's vehicle or identity by plate/VIN.

## When to use
Narrow and conditional: you have lawful access to an Enterprise Plus account (your own, or the subject's via consent/legal process) and need that account's rental history — dates, billing `name`/`address`, and vehicle details. Common OSINT expectations here are wrong: you cannot enter a `vehicle-plate` or `vin` and get an owner back. Treat the MetaOSINT "vehicle lookup" framing as a mislabel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.enterprise.com/en/reserve/receipts.html and sign into the Enterprise Plus account you are authorised to use.
2. Under Reservations → "Get a Receipt", view receipts for rentals made on that account (available ~48 hours after return, for 360 days).
3. Read the receipt for renter `name`, billing `address`, rental/return dates, location, and vehicle.
4. Only proceed if you own the account or have lawful authority; otherwise stop.
5. Pivot: confirmed rental dates/locations feed a timeline; the vehicle details feed other vehicle records.

## Inputs → Outputs
- **In:** an authorised Enterprise Plus account login (the `name` on the account)
- **Out:** that account's rental receipts — `name`, billing `address`, `document-id` (receipt/agreement), dates, vehicle
- **Empty/negative result looks like:** no receipts (no qualifying rentals, or outside the 48h–360-day window). There is no anonymous/third-party query path at all.

## Gotchas & OpSec
- **Not a public lookup:** no plate/VIN → owner capability; requires the account holder's credentials.
- Legal: accessing another person's account without authorisation is unlawful — use only your own account or proper legal process.
- Data window: available 48 hours after return, retained ~360 days.

## Overlaps ("do both")
- Pairs with lawful records requests and DMV/insurance channels — for a *third party's* vehicle history you need those authorised routes, not this self-service receipt page.

## Trust & verifiability
`trust: trusted` — first-party, authoritative data from Enterprise, but access-gated to the account holder; its investigative value is limited to situations where you already have legitimate account access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | enterprise-rental-receipts |
| category | transportation |
| selectorsIn → selectorsOut | name → name, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
