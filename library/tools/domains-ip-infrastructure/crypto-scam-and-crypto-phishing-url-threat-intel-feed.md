---
id: crypto-scam-and-crypto-phishing-url-threat-intel-feed
name: Crypto Scam & Crypto Phishing URL Threat Intel Feed
description: Use when you have a `domain`/URL (or want to enrich one) and want to check it against a free feed of known crypto-scam/phishing sites — returns domain classification, associate leads.
url: https://github.com/spmedia/Crypto-Scam-and-Crypto-Phishing-Threat-Intel-Feed
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a domain/URL against a free, community-maintained list of crypto scam and phishing sites.
selectorsIn:
- domain
selectorsOut:
- domain
- crypto-wallet
status: live
pricing: free
costNote: Free, open dataset on GitHub; clone or read the raw files, no account.
opsec: passive
opsecNote: You match a domain/URL against downloaded lists locally — nothing touches the scam site or the target, so it's passive. Do NOT visit the listed phishing URLs directly to "confirm"; that risks drive-by malware and tips off the operator. Analyse them in a sandbox/URL scanner instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A single researcher's (spmedia) crowd-aggregated feed. Useful for enrichment and blocklisting, but unofficial and time-sensitive — a domain's absence isn't proof it's safe, and inclusion should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- phishingseclists
- threat-actor-usernames-scrape
- urlscan-io
- telegram-channel-joiner
tags:
- domain-and-ip-research
- threat-intel
- phishing
- crypto
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Crypto Scam & Crypto Phishing URL Threat Intel Feed

> A free, GitHub-hosted feed of known crypto-scam and crypto-phishing URLs — a quick way to check whether a domain in your case is already flagged as a scam.

## When to use
You have a `domain`/URL tied to a crypto lead (a "wallet drainer" link, a fake exchange, an investment-scam site a subject or victim interacted with) and want to know if it's a documented scam. Also useful in bulk to enrich a set of domains or to seed a blocklist. Fraud/CTI-oriented; low relevance to a person-centric missing-persons case, higher when the case involves crypto fraud.

## How to use it (`bestInteractionPattern`: cli)
1. Clone or open the repo and pull the feed file(s).
2. Search/match your `domain`(s) against the list (`grep`, or load into your enrichment pipeline).
3. A match = the URL is documented as crypto scam/phishing; note any associated wallet addresses or campaign notes included.
4. Do not open flagged URLs directly — inspect via a scanner/sandbox.
5. Pivot: a listed `domain` → `[[urlscan-io]]` for a safe look and infrastructure; an associated `crypto-wallet` → blockchain tracing; the operator's reuse patterns → related domains.

## Inputs → Outputs
- **In:** `domain`/URL to check (or a batch)
- **Out:** `domain` scam/phishing classification, sometimes associated `crypto-wallet` addresses/campaign context
- **Empty/negative result looks like:** no match — meaning the domain isn't in *this* feed (which is partial and lags fast-moving scam infra), NOT that it's safe. Corroborate with other threat-intel before clearing a URL.

## Gotchas & OpSec
- **Absence ≠ safe:** scam domains spin up faster than any feed updates. Use inclusion as a positive signal, not exclusion as a clearance.
- Static snapshot — re-pull for freshness.
- Never visit flagged phishing URLs directly; sandbox them.

## Overlaps ("do both")
- Pairs with `[[urlscan-io]]` (safe remote inspection) and other blocklists/`[[phishingseclists]]`; corroborate a classification across feeds before acting.

## Trust & verifiability
`trust: community` — an unofficial, single-maintainer feed. Good for cheap enrichment and lead generation; confirm any scam attribution with an independent source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crypto-scam-and-crypto-phishing-url-threat-intel-feed |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
