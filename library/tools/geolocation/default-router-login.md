---
id: default-router-login
name: Default Router Login
description: Use when you have a router brand/model or a gateway `ip-address` and want its default credentials and admin address — returns default IP, username, and password.
url: https://www.cleancss.com/router-default/
category: geolocation
path:
- geolocation
bestFor: Looking up factory-default admin IP, username, and password for a router by brand/model.
selectorsIn:
- device-id
- ip-address
selectorsOut:
- ip-address
- password
status: live
pricing: free
costNote: Free reference database; no account. Browser-based lookup.
opsec: passive
opsecNote: Browsing the reference database is passive and touches no target. Using the credentials to log into a router you do not own is unauthorised access — only apply them to devices you own or are explicitly authorised to test. The lookup itself leaks nothing about your target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large community/vendor-sourced list of factory defaults hosted by CleanCSS. Broadly accurate for common models, but defaults change by firmware/region — treat as reference, not guarantee.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- routerpasswords-com
- shodan
aliases:
- CleanCSS router defaults
- default gateway credentials
tags:
- router
- default-credentials
- network-recon
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Default Router Login

> A searchable database of factory-default router settings — brand/model in, default admin IP + username + password out.

## When to use
Network/infrastructure context: when you know a router's brand and model (a `device-id`) — or you're on a network and want the gateway's admin address — and need its factory-default admin IP and credentials. Useful for authorised network assessments, recovering access to your own equipment, and understanding the default posture of a device you've fingerprinted (e.g. via a banner/Shodan result).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cleancss.com/router-default/.
2. Search or browse by manufacturer, then select the model.
3. Read the entry: default gateway `ip-address` (e.g. 192.168.1.1), default username, and default `password`.
4. Apply only to a device you own or are authorised to test.
5. Pivot: a device model fingerprinted via `[[shodan]]` maps here to its default admin path; confirms whether an exposed device likely still uses defaults.

## Inputs → Outputs
- **In:** `device-id` (router brand/model) or gateway `ip-address`
- **Out:** default admin `ip-address`, default username, default `password`
- **Empty/negative result looks like:** the exact model isn't listed, or the listed defaults don't work — the device was reconfigured, uses per-unit random defaults (common on newer ISP gear), or a firmware/region variant differs; check the vendor's documentation.

## Gotchas & OpSec
- **Authorised use only:** applying these credentials to someone else's router is unauthorised access. This is a reference, not a green light.
- Modern routers increasingly ship with unique per-device passwords (printed on a label), so a generic default often won't apply.
- Firmware/region variations mean the listed default can be wrong — verify against the specific model's manual.

## Overlaps ("do both")
- Pairs with `[[routerpasswords-com]]` — a second default-credentials database with different coverage; cross-check when one lacks your model. Combine with `[[shodan]]` to identify the device before looking up its defaults.

## Trust & verifiability
`trust: community` — a broad, community-sourced reference. Good for common models; always verify the specific model/firmware, since defaults drift and newer devices randomise credentials.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | default-router-login |
