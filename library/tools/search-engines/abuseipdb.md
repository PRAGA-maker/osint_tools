---
id: abuseipdb
name: AbuseIPDB
description: Use when you have an `ip-address` and want its abuse reputation — returns crowd-reported malicious activity, a confidence-of-abuse score, and the ISP/usage/geolocation for the IP.
url: https://www.abuseipdb.com/
category: search-engines
path:
- search-engines
bestFor: Checking an IP address's abuse history and reputation, with ISP and coarse location.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free to check an IP on the website (with a free account for the API/more detail). High-volume API use is paid, but interactive per-IP checks are free.
opsec: passive
opsecNote: You query AbuseIPDB's database, not the IP itself, so the target host isn't contacted. AbuseIPDB logs your account/queries; use a research account. Reporting an IP is public — don't report during an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large crowd-sourced IP-reputation database; reports are user-submitted (so individual reports are unverified), but the aggregate score and the ISP/geo metadata are useful signals.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- search-arin-net
aliases:
- Abuse IP DB
- abuseipdb.com
tags:
- speciality-search-engines
- ip-reputation
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# AbuseIPDB

> A crowd-sourced IP-reputation database — check an address for reported abuse (spam, brute-force, scanning) and read its confidence score, ISP, usage type, and coarse location.

## When to use
You have an `ip-address` from a header, log, or metadata and want to characterize it: is it a known-bad IP (spam, attacks), and what kind of address is it — residential, hosting/VPN, corporate? AbuseIPDB's report history and abuse-confidence score flag malicious infrastructure, while its metadata (ISP/`employer-org`, usage type, country `geolocation`) helps you judge whether an IP plausibly belongs to a person versus a datacenter/VPN. It characterizes infrastructure, not people, so direct person-finding relevance is low but it's a strong IP-triage step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.abuseipdb.com/ and enter the `ip-address` in the check box.
2. Read the **abuse-confidence score**, number and type of reports, and dates.
3. Note the **ISP**, **usage type** (e.g. Data Center/Web Hosting/Transit vs residential ISP), domain, and country/geolocation.
4. Use usage type to judge attribution: a hosting/VPN IP means the real user is masked; a residential ISP IP is more likely tied to a subscriber (still needs legal process to identify).
5. Pivot: the ISP/netblock → [[search-arin-net]] / RIR Whois; a residential ISP + location → IP-geolocation context; a flagged VPN/proxy → expect the true origin to be hidden.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** abuse-confidence score and report history, plus ISP (`employer-org`), usage type, and country (`geolocation`)
- **Empty/negative result looks like:** score 0 / no reports — the IP simply hasn't been reported, which is NOT proof it's benign or unused. Weigh the metadata regardless of the score.

## Gotchas & OpSec
- Reports are **user-submitted and unverified**; a high score suggests bad reputation but individual reports can be wrong or malicious. Use the aggregate as a signal, not proof.
- Usage-type/ISP data is the more reliable part for attribution triage.
- OpSec: **passive** — a database query. Don't submit abuse *reports* during an investigation (they're public); use a research account.

## Overlaps ("do both")
- Pairs with [[search-arin-net]] (authoritative registration) and IP-geolocation/VPN-detection tools — AbuseIPDB adds reputation and usage type on top of who-owns-it and where-is-it.

## Trust & verifiability
`trust: community` — a widely-used crowd-sourced reputation service; the aggregate score and ISP/usage metadata are dependable signals, but treat any single report as unverified until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abuseipdb |
| category | search-engines |
| selectorsIn → selectorsOut | ip-address → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
