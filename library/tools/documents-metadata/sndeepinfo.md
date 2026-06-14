---
id: sndeepinfo
name: SNDeepInfo
description: Use when you have an IMEI, serial, ICCID, MEID, or Apple part number — decode it into device make/model/specs and (for Apple) warranty/blacklist status to identify a recovered device.
url: https://sndeep.info/en
category: documents-metadata
path:
- documents-metadata
bestFor: Decoding a device IMEI/serial/ICCID/MEID/Apple part number into make, model, specs, and (where available) warranty/blacklist status.
selectorsIn: [device-id, document-id]
selectorsOut: [device-id, metadata-exif]
status: live
pricing: freemium
costNote: Basic IMEI/serial decoding is free; deeper Apple/warranty/blacklist checks may require credits or a paid lookup.
opsec: passive
opsecNote: Submitting a device identifier to a third-party service is passive toward the owner but discloses the identifier to the operator. Use a clean session; avoid submitting case-sensitive identifiers you would not want logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: SNDeepInfo (sndeep.info) is a long-established, widely used IMEI/serial decoder cited across OSINT directories; function reasoned from known product, not re-verified. Apple/blacklist data accuracy varies and some checks are gated.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: [SN DEEP INFO]
tags:
- IMEI and serial numbers
source: cyb-detective
lastVerified: ''
enrichment: full
---

# SNDeepInfo

> Established device-identifier decoder — turns an IMEI, serial, ICCID, MEID, or Apple part number into device make/model/specs and, for Apple, warranty/blacklist signals.

## When to use
You have a recovered phone/device or just its `device-id` (IMEI/serial/ICCID/MEID/Apple part number) and need to identify exactly what it is (make, model, storage, color, region) and whether it is reported lost/blacklisted. In missing-persons work this confirms a found device's identity and can flag whether it was reported lost/stolen, which is a lead toward the owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://sndeep.info/en and select the identifier type (IMEI, serial, ICCID, MEID, Apple part number).
2. Enter the identifier (dial *#06# for IMEI, or read from the SIM tray/settings/box) and submit.
3. Read the decoded make/model/specs and any warranty/blacklist status; some Apple-specific or blacklist checks may require credits.
4. Pivot: confirmed model/region narrows where the device was sold; a "lost/blacklisted" flag routes to carrier/manufacturer lawful-process channels and supports owner identification.

## Inputs → Outputs
- **In:** `device-id` (IMEI / serial / ICCID / MEID / Apple part number), i.e. a device `document-id`
- **Out:** make/model/specs and status as `metadata-exif`-style device attributes; not the owner's identity directly
- **Empty/negative result looks like:** "invalid"/"not found" or a paywall on the deeper check — basic decoding should still resolve a valid IMEI to a model.

## Gotchas & OpSec
- Human-in-the-loop: none for basic decoding; some advanced checks gate behind credits.
- OpSec: passive toward the owner; you reveal the identifier to the operator. Use a clean session.
- Blacklist/warranty data is best-effort and can be stale — corroborate before relying on it legally.

## Overlaps ("do both")
- Pairs with [[checking-mi-account]] (Xiaomi-specific lock check) and other IMEI checkers to cross-validate device identity and status.

## Trust & verifiability
`trust: community` — long-running, well-known decoder with documented function; entry reasons from known behavior rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sndeepinfo |
| category | documents-metadata |
| selectorsIn → selectorsOut | device-id, document-id → device-id, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
