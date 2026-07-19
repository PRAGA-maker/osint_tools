---
id: askmid
name: askMID
description: Use when you have a UK `vehicle-plate` and want to confirm whether that vehicle is insured on the Motor Insurance Database — returns an insured/not-insured status (no owner PII).
url: https://ownvehicle.askmid.com
category: transportation
path:
- transportation
bestFor: Confirming whether a UK-registered vehicle is currently insured (yes/no status).
selectorsIn:
- vehicle-plate
selectorsOut: []
status: live
pricing: free
costNote: Free public check; run by the Motor Insurers' Bureau (MIB). Now routes through the MIB's "Navigate" portal (askMID redirects there since 2024).
opsec: active
opsecNote: You query the MIB's live database about a specific plate. Access is legally gated — the free check is intended for the registered keeper of the vehicle or a party involved in an accident with it, not for arbitrary third-party lookups. Using it outside those grounds is outside its terms; do not rely on it for covert enumeration.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Motor Insurers' Bureau service — the authoritative source of vehicle insurance status; not a scraper.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ask MID
- Motor Insurance Database check
- Navigate MID check
tags:
- vehicle
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# askMID

> The UK Motor Insurers' Bureau's public front end to the Motor Insurance Database — tells you whether a given registration is currently insured, and nothing more.

## When to use
You have a UK `vehicle-plate` and a legitimate basis to check its insurance status — you're the registered keeper confirming your own cover, or you were involved in an accident with the vehicle. A positive result confirms the vehicle is on-road and insured; it does **not** reveal the owner, insurer, or address (those require the MIB's separate post-accident "share my details" process with an incident reference).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ownvehicle.askmid.com (you'll be routed to the MIB's Navigate portal).
2. Choose the appropriate check — "is my vehicle insured?" (keeper) requires you to confirm you are the registered keeper; the accident-based check requires incident details.
3. Enter the `vehicle-plate` (VRM).
4. Read the result: a simple insured / not-found-as-insured status for that registration.
5. Pivot: an "insured" result corroborates the vehicle is active/on-road; combine with a DVLA vehicle-enquiry check (tax/MOT) for a fuller road-legal picture.

## Inputs → Outputs
- **In:** UK `vehicle-plate` (VRM)
- **Out:** insurance status (insured / not confirmed) — **no** name, address, or insurer
- **Empty/negative result looks like:** "we couldn't confirm this vehicle is insured" — which can mean genuinely uninsured, a data lag (new policies take days to appear on the MID), or that you lacked the gated grounds to run the check.

## Gotchas & OpSec
- Human-in-the-loop: **legal-gate** — the free check is for keepers or accident-involved parties, not open third-party lookups; respect that scope.
- MID data lags real-world cover by a few days, so a "not insured" result is not proof of no insurance.
- OpSec: **active** — you're touching the official MIB database; there's no owner-facing alert, but the query is against a real authority, so use it only on proper grounds.

## Overlaps ("do both")
- Pairs with the DVLA vehicle-enquiry service (tax and MOT status by plate) — askMID answers "insured?", DVLA answers "taxed and MOT'd?"; together they establish whether a UK vehicle is fully road-legal.

## Trust & verifiability
`trust: trusted` — it's the Motor Insurers' Bureau's own authoritative database, so the insurance signal is definitive (subject only to the known few-day update lag).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | askmid |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (legal-gate) |
