---
id: ibm-x-force-exchange
name: IBM X-Force Exchange
description: Use when you have a `domain`, `ip-address`, URL, or file hash and want IBM's threat-intel reputation and reports on it — returns domain, ip-address reputation and infrastructure leads.
url: https://exchange.xforce.ibmcloud.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Checking the reputation and threat context of an IOC (domain, IP, URL, hash) against IBM X-Force intelligence.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier after registration covers interactive IOC lookups; higher API rate limits and premium feeds require paid plans.
opsec: passive
opsecNote: Queries hit IBM's threat database, not the target's infrastructure, so lookups are passive and invisible to your subject. Your searches are tied to your X-Force account; use an account you're comfortable associating with the investigation.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by IBM Security (X-Force). A reputable commercial threat-intel platform; reputation scores are IBM's assessment — corroborate with other feeds before acting on a verdict.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- ibm-x-force-exchange-current-malicious-activity
- virustotal
- urlscan-io
tags:
- threat-intel
- ioc-reputation
- domain-and-ip-research
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# IBM X-Force Exchange

> IBM's threat-intelligence sharing platform — look up a domain, IP, URL, or file hash and get its reputation, associated malware/campaigns, and related infrastructure.

## When to use
You have an indicator of compromise (a suspicious `domain`, `ip-address`, URL, or malware hash) from your investigation and want to know if it's known-malicious and what it's tied to. Useful for enriching infrastructure leads (phishing, malware C2, scam hosting). Infra/CTI-oriented; low relevance to a person-centric missing-persons case.

## How to use it (`bestInteractionPattern`: web-manual / api)
1. Register for a free IBM X-Force Exchange account and sign in.
2. Search the IOC (domain / IP / URL / hash).
3. Read the report: risk score, categorisation, associated malware families/campaigns, passive DNS, and related IPs/domains.
4. Use "collections" to organise findings if working a larger case; the API supports automation.
5. Pivot: related domains/IPs → map the campaign; a hash → sample sources; corroborate the verdict in `[[virustotal]]` and inspect live with `[[urlscan-io]]`.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, URL, or file hash
- **Out:** reputation/risk verdict plus related `domain`s and `ip-address`es (infrastructure links)
- **Empty/negative result looks like:** "no reports" / low-risk — meaning IBM has nothing on it, which is NOT a clean bill of health (novel infrastructure is unknown to every feed at first). Cross-check other sources.

## Gotchas & OpSec
- **Unknown ≠ safe:** a clean X-Force result doesn't clear an indicator; new malicious infra isn't yet catalogued.
- Requires a (free) account; rate limits and richer feeds are paywalled.
- Reputation is IBM's judgement — corroborate before attributing or blocking on it alone.

## Overlaps ("do both")
- Pairs with `[[virustotal]]` (multi-engine reputation) and `[[urlscan-io]]` (safe live inspection); different feeds see different infrastructure, so run several. See `[[ibm-x-force-exchange-current-malicious-activity]]` for the live-threat view.

## Trust & verifiability
`trust: trusted` — a reputable vendor platform. Verdicts are reliable as one authoritative opinion; confirm across feeds and inspect the live indicator before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ibm-x-force-exchange |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
