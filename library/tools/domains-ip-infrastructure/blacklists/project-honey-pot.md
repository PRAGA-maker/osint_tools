---
id: project-honey-pot
name: Project Honey Pot
description: Use when you have an `ip-address` and want its spam/abuse history — returns a threat classification (harvester, spammer, dictionary attacker) with first/last-seen activity.
url: https://www.projecthoneypot.org/list_of_ips.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Checking whether an IP has a history of spam harvesting, comment spam, or dictionary/brute-force attacks.
input: IP address
output: Threat score, spam reports, attack activity
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
opsec: passive
opsecNote: You query Project Honey Pot's honeypot-collected database, not the host at the IP, so the target machine isn't contacted or alerted. Data reflects behavior seen by honeypots — it classifies an address, not a person, and shared/dynamic IPs may carry a prior tenant's history.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, respected anti-spam project (behind the http:BL / Http:BL DNSBL); data is from a distributed honeypot network.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Project Honey Pot
- projecthoneypot.org
tags:
- ip-reputation
- spam-blacklist
- threat-history
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Project Honey Pot

> A distributed honeypot network's IP-reputation lookup — check whether an IP is a known email harvester, spam server, comment spammer, or dictionary attacker, with dates of activity.

## When to use
You have an `ip-address` from a suspicious email header, a comment/registration, or a connection log and want to know if it has a history of abuse. Project Honey Pot classifies IPs by observed bad behavior (harvesting, spamming, brute-forcing) with first/last-seen timestamps — useful for triaging whether an IP tied to a scam or intrusion in your investigation is known-bad infrastructure worth pivoting on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.projecthoneypot.org/ and use "Lookup IP" (or go directly to the IP's page).
2. Enter the target `ip-address`.
3. Read the record: threat classification, total bad events, first/last activity dates, and geographic origin (`selectorsOut`).
4. Pivot: the classification + AS/geo point to hosting/botnet infrastructure; cross-check the IP in other reputation sources. Programmatic checks use the http:BL DNSBL (needs a free API key).

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `ip-address` reputation (threat type, event count, first/last seen), `geolocation` (origin)
- **Empty/negative result looks like:** no record / not listed — the IP hasn't tripped a honeypot, meaning it isn't known-bad here, NOT that it's proven clean.

## Gotchas & OpSec
- Human-in-the-loop: individual web lookups are open; viewing full lists or using the http:BL API needs a free account/key.
- OpSec: passive — honeypot data, no contact with the target host.
- Behavioral, address-level data: it tells you what an IP has *done*, not who used it; dynamic/shared IPs can inherit a previous user's reputation.

## Overlaps ("do both")
- Pairs with [[crowdsec]], AbuseIPDB, Spamhaus, and GreyNoise — cross-check an IP across reputation sources since each has different sensor coverage; Project Honey Pot is especially strong on email-harvesting and comment-spam history.

## Trust & verifiability
`trust: trusted` — a long-established, respected anti-spam project with a real distributed honeypot network. Its behavioral verdicts are reliable indicators of abuse, but they characterize an address, so treat any attribution to a person with caution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | project-honey-pot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
