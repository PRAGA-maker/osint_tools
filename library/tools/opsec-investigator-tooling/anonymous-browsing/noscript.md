---
id: noscript
name: NoScript
description: Use when you want to harden your investigator browser — a FOSS extension that blocks JavaScript by default, cutting fingerprinting/tracking and XSS risk during OSINT.
url: https://noscript.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Blocking scripts by default to reduce browser fingerprinting and active tracking while investigating.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (FOSS), donation-supported; no account.
opsec: passive
opsecNote: This is investigator-side hardening, not a lookup. By blocking JavaScript except on sites you whitelist, it shrinks the fingerprinting and beacon surface a target's site can use to profile your visit. Some OSINT tools need JS to function — whitelist them per-site and temporarily, then revoke.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Long-established, widely-audited FOSS extension (Giorgio Maone), bundled in the Tor Browser; a reputable, mainstream security tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- NoScript Security Suite
tags:
- opsec
- anonymous-browsing
- browser-hardening
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# NoScript

> A default-deny JavaScript blocker for the investigator's browser — it reduces how much a target site can fingerprint, track, or attack you, one whitelisted site at a time.

## When to use
You're browsing sites that could profile or de-anonymize you — a subject's own website, a sketchy forum, a link of unknown provenance — and you want to minimize the active code that runs. NoScript blocks JavaScript/WebGL/other active content by default, so trackers, canvas-fingerprinting scripts, and drive-by XSS don't execute unless you explicitly allow them. It's OpSec infrastructure, not a data source.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install NoScript from https://noscript.net/ into your dedicated OSINT browser (Firefox/Chrome/Edge/Brave; it also ships in Tor Browser).
2. Browse with scripts blocked by default — pages render as static HTML where possible.
3. When a tool genuinely needs JS, use the toolbar to grant *temporary*, per-site permission (Temp Trusted), then reload.
4. Revoke permissions when done; keep the default-deny posture for untrusted sites.
5. Pair with a compartmentalized profile/VPN so script-blocking complements network-level anonymity.

## Inputs → Outputs
- **In:** none — it's a browser hardening layer, not a query tool
- **Out:** none — it changes your exposure, not your findings
- **Empty/negative result looks like:** N/A; a "broken" page usually means a required script is blocked — grant it temporarily if you trust the site.

## Gotchas & OpSec
- Many modern OSINT tools are JS-heavy and will appear broken until whitelisted — expect to manage per-site allows.
- Blocking scripts reduces but does not eliminate fingerprinting (IP, headers, TLS still leak) — combine with a VPN/Tor and a clean profile.
- OpSec: passive and defensive; it lowers *your* footprint and never touches the subject.

## Overlaps ("do both")
- Pairs with a VPN/Tor and a containerized browser profile — NoScript handles the active-content/fingerprint layer while those handle the network-identity layer; use them together for a hardened investigator setup.

## Trust & verifiability
`trust: trusted` — a mature, widely-reviewed FOSS project bundled in Tor Browser; its behavior is transparent and well-documented.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | noscript |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
