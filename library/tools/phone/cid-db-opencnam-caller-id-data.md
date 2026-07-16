---
id: cid-db-opencnam-caller-id-data
name: OpenCNAM (Caller ID Data)
description: Use when you have a US `phone` number and want the caller-name (CNAM) registered to it — returns the CNAM string (the name that shows on caller ID).
url: https://www.opencnam.com/
category: phone
path:
- phone
bestFor: Looking up the CNAM (caller-ID name) attached to a North American phone number via a simple HTTP API.
selectorsIn:
- phone
selectorsOut:
- name
status: live
pricing: freemium
costNote: A limited "Hobbyist" tier offers free CNAM lookups (rate-limited, less complete); the "Professional" tier with full accuracy and volume requires an account, an Account SID + Auth Token, and payment.
opsec: passive
opsecNote: A CNAM query hits OpenCNAM's database, not the subject's handset, so it is passive and does not ring or alert the target. The service logs the numbers you query; use an API token tied to a research account, not personal identifiers.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: OpenCNAM is an established caller-ID data provider; CNAM reflects the name the line's carrier registered, which is often a household/business name and can be blank or stale — accurate as "the registered caller name," not as verified identity.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- OpenCNAM
- CNAM lookup
tags:
- phone
- caller-id
- cnam
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- open-cnam
---

# OpenCNAM (Caller ID Data)

> A caller-ID (CNAM) lookup API — turn a US/Canada number into the name that carriers show on caller ID, straight from an HTTP request.

## When to use
You have a North American `phone` number and want the registered caller name (CNAM) — the string that appears on a recipient's caller ID. CNAM is often a real household or business name tied to the line, so it's a fast corroboration of who a number belongs to. Reach for it early in phone-OSINT as a lightweight, scriptable check before heavier people-search aggregators.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at opencnam.com to get an Account SID + Auth Token (the free Hobbyist tier works for occasional lookups).
2. Call the API: `GET https://api.opencnam.com/v3/phone/+1XXXXXXXXXX?account_sid=...&auth_token=...` (or the documented v2/v3 endpoint).
3. Read the returned CNAM `name` string.
4. For accuracy/volume, use the paid Professional tier; the free tier is rate-limited and less complete.
5. Pivot: a CNAM name feeds people-search (`[[usphonebook]]`, `[[ufind-name]]`) and email-permutation (`[[mailfoguess]]`); a business CNAM points to an `employer-org`.

## Inputs → Outputs
- **In:** `phone` (US/Canada, E.164 e.g. `+16185551234`)
- **Out:** the CNAM `name` registered to the number
- **Empty/negative result looks like:** an empty/`"UNAVAILABLE"` CNAM — many mobile numbers have no CNAM record, the carrier suppresses it, or the free tier can't resolve it; blank ≠ invalid number.

## Gotchas & OpSec
- CNAM ≠ identity: it's the carrier-registered caller name, which can be a spouse, a business, an old subscriber, or blank — corroborate, never treat as proof.
- Mobile gaps: CNAM coverage is strongest for landlines/business lines and weakest for mobiles.
- API key required for reliable use; the free tier is throttled.
- OpSec: passive — queries hit OpenCNAM, not the target's phone.

## Overlaps ("do both")
- Pairs with `[[usphonebook]]`/`[[ufind-name]]` — CNAM gives the registered name; aggregators add address/relatives around it.
- Pairs with Truecaller-style crowd data — CNAM is carrier-registered, Truecaller is user-reported, so they cross-check each other.

## Trust & verifiability
`trust: community` — an established caller-ID data provider; the CNAM value is authoritative as "the registered caller name" but is frequently blank, stale, or non-personal, so use it as a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cid-db-opencnam-caller-id-data |
