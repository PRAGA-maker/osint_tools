---
id: bgp-malicious-content-ranking
name: BGP Malicious Content Ranking
description: Use when you have an `ip-address` or ASN and want to know how malicious the hosting network is — returns a threat-rank score for the Autonomous System.
url: https://bgpranking.circl.lu/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- bgp
bestFor: Scoring an ASN/network for concentration of malicious activity from aggregated blocklists.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free public service run by CIRCL; open-source, with API access — no account required.
opsec: passive
opsecNote: You query CIRCL's aggregated blocklist database, not the target network, so the subject host gets no signal. Fully passive infrastructure reconnaissance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CIRCL (Computer Incident Response Center Luxembourg), a national CERT; open-source and widely used in threat-intel workflows.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CIRCL BGP Ranking
- BGP Ranking
tags:
- domains-ip-infrastructure
- bgp
- threat-intel
- asn
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- lookyloo
---

# BGP Malicious Content Ranking

> CIRCL's BGP Ranking scores Autonomous Systems by how much malicious activity is seen on them — a way to judge the "neighbourhood" a host lives in.

## When to use
You have an `ip-address` (or already know the ASN) from DNS/WHOIS/hosting pivots and want to assess the network hosting it: is this a clean commercial ASN or one saturated with malware, phishing, and botnet traffic? A high rank is a red flag that a domain/host is sitting on abuse-prone infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bgpranking.circl.lu/ (or use the documented API / `bgpranking` client for automation).
2. Search by `ip-address` (it resolves to the announcing ASN) or by ASN directly. Optionally filter by IPv4/IPv6, specific blocklists (abuse.ch, dshield, emergingthreats, etc.), and date.
3. Read the score: a numeric rank plus ASN description and country. Higher = more malicious activity aggregated across sources; compare relative to other ASNs.
4. Pivot: a bad ASN feeds host-level reputation checks like `[[malwareurl]]` and passive-DNS to see what else that network hosts.

## Inputs → Outputs
- **In:** `ip-address` or ASN
- **Out:** ASN threat-rank score, ASN description/country (the `ip-address`'s network context)
- **Empty/negative result looks like:** a low/near-baseline rank or no listings — the ASN has little aggregated abuse; this doesn't clear an individual host, only its network.

## Gotchas & OpSec
- The score is ASN-level, not host-level — a benign site can live on a poorly-ranked ASN and vice versa; use it as context, not a verdict.
- Rankings are relative and time-dependent (set the date to compare historically).
- Depends on which blocklists you include — the mix of sources shifts the score.

## Overlaps ("do both")
- Pairs with `[[malwareurl]]` and `[[lookyloo]]` — this rates the whole network while those inspect the specific host/URL, so together you get both "bad network?" and "bad host?".

## Trust & verifiability
`trust: trusted` — maintained by CIRCL, a national CERT, on open-source code with transparent data sources; the scoring methodology is documented and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bgp-malicious-content-ranking |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
