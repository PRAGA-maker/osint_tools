---
id: ismalicious
name: isMalicious
description: Use when you have a `domain`, `ip-address`, URL, `email`, `crypto-wallet` or file hash and want an aggregated reputation verdict across 570+ threat sources — returns malicious/clean scoring plus WHOIS/DNS/SSL enrichment.
url: https://ismalicious.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop reputation/threat check of an indicator against hundreds of intel sources.
selectorsIn:
- domain
- ip-address
- email
- crypto-wallet
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free account = 30 checks/month with a free API key (no card); Pro tier ~€99/mo for 10,000 checks. Anonymous users get limited results.
opsec: passive
opsecNote: You submit the indicator to a third-party aggregator that logs your queries and account; it does not alert the indicator's owner. Use a sock-puppet email/API key and avoid submitting indicators you don't want a vendor to retain.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates 570+ public/commercial feeds and shows which sources flagged an indicator, so verdicts are traceable; it's a third-party roll-up, not an original source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ismalicious.com
tags:
- domain-and-ip-research
- reputation
- threat-intel
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- virustotal
---

# isMalicious

> Multi-source reputation lookup: paste any indicator and see an aggregated malicious/clean verdict with the sources behind it and WHOIS/DNS/SSL context.

## When to use
You have an indicator — a `domain`, `ip-address`, URL, `email`, `crypto-wallet`, or file hash — and want a fast, sourced answer to "is this bad?" isMalicious rolls up 570+ threat feeds into a single reputation score, shows which sources flagged it, and adds enrichment (WHOIS, DNS, SSL cert, geolocation, MITRE ATT&CK mapping). Good for triaging a suspicious selector before deciding whether to dig deeper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ismalicious.com and enter the indicator (auto-detects type).
2. For full detail, create a free account (30 checks/month, free API key, no card).
3. Read the verdict: aggregated score, the list of sources that flagged it, and enrichment panels (WHOIS/DNS/SSL/geo).
4. For automation, use the free API key within the monthly quota; bulk/blocklist export needs a paid tier.
5. Pivot: a flagged `domain`/`ip-address` feeds infrastructure recon and passive DNS; cross-check the verdict against `[[virustotal]]`.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, URL, `email`, `crypto-wallet`, or file hash
- **Out:** aggregated reputation verdict, list of flagging sources, WHOIS/DNS/SSL/geo enrichment, related `domain`/`ip-address`
- **Empty/negative result looks like:** "clean" / no source flags — the indicator isn't in the aggregated feeds; that's weak evidence of safety (new/targeted threats won't show), not proof.

## Gotchas & OpSec
- Human-in-the-loop: the free tier is capped at 30 checks/month and tight per-minute limits — budget your lookups.
- A "clean" verdict only means "not yet flagged by these feeds"; absence of detection ≠ safe.
- OpSec: passive, but the vendor logs your queries and ties them to your account — use a sock-puppet email.

## Overlaps ("do both")
- Pairs with `[[virustotal]]` — both aggregate reputation, but their source sets differ; a second opinion catches indicators one roll-up misses.

## Trust & verifiability
`trust: community` — a transparent aggregator that names the sources behind each verdict, so you can trace and confirm a flag; it's a secondary roll-up, so always check the underlying source for high-stakes calls.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ismalicious |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email, crypto-wallet → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
