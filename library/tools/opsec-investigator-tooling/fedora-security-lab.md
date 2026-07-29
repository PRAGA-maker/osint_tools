---
id: fedora-security-lab
name: Fedora Security Lab
description: Use when you want a ready-made security/forensics workstation — returns a live-bootable Fedora spin preloaded with pentesting and forensic tools.
url: https://labs.fedoraproject.org/security/download/index.html
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A safe, disposable live environment preloaded with security-testing and forensic tooling for investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source Fedora spin; download the ISO and boot from USB/VM. No account.
opsec: passive
opsecNote: The distro itself contacts no target — it is a toolkit you run locally. Booting it live (from USB, non-persistent) gives a clean, disposable workstation that leaves no trace on the host, which is good OpSec for sensitive investigations. Any active reconnaissance you then perform with its tools carries that tool's own footprint; route through a VPN/proxy as appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: An official spin of the Fedora Project (Red Hat-sponsored); reputable, signed ISOs. It bundles established open-source security tools rather than being a novel data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- kali-linux
- tails
aliases:
- Fedora Security Spin
tags:
- linux-distro
- pentesting
- forensics
- toolkit
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Fedora Security Lab

> An official Fedora "spin" that boots into a clean desktop preloaded with security-testing and forensic tools — a ready-made investigator workstation you can run live and disposable.

## When to use
When you want a trusted, self-contained environment with the security/forensic toolset already installed and configured, rather than assembling tools on your daily machine. Boot it live and non-persistent for a clean-room session that leaves nothing on the host — good hygiene for sensitive OSINT and forensic work.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the ISO from https://labs.fedoraproject.org/security/download/index.html and verify its checksum/signature.
2. Write it to a USB (e.g. with Fedora Media Writer) or attach it to a VM.
3. Boot **live** (non-persistent) for a disposable session, or install to disk/VM for a persistent lab.
4. Use the preloaded tools (network analysis, password/forensics, web testing) for your task; the spin's menu groups them by function.
5. Pivot: results from tools run here feed the rest of your OSINT workflow; the clean environment is the enabler, not the data source.

## Inputs → Outputs
- **In:** none (an environment, not a selector-driven lookup)
- **Out:** a running workstation with security/forensic tooling ready to use
- **Empty/negative result looks like:** n/a — it is a platform. If a specific tool you need isn't bundled, install it via `dnf` or use a more specialised distro.

## Gotchas & OpSec
- It is a toolkit distribution, not an investigation service — value is a clean, curated environment.
- Live/non-persistent boot maximises host-side OpSec; a persistent install trades that for convenience.
- Bundled tool versions track the release; update after first boot for current signatures/definitions.

## Overlaps ("do both")
- Compare with `[[kali-linux]]` (the best-known offensive-security distro, broader tool set) and `[[tails]]` (amnesic, anonymity-focused). Choose Fedora Security Lab for a Fedora-based security/forensics workstation; Kali for the widest pentest arsenal; Tails when anonymity is the priority.

## Trust & verifiability
`trust: trusted` — an official, signed Fedora Project spin. Verify the ISO signature before use; the tools it ships are mainstream open-source utilities you can validate independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fedora-security-lab |
