---
id: gov-uk-9
name: GOV.UK — View or Share Driving Licence
description: Use when you (lawfully) hold a subject's driving-licence number plus their NI number and postcode, or they give you a share code — the DVLA self-service returns licence status, entitlements, and penalty points. Not a third-party lookup.
url: https://www.gov.uk/view-driving-licence
category: public-records
path:
- public-records
bestFor: Verifying a UK driving licence's validity, categories, and penalty points via DVLA's self/share service.
selectorsIn:
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free official DVLA service; no account, but strict identity inputs required.
opsec: passive
opsecNote: The service requires the licence holder's own three identifiers (driving-licence number, National Insurance number, postcode) or a time-limited "share code" they generate. You cannot query an arbitrary person — attempting to use someone's identifiers without authority is unlawful. Treat this as a verification-with-consent tool, not reconnaissance.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK DVLA service; authoritative for licence data, but gated behind the holder's personal identifiers or an explicitly shared code.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- View Driving Licence
- DVLA share driving licence
- check driving licence
tags:
- professionlicensing
- Profession & Licensing Sites
- dvla
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# GOV.UK — View or Share Driving Licence

> DVLA's official "view your driving licence" service — powerful for verification, but it only works with the holder's own identifiers or a share code, so it is a consent-based check, not a way to look up a stranger.

## When to use
You need to verify a UK driving licence — its validity, vehicle categories/entitlements, and current penalty points/disqualifications — in a scenario where you legitimately have access: the licence holder provides their details or generates a "share code" (common for employers, car hire, and vetting). It is genuinely useful for confirming identity/entitlement with cooperation. It is NOT a reconnaissance tool: you cannot enter just a name and get someone's record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gov.uk/view-driving-licence.
2. Either: enter the holder's **driving-licence number + National Insurance number + postcode** (their own, provided with authority), or use a **share code** they generated (via the "share your driving licence" service).
3. Read the returned details: licence status, categories held, endorsements/penalty points, disqualifications.
4. Use only with lawful authority/consent — misusing another person's identifiers is an offence.
5. Pivot: confirmed entitlements/points corroborate identity and driving history for vetting or an investigation with proper basis.

## Inputs → Outputs
- **In:** `document-id` (driving-licence number) **plus** NI number and postcode, or a share code
- **Out:** licence validity, vehicle categories, penalty points/endorsements, disqualifications
- **Empty/negative result looks like:** you cannot proceed without all three identifiers or a code — by design; there is no name-only search.

## Gotchas & OpSec
- Legal gate: requires the holder's personal identifiers or an issued share code — not usable for covert lookups.
- Share codes are time-limited and single-purpose; get a fresh one from the holder.
- This shows licence/driving data only — not addresses or general PII.

## Overlaps ("do both")
- Complements consent-based vetting (right-to-work/DBS) and, for enforcement with legal basis, DVLA data-request routes — this is the self/share verification surface.

## Trust & verifiability
`trust: trusted` — an authoritative DVLA service; the data is definitive, but access is legitimately restricted to the holder or their nominee, so use it only within that boundary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-9 |
| category | public-records |
| selectorsIn → selectorsOut | document-id →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
