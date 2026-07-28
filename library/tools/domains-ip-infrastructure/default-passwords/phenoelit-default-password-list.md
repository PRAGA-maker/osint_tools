---
id: phenoelit-default-password-list
name: Phenoelit Default Password List
description: Use when you have a device make/model (`device-id`) and want its factory-default credentials — returns the vendor's default username/`password` pairs.
url: https://phenoelit.de/dpl/dpl.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up factory-default login credentials for networking/hardware by vendor and model.
selectorsIn:
- device-id
selectorsOut:
- password
status: degraded
pricing: free
costNote: Free static reference page; no account. Content is frozen (last substantive update ~2008).
opsec: passive
opsecNote: This is a static reference list — reading it contacts nobody but Phenoelit. Actually USING a default credential against a device you don't own is intrusion; only apply on systems you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing, well-known reference maintained by the Phenoelit group. Data is accurate for its era but stale; the .org host is unreliable, the .de mirror is the working copy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Phenoelit DPL
- Default Password List
tags:
- default-passwords
- reference-list
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Phenoelit Default Password List

> The classic Phenoelit reference of factory-default logins by vendor and model — a static lookup table, frozen but still handy for older hardware.

## When to use
You have identified a piece of networking or embedded hardware by vendor/model (`device-id`) — a router, switch, PBX, camera — and want its shipped default username/`password`. Firmly a pentest/lab reference; only marginally OSINT and low relevance to missing-persons work. Reach for it when you are authorised to assess a device and want to test whether defaults were ever changed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://phenoelit.de/dpl/dpl.html (use the `.de` mirror — the `.org` host is frequently unreachable).
2. Browse or in-page search (Ctrl-F) for the vendor and model.
3. Read off the Access Type, default Username and `password` columns.
4. Apply only on hardware you own or are explicitly authorised to test.

## Inputs → Outputs
- **In:** `device-id` (vendor + model)
- **Out:** default username / `password` pair(s), with access type
- **Empty/negative result looks like:** the vendor/model isn't in the table — likely because the device post-dates the list. Consult a maintained modern default-credential source instead.

## Gotchas & OpSec
- Human-in-the-loop: none to read the list.
- OpSec: reading is **passive**; *using* a credential against a live device is an active intrusion and may be illegal without authorisation.
- The list is essentially frozen (~2008), so it skews toward legacy hardware; treat it as historical reference, not current.

## Overlaps ("do both")
- Standalone reference; combine with a maintained default-credential database when the target device is modern.

## Trust & verifiability
`trust: community` — a venerable, well-known list from the Phenoelit group; accurate for its vintage but outdated, and served reliably only from the `.de` mirror.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phenoelit-default-password-list |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | device-id → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
