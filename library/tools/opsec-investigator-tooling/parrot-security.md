---
id: parrot-security
name: Parrot Security
description: Use when you need a ready-made pentest/OSINT Linux workstation — returns a Debian-based distro pre-loaded with investigation and security tooling.
url: https://twitter.com/ParrotSec
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A privacy-hardened Linux distribution pre-packed with OSINT, forensics, and pentest tools.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; download the ISO at parrotsec.org at no cost.
opsec: active
opsecNote: Investigator-side tooling. Parrot bundles anonymity features (AnonSurf to route traffic over Tor) and sandboxed apps, but running it does not make you anonymous by default — configure AnonSurf/VPN before touching targets, and keep the OSINT work in a dedicated puppet environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Well-established security distribution maintained by the Parrot Project (Parrot OS / Parrot Security Edition); an actively-developed Kali alternative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- global-terriorism-database
- murph-live
- tormap
- twitter
- twitter-advanced-search
- twitter-analytics
aliases:
- ParrotSec
- Parrot OS
- Parrot Security OS
tags:
- Virtual Machines/Linux distributions
- pentest-distro
- linux
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Parrot Security

> A Debian-based security distribution — a Kali-style workstation pre-loaded with pentest, forensics, and OSINT tooling plus built-in anonymity options.

## When to use
You want a purpose-built environment for investigations rather than installing dozens of tools onto your daily machine. Parrot Security Edition ships with recon/OSINT utilities, forensics kits, and AnonSurf (system-wide Tor routing) preconfigured — a clean, disposable base for a case.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the ISO from the official site, **parrotsec.org** (the harvested URL points to the project's Twitter/X account, @ParrotSec — go to the project site for the actual download).
2. Verify the ISO signature, then run it in a VM (VirtualBox/VMware/QEMU) or on a USB for isolation.
3. Take a clean VM snapshot before each case so you can revert and leave no cross-case residue.
4. Enable AnonSurf or a VPN before any active collection; keep puppet browsers/accounts separate.
5. Use the bundled recon tooling; export findings to an encrypted external volume.

## Inputs → Outputs
- **In:** none (it is an operating system)
- **Out:** none (an equipped, isolatable workstation — not subject data)
- **Empty/negative result looks like:** N/A — success is a working, tooled VM; failure is boot/driver issues, fixed via VM settings.

## Gotchas & OpSec
- The distro is not anonymity by default — you must turn on AnonSurf/VPN; a fresh Parrot install still leaks your real IP to sites otherwise.
- The seeded URL is a Twitter/X handle, not a download — use parrotsec.org.
- Heavy toolset; run in a VM/snapshot so a case leaves no trace on your host.
- Overlaps heavily with Kali — pick one; running OSINT from a general distro + curated tools is also fine.

## Overlaps ("do both")
- Pairs with [[tails-live-os]] and disposable VMs — Parrot is the tooled, revertible workstation, while Tails is the amnesic Tor-only browsing environment; use Tails for high-risk browsing and Parrot for heavier tooling.

## Trust & verifiability
`trust: trusted` — a mature, widely-used open-source security distribution with reproducible releases and an active maintainer community.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | parrot-security |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
