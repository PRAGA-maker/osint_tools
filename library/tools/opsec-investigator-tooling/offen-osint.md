---
id: offen-osint
name: OffenOsint
description: Use when you want a ready-made virtual machine preloaded with 50+ OSINT and recon tools instead of installing each one — returns a working investigation environment (name, username, domain, ip-address leads via its bundled tools).
url: https://github.com/Double2Sky/OffenOsint
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A downloadable Kali-based VM image pre-configured with a full OSINT/recon toolchain and Tor/VPN plumbing.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
- ip-address
status: live
pricing: free
costNote: Free .OVA download; built on Kali Linux and other FOSS tools. Needs VirtualBox and disk space to run.
opsec: passive
opsecNote: The VM ships with Tor/VPN plumbing so you can route collection through an anonymizing layer — configure and verify it BEFORE running any active tool. The image itself is inert; opsec depends on how you use the bundled tools (some, like port scanners, are active and touch targets). Download the OVA from the official repo and verify integrity before importing.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Community project (Double2Sky) bundling well-known FOSS tools; it repackages trusted upstreams but is itself an individual's beta release — inspect what it installs before trusting it with sensitive work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- OffenOsint
- Offensive OSINT VM
tags:
- Virtual Machines/Linux distributions
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# OffenOsint

> A pre-built Kali-based virtual machine that saves you from installing a whole OSINT toolchain by hand — theHarvester, Amass, Spiderfoot, Recon-ng, Sherlock, EyeWitness and 50+ more, ready to run.

## When to use
You want an isolated, disposable investigation workstation with the common OSINT/recon stack already installed and Tor/VPN wiring in place — rather than spending an afternoon apt-installing and configuring tools on a fresh box. Good for spinning up a clean, attributable-free environment per case. This is infrastructure, not a lookup: the OSINT payload comes from the tools it bundles.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install VirtualBox on your host.
2. Download the `.OVA` image from the official repo (https://github.com/Double2Sky/OffenOsint) and verify its checksum.
3. **File → Import Appliance** in VirtualBox and boot the VM.
4. Configure and confirm the VPN/Tor routing before any active collection, then use the bundled tools (theHarvester for `email`/`name`, Amass for `domain`, Sherlock for `username`, Spiderfoot for broad pivots).
5. Snapshot a clean state so you can roll back per case; treat the VM as disposable.

## Inputs → Outputs
- **In:** whatever the bundled tools take — a `name`, `username`, `domain`, or `email`
- **Out:** the union of those tools' outputs — `social-profile` matches, `domain`/subdomain maps, `ip-address` and harvested `email` leads
- **Empty/negative result looks like:** not applicable at the VM level — empty results come from the individual tools; a failed import usually means a VirtualBox version mismatch.

## Gotchas & OpSec
- Human-in-the-loop: you must review and configure the VM (VPN/Tor, tool API keys) before serious use — a beta community image should be inspected, not blindly trusted.
- OpSec: the image is passive, but the tools inside range from passive (theHarvester) to active (port scanners); know which you're running. Route through the built-in anonymizer and never leak your real IP during active recon.
- Kali-based images go stale; update packages after first boot.

## Overlaps ("do both")
- Complements every individual CLI tool in this library — OffenOsint is the container that runs them; use the library's tool-specific skills for how to drive each bundled utility.

## Trust & verifiability
`trust: community` — repackages trusted FOSS upstreams, but is one contributor's beta appliance; verify the download and audit what it installs before using it for sensitive investigations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | offen-osint |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, username, domain → social-profile, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
