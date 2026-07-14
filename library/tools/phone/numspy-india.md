---
id: numspy-india
name: NumSpy (India)
description: Use when you have an Indian mobile `phone` number and want carrier/region (and, when its data source works, name) — a legacy CLI that queried a TrueCaller-style API; largely defunct now.
url: https://github.com/bhattsameer/NumSpy-older
category: phone
path:
- phone
bestFor: Basic Indian mobile-number enrichment (carrier/circle/region) — where a working data source is available.
selectorsIn:
- phone
selectorsOut:
- name
- geolocation
status: down
pricing: free
costNote: Free open-source Python CLI; you run it yourself.
opsec: passive
opsecNote: You run a local script that queries an external number-lookup API; the number's owner is not directly notified. But you are sending the target number to a third-party API — use responsibly and avoid attributable infrastructure.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A small, archived (read-only since Jan 2020) regional tool relying on a TrueCaller-style API that is almost certainly no longer functional; the author points to a newer pip-installable NumSpy.
missingPersonsRelevance: high
coverage:
- in
auth: none
api: false
localInstall: true
registration: false
aliases:
- NumSpy
- NumSpy-older
tags:
- phone
- india
- regional
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# NumSpy (India)

> A legacy Python CLI for enriching Indian mobile numbers via a TrueCaller-style API — historically returned name/carrier/region, but the repo is archived and its data source is very likely dead.

## When to use
You have an Indian mobile `phone` number and want carrier, telecom circle/region, and possibly a name. In practice, treat this specific repo as `down`: it was archived read-only in January 2020 and depends on an external API that has almost certainly stopped working. The author redirects users to a newer pip-installable NumSpy — check that (and other maintained Indian number tools) before spending time here.

## How to use it (`bestInteractionPattern`: cli)
1. Recognise the caveat: `bhattsameer/NumSpy-older` is archived; look at the newer NumSpy version the repo points to first.
2. If testing the legacy tool: clone it and run `python3 NumSpy.py --number <mobile_number>` (or the bundled GUI/.exe), optionally `-o` to save output.
3. Expect failures or empty results if the upstream API is offline.
4. Verify any returned "name" independently — TrueCaller-style crowd data is often wrong or outdated.
5. Pivot: a confirmed carrier/circle narrows region; a name is a lead for people-search, never proof.

## Inputs → Outputs
- **In:** `phone` (Indian mobile number)
- **Out:** carrier, telecom circle (`geolocation`, region-level), and — if the API works — a crowd-sourced `name`
- **Empty/negative result looks like:** errors or no data — now the expected outcome given the dead API/archived status.

## Gotchas & OpSec
- Very likely non-functional: archived tool + defunct API. Don't rely on it; prefer maintained alternatives.
- Crowd-sourced names (TrueCaller-style) are unreliable and can misattribute — verify.
- You transmit the target number to a third-party API — mind the trust/leak implications.

## Overlaps ("do both")
- Pairs with the newer NumSpy (pip) and `[[phoneinfoga]]` — use maintained tools for real work; this entry documents the legacy tool and its limits.

## Trust & verifiability
`trust: unverified` — an archived, single-author regional tool with a probably-dead data source; any output must be independently confirmed, and absence of output is expected, not meaningful.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numspy-india |
| category | phone |
| selectorsIn → selectorsOut | phone → name, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
