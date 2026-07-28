---
id: many-passwords
name: Many Passwords
description: Use when you have a `device-id` (router/IoT make & model) and want the manufacturer's factory default login — returns candidate `password` values.
url: https://many-passwords.github.io/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Looking up factory default usernames/passwords for a router, camera, or IoT device by manufacturer and model.
selectorsIn:
- device-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source (MIT); browse online or download the full dataset as CSV/JSON, no account needed.
opsec: passive
opsecNote: Browsing or downloading the credential list is pure passive OSINT — nothing touches the subject or their device. Actually trying a credential against a live device is intrusion and out of scope for research; treat this only as reference data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained GitHub project aggregating vendor default-credential lists; always confirm against the device's own manual, since defaults vary by firmware revision.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- many-passwords.github.io
tags:
- Passwords
- default-credentials
- iot
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Many Passwords

> A searchable, downloadable index of factory-default credentials for thousands of IoT/network devices — useful context, not an attack tool.

## When to use
You have a `device-id` — a make and model surfaced from a Shodan/Censys banner, an EXIF/router fingerprint, a photo of a label, or a network scan in an authorized engagement — and want to know the vendor's out-of-the-box username/password. Knowing whether a device likely still runs default credentials informs exposure assessment and helps corroborate what hardware a subject or location uses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://many-passwords.github.io/.
2. Search by manufacturer (e.g. `Hikvision`, `TP-Link`, `MySQL`) or model in the on-page search box.
3. Read the returned rows: vendor, model/product, default username, default password, and notes.
4. For bulk work, use **Download CSV** / **Download JSON** to pull the whole dataset locally, or clone the `many-passwords/many-passwords` repo and query the JSON.
5. Pivot: pair a positive default-credential match with a device-exposure lookup ([[shodan]]-style) to gauge whether an internet-facing device is likely still on factory settings — for assessment only.

## Inputs → Outputs
- **In:** `device-id` (manufacturer + model, or product name)
- **Out:** candidate default `password` (and username) strings
- **Empty/negative result looks like:** "No results found" — the vendor/model isn't in the dataset; check the device manual or the vendor's own docs instead.

## Gotchas & OpSec
- These are **defaults**, not confirmed live credentials — many devices are configured off default. Never treat a listing as "this device's password."
- Using a credential against a device you don't own/aren't authorized to test is unauthorized access — this file is reference data only.
- OpSec: passive; browsing/downloading the list reveals nothing to any subject.

## Overlaps ("do both")
- Pair with device-discovery tools (Shodan/Censys) — those tell you a device is exposed; Many Passwords tells you the factory login it may still use.

## Trust & verifiability
`trust: community` — an open-source, community-curated aggregation of vendor defaults; accurate in aggregate but firmware-dependent, so verify against the manufacturer's documentation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | many-passwords |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | device-id → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
