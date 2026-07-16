---
id: csi-linux
name: CSI Linux
description: Use when you want a pre-built, isolated OSINT/forensics workstation — returns a ready-to-run Linux VM bundling investigation, dark-web, and forensics tooling.
url: https://csilinux.com/csi-linux-downloads/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-made virtual-machine investigation platform preloaded with OSINT, dark-web, and digital-forensics tools, kept separate from your host.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The base CSI Linux VM is a free download; the project also sells paid training, certifications, and some premium add-on tooling. The core platform is free to run.
opsec: passive
opsecNote: Its whole point is OpSec — run investigations inside a disposable VM so browsing artifacts, cookies, and downloads never touch your real host, and route traffic through VPN/Tor. Snapshot before an op and roll back after. Downloading the ISO is passive; keep the download itself under a persona if that matters to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: An established, widely-referenced investigation-focused Linux distribution; download only from the official csilinux.com and verify checksums, as with any security VM.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- CSI Linux distro
tags:
- vm
- linux-distro
- forensics
- investigator-platform
source: ultimate-osint
lastVerified: '2026-07-16'
enrichment: full
---

# CSI Linux

> A pre-built investigation workstation — a Linux VM that bundles OSINT, dark-web, and forensics tooling so you can run casework in an isolated, disposable environment instead of on your daily machine.

## When to use
You want a clean, compartmentalized platform for investigative work: many tools preinstalled, network routing (VPN/Tor) baked in, and everything sandboxed away from your personal system. Reach for CSI Linux when setting up an OSINT/forensics environment from scratch would take too long, or when OpSec demands that investigation artifacts never land on your host. It's infrastructure, not a per-selector lookup.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the CSI Linux VM/appliance from the official downloads page and verify the checksum.
2. Import it into VirtualBox/VMware (or run per the project's install guide).
3. Take a clean snapshot before starting a case so you can roll back afterward.
4. Configure networking (VPN and/or Tor) before touching any target, and use sock-puppet accounts inside the VM.
5. Run your investigation using the bundled tools; when done, export findings and revert the snapshot to wipe artifacts.
6. Pivot: CSI Linux is the workbench — the individual OSINT tools you run inside it are what produce selectors.

## Inputs → Outputs
- **In:** none (it's a platform, not a query tool)
- **Out:** an isolated investigation environment; outputs come from the tools you run within it
- **Empty/negative result looks like:** N/A — success is a working, isolated VM; failure is a broken import or unverified/corrupt download (re-download from the official source and re-check the hash).

## Gotchas & OpSec
- Only download from the official csilinux.com and verify integrity — a tampered investigation VM would be a disaster.
- It's heavyweight; a targeted toolset (or a hardened Tails/Whonix for anonymity) may suit some tasks better.
- Keep it updated — bundled tools go stale between releases.
- OpSec: snapshot/rollback and route through VPN/Tor; never run a live target from your host.

## Overlaps ("do both")
- Complements anonymity-focused distros (Tails, Whonix) — CSI Linux is a full investigation toolkit, whereas those prioritize leaving no trace; some investigators run OSINT in CSI Linux behind a Whonix gateway.

## Trust & verifiability
`trust: trusted` — a well-known, actively maintained investigation distro; the platform is reputable, but its trust rests on you downloading the genuine image and verifying it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | csi-linux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
