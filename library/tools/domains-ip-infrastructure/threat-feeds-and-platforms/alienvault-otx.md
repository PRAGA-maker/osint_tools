---
id: alienvault-otx
name: AlienVault OTX
description: Use when you have a `domain`, `ip-address`, or file hash and want community-sourced threat context — returns related indicators, malware/campaign tags, and passive DNS.
url: https://otx.alienvault.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Enriching a domain/IP/hash with crowd-sourced "pulses" (threat reports) and pivoting to related indicators.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free to browse and search; a free account (and API key) unlocks the DirectConnect API and subscribing to pulses. No paid tier required for core lookups.
opsec: passive
opsecNote: You query AT&T/LevelBlue's OTX servers, not the target's infrastructure, so the subject is not alerted. OTX does log searches against your account; use a research account, not one tied to your real identity, if attribution matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, widely-used platform operated by LevelBlue (formerly AT&T Cybersecurity / AlienVault). Underlying pulses are community-contributed, so individual indicators vary in quality; the platform itself is reputable.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- alienvault-open-threat-exchange
aliases:
- Open Threat Exchange
- OTX
- LevelBlue OTX
tags:
- threat-intel
- passive-dns
- ioc-enrichment
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# AlienVault OTX

> Crowd-sourced threat-intelligence exchange: paste an indicator, get the community's reports, related IOCs, and passive DNS around it.

## When to use
You have an `ip-address`, `domain`, or file hash surfaced during infrastructure or malware analysis and want to know whether it appears in known threat activity — and what else it connects to. OTX aggregates "pulses" (analyst-authored threat reports) plus passive DNS, so a single lookup can reveal sibling domains, resolving IPs, and campaign/malware tags to pivot on. It is an enrichment/pivot tool, not a people-finder — its missing-persons value is indirect (mapping infrastructure behind a scam, sextortion, or trafficking site).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://otx.alienvault.com/ and (optionally) create a free account — browsing works logged-out, but subscribing to pulses and the API need login.
2. Paste an `ip-address`, `domain`, hostname, URL, or file hash into the search box.
3. Read the indicator page:
   - **Pulses** — threat reports that reference this indicator (with tags like malware family, campaign, adversary).
   - **Passive DNS** — historical `domain` ↔ `ip-address` resolutions to pivot on.
   - **Related** indicators, WHOIS, and URL/file analysis tabs.
4. Pivot: take a related domain/IP back into the search box, or export via the DirectConnect API (needs a free API key from your account settings) for bulk enrichment.

## Inputs → Outputs
- **In:** `ip-address`, `domain` (also hostname, URL, file hash, CVE)
- **Out:** related `domain` / `ip-address` indicators, passive-DNS history, malware/campaign tags
- **Empty/negative result looks like:** "0 pulses" and sparse passive DNS — means no one in the community has reported this indicator, NOT that it is clean; absence of reports is not evidence of safety.

## Gotchas & OpSec
- Human-in-the-loop: an account login is needed for API access and pulse subscriptions; core search is available without it.
- Pulses are community-submitted — a scary tag may be one analyst's low-confidence guess. Corroborate before acting.
- Passive DNS coverage is uneven; missing history does not mean a resolution never existed.
- OpSec: passive toward the target (you never touch their servers), but your searches are logged to your OTX account.

## Overlaps ("do both")
- Pairs with `[[alienvault-open-threat-exchange]]` (the same platform seeded separately) and other passive-DNS / reputation sources, since OTX's DNS history is partial and cross-checking a second feed catches resolutions it misses.

## Trust & verifiability
`trust: trusted` — the platform is a mature, well-known service run by LevelBlue; treat the aggregated indicators as reputable-but-verify, because their quality depends on the individual community contributor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alienvault-otx |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
