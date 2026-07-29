---
id: ip-search-network-entity-reputation-database
name: IP search - Network Entity Reputation Database
description: Use when you have an `ip-address` (or ASN/subnet) and want to know if it is a known malicious/abusive host — returns a reputation score, threat categories, and linked infrastructure context.
url: https://nerd.cesnet.cz/nerd/ips/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scoring whether an IP tied to a subject (a login, an email header, a server) is a known bad actor, aggregated from many threat feeds.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Free to browse and search the public instance; the RESTful API and bulk data feeds require a (free) API token and are rate-limited.
opsec: passive
opsecNote: You query CESNET's aggregated database, not the IP itself — no packet ever reaches the target host. Searches run against a third-party academic service; assume the query may be logged there, but the subject is not touched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CESNET (Czech national research & education network) and its Liberouter team; open-source, academically published, sourced from Warden and MISP feeds.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- network-entity-reputation-database-nerd
aliases:
- NERD
- NERD IP search
tags:
- ip-reputation
- threat-intelligence
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# IP search - Network Entity Reputation Database

> CESNET's NERD as a searchable reputation oracle: is this IP a known-malicious network entity, and how confident is that verdict?

## When to use
You have an `ip-address` — from an email header, a login-alert, a server hosting a suspect site, a message the subject received — and want to know whether it is a documented bad actor (scanner, brute-forcer, malware host, spam source) before you weight it as evidence. You can also search by hostname suffix, ASN, or country to find flagged IPs in a range. It profiles *infrastructure*, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nerd.cesnet.cz/nerd/ips/.
2. Filter by `ip-address`/subnet (CIDR), hostname suffix, ASN, country, source feed (Warden, blacklists, DShield, OTX, MISP), or event category.
3. Read the result row(s):
   - **Reputation score** (0–1) — higher = more alerts, more sources, older activity = more likely a true positive.
   - **Threat categories** — e.g. login attempts, scanning, malware.
   - **Context** — ASN, country (`geolocation`), hostname (`domain`), and outbound links to Shodan/Censys/AbuseIPDB.
4. Pivot: a high score corroborates that an IP is hostile infrastructure; the linked Shodan/Censys entries and hostname feed further infrastructure OSINT.

## Inputs → Outputs
- **In:** `ip-address` (or ASN / hostname suffix / country)
- **Out:** reputation score, threat categories, ASN, country (`geolocation`), hostname (`domain`), external-tool links
- **Empty/negative result looks like:** "no record" / no rows — the IP is not in NERD's feeds, i.e. *not reported*, which is not proof it is clean.

## Gotchas & OpSec
- Passive: nothing is sent to the target IP.
- Absence of a record ≠ benign; NERD only knows what its feeds report.
- The score is a confidence aggregate, not a binary — read the underlying categories/sources, don't treat 0.5 as a hard line.

## Overlaps ("do both")
- Pairs with `[[network-entity-reputation-database-nerd]]` (same NERD service) and cross-check against AbuseIPDB/Shodan (linked directly from each result) — NERD aggregates European academic feeds that some commercial reputation tools miss.

## Trust & verifiability
`trust: trusted` — a first-party, open-source academic service (CESNET/Liberouter) with a published methodology; scores are transparent and traceable to source feeds.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-search-network-entity-reputation-database |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
