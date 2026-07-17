---
id: digi-netra
name: DIGI-NETRA
description: Use when you have a `phone`, `username`, `ip-address` or `email` and want a quick multi-source CLI trace — returns carrier/geo, cross-platform profiles and basic breach/social signals in one menu.
url: https://github.com/Kauravsrestha-Duryodhan/DIGI-NETRA
category: people-search
path:
- people-search
bestFor: A single interactive CLI that runs basic phone/username/IP/email recon from one menu.
selectorsIn:
- phone
- username
- ip-address
- email
selectorsOut:
- geolocation
- social-profile
- ip-address
- phone
status: live
pricing: free
costNote: Free and open-source (Python). No cost; you install and run it yourself.
opsec: passive
opsecNote: Most modules query third-party lookup services/public data, so the target isn't directly contacted — but some checks (e.g. probing whether a number has WhatsApp/Instagram, or username enumeration) may hit the platform from your IP. Run behind a VPN and treat username/phone platform checks as potentially active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community Python toolkit that wraps existing lookups; convenient but thin, and its results are only as good as the underlying free sources. Verify everything.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- phoneinfoga
- sherlock
- holehe
aliases:
- diginetra
tags:
- phone
- username
- ip
- email
- cli
- recon
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# DIGI-NETRA

> A beginner-friendly all-in-one CLI that bundles basic phone, username, IP, and email lookups behind a single interactive menu.

## When to use
You want a fast, low-setup first pass over a `phone`, `username`, `ip-address`, or `email` and don't want to run four separate tools. DIGI-NETRA gives you an interactive menu: carrier/region for a number and whether it's on WhatsApp/Instagram, a username sweep across platforms, IP geolocation/ISP, and basic email breach/social checks. Treat it as a convenience wrapper for a quick sweep — then confirm anything useful with the dedicated, higher-quality tools it imitates.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/Kauravsrestha-Duryodhan/DIGI-NETRA` and install its Python requirements.
2. Run the script and pick a module from the interactive menu (phone / username / IP / email).
3. Enter the selector and read the module's output.
4. Because modules wrap free public sources, cross-check hits against a purpose-built tool before trusting them.
5. Pivot: a resolved `social-profile` from the username module feeds deeper profiling; carrier/region from the phone module scopes further phone-OSINT; IP geolocation feeds infrastructure work.

## Inputs → Outputs
- **In:** `phone`, `username`, `ip-address`, or `email`
- **Out:** `geolocation` (carrier/IP-level), `social-profile` cross-platform hits, `ip-address`/`phone` metadata
- **Empty/negative result looks like:** a module returns nothing or errors (a wrapped source changed/blocked it) — that's a tooling gap, not confirmation the selector is clean. Re-run the check in a dedicated tool.

## Gotchas & OpSec
- Thin wrapper: phone "geolocation" is carrier/region level only, and username/email results are basic — never report them as definitive.
- OpSec: mostly passive, but platform-presence checks (WhatsApp/Instagram for a number, username enumeration) can hit those services from your IP — use a VPN and a sock puppet where relevant.
- Small project: modules can break when upstream free sources change.

## Overlaps ("do both")
- Pairs with the specialised tools it wraps — `[[phoneinfoga]]` for phone, `[[sherlock]]` for usernames, `[[holehe]]` for email — use DIGI-NETRA for a quick sweep, then those for depth and reliability.

## Trust & verifiability
`trust: community` — a small open-source convenience toolkit. It's inspectable but relies entirely on free upstream sources, so its output is lead-quality; verify every finding in a dedicated tool before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digi-netra |
| category | people-search |
| selectorsIn → selectorsOut | phone, username, ip-address, email → geolocation, social-profile, ip-address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
