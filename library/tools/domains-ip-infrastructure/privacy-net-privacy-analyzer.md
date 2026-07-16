---
id: privacy-net-privacy-analyzer
name: Privacy.net Privacy Analyzer
description: Use when you want to see exactly what your own browser/IP leaks before running an investigation — returns your ip-address, browser fingerprint, and which sites you're logged into.
url: https://privacy.net/analyzer/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Auditing your own browser's exposure (IP, fingerprint, logged-in accounts) for OpSec before doing OSINT work.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- device-id
status: live
pricing: free
costNote: Free browser-based analyzer; no account or install.
opsec: passive
opsecNote: This tool inspects YOUR OWN browser session, not a target — run it on the research machine you plan to investigate from. It notably detects which of ~30 popular sites you are currently logged into, so run it in your sock-puppet browser to confirm you are NOT signed into personal accounts before starting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running privacy-education site (Privacy.net); the analyzer runs client-side tests illustrating real fingerprinting/leak vectors. Results reflect your current browser, not any remote database.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Privacy.net Analyzer
- browser privacy analyzer
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- opsec
- browser-fingerprint
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- privacy-net
---

# Privacy.net Privacy Analyzer

> A client-side audit of everything your own browser gives away — IP, fingerprint, autofill, and which sites you're logged into — so you can lock down OpSec before investigating.

## When to use
This is an **OpSec self-check**, not a target lookup. Run it on the exact browser/machine you will use for an investigation to confirm your research persona isn't leaking your real identity: it shows your `ip-address`, builds a browser fingerprint from your attributes, and — critically — detects which of ~30 popular sites you're currently signed into. Use it to verify your sock-puppet browser is clean (no personal logins, VPN engaged, fingerprint as generic as possible) before you touch a subject's footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the **research browser you plan to use**, open https://privacy.net/analyzer/.
2. Let it run its test categories: Basic Info, Autofill Leak, User Account Tests, Browser Capability, Fingerprint Analysis.
3. Read the results: your exposed IP/location, User-Agent, fingerprint uniqueness, and any logged-in accounts it detects.
4. Act on it: if it shows your real IP, personal logins, or a highly unique fingerprint, fix that (VPN, log out, hardened profile) before continuing OSINT work.

## Inputs → Outputs
- **In:** `ip-address` (implicitly — your own connection/browser; nothing is typed)
- **Out:** your `ip-address` + geolocation, `device-id`-style browser fingerprint, and a list of sites you're logged into
- **Empty/negative result looks like:** a clean run shows a generic fingerprint, VPN/proxy IP, and no detected logins — that is the desired OpSec state, not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none; it runs automatically on page load.
- OpSec: passive and inward-facing — it profiles you, not a target. That is the point; it never contacts your subject.
- The logged-in-account detection is a real leak vector; treat any account it finds as an identity risk in that browser.

## Overlaps ("do both")
- Pairs with `[[privacy-net]]` and any IP/DNS-leak checker — this covers browser-level exposure, those cover network-level; run both to fully clear a research setup.

## Trust & verifiability
`trust: community` — an established privacy-education site running transparent client-side tests. Its findings are directly observable in your own browser, so they're self-verifying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privacy-net-privacy-analyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
