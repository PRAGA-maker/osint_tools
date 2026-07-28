---
id: dracos-linux
name: Dracos Linux
description: Use when you want a lightweight, CLI-focused penetration-testing/OSINT Linux distro to run recon tools from a clean, disposable environment — a full investigation OS.
url: https://dracos-linux.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A lightweight Debian-based pentest/forensics distro for running recon and analysis tools in a compartmentalised environment.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPLv3); download the ISO and run in a VM or on hardware. No account.
opsec: passive
opsecNote: The distro is your working environment, not a data source. Run it in a VM/live-USB dedicated to a case so tooling and artefacts stay compartmentalised, and route it through a VPN/Tor. As a smaller community distro, vet the ISO checksum on download.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: An Indonesian open-source pentest distro (screetsec/DracOS), actively maintained but far smaller and less audited than Kali/Parrot; verify the ISO and treat bundled tools with normal caution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DracOS
- Dracos GNU/Linux
tags:
- linux-distro
- pentest
- investigator-tooling
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Dracos Linux

> A lightweight, terminal-first penetration-testing Linux distribution — a self-contained environment preloaded with recon, forensics and analysis tools for running an investigation off your daily machine.

## When to use
You want a dedicated, disposable operating environment to run OSINT/pentest tooling from — separate from your personal machine, easy to snapshot and reset per case. Dracos bundles information-gathering, forensics, malware-analysis and reverse-engineering tools in a lightweight Debian-based distro that boots fast on low-end hardware or in a VM. Reach for it (or an alternative like Kali/Parrot) when you want compartmentalisation and a ready toolkit rather than installing tools piecemeal.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the ISO from https://dracos-linux.org and verify its checksum.
2. Run it as a live-USB or in a VM (snapshot a clean state per investigation).
3. Use the bundled information-gathering/forensics tools; add your own as needed.
4. Route the environment through a VPN/Tor and keep case artefacts inside the compartment.
5. Reset to the clean snapshot between cases so nothing bleeds across investigations.

## Inputs → Outputs
- **In:** n/a — it's the environment you run other tools in, not a selector-in lookup.
- **Out:** n/a — the tools you run inside it produce the intel.
- **Empty/negative result looks like:** n/a. Judge it as a workspace/toolkit, not a data source.

## Gotchas & OpSec
- OpSec: it's your working environment — compartmentalise per case (VM/snapshot), and route through VPN/Tor.
- Smaller, less-audited than Kali/Parrot: verify the ISO checksum and don't assume every bundled tool is current or safe.
- It finds nothing on its own; value is convenience and compartmentalisation, not capability you couldn't assemble elsewhere.

## Overlaps ("do both")
- Interchangeable with Kali/Parrot and other pentest distros — pick one as your case environment; Dracos's edge is being lightweight. Run your actual OSINT tools inside whichever you choose.

## Trust & verifiability
`trust: community` — an actively-maintained but niche open-source distro; verify downloads and treat it like any community security tooling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dracos-linux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
