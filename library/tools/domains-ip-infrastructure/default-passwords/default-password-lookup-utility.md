---
id: default-password-lookup-utility
name: Default Password Lookup Utility
description: Use when you have a device make/model (router, switch, camera…) and want its factory-default credentials — returns the vendor's default password.
url: https://fortypoundhead.com/tools_dpw.asp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up factory default usernames/passwords for a networked device by manufacturer.
selectorsIn:
- device-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free web lookup; no account required.
opsec: passive
opsecNote: Passive — you query a static reference database of published default credentials, not any live device. The lookup reveals nothing to a device owner. Actually USING a credential against a device you don't own is a separate, active, and potentially unlawful act — out of scope here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: FortyPoundHead is a long-running IT knowledge-base; the ~1,800-entry default-password list is community-compiled and can be stale or incomplete, so treat entries as candidates rather than guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- FortyPoundHead Default Password Lookup
- default password database
tags:
- default-credentials
- device-hardening
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Default Password Lookup Utility

> A searchable database (~1,800 entries) of manufacturers' factory default usernames and passwords for routers, switches, cameras, and other gear.

## When to use
You have identified a network device by make/model (`device-id`) — from a banner grab, a Shodan result, an equipment label, or documentation — and want to know its out-of-the-box default credentials. Primarily a defensive/audit and infrastructure-context tool: confirming whether a device still ships with well-known credentials, not for unauthorised access.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fortypoundhead.com/tools_dpw.asp.
2. Search by phrase (e.g. `Cisco`, `Linksys`, `Hikvision`) or browse the full list for a manufacturer.
3. Read the returned rows: manufacturer, model/context, default username, and default password.
4. Match the entry to your exact model — vendors reuse and change defaults across firmware, so pick the closest model/version.
5. Use in context only: e.g. flagging that an exposed device likely still uses vendor defaults during a security review, or corroborating device identity.

## Inputs → Outputs
- **In:** `device-id` (manufacturer/model string)
- **Out:** factory-default `password` (and username) for matching devices
- **Empty/negative result looks like:** no rows for that manufacturer/model — either the device isn't catalogued or it never shipped with a documented default. Absence here is not assurance a device is secure; cross-check a second default-credential database.

## Gotchas & OpSec
- Community-compiled and finite (~1,800 entries); big vendors are covered better than niche/consumer IoT.
- Defaults change across firmware revisions and regions — a listed pair may no longer apply.
- Legal line: looking up a default is passive research; entering it on a device you are not authorised to access is unauthorised access. Keep to authorised audits/CTF/defensive contexts.
- OpSec: the lookup is passive and leaks nothing to any device owner.

## Overlaps ("do both")
- Cross-reference other default-credential sources (CIRT.net's default password database, RouterPasswords-style lists) — coverage differs by vendor, so a miss in one is often a hit in another.

## Trust & verifiability
`trust: community` — a useful but crowd-maintained list; verify a listed default against vendor documentation for the exact model/firmware before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | default-password-lookup-utility |
