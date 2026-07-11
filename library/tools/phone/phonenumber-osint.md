---
id: phonenumber-osint
name: PhoneNumber-OSINT
description: Use when you have a `phone` number and want its basic technical metadata — returns country, region, carrier/provider, timezone, and line-type validity, all computed offline.
url: https://github.com/spider863644/PhoneNumber-OSINT
category: phone
path:
- phone
bestFor: Fast offline phone-number triage — country, carrier, timezone, and validity from the number alone.
selectorsIn:
- phone
selectorsOut:
- phone
- geolocation
status: live
pricing: free
costNote: Free and open-source CLI (Python). No fees, no API keys for the core libphonenumber-based lookups.
opsec: passive
opsecNote: The core metadata is derived offline from the number's structure (via the libphonenumber dataset) — no query reaches the target or their carrier, so it's fully passive. Nothing is disclosed to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small community CLI wrapping standard phone-metadata libraries; the country/carrier/timezone data is as reliable as libphonenumber (good), but it does NOT identify the owner.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- PhoneNumber OSINT
- spider863644/PhoneNumber-OSINT
tags:
- Phone numbers
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# PhoneNumber-OSINT

> A lightweight CLI that decodes a phone number's structure into country, carrier, and timezone — the fast offline triage step before you spend effort on owner attribution.

## When to use
You have a `phone` number and want to immediately establish the basics: which country/region it belongs to, its likely carrier, its timezone, and whether it's a valid/plausible number and line type. Best as the first move on any number — it tells you where to point owner-lookup tools next, without touching the network. It does **not** return a name.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install (works on Linux/Termux):
   ```
   git clone https://github.com/spider863644/PhoneNumber-OSINT.git
   cd PhoneNumber-OSINT
   pip install -r requirements.txt
   ```
2. Run: `python3 phonenumber_osint.py` and supply the number in international format (`+CC...`).
3. Read the output: country/region, carrier/provider, timezone(s), and validity/line-type.
4. Use the country + carrier to choose the right owner-attribution tool for that region.
5. Pivot: feed the number into `[[truecaller-com]]` or a regional carrier/people-search to get from metadata to a `name`.

## Inputs → Outputs
- **In:** `phone` (E.164 / international format)
- **Out:** country/region (`geolocation`), carrier, timezone, validity/line-type — normalized `phone`
- **Empty/negative result looks like:** "invalid number" or blank carrier — the number is malformed, a non-geographic/VoIP range, or missing a country code. Carrier data can also be stale for ported numbers.

## Gotchas & OpSec
- No owner: this is metadata only — it never identifies who owns the number; pair it with an attribution tool.
- Ported numbers: original-carrier data may be wrong after number porting.
- OpSec: fully passive/offline — nothing reaches the subject or their carrier.

## Overlaps ("do both")
- Pairs with `[[truecaller-com]]` and regional people-search — this establishes country/carrier offline, then those tools attempt the owner name; run this first to aim the second step.

## Trust & verifiability
`trust: community` — a thin wrapper over reliable phone-metadata libraries; the technical fields are trustworthy, but there is no owner data to over-trust.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phonenumber-osint |
| category | phone |
| selectorsIn → selectorsOut | phone → phone, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
