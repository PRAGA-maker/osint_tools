---
id: searchable-fcc-id-database
name: Searchable FCC ID Database
description: Use when you have an FCC ID from a wireless device (`device-id`) and want to identify it — returns manufacturer, model, internal photos, manuals, and test reports.
url: https://www.fcc.gov/oet/ea/fccid
category: public-records
path:
- public-records
bestFor: Identifying a radio-emitting device (phone, router, tracker, drone, IoT gadget) from the FCC ID printed on it.
selectorsIn:
- device-id
selectorsOut:
- device-id
- employer-org
- metadata-exif
status: live
pricing: free
costNote: Free official US FCC database; no account or payment.
opsec: passive
opsecNote: Public federal certification lookup; you query a device ID, not a person, and no one is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Federal Communications Commission equipment-authorization database; authoritative first-party certification records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fcc-license-search
aliases:
- FCC ID lookup
- FCC OET equipment authorization
tags:
- device-identification
- fcc
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Searchable FCC ID Database

> The FCC's equipment-authorization database — decode the FCC ID stamped on any wireless device into its maker, model, and even internal photos.

## When to use
You've recovered or photographed a device — a phone, router, GPS tracker, drone, bodycam, IoT sensor — and it carries an "FCC ID" label (required on anything that emits radio in the US). Looking it up identifies the exact manufacturer and model, and the certification filing often includes internal/external photos, user manuals, and RF test reports. Useful for identifying an unknown device found at a scene, confirming what a listed model actually is, or spotting a hidden tracker/camera.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the FCC ID off the device label (format: a grantee code + product code, e.g. `BCG-E1234`).
2. Go to https://www.fcc.gov/oet/ea/fccid and enter the Grantee Code (first 3–5 chars) and Product Code separately.
3. Open the matching grant to see applicant (manufacturer), equipment class, frequencies, and the exhibit documents.
4. Download the exhibits: internal photos, external photos, user manual, test setup photos — these reveal what the device is and how it works.
5. Pivot: manufacturer name → corporate records; a device model → understanding its tracking/recording capability; third-party mirrors like fccid.io present the same records with easier browsing.

## Inputs → Outputs
- **In:** an FCC ID (`device-id`) from a device label
- **Out:** manufacturer (`employer-org`), model, frequencies, and exhibit documents/photos (`metadata-exif`, `device-id`)
- **Empty/negative result looks like:** no grant found — the ID was misread (check O vs 0, I vs 1), the device is grey-market/uncertified, or it's certified under a different scheme (e.g. non-US). Re-read the label carefully.

## Gotchas & OpSec
- US-scope: only devices certified for the US market appear. Foreign-only devices won't be here (check CE/other regulators).
- FCC IDs are easy to mis-transcribe; the grantee/product split matters — enter them in the right fields.
- Some newer filings have confidentiality requests that redact internal photos/schematics.

## Overlaps ("do both")
- Pairs with `[[fcc-license-search]]` — that covers licensed *operators/callsigns* (people/orgs holding radio licenses); this covers *equipment* certification. Different questions, complementary.

## Trust & verifiability
`trust: trusted` — first-party US FCC data. Certification records are authoritative; the exhibit photos and manuals are the manufacturer's own submissions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchable-fcc-id-database |
| category | public-records |
| selectorsIn → selectorsOut | device-id → device-id, employer-org, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
