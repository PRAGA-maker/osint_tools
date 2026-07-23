---
id: default-passwords-db
name: Default Passwords DB
description: Use when you have a device/vendor `employer-org` or product model and want its factory default credentials — returns candidate default `password`(s) for authorised testing.
url: https://cirt.net/passwords/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- default-passwords
bestFor: Looking up factory default usernames/passwords for network devices and software by vendor.
selectorsIn:
- employer-org
selectorsOut:
- password
status: live
pricing: free
costNote: Free, publicly accessible reference database on cirt.net (maintainers of Nikto); no account.
opsec: passive
opsecNote: Browsing the database is passive — it is a static reference and reveals nothing about any target. Actually using a default credential against a live device is active, intrusive, and must be authorised.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing reference maintained by the CIRT.net / Nikto project; entries are community-contributed and may be dated for newer hardware.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CIRT.net default password database
tags:
- domains-ip-infrastructure
- default-passwords
- credentials
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Default Passwords DB

> CIRT.net's classic default-credentials reference — the factory username/password for hundreds of vendors' devices and software, for authorised access testing.

## When to use
You have identified a device or product (by `employer-org`/vendor and model) — a router, camera, switch, appliance, or piece of enterprise software — and need its factory default credentials, either to test whether they were ever changed (authorised assessment) or to recover access to your own equipment. The DB covers 500+ vendors and 2,000+ credential sets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cirt.net/passwords/.
2. Browse or search by vendor (`employer-org`) — e.g. Cisco, Netgear, HP, Oracle.
3. Read the entry: default username/password pairs (and sometimes the access path) for each product.
4. Use the candidate `password` only against systems you are authorised to test. Pivot: a device found on default creds is a finding for your infrastructure report.

## Inputs → Outputs
- **In:** `employer-org` / vendor (and product model)
- **Out:** candidate default `password`(s) and usernames for that product
- **Empty/negative result looks like:** vendor/model not listed — the DB skews toward older and well-known hardware; check the vendor's own documentation for newer models.

## Gotchas & OpSec
- Reference is passive; *using* a credential against a live system is active and often illegal without authorisation.
- Entries can be stale — modern devices increasingly ship with unique per-unit passwords, so a listed default may not apply.
- Not exhaustive; absence of a vendor doesn't mean no default exists.

## Overlaps ("do both")
- Complements device-search engines (Shodan/Censys-style) — those find exposed devices; this supplies the default credentials to test against your authorised targets.

## Trust & verifiability
`trust: community` — a respected, long-running reference from the Nikto/CIRT.net project, but community-sourced and dated in places; verify against vendor docs for current models.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | default-passwords-db |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
