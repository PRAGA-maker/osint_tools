---
id: matika
name: Mitaka (OSINT browser extension)
description: Use when you have an `ip-address`, `domain`, `email`, hash or `crypto-wallet` selector on a page and want to pivot it across many intel engines — returns `domain`/infrastructure and threat-intel leads.
url: https://chromewebstore.google.com/detail/mitaka/bfjbejmeoibbdpfdbmbacmefcbannnbg
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click right-click pivoting of a selected IoC/selector (IP, domain, URL, hash, email, BTC address) to dozens of OSINT/intel engines.
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
costNote: Free, open-source browser extension (MIT). Some destination engines it links to may themselves require accounts/API keys.
opsec: passive
opsecNote: The extension itself only opens search URLs; it does not phone home (developer discloses no data collection). But each engine you launch (VirusTotal, Shodan, urlscan, Censys…) receives and may log the selector you pivoted — treat those queries as active toward the infrastructure, and use a clean browser/API keys as appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Open-source (github.com/ninoseki/mitaka) by Manabu Niseki, widely used in the DFIR/OSINT community; code is auditable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Mitaka
- ninoseki/mitaka
tags:
- browser-extension
- ioc-pivot
- threat-intel
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Mitaka (OSINT browser extension)

> A right-click OSINT multiplier: select an IP, domain, URL, hash, email or Bitcoin address on any page and instantly launch it against dozens of intel engines — huge time-saver during infrastructure/selector pivoting.

## When to use
You are reading a page (a breach report, a scam site, an email header, a wallet on a blockchain explorer) and want to pivot a selector without manually visiting each service. Mitaka extracts and "refangs" indicators (e.g. `hxxp://`, `1.1.1[.]1` → usable form) from selected text and offers a context-menu of searches: VirusTotal, Shodan, Censys, urlscan.io, SecurityTrails, blockchain explorers, and many more. Best for the domain/IP/infrastructure and financial-crypto phases of an investigation.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Mitaka from the Chrome Web Store (also available for Firefox) in a clean/sock-puppet browser profile.
2. On any page, select the text of a selector — an `ip-address`, `domain`, URL, file hash, `email`, or `crypto-wallet` (BTC/ETH) address.
3. Right-click → **Mitaka** → choose the engine (or "Search all" for a type) to open that selector on the chosen service.
4. Pivot: domain/IP results feed WHOIS, passive-DNS and Shodan follow-up; a wallet feeds blockchain-tracing; a hash feeds malware intel.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, URL, file hash, `email`, or `crypto-wallet` (selected on a page)
- **Out:** launches the selector on intel engines that return `domain`/`ip-address` infrastructure, reputation, passive DNS, hosting and threat context
- **Empty/negative result looks like:** the context menu offers no match (selection wasn't a recognised indicator), or the launched engine returns nothing — a clean/unknown indicator, not a Mitaka failure.

## Gotchas & OpSec
- Mitaka only *opens* searches; the intelligence and any rate limits/logins live on the destination engines.
- Launching a selector queries third-party services that log it — fine for infrastructure, but avoid pivoting a live target's private selectors from an attributable session.
- Keep the extension scoped to a dedicated OSINT browser profile to avoid cross-contaminating personal browsing.

## Overlaps ("do both")
- Pairs with dedicated WHOIS/passive-DNS, Shodan/Censys, urlscan and blockchain-explorer tools — Mitaka is the launcher; those are the depth. Also complements other right-click IoC extensions.

## Trust & verifiability
`trust: trusted` — open-source and auditable, from a well-known author; it adds no data of its own, so trust reduces to the engines you send selectors to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | matika |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain, email, crypto-wallet → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
