---
id: mnemonic
name: Mnemonic PassiveDNS
description: Use when you have a `domain` or `ip-address` and want its historical DNS resolutions — returns which IPs a domain resolved to over time (and vice-versa), with first/last-seen timestamps.
url: https://passivedns.mnemonic.no/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- passivedns
bestFor: Historical passive-DNS — mapping a domain's past IP resolutions (and reverse) with timestamps, without touching the domain.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free passive-DNS service from mnemonic (a Norwegian security firm); public web queries are open, with heavier/API use gated by a requested free key.
opsec: passive
opsecNote: Truly passive — it returns DNS observations from mnemonic's own sensors and never queries the target domain, so the subject sees nothing. mnemonic logs your searches; use a clean session for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by mnemonic, an established Norwegian cybersecurity company; a long-standing, well-regarded passive-DNS source used across the industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- mnemonic PassiveDNS
- passivedns.mnemonic.no
tags:
- passivedns
- dns-history
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Mnemonic PassiveDNS

> A passive-DNS database from mnemonic: query a `domain` or `ip-address` and get its historical resolutions — which IPs it pointed to, when, and what else shared those IPs — all without ever contacting the target.

## When to use
You have a `domain` or `ip-address` and need its history, not just its current state: what IP a domain resolved to last year, which domains once shared an IP, when a hostname first appeared or went dark. This is essential for tracking infrastructure that has since moved — a phishing domain that changed hosts, a site that briefly co-located with others, or reconstructing a timeline of a domain's life.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://passivedns.mnemonic.no/.
2. Enter a `domain` (to see its historical IP resolutions) or an `ip-address` (to see domains that resolved to it).
3. Read the results — each record shows the answer, record type, and first-seen / last-seen timestamps.
4. Sort by time to build the resolution timeline; note overlaps where multiple domains shared one IP.
5. Pivot: a historical IP feeds reverse-IP and hosting research; co-resolving domains feed a link graph; timestamps anchor a chronology.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** historical DNS records — resolved `ip-address`es / `domain`s with first-seen and last-seen dates
- **Empty/negative result looks like:** no records — mnemonic's sensors never observed that resolution (coverage is sensor-based, not exhaustive), so a blank is a coverage gap, not proof the resolution never existed. Cross-check another passive-DNS source.

## Gotchas & OpSec
- Passive-DNS coverage is sensor-dependent — mnemonic sees what its collection network saw, so results differ from other passive-DNS providers; use more than one for completeness.
- Heavy or programmatic use is gated behind a requested free API key; the open web lookup is rate-limited.
- OpSec: fully passive — the target domain is never queried; only mnemonic sees your search.

## Overlaps ("do both")
- Pairs with other passive-DNS sources (SecurityTrails, DNSDB, CIRCL) and with live WHOIS — each passive-DNS provider has a different sensor footprint, so run a domain across several to reconstruct the fullest resolution history.

## Trust & verifiability
`trust: trusted` — run by mnemonic, an established security firm; a reputable, long-standing passive-DNS source, with the inherent caveat that any single passive-DNS view is partial by nature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mnemonic |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
