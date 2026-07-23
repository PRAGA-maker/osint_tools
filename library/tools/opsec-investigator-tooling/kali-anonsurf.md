---
id: kali-anonsurf
name: Kali Anonsurf
description: Use for investigator opsec — routes your entire system's network traffic through Tor at the OS level and adds anti-forensic helpers, so all tools inherit anonymized egress.
url: https://github.com/Und3rf10w/kali-anonsurf
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: System-wide Tor routing of all investigator traffic, plus RAM-wipe/anti-forensic helpers.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: This is your own opsec layer, not a query tool. It forces ALL system traffic through Tor via iptables, so every tool you run egresses from Tor exit nodes — but that means active investigative tools (scanners, scrapers) now originate from shared, often-flagged Tor exits, which many sites block or treat as suspicious. Tor also breaks or slows some tools. Verify your real IP is masked before relying on it, and know that Tor anonymity ≠ invisibility.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A port of ParrotSec's anonsurf to Kali/Debian (GPL-3.0, actively maintained); shipped/used in the Trace Labs OSINT VM.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- anonsurf
- Und3rf10w/kali-anonsurf
tags:
- anonymity
- tor
- opsec
source: tracelabs-repos
lastVerified: '2026-07-23'
enrichment: full
---

# Kali Anonsurf

> A system-wide anonymizer — flip it on and every bit of your machine's network traffic is forced through Tor via iptables, with RAM-wiping (Pandora) and i2p helpers for anti-forensics.

## When to use
Investigator opsec, not a lookup. Reach for it when you want *all* traffic from your investigation machine to egress via Tor without configuring each tool individually — a blanket network-anonymity layer for browsing and OSINT work. It's part of the Trace Labs search-party VM toolset. Best paired with the understanding that it masks your origin IP, not your behavior.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/Und3rf10w/kali-anonsurf (or `apt install anonsurf` on Trace Labs/Parrot-derived systems).
2. Start it: `anonsurf start` — traffic is now routed through Tor system-wide.
3. Confirm with `anonsurf status` / check your apparent IP (e.g. via a "what's my IP" service) to verify you're on a Tor exit.
4. Use `anonsurf change` to get a new circuit/IP, `anonsurf stop` to restore normal routing, and Pandora to wipe RAM when finishing.

## Inputs → Outputs
- **In:** none (a system opsec toggle — no OSINT selector)
- **Out:** all traffic anonymized via Tor (an opsec state, not subject data)
- **Empty/negative result looks like:** your real IP still showing after `start` — a misconfiguration or leak; stop and troubleshoot before doing anything sensitive.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **active egress via Tor** — great for hiding your origin, but Tor exit IPs are shared and widely flagged/blocked, so active scanners/scrapers may fail or look hostile, and some sites block Tor entirely. Tor hides the network path, not sloppy behavior (logins, unique accounts) that can deanonymize you.
- DNS/app leaks are possible; verify masking before trusting it, and expect slower connections.

## Overlaps ("do both")
- Alternative to a VPN or the Whonix/Tails approach and complementary to a sock-puppet browser — use anonsurf for system-wide Tor egress, and layer disciplined account/browser separation on top (Tor alone isn't enough).

## Trust & verifiability
`trust: trusted` — an actively-maintained GPL-3.0 port of ParrotSec's well-known anonsurf, used in the Trace Labs VM. The tool is reliable; the responsibility for verifying no leaks and using it appropriately (Tor's limits, exit-node blocking) is yours.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kali-anonsurf |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
