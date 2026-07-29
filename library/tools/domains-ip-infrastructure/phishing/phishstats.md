---
id: phishstats
name: PhishStats
description: Use when you have a `domain`, `ip-address`, or URL and want to know if it's linked to phishing — returns matching phishing records with scores and infrastructure.
url: https://phishstats.info/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- phishing
bestFor: Checking a URL/domain/IP against a community phishing feed and pivoting on shared phishing infrastructure.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free search UI and JSON REST API, no signup needed to read (50 requests/day/IP anonymous, 150/day registered). Data refreshes roughly every 90 minutes.
opsec: passive
opsecNote: Querying PhishStats hits its own database, not the phishing site — you don't touch the malicious infrastructure and nothing is disclosed to the operator. If you later visit a listed phishing URL to verify, do so in an isolated/sandboxed environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Community-driven phishing intelligence running since 2014, combining automated detection and infosec-community submissions with a verification engine. Scores are indicative; verify before acting.
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
- phishtank
- urlscan-io
- virustotal
aliases:
- phishstats.info
tags:
- phishing
- threat-intel
- reputation
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# PhishStats

> A free, community-fed phishing intelligence database — search a URL, `domain`, or `ip-address` to see whether it's tied to phishing and what infrastructure it shares.

## When to use
You have a suspicious URL, `domain`, or `ip-address` connected to your investigation (a link a subject received or sent, infrastructure you're mapping) and want to check it against known phishing activity. PhishStats also supports threat hunting — filter by IP, ASN, or date to find clusters of related phishing sites on the same infrastructure.

## How to use it (`bestInteractionPattern`: api)
1. Use the web search at https://phishstats.info/ for interactive lookups, or the JSON REST API for automation.
2. Query by URL, `domain`, `ip-address`, ASN, or date range (API example: `GET /api/phishing?_where=(ip,eq,<ip>)`).
3. Read the results: phishing URLs with threat scores, hosting `ip-address`/country, and associated `domain`s.
4. Respect the free rate limit (50/day anonymous, 150/day registered); register for the higher tier if needed.
5. Pivot: a hosting `ip-address`/ASN feeds a hunt for sibling phishing domains; individual URLs feed `[[urlscan-io]]` / `[[virustotal]]` for rendering and reputation.

## Inputs → Outputs
- **In:** URL / `domain` / `ip-address` (or ASN, date range)
- **Out:** matching phishing records with threat scores, hosting `ip-address`, related `domain`s
- **Empty/negative result looks like:** no matches — the indicator isn't in PhishStats' feed (not proof it's clean, just unseen here); cross-check PhishTank and VirusTotal.

## Gotchas & OpSec
- Coverage is community/feed-based — absence is not innocence; combine multiple phishing feeds.
- Scores are heuristic/ML-assisted; treat a listing as a strong lead, and confirm the URL is genuinely malicious before attribution.
- Free API is rate-limited; batch responsibly and register for more headroom.

## Overlaps ("do both")
- Pairs with `[[phishtank]]` (another community phishing DB with different coverage) and `[[urlscan-io]]` / `[[virustotal]]` (render and reputation). Do both: check several feeds, then render/verify the specific URL.

## Trust & verifiability
`trust: community` — a long-running, transparent community feed. Reliable as a lead source; verify each hit (render in a sandbox, cross-reference) before treating it as confirmed phishing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phishstats |
