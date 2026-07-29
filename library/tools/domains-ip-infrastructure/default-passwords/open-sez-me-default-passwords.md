---
id: open-sez-me-default-passwords
name: Open Sez Me Default Passwords
description: Use when you have a `device-id` (router/printer/appliance make and model) and want its factory default credentials — returns known default `password`/username pairs.
url: https://open-sez.me/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up factory-default login credentials for a specific hardware vendor/model.
selectorsIn:
- device-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free, ad-supported static reference site; no account.
opsec: passive
opsecNote: Browsing the list is passive and reveals nothing to any third party. Actually using a default credential against a device you don't own is unauthorised access — the site is a reference, not a licence; stay within authorised/consented scope.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community-maintained default-password directory (6,000+ entries, 800+ vendors), last refreshed 2025; accuracy is best-effort and unverified per-entry.
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
- Open Sez Me
- open-sez.me
tags:
- default-passwords
- hardware-credentials
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Open Sez Me Default Passwords

> A long-standing lookup of factory default credentials: give it a vendor/model and it tells you the out-of-the-box username/password.

## When to use
You have a `device-id` — the make and model of a router, IP camera, printer, or other appliance (e.g. found in a subject's home, seized-device inventory, or a photo's visible label) — and, within an *authorised* investigation, need the manufacturer's default credentials to access a device that has never had its password changed. It is a hardware-credential reference, not a people-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://open-sez.me/.
2. Find the vendor via the alphabetical index (each vendor has its own page, e.g. `default-passwords-<vendor>.html`).
3. Locate the model/product row and read the default username and `password` (and any notes like "admin/admin", blank password, or a per-serial scheme).
4. Pivot: use the credential only on devices you are authorised to access; a "default changed" outcome tells you the owner configured the device, which is itself a small behavioural signal.

## Inputs → Outputs
- **In:** `device-id` (vendor + model)
- **Out:** default username / `password` pair(s), notes on the credential scheme
- **Empty/negative result looks like:** vendor not indexed or model absent — no known default is listed; the device may use per-unit credentials or simply isn't catalogued.

## Gotchas & OpSec
- Passive to browse; **using** a credential against hardware you don't own or aren't authorised to test is illegal — legal-gate this to consented/authorised scope.
- Entries are community-submitted and can be stale or wrong for a specific firmware revision.
- Many modern devices ship with unique per-serial passwords, defeating any generic default list.

## Overlaps ("do both")
- Complements device-fingerprinting tools (Shodan/Censys banners) that tell you *what* a device is: identify the model there, then resolve its default credential here.

## Trust & verifiability
`trust: community` — a well-known volunteer-maintained list; treat any single entry as a lead to test (within authorisation), not a guarantee, since per-model defaults change across firmware and regions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-sez-me-default-passwords |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | device-id → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
