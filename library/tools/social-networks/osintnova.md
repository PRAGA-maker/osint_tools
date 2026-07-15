---
id: osintnova
name: OSINTNova
description: Use when you have almost any selector (`username`, `email`, `phone`, `ip-address`, `domain`, `vehicle-plate`, `crypto-wallet`, `image`) and want a one-stop platform that runs 50+ lookups — returns social-profile, breach, infra and metadata results.
url: https://app.osintnova.com/
category: social-networks
path:
- social-networks
bestFor: A single web console that fans one selector out across many OSINT modules (social, people, infra, crypto, vehicle, image).
selectorsIn:
- username
- email
- phone
- ip-address
- domain
- vehicle-plate
- vin
- crypto-wallet
- image
selectorsOut:
- social-profile
- name
- email
- phone
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free signup (Google or Discord login) unlocks the majority of commands; some tools are gated behind a PRO tier. No cost for the bulk of lookups after registering.
opsec: active
opsecNote: This is a third-party aggregator — every selector you enter is sent to their servers and to the downstream services each module queries, and you must log in (tying your searches to a Google/Discord identity). Register with a dedicated sock-puppet account, never a personal one. Some modules (e.g. account-existence, phone) actively touch target platforms.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community OSINT aggregator; it wraps many third-party sources of varying quality, so results are only as good as the underlying module. Corroborate hits at the original source.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- osintnova
- app.osintnova.com
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- aggregator
- osint-platform
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# OSINTNova

> A web-based OSINT console that bundles 50+ lookup modules — social media, people/phone, IP/domain/email infra, crypto, vehicle (VIN/plate), image metadata, dark web and Wayback — behind one login.

## When to use
You have a single selector and want to spray it across many sources fast without opening a dozen sites. OSINTNova covers social-media intelligence (Discord, Instagram, Facebook, YouTube, Steam, username across 50+ platforms), people/phone lookups, digital infrastructure (IP, domain, URL, email, headers), crypto wallet analysis, vehicle info (VIN/plate), image metadata extraction, dark-web search, and archive snapshots. Good as a first-pass breadth tool; not a substitute for going to authoritative sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://app.osintnova.com/ and sign up with a sock-puppet Google or Discord account (login is required).
2. Pick the module matching your selector (e.g. "username search", "phone lookup", "image metadata").
3. Enter the selector and run it; free-tier commands cover most modules, PRO-marked ones are gated.
4. Read the module's output — profiles, breach hits, infra records, or metadata depending on the tool.
5. Pivot: take each hit to its authoritative source to confirm (e.g. open the actual profile, verify the breach, re-run EXIF locally).

## Inputs → Outputs
- **In:** `username` / `email` / `phone` / `ip-address` / `domain` / `vehicle-plate` / `vin` / `crypto-wallet` / `image`
- **Out:** `social-profile` links, `name`, secondary `email`/`phone`, `geolocation`, `metadata-exif`, breach/infra records — varies by module
- **Empty/negative result looks like:** a module returning nothing usually means the underlying source had no hit; because it aggregates, a null here is not authoritative — check the primary source directly before concluding.

## Gotchas & OpSec
- Login required and searches are tied to your account — use a dedicated research identity.
- Aggregators wrap sources of mixed reliability; treat every result as a lead to verify at origin.
- Some modules are actively intrusive (account-existence, phone) and some are PRO-gated; know which module you're firing before you fire it.

## Overlaps ("do both")
- Overlaps heavily with dedicated single-purpose tools (username enumerators, EXIF viewers, phone/IP lookups) — use OSINTNova for breadth/triage, then the dedicated tool for depth and to verify.

## Trust & verifiability
`trust: community` — a community aggregator with no data of its own; reliability tracks the underlying module, so always corroborate a hit at the authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintnova |
| category | social-networks |
| selectorsIn → selectorsOut | username, email, phone, ip-address, domain, vehicle-plate, vin, crypto-wallet, image → social-profile, name, email, phone, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
