---
id: mot-history
name: MOT History
description: Use when you have a UK `vehicle-plate` and want the vehicle's official test history — returns make/model/colour, the mileage recorded at every MOT, and pass/fail/advisory records back to 2005.
url: https://www.check-mot.service.gov.uk
category: transportation
path:
- transportation
bestFor: Confirming a UK registration maps to a specific vehicle and tracing its recorded mileage and defect timeline over the years.
selectorsIn:
- vehicle-plate
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free official DVSA service; no account, no payment, registration number only.
opsec: passive
opsecNote: This is a public government lookup keyed only on the plate — the vehicle's owner is never notified and cannot see who searched. DVSA logs the request against your IP; use a clean/sock-puppet session for a fully arm's-length query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the DVSA (UK Driver & Vehicle Standards Agency); the MOT records are first-party government data, authoritative for any vehicle tested in England, Scotland or Wales.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- free-car-license-plate-lookup
- vincheck-info
- vin-check-reports
aliases:
- check-mot.service.gov.uk
- DVSA MOT history check
- Check MOT history
tags:
- vehicle
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# MOT History

> The DVSA's free MOT history lookup — turn a UK number plate into the vehicle's make/model/colour and a year-by-year record of mileage, MOT passes/fails and advisories.

## When to use
You have a UK `vehicle-plate` tied to a subject (from a photo, a witness, a classified ad, or another record) and want to confirm exactly which vehicle it is and reconstruct its history. The recorded odometer readings at each annual test let you spot whether a car has been driven (and roughly how much) year to year — a useful liveness/activity signal — and advisories/failures describe the vehicle's condition. Note: this service does **not** return the owner's name or address; it is anonymous with respect to the keeper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.check-mot.service.gov.uk in a clean browser session.
2. Enter the vehicle registration (`vehicle-plate`) and submit.
3. Read the results:
   - **Vehicle summary** — make, model, colour, year of manufacture, fuel type, engine size.
   - **MOT test history** — each test's date, result (pass/fail), the **mileage recorded**, and any advisory or failure notes, going back to 2005.
   - **MOT expiry / tax status** at the top.
4. Pivot: compare successive mileage readings to gauge annual usage or spot odometer anomalies; use make/model/colour to corroborate a sighting or photo; cross-check the plate against classifieds and vehicle-history services.

## Inputs → Outputs
- **In:** `vehicle-plate` (UK registration)
- **Out:** `physical-description` of the vehicle (make/model/colour/year), recorded mileage timeline, MOT pass-fail-advisory history
- **Empty/negative result looks like:** "No details held by DVSA" / no MOT history — the vehicle is under three years old (no MOT due yet), untested, exempt (e.g. very old), or the plate is wrong. Not proof the vehicle doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none — no captcha, no login.
- OpSec: **passive** — nothing is sent to the vehicle's owner; only DVSA logs the query. The lookup reveals nothing about the person searching to the subject.
- Owner identity is **not** exposed here. To go from plate to keeper you need a separate, access-controlled DVLA route (lawful basis required) — do not expect names/addresses from this tool.
- Mileage is self-reported by the testing garage and can contain clerical errors; a sudden drop may be a typo rather than clocking, so corroborate.

## Overlaps ("do both")
- Pairs with `[[vin-check-reports]]` and `[[vincheck-info]]` — those are US/VIN-oriented, while MOT History is the authoritative UK plate source; use whichever matches the vehicle's country.
- Combine with `[[free-car-license-plate-lookup]]` for additional plate-decoding coverage.

## Trust & verifiability
`trust: trusted` — it is the DVSA's own service, so the MOT records are the definitive government dataset; the only caveat is garage-entered mileage typos.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mot-history |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
