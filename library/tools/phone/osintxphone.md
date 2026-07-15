---
id: osintxphone
name: osintxphone
description: Use when you have a Mexican `phone` and want its carrier, portability status and region — returns geolocation (region/carrier).
url: https://github.com/e-m3din4/osintxphone
category: phone
path:
- phone
bestFor: Enriching a 10-digit Mexican phone number with carrier and region data via the IFT registry.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: live
pricing: free
costNote: MIT-licensed open-source script (free), but it queries the IFT (Instituto Federal de Telecomunicaciones) API — you must supply your own IFT API key in config.json, so the practical barrier is obtaining that key.
opsec: passive
opsecNote: Lookups hit Mexico's telecom regulator (IFT), not the subscriber's device, so the target is not alerted — passive. The query is tied to your IFT API key/account, so use a dedicated key and run from a clean environment.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small single-author OSS tool (~20 GitHub stars, MIT). Thin community footprint; audit the short Python source before running.
missingPersonsRelevance: high
coverage:
- mx
auth: api-key
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- OSINT-x-Phone
- osint x phone
tags:
- phone
- mexico
- regional
source: gh-topic-osint-resources
lastVerified: '2026-07-15'
enrichment: full
---

# osintxphone

> A small Python CLI that resolves a Mexican phone number against the IFT registry to return its carrier, portability status and geographic region — one of the few Mexico-specific phone tools.

## When to use
You have a 10-digit Mexican `phone` number and need to know which carrier holds it, whether it has been ported, and its geographic region/state. This narrows a Mexican number's likely location and helps confirm whether a claimed carrier/region is plausible.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/e-m3din4/osintxphone`.
2. Install the dependency: `pip install requests`.
3. Obtain an IFT API key and place it in `config.json` in the same directory.
4. Run: `python3 OSINT-x-Phone.py <10-digit-number>` (use `-h` for help).
5. Read the returned carrier / region / portability fields. Pivot: the region narrows a `geolocation`; the carrier informs which messaging/recovery pivots to try next.

## Inputs → Outputs
- **In:** `phone` (10-digit Mexican number)
- **Out:** `geolocation` — carrier name, portability flag, and region/state derived from the numbering plan
- **Empty/negative result looks like:** an API error or an empty/"not found" response — usually a malformed number, a non-Mexican number, or a missing/expired IFT API key rather than proof the number is unassigned.

## Gotchas & OpSec
- Mexico-only: it validates against the IFT plan, so non-Mexican numbers won't resolve.
- The hard gate is the IFT API key — without it the script cannot query; obtaining one is a manual, human-in-the-loop step.
- Carrier lookups reflect the current numbering assignment, not the subscriber's identity — this returns no name.
- OpSec: passive to the target; audit the ~100-line source before trusting it with a key.

## Overlaps ("do both")
- Pairs with a global phone tool for the name/identity layer this can't provide — use osintxphone for authoritative Mexican carrier/region, then a broader lookup for reputation/social links.

## Trust & verifiability
`trust: community` — an open-source, MIT-licensed script from a single author with a small following; the data itself derives from Mexico's official IFT registry, so the carrier/region signal is authoritative even though the wrapper is unaudited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintxphone |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
