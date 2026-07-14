---
id: phonumspy
name: PhoNumSpy
description: Use when you have a `phone` number and want carrier/location enrichment plus a web/social footprint sweep — returns geolocation, social-profile, and name leads.
url: https://github.com/CyberNDR/PhoNumSpy
category: phone
path:
- phone
bestFor: Enriching a phone number with carrier/region/line-type data and hunting its linked web and social-media footprint.
selectorsIn:
- phone
selectorsOut:
- geolocation
- social-profile
- name
status: live
pricing: free
costNote: Free and open-source Python CLI; no fees or API key required for the core lookup.
opsec: active
opsecNote: Beyond the offline carrier/region parse, it runs web and social searches that touch third-party sites — that traffic originates from your host. Run from a sock-puppet context; the number owner is not contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community tool (~46 stars); the carrier/region data comes from the libphonenumber-style metadata and is reliable, but the web/social "footprint" results are heuristic and need verification.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- phoneinfoga
- truecaller
aliases:
- PhoNumSpy
- Phone Number Spy
tags:
- phone-osint
- carrier-lookup
- social-footprint
source: gh-topic-footprinting
lastVerified: '2026-07-14'
enrichment: full
---

# PhoNumSpy

> A command-line phone-number enrichment tool: parse a number into carrier/region/line-type, then sweep the web and social platforms for where it appears.

## When to use
You have a `phone` number and want a fast first pass: which country/region and carrier it belongs to, whether it's a mobile/landline/VoIP or a known disposable/burner range, and any web or social-media footprint tied to it. Use it to triage a number early — validate it, geolocate it roughly, and get leads before reaching for heavier phone-OSINT tooling.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/CyberNDR/PhoNumSpy and install its Python requirements.
2. Run it against the number in international format (e.g. `+1...`).
3. Read the offline parse: country code, region/city, carrier, line type — and whether it matches temporary/disposable-number providers (a burner flag).
4. Read the footprint sweep: web/social hits mentioning the number (`social-profile`, `name` leads).
5. Pivot: a name/profile hit feeds people-search; a burner flag reframes the whole lead; the region feeds geolocation.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `geolocation` (country/region/city), `social-profile` + `name` (footprint hits), carrier & line-type, disposable-number flag
- **Empty/negative result looks like:** valid carrier/region but no web/social footprint — common for numbers not publicly posted; absence of a footprint isn't proof the number is unused. A "disposable provider" match strongly suggests a burner.

## Gotchas & OpSec
- **Active:** the footprint sweep hits third-party sites — use a sock-puppet host.
- Carrier/region is reliable metadata; the web/social hits are heuristic — verify each before attributing.
- Portability means the carrier may be the current one, not the original — don't over-read it.

## Overlaps ("do both")
- Pairs with `[[phoneinfoga]]` (the standard phone-OSINT framework with richer footprint scanning) and `[[truecaller]]` (crowd-sourced caller ID → name). Run PhoNumSpy for a quick parse, then PhoneInfoga/Truecaller for depth.

## Trust & verifiability
`trust: community` — a small open-source tool. The metadata parse is trustworthy; the footprint results are leads to corroborate against the source pages.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phonumspy |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
