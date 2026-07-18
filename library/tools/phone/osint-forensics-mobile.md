---
id: osint-forensics-mobile
name: OSINT-FORENSICS-MOBILE
description: Use when you have a `phone`, `device-id` (IMEI), or a seized Android/iOS device and want a curated index of mobile-OSINT and forensics tools — returns pointers to phone lookups, IMEI decoders, cell-tower maps, and extraction toolkits.
url: https://github.com/CScorza/OSINT-FORENSICS-MOBILE
category: phone
path:
- phone
bestFor: A jumping-off catalogue for mobile-number, IMEI, cell-network, and device-forensics tooling.
selectorsIn:
- phone
- device-id
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, open GitHub repository (MIT-style curated list); individual tools it links may have their own pricing.
opsec: passive
opsecNote: Reading the list itself leaks nothing. OpSec risk lives in the linked tools — many phone-number and IMEI lookups query third parties, and forensic extraction of a device is inherently active — so assess each linked tool on its own before running it against a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by CScorza, an active Italian OSINT/forensics author; the list is curated and reasonably current but is a directory, not a vetted or tested toolchain.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CScorza mobile OSINT list
- OSINT Forensics Mobile
tags:
- mobile
- forensics
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-18'
enrichment: full
---

# OSINT-FORENSICS-MOBILE

> A curated GitHub directory of mobile-focused OSINT and forensics tools — phone-number search, IMEI decoding, cell-tower mapping, messaging-app analysis, and device extraction, all in one index.

## When to use
You have a `phone` number, an IMEI/`device-id`, or physical access to a subject's Android/iOS handset, and you need to know *which* tool does the job. This repo is a menu, not an engine: use it to discover the right specialised resource (a caller-ID service, an IMEI decoder, a cell-tower locator like CellMapper/OpenCelliD, a WhatsApp/Telegram analysis utility, or a forensic extractor such as Andriller/ALEAPP/MVT) and then go run that tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/CScorza/OSINT-FORENSICS-MOBILE and read the README's section index.
2. Jump to the section matching your selector:
   - **Phone number** → phone-directory / caller-ID tools.
   - **IMEI / `device-id`** → IMEI-analysis decoders.
   - **Cell network / `geolocation`** → CellMapper, OpenCelliD, coverage maps.
   - **Messaging** → WhatsApp/Telegram chat-export and group-search tools.
   - **Seized device** → Andriller CE, ALEAPP, Mobile Verification Toolkit + teardown guides.
3. Click through to the individual tool and evaluate it on its own page before use.
4. Pivot: a phone lookup may yield a `social-profile`; cell/IMEI work may yield `geolocation` or device attribution.

## Inputs → Outputs
- **In:** `phone`, `device-id` (IMEI), or a physical device
- **Out:** pointers to tools that turn those into `social-profile`, `geolocation`, or extracted device data
- **Empty/negative result looks like:** a category with only stale/dead links — the list is community-maintained, so a linked tool may have shut down; verify the destination is live before relying on it.

## Gotchas & OpSec
- This is a **catalogue**, not a single lookup — the "output" is other tools, so budget time to evaluate each destination.
- Device forensics (extraction, MVT, Andriller) is legally sensitive and requires lawful access to the handset; do not treat these as remote lookups.
- OpSec: reading the repo is passive; the tools it links range from passive (IMEI decode) to active (contacting a carrier lookup) — judge each individually.

## Overlaps ("do both")
- Pairs with a general OSINT-framework directory: this list is the deep, phone/device-specific slice, so use it when a broad framework's mobile section is too shallow.

## Trust & verifiability
`trust: community` — a single maintainer's curated list. The curation is knowledgeable and the sections are well-organised, but link rot is inevitable in any directory, so treat each entry as a lead to verify, not a guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-forensics-mobile |
