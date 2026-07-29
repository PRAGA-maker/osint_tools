---
id: huron-osint
name: Huron OSINT (OsintDistro)
description: Use when you want a pre-built OSINT virtual machine bundling Maltego, Recon-ng, Shodan and metadata tools — a ready-made investigation environment, not a per-selector lookup.
url: https://github.com/HuronOsint/OsintDistro
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-to-run OSINT Linux VM (OVA) preloaded with common investigation tools and a Tor/tracker-blocking browser setup.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free download (VM image hosted on Mega, linked from the GitHub repo); no license fee.
opsec: passive
opsecNote: A self-contained VM is itself an OpSec win — run investigations in a disposable, isolated machine separated from your host identity. But an unmaintained image ships outdated, unpatched software; sandbox it, keep snapshots, and update the tools before trusting it with sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A small community project (HuronOsint/OsintDistro, ~60 stars) distributed as an OVA via Mega, largely at v1.0 with minimal recent commits — verify the image and its bundled tools before use.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OsintDistro
- Huron distro
tags:
- Virtual Machines/Linux distributions
- osint-vm
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Huron OSINT (OsintDistro)

> A pre-built OSINT virtual machine (Spanish-origin) bundling Maltego, Recon-ng, Shodan tooling, ExifTool and a privacy browser stack — an investigation environment to boot, not a lookup service.

## When to use
You want a disposable, isolated workstation with common OSINT tools already installed rather than assembling one yourself, and prefer a downloadable VM over building on Kali/Tsurugi/Trace Labs. Huron/OsintDistro gives you Maltego, Recon-ng, Shodan integration, social-media tooling, image-metadata (ExifTool), Tor Browser, and tracking blockers in one image. It returns no selectors of its own — it's the container for tools that do.

## How to use it (`bestInteractionPattern`: desktop-app)
1. From the GitHub repo, follow the download link (the OVA is hosted on Mega).
2. Import the `.ova` into VirtualBox/VMware; take a clean snapshot before first use.
3. Boot into the VM, connect through a sock-puppet VPN/Tor, and update the bundled tools (they may be stale).
4. Run your investigation inside the VM; revert to the clean snapshot afterward to discard traces.

## Inputs → Outputs
- **In:** none (it is an environment)
- **Out:** none directly — it hosts tools (Maltego, Recon-ng, Shodan, ExifTool) that produce the selectors
- **Empty/negative result looks like:** N/A — but a broken/outdated import or dead Mega link is the failure mode; fall back to a maintained distro (Kali, Tsurugi) if so.

## Gotchas & OpSec
- **Unmaintained (~v1.0):** bundled tools and OS packages are likely outdated and unpatched — update before serious use, and don't trust the image blindly.
- Third-party OVA from a file host: verify integrity and scan before importing; run only in a sandboxed hypervisor, never on bare host.
- **Passive** by nature (a workstation), but everything you run inside it inherits your egress — route through sock-puppet networking.

## Overlaps ("do both")
- An alternative to maintained OSINT distros; if Huron is stale, prefer a current distro and install Maltego/Recon-ng/ExifTool yourself. Use the VM as the isolation layer for the individual tools catalogued elsewhere.

## Trust & verifiability
`trust: community` — a small, lightly maintained community project distributed via an off-GitHub file host; usable but verify the image and update its tooling before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | huron-osint |
