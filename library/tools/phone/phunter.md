---
id: phunter
name: Phunter
description: Use when you have a `phone` number and want a one-shot OSINT profile of it — returns country/operator, line type, location hints, reputation and linked-account signals.
url: https://github.com/N0rz3/Phunter
category: phone
path:
- phone
bestFor: Command-line phone-number reconnaissance — carrier/line-type/location plus spam reputation and checks for accounts linked to the number.
selectorsIn:
- phone
selectorsOut:
- geolocation
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python CLI). Some enrichment relies on scraping public sources; no paid key required for core use.
opsec: passive
opsecNote: Most lookups are against reference/reputation data and public sources, not the number's owner, so it's largely passive. Some modules probe whether the number is registered on services (e.g. account-existence checks) — those can, in principle, be visible to the platform; run from a sock-puppet context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community Python tool (N0rz3) that wraps libphonenumber-style parsing plus scraped reputation/account signals; parsing is reliable, scraped signals vary in accuracy and can break as sources change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- numberingplans-com
- telegram-finder
- zehef
aliases:
- N0rz3/Phunter
tags:
- Phone numbers
- phone-osint
- cli
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Phunter

> A one-command phone-number OSINT tool — decode a number's country/operator/line-type, guess its location, pull spam reputation, and check whether it's tied to accounts.

## When to use
You have a `phone` number and want a fast, consolidated first pass before deeper manual work. Phunter combines number parsing (country, carrier, line type, possible locations) with reputation lookups (spammer or not) and checks for accounts/services linked to the number — the kind of triage that tells you whether a number is a real personal mobile worth pursuing.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/N0rz3/Phunter (Python; `pip install -r requirements.txt`).
2. Run it against the target number in international format (e.g. `python phunter.py -p +1...`).
3. Read the report: valid/possible, country, operator, line type, location guesses, reputation, and any linked-account findings.
4. Treat location/carrier as *issuing* info (portability applies) and reputation as a lead.
5. Pivot: confirm country/type with `[[numberingplans-com]]`; test messaging-app linkage with `[[telegram-finder]]`; a real mobile then justifies deeper people-search.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** `geolocation` (country/possible area), `metadata-exif` (operator, line type, reputation), and `social-profile`/account-linkage signals
- **Empty/negative result looks like:** "invalid/parse failed" or thin enrichment — bad number, VoIP/burner, or scraped sources changed; a sparse result isn't proof the number is unused.

## Gotchas & OpSec
- Scraped reputation/account signals **drift** as upstream sites change; verify anything pivotal.
- Carrier/location reflect issuance, not necessarily current (portability, roaming).
- OpSec: mostly passive, but account-existence probes touch third-party services — use a sock-puppet setup.

## Overlaps ("do both")
- Pairs with `[[numberingplans-com]]` (authoritative number/IMSI decoding) and `[[telegram-finder]]` (messaging linkage) — Phunter is the fast aggregator; confirm its guesses with those focused tools.

## Trust & verifiability
`trust: community` — reliable for standards-based parsing, looser for scraped reputation/linkage; corroborate the interesting signals with a dedicated source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phunter |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, metadata-exif, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>
