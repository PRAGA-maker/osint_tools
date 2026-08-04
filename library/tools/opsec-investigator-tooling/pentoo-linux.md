---
id: pentoo-linux
name: Pentoo Linux
description: Use when you want a ready-made, isolated OS for security/OSINT work — returns a bootable Gentoo-based live environment preloaded with pentesting and recon tools.
url: https://www.pentoo.ch
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A bootable live-USB security distro giving you a clean, isolated environment for recon and pentesting.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; download the ISO and run as a live USB/CD or install it.
opsec: passive
opsecNote: Running from a live USB gives you a disposable, non-persistent environment that doesn't touch your host disk — an OpSec win for keeping investigative work isolated. It is a toolbox, not a network query; OpSec depends on how you configure networking (route through Tor/VPN as needed).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-standing, actively maintained open-source security distribution based on Gentoo Linux, with an established community (GitHub, Discord/IRC); reputable within the security field.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- pentoo
- pentoo linux
tags:
- Sock Puppets
- linux-distro
- pentesting
- opsec
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Pentoo Linux

> A Gentoo-based live security distro: boot it from a USB to get a clean, isolated, tool-laden environment for reconnaissance and penetration testing without touching your host machine.

## When to use
You want a separate, disposable operating environment for investigative or security work — one that isn't your day-to-day machine and leaves no traces on your host disk. Pentoo is a live CD/USB (32/64-bit, installable) built on Gentoo and preloaded with penetration-testing and reconnaissance tooling, giving you an isolated base for OSINT/security tasks and a way to compartmentalize a sensitive investigation.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the current Pentoo ISO from https://www.pentoo.ch.
2. Write it to a USB stick (e.g. with `dd`/Rufus/Etcher) and boot from it — or install it in a VM for a persistent lab.
3. Boot into the live environment; it runs from RAM/USB, so nothing is written to the host by default.
4. Configure networking for your OpSec posture (route through Tor/VPN before doing attributable work), then use the bundled recon/security tools.
5. Pivot: use the isolated environment to run other command-line OSINT tools safely; discard the session when done for a clean slate.

## Inputs → Outputs
- **In:** none (it's an operating environment/toolkit, not a lookup)
- **Out:** a working, isolated security OS with recon/pentest tooling
- **Empty/negative result looks like:** not applicable — verify the download's checksum/signature; a failed boot usually means a bad write or a UEFI/secure-boot setting to adjust.

## Gotchas & OpSec
- It's a *platform*, not a data source — it doesn't find anything itself; it hosts the tools that do.
- Live/non-persistent by default is the OpSec benefit; if you install it, you take on persistence and its risks.
- Networking is yours to configure — Pentoo doesn't anonymize traffic for you unless you set that up.
- Verify the ISO signature before booting.

## Overlaps ("do both")
- Complements Trace Labs' OSINT VM and Kali/other security distros — Pentoo is the Gentoo-based option; pick whichever bundles the toolset you need, and keep investigative work off your daily-driver OS regardless.

## Trust & verifiability
`trust: trusted` — an established, actively maintained open-source distro with a public repo and community; reputable, provided you download from the official site and verify the image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pentoo-linux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
