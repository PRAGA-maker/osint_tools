---
id: blackarch-linux
name: BlackArch Linux
description: Use when you want a ready-made investigation workstation — returns an Arch-based distro pre-loaded with 2800+ security/OSINT tools for recon, forensics, and analysis.
url: https://www.blackarch.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A single Linux environment pre-packaged with thousands of security and OSINT tools.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; download the ISO or add the BlackArch repo to an existing Arch install at no cost.
opsec: passive
opsecNote: "BlackArch is just the platform — installing it and its tools is passive and reveals nothing to any target. OpSec depends entirely on *how* you use the tools inside it: run investigations from a VM/live-USB, route traffic through a VPN/Tor, and keep separate instances per identity. Some bundled tools are active (they touch targets) — the distro doesn't anonymize you by itself."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A well-established Arch-based penetration-testing distribution with a large curated tool repository and public packaging; reputable, though (as with any pentest distro) you should vet individual bundled tools before use.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- BlackArch
- blackarch.org
tags:
- Virtual Machines/Linux distributions
- pentest-distro
- osint-workstation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# BlackArch Linux

> An Arch-based security distribution bundling 2800+ tools — an off-the-shelf workstation for recon, forensics, and OSINT without hand-installing each tool.

## When to use
You want a dedicated, disposable investigation environment where the common OSINT/recon tools (subdomain enumerators, metadata extractors, scanners, forensics utilities) are already installed and updated. Use it as a VM or live-USB per case/identity so tooling stays isolated from your host. It's infrastructure for doing OSINT, not a data source, so it produces no selectors and rates low for missing-persons relevance directly.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the ISO from https://www.blackarch.org (or add the BlackArch repository to an existing Arch install).
2. Run it as a **VM or live-USB**, not on your daily host, so investigations stay compartmentalized.
3. Install tool groups as needed (`pacman -S blackarch-<category>`, e.g. `blackarch-recon`).
4. Configure networking first — VPN/Tor and a sock-puppet posture — before running any tool that touches a target.
5. Snapshot the VM per identity/case; discard when done to avoid cross-contamination.

## Inputs → Outputs
- **In:** — (a tooling environment, not a query)
- **Out:** — (whatever the tools you run inside it produce)
- **Empty/negative result looks like:** n/a — BlackArch is the platform; "results" come from the individual tools, not the distro.

## Gotchas & OpSec
- The distro is **not** anonymity software — your IP/fingerprint still apply; add VPN/Tor and run from a VM/live-USB.
- Many bundled tools are **active** (they probe/contact targets) — know which before pointing them at a live subject.
- Rolling-release Arch base can break on updates; snapshot VMs before major upgrades.

## Overlaps ("do both")
- An alternative to Kali/Tsurugi-style OSINT distros — pick one workstation base, then run the specific tools (e.g. [[owasp-maryam]], [[metafinder]], [[urlcrazy]]) inside it. The distro is the shell; those are the payload.

## Trust & verifiability
`trust: trusted` — a reputable, long-running pentest distribution with public packaging; it's a reliable platform, but the standard advice applies — vet and understand each bundled tool before you run it against anything.
