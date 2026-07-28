---
id: tails-live-os
name: Tails Live OS
description: Use when you need a disposable, Tor-routed workstation for sensitive OSINT — returns an amnesic Debian environment that leaves no trace and hides your real IP.
url: https://tails.boum.org/
category: ai-analysis-automation
path:
- ai-analysis-automation
- virtual-machines
bestFor: Booting a throwaway, Tor-only operating system for high-risk research with zero local footprint.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Completely free and open source; only cost is a USB stick (8GB+) to write the image to.
opsec: active
opsecNote: This is investigator-side OpSec. All traffic is forced through Tor, so the sites you visit see a Tor exit node, not your real `ip-address`; the OS is amnesic and forgets everything on shutdown. Caveat — exiting to a login page or logging into personal accounts over Tor still deanonymises you; keep puppet identities strictly separate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Developed by the Tails project, which merged with the Tor Project in 2024; endorsed by the EFF and used by journalists and activists worldwide.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Tails
- The Amnesic Incognito Live System
- tails.net
tags:
- privacy-and-encryption-tools
- anonymity
- tor
- live-os
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Tails Live OS

> A portable, amnesic live operating system that routes everything through Tor and vanishes on shutdown — the standard clean-room for high-risk investigations.

## When to use
You are about to do research where your real `ip-address` or a persistent local footprint would be dangerous or compromising (adversarial targets, hostile networks, source protection). Boot Tails from a USB stick to get a fresh, Tor-only environment that keeps nothing between sessions.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the image from https://tails.net (redirected from tails.boum.org) and verify it with the provided signature/verification extension.
2. Write it to an 8GB+ USB stick (balenaEtcher, GNOME Disks, or the Tails installer).
3. Reboot the machine and boot from the USB (may require changing boot order / disabling Secure Boot).
4. Optionally enable **Persistent Storage** (an encrypted volume) if you must carry files or credentials between sessions — otherwise everything is wiped on shutdown.
5. Work inside the pre-hardened Tor Browser and bundled tools; shut down to erase all traces.

## Inputs → Outputs
- **In:** none (it is an operating system, not a lookup)
- **Out:** none (provides an anonymised environment, not selectors)
- **Empty/negative result looks like:** N/A — success is simply a working Tor-routed desktop; failure looks like the machine refusing to boot from USB (fix via BIOS/Secure Boot settings).

## Gotchas & OpSec
- Amnesia is the point: unless you enable encrypted Persistent Storage, nothing survives a reboot — save findings to an external, encrypted volume.
- Tor ≠ magic anonymity — logging into any account tied to your real identity inside Tails links that session to you.
- Some sites block or CAPTCHA Tor exit nodes heavily; expect friction.
- Verify the download signature; a tampered image defeats the entire purpose.

## Overlaps ("do both")
- Pairs with other virtual-machine / sandbox OSINT setups — Tails gives amnesic Tor routing on bare metal, while a disposable VM (e.g. a purpose-built analyst distro) gives a snapshot-revertible environment; choose Tails when you need to leave no trace on the host.

## Trust & verifiability
`trust: trusted` — flagship privacy OS, open source, reproducible builds, now part of the Tor Project; widely audited and endorsed by security professionals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tails-live-os |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
