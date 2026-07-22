---
id: default-router-passwords
name: Default Router Passwords
description: Use when you have a router/DVR/camera make and model (`device-id`) and want its factory default login — returns the default `password` and username.
url: https://www.routerpasswords.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up the factory default username/password for a specific network device by manufacturer and model.
selectorsIn:
- device-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free, open community database; no account needed to search.
opsec: passive
opsecNote: Searching the database is a passive reference lookup that touches no target device. Actually using a returned credential against a device you are not authorised to access is intrusive and may be illegal — the lookup is OSINT, the login is not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained default-credential list; entries are crowd-contributed, so a given pair may be outdated or wrong for a specific firmware revision.
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
- routerpasswords.com
- default password database
tags:
- default-passwords
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Default Router Passwords

> A searchable community database of factory-default credentials for routers, DVRs, IP cameras, alarm panels and other network gear, indexed by manufacturer and model.

## When to use
You have identified a network device — from a service banner, a Shodan/Onyphe result, a photo of a label, or a make/model in a report — and want to know its out-of-the-box default login. Useful for context (has the owner ever changed the default? what admin interface am I looking at?) and, in authorised assessments, for a first credential to test.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.routerpasswords.com/.
2. Select the manufacturer from the dropdown (2Wire, Cisco, Linksys, Netgear, Hikvision, etc.).
3. Submit to list that vendor's models with their default username, password and (where known) the protocol/interface.
4. Match the row to your specific model/firmware.
5. Pivot: combine with a device fingerprint from `[[onyphe]]` or a scan result to know which admin panel a given exposed `ip-address` presents.

## Inputs → Outputs
- **In:** a device manufacturer + model (`device-id`)
- **Out:** default username and `password` for that device
- **Empty/negative result looks like:** an obscure or newer model may not be listed, or may list several revisions — absence just means the community hasn't recorded it; try the vendor's own manual.

## Gotchas & OpSec
- Crowd-sourced and vendor-wide: many models ship with per-device unique passwords now, so a listed default may not apply to a specific unit.
- OpSec: the lookup is passive OSINT. **Do not** use a returned credential to access a device you don't own or aren't authorised to test — that crosses from research into unauthorised access.

## Overlaps ("do both")
- Pairs with internet-scan engines like `[[onyphe]]` — the scanner tells you a device is exposed and its model; this database tells you the credential it likely shipped with.

## Trust & verifiability
`trust: community` — entries are user-contributed and can be stale or model-imprecise; cross-check against the manufacturer's official documentation before relying on a pair.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | default-router-passwords |
