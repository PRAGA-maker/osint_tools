---
id: fcc-io
name: Fcc.io
description: Use when you have an FCC ID off a wireless device (`device-id`) and want the manufacturer and filing behind it — returns the grantee `employer-org` + `address` and product details from the FCC equipment database.
url: http://fcc.io/
category: phone
path:
- phone
bestFor: Fast-linking an FCC ID printed on a device to its official FCC equipment-authorization record.
selectorsIn:
- device-id
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free. It is a thin URL shortcut/redirector to the FCC's own public equipment-authorization search; no account or payment.
opsec: passive
opsecNote: You query a public equipment-registration database about a device/manufacturer, not about a person. Nothing reaches the target. The redirect resolves to the official FCC site — safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: fcc.io itself is a community-built convenience redirector; the data it lands you on is the FCC's authoritative first-party equipment database.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nanpa-area-code-query
aliases:
- fcc.io
- FCC ID lookup
tags:
- fcc-id
- device
- hardware
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Fcc.io

> A one-line shortcut into the FCC's equipment-authorization database: type an FCC ID and land on the manufacturer filing, test reports, and photos the FCC holds for that device.

## When to use
You have an **FCC ID** — the alphanumeric string printed on virtually every wireless device sold in the US (phones, routers, radios, IoT, drones, hidden cameras, key fobs) — as a `device-id` and want to identify the equipment and the company behind it. The linked FCC filing names the **grantee** (`employer-org`) and its `address`, the device model, internal/external photos, frequencies, and user-manual excerpts. Useful for identifying an unknown device from a photo of its label, or attributing hardware found at a scene.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the FCC ID off the device label (format like `NPI71646`; the part before any dash is the grantee code).
2. Go to `https://fcc.io/<FCC-ID>` (e.g. `fcc.io/NPI71646`) — or use fcc.io's search box.
3. It redirects to the FCC equipment-authorization results for that ID.
4. Read the record: grantee company (`employer-org`) and `address`, product name/model, frequency bands, and any attached photos/manuals.
5. Pivot: the grantee company + product tells you what the device is and does; internal photos help confirm a device's identity; combine with a manual search of the device model online.

## Inputs → Outputs
- **In:** `device-id` (an FCC ID string)
- **Out:** grantee `employer-org`, grantee `address`, device model, photos, RF details
- **Empty/negative result looks like:** the FCC search returns no grant for the ID — the string is mistyped, it's a counterfeit/unauthorised device, or the label isn't an FCC ID at all. It doesn't mean the device is untraceable; recheck the characters.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a redirect to a public database.
- OpSec: **passive** — you look up a device registration, never a person; nothing is disclosed to anyone.
- FCC IDs identify the *grantee/manufacturer*, not the end user — the record tells you what the hardware is, not who owns the specific unit.

## Overlaps ("do both")
- Loosely related to `[[nanpa-area-code-query]]` only in the "telecom identifier lookup" sense; functionally fcc.io is about hardware provenance. For unknown-device work, pair it with a plain web search of the recovered model number and the grantee company name.

## Trust & verifiability
`trust: community` — the redirector is a hobbyist convenience, but it deposits you on the FCC's authoritative equipment-authorization records, so the grantee and device data are first-party and reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fcc-io |
| category | phone |
| selectorsIn → selectorsOut | device-id → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
