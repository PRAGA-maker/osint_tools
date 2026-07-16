---
id: scamadvisor
name: ScamAdviser
description: Use when you have a domain, phone, IBAN, or crypto wallet and want a fast trust/scam assessment plus site metadata — returns a trust score and domain/registration signals.
url: https://www.scamadviser.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly checking whether a website (or phone/IBAN/crypto address) is likely a scam, with a trust score and supporting signals.
selectorsIn:
- domain
- phone
- crypto-wallet
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free trust-score lookups for websites, phone numbers, IBANs and crypto addresses; deeper "manual check" and business-verification features are upsold but the core check is free.
opsec: passive
opsecNote: You query ScamAdviser's own index about a third-party site/identifier — the site owner is not notified and nothing about your subject beyond the identifier is submitted. Standard passive hygiene; ScamAdviser sees your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used commercial trust-rating service (~2.5M monthly visitors) with an algorithmic score; treat the score as a heuristic aggregated from WHOIS/registration/reputation signals, not a definitive verdict.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ScamAdviser
- scamadviser.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- scam-check
- domain-reputation
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# ScamAdviser

> A one-box trust/scam checker for websites (and phones, IBANs, crypto addresses) that returns a 1–100 trust score plus the registration and reputation signals behind it.

## When to use
A subject has pointed you at a website, given a phone number, sent an IBAN, or shared a crypto address, and you need a fast read on whether it's legitimate or a scam. ScamAdviser aggregates WHOIS age, hosting/registration data, blacklist status, and review authenticity into a single score and surfaces the underlying domain/registration facts — useful for vetting a site connected to a subject, or triaging a fraud/romance-scam angle in a missing-persons or financial investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scamadviser.com.
2. Paste the identifier — a website/domain, phone number, IBAN, or crypto wallet — into the search box and submit.
3. Read the trust score (higher = safer) and the supporting panel: domain age, registrar/country, server location, SSL, and review signals.
4. Pivot: registration/hosting facts (registrar, country, IP) feed WHOIS and IP-infrastructure tools; a low score flags a lead as likely fraudulent.

## Inputs → Outputs
- **In:** `domain` (also `phone`, IBAN, or `crypto-wallet`)
- **Out:** trust score (0–100) plus `domain` / `ip-address` and registration metadata
- **Empty/negative result looks like:** a brand-new or obscure domain returns a low-confidence/low score simply because there is little data — that is "unknown," not proof of scam; read the underlying signals.

## Gotchas & OpSec
- Human-in-the-loop: none; single-box lookup.
- OpSec: passive — the checked site's owner isn't notified. ScamAdviser sees your IP; use a research browser if that matters.
- The score is algorithmic and can both over- and under-flag; always read the component signals and corroborate with primary WHOIS/hosting lookups before concluding.

## Overlaps ("do both")
- Pairs with first-party WHOIS/IP tools in this category — ScamAdviser gives a fast heuristic and reputation view, those give authoritative registration records; run both on a suspect domain.

## Trust & verifiability
`trust: community` — a large, established commercial reputation service, but its score is a proprietary heuristic. Treat it as triage; verify load-bearing facts against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scamadvisor |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, phone, crypto-wallet → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
