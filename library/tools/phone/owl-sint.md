---
id: owl-sint
name: Owl-sint
description: Use when you have a phone number (or an IP/Instagram handle) and want a scripted OSINT lookup — returns carrier/line and geographic metadata for the number plus related pivots.
url: https://github.com/IccTeam/Owl-sint
category: phone
path:
- phone
bestFor: Command-line phone-number metadata lookups (carrier, line type, region) with side utilities for IP and Instagram.
selectorsIn:
- phone
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free and open-source on GitHub (GPL-3.0). Requires local Python; some sub-features may depend on third-party APIs/keys.
opsec: passive
opsecNote: Number metadata (carrier, country, line type) is derived from numbering-plan libraries and does not contact the subscriber, so it is passive and non-alerting. Its "location tracking" and Instagram/IP features may query third-party services from your IP — run behind a VPN, and be sceptical of any precise-location claim.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small community GitHub project (~110 stars); the phone-metadata output is standard and reliable, but its "tracking"/location and social features are unaudited — verify results.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Owl-sint
- OwlSint
tags:
- phone
- lookup
- cli
- self-hosted
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Owl-sint

> A small Python CLI that wraps phone-number metadata lookups (carrier, line type, region) with extra IP and Instagram pivots — a self-hosted starting point for a number.

## When to use
You have a `phone` number and want its baseline metadata — the country/region it maps to, the carrier it was allocated to, and whether it's mobile/landline/VoIP — from a scriptable local tool rather than a web form. That metadata shapes the whole investigation: it tells you which country's directories apply and whether normal reverse-lookup even makes sense. Owl-sint also bundles IP-lookup and Instagram-info helpers for adjacent pivots.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/IccTeam/Owl-sint` and enter the folder.
2. Install Python dependencies per the repo's README (it's Python with some Bash).
3. Run the tool and choose the phone-number lookup; enter the number in full international format (`+<country><number>`).
4. Read the output: country/region, carrier, and line type. Treat any "location/tracking" output as approximate at best.
5. Pivot: the region/carrier feeds the right national directory or reverse-phone service; an associated IP or Instagram handle feeds those respective tools.

## Inputs → Outputs
- **In:** a `phone` number (international format); optionally an IP or Instagram handle for its side features
- **Out:** `geolocation` (country/region the number maps to), carrier/line metadata, and — via helpers — `social-profile`/IP context
- **Empty/negative result looks like:** only generic country/carrier data and no "location," or errors on malformed input. That baseline is the real value; do not expect true subscriber identity or a precise map pin from a number alone.

## Gotchas & OpSec
- Phone metadata comes from numbering-plan libraries (à la libphonenumber) — reliable for country/carrier/line type, but **carrier reflects allocation, not current provider** (portability).
- Be sceptical of "phone tracking/location" claims — a number does not yield a live GPS position; treat such output as marketing, not fact.
- Side features (IP/Instagram) may hit third-party services from your IP — run behind a VPN.
- Community project; verify anything you'll rely on.

## Overlaps ("do both")
- Pairs with web reverse-phone and national directory tools — Owl-sint classifies the number, those tools attempt subscriber attribution.
- Complements `[[telecom-tariffs-co-uk]]` for UK ranges and Ofcom/numbering data for authoritative allocation.

## Trust & verifiability
`trust: unverified` — a small, unaudited GitHub project; its core numbering-plan metadata is standard and trustworthy, but its tracking/social extras are not — corroborate every actionable result against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owl-sint |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
