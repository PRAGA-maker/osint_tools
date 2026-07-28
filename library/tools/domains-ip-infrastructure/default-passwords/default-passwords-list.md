---
id: default-passwords-list
name: Default passwords list
description: Use when you have a `device-id` (make/model of a router, camera or appliance) and want its factory-set credentials — returns default username/password pairs by manufacturer.
url: https://default-password.info/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up the factory default login for a specific device make/model, indexed by manufacturer.
selectorsIn:
- device-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free public reference site; no account required. Community-contributed ("Add your device").
opsec: passive
opsecNote: Browsing the reference list is entirely passive and reveals nothing to any target. Actually using a default credential against a device you do not own is intrusive and likely unlawful — this entry is for identification/reference only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowd-maintained directory of published factory defaults; entries are user-contributed, so verify against the vendor's own manual before relying on any pair.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- phenoelit-default-password-list
aliases:
- default-password.info
- default password database
tags:
- default-passwords
- device-credentials
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Default passwords list

> A searchable, manufacturer-indexed directory of factory-default usernames and passwords for routers, cameras, and other networked devices.

## When to use
You have identified a specific device — a router, IP camera, DVR, printer or IoT appliance — by make and model (a `device-id`, often recovered from a banner, a service fingerprint, or a photo of a label) and you need to know its factory-default credentials. Useful in a defensive/authorized context (checking whether a device you're assessing still ships with well-known defaults) and as background intelligence on how a device is likely configured.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://default-password.info/.
2. Use the search box, or browse the alphabetical A–Z manufacturer index (2wire … Zyxel).
3. Open the manufacturer, then find the specific model.
4. Read the listed default username/password pair(s) and any notes (some models have multiple defaults across firmware versions).
5. Cross-check the pair against the device's official manual before relying on it — crowd entries can be wrong or model-specific.

## Inputs → Outputs
- **In:** `device-id` (manufacturer + model)
- **Out:** `password` (default credential pair, sometimes with default IP/URL to the admin panel)
- **Empty/negative result looks like:** the manufacturer or model isn't listed — the site is community-maintained and incomplete; check the vendor manual or `[[phenoelit-default-password-list]]` instead.

## Gotchas & OpSec
- **Authorization matters:** looking up a default is passive and legal; *using* it against a device you don't own or aren't authorized to test is not. Keep this to reference and authorized assessments.
- Crowd-sourced data — a listed pair may be wrong, outdated, or apply only to certain firmware. Verify before trusting.
- Many deployed devices have had defaults changed; a match here is a hypothesis, not a fact about the live device.

## Overlaps ("do both")
- Pairs with `[[phenoelit-default-password-list]]` — a second, long-established default-credential reference; check both since coverage of makes/models differs.

## Trust & verifiability
`trust: community` — a crowd-maintained reference of published factory defaults; individual entries are user-contributed and unverified, so confirm any credential against the manufacturer's official documentation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | default-passwords-list |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | device-id → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
