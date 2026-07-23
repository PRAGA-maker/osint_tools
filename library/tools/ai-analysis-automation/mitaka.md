---
id: mitaka
name: Mitaka
description: Use when you have an `ip-address`, `domain`, `email`, `crypto-wallet` or file hash and want one-click enrichment across 65+ threat-intel services — returns pivots to related `domain`/`ip-address` and reputation data.
url: https://github.com/ninoseki/mitaka
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Right-click enrichment of a selected indicator (IP, domain, email, hash, wallet) across dozens of OSINT/threat-intel engines.
selectorsIn:
- ip-address
- domain
- email
- crypto-wallet
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT). Installed from the Chrome Web Store or Firefox Add-ons; some linked services need their own free/paid API keys or accounts.
opsec: passive
opsecNote: Mitaka itself collects nothing (verifiable in source), but every pivot you click sends the indicator to a third-party service (VirusTotal, Shodan, urlscan, etc.) from your session — treat each click as an active query on that service and use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source extension by ninoseki, widely used by DFIR/threat-intel analysts; code is public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ninoseki/mitaka
tags:
- browser-extension
- threat-intel
- ioc
- enrichment
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- mihari
- miteru
---

# Mitaka

> Browser extension that turns any selected indicator into a right-click menu of 65+ OSINT and threat-intel lookups.

## When to use
You are looking at an `ip-address`, `domain`, `email`, file hash, or `crypto-wallet` (Bitcoin/Ethereum) in a page and want to enrich it fast without hand-copying it into a dozen sites. Highlight the value, right-click, and Mitaka offers to search it across VirusTotal, Shodan, Censys, urlscan, SecurityTrails, OTX and more — plus "scan" actions to submit it. Strongest for infrastructure/malware pivoting; it auto-detects the indicator type and de-fangs obfuscated IoCs (`hxxp`, `1[.]2[.]3[.]4`).

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Mitaka from the Chrome Web Store or Firefox Add-ons.
2. In any page, select the indicator text (IP, domain, email, hash, or wallet address).
3. Right-click → **Mitaka** → pick a **Search** action (opens the chosen engine on that indicator) or a **Scan** action (submits it, e.g. to urlscan/VT).
4. Read the opened service for reputation, related infrastructure, and pivots (`domain` ↔ `ip-address`, passive DNS, certs).
5. Chain: feed the pivots back into another Mitaka search, or into a monitoring workflow with `[[mihari]]`.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, `email`, `crypto-wallet`, or file hash (auto-detected)
- **Out:** links to per-service enrichment — related `domain`/`ip-address`, passive DNS, WHOIS, reputation/malware verdicts
- **Empty/negative result looks like:** the chosen engine returns "not found" / no data for that indicator — try another of the 65+ engines rather than concluding the indicator is clean.

## Gotchas & OpSec
- The extension records nothing, but each click queries a third-party service from your IP/session — use a sock-puppet browser and be aware some services rate-limit or require an API key/login.
- Result quality depends entirely on the downstream engine, not on Mitaka.
- Wallet/email selectors are supported but the deepest value is infrastructure (domain/IP/hash) pivoting.

## Overlaps ("do both")
- Pairs with `[[mihari]]` (same author) — Mitaka is the interactive, right-click enrichment front-end, while Mihari continuously hunts and stores matching indicators; do ad-hoc pivots in Mitaka, then persist watchlists in Mihari.

## Trust & verifiability
`trust: community` — a widely-adopted open-source extension whose source is public and whose author states no user data is collected; the enrichment itself is only as trustworthy as each linked service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mitaka |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address, domain, email, crypto-wallet → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
