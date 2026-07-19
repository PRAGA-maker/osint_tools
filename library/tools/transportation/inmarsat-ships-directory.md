---
id: inmarsat-ships-directory
name: Inmarsat Ships Directory
description: Use when you have a vessel name/ID and want its satellite contact numbers — returns Inmarsat mobile numbers (phone/telex/fax) for ships fitted with Inmarsat terminals.
url: http://www.inmarsat.com/ships-directory
category: transportation
path:
- transportation
bestFor: Finding the satellite phone/fax numbers for a specific ocean-going vessel equipped with Inmarsat.
selectorsIn:
- name
- device-id
selectorsOut:
- phone
- device-id
status: live
pricing: free
costNote: Free public directory operated by Inmarsat Maritime; no account needed.
opsec: passive
opsecNote: You query Inmarsat's own vessel directory, not the ship or crew — passive. Do NOT call the numbers you find as part of reconnaissance; satellite calls are billed and a call is direct contact with the vessel, which is active and traceable. Stop at collecting the number.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party directory from Inmarsat (now Viasat), the satellite operator itself — authoritative for Inmarsat-registered maritime terminals.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Inmarsat Maritime ships directory
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Inmarsat Ships Directory

> The satellite operator's own lookup of vessels fitted with Inmarsat terminals — turn a ship's name into its at-sea satellite contact numbers.

## When to use
You have a `name` or identifier of an ocean-going vessel (a ship a person was aboard, a fishing/cargo/yacht vessel in a case) and need a way to reach or identify it at sea. The directory returns the Inmarsat Mobile Number(s) — the satellite phone/telex/fax — assigned to a ship's terminal, which confirms the vessel is Inmarsat-equipped and gives an authoritative contact/identity handle to pair with AIS tracking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Inmarsat Ships Directory (http://www.inmarsat.com/ships-directory, which forwards to the current Inmarsat Maritime customer-service page).
2. Search by vessel `name` (or Inmarsat mobile number / terminal ID if you already have one).
3. Read the returned Inmarsat Mobile Numbers and terminal details (`device-id`) for the vessel.
4. Pivot: cross-reference the vessel on AIS/`[[marinetraffic]]`-style trackers for position; a confirmed terminal/`device-id` ties records together; the `phone` corroborates ownership/operator identity via maritime registries.

## Inputs → Outputs
- **In:** vessel `name` (or Inmarsat number / `device-id`)
- **Out:** `phone` (Inmarsat satellite numbers), terminal `device-id` / equipment details
- **Empty/negative result looks like:** no listing — the vessel has no Inmarsat terminal, uses another provider (Iridium/Thuraya/VSAT), or isn't registered in this directory; fall back to AIS trackers and flag-state registries.

## Gotchas & OpSec
- Human-in-the-loop: none for the lookup.
- OpSec: the search is passive, but **calling** a number you find is direct, billed contact with the vessel — don't do it as recon. Collect the number; act on it only through proper channels.
- Only Inmarsat-equipped vessels appear; small/coastal craft and non-Inmarsat terminals won't be listed.

## Overlaps ("do both")
- Pairs with AIS trackers like `[[marinetraffic]]` and flag/registry lookups — the directory gives the satellite contact/identity, AIS gives live position and voyage history; together they locate and identify a vessel.

## Trust & verifiability
`trust: trusted` — it's the satellite operator's own directory, so the terminal/number data is authoritative for Inmarsat-registered ships; absence only means "not Inmarsat," not "no such vessel."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmarsat-ships-directory |
| category | transportation |
| selectorsIn → selectorsOut | name, device-id → phone, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
