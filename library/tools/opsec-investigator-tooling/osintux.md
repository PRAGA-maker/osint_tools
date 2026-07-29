---
id: osintux
name: Osintux
description: Use when you want a preconfigured Spanish-language Linux environment for OSINT work — returns a Debian-based distro bundling investigation and anonymity tools.
url: https://www.osintux.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-made, Spanish-language OSINT Linux distribution with investigation and privacy tools preinstalled — an investigator workstation, especially for Spanish-speaking analysts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GNU GPL); downloaded as an image and run/installed. No account or cost.
opsec: passive
opsecNote: A defensive/tooling environment for the investigator — it runs no queries itself. Run it live/in a VM and route through a VPN/Tor for a clean, separated investigation environment. Verify the download image before booting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Community project (Spanish OSINT community, active as of 2024); useful curated toolset, but a smaller/independent distro — verify the image and keep tools updated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- septor-linux
- tracelabs-osint-vm
- virtualbox
aliases:
- Osintux
- OSINTUX
- osintux.org
tags:
- Virtual Machines/Linux distributions
- osint-workstation
- spanish
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Osintux

> A Spanish-language, Debian-based Linux distribution built for open-source intelligence — a ready-to-go investigator workstation with OSINT and privacy tools preinstalled.

## When to use
You want a curated, disposable OSINT environment without assembling tools yourself — and, for Spanish-speaking analysts, one in Castellano. Boot Osintux (ideally live or in a VM), and you get a desktop with investigation and anonymity utilities ready. Like other OSINT distros, it finds nothing on its own — it's the *environment* you run investigations from, keeping them off your host.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the image from https://www.osintux.org/ (documentation is in Spanish, including a guide to making a bootable USB).
2. Verify the image's checksum, then run it live from USB or as a VM guest (e.g. in `[[virtualbox]]`).
3. Route traffic through a VPN/Tor for separation, and use the preinstalled OSINT/privacy tools for your workup.
4. Work from the isolated environment; for maximum hygiene run live (no persistence) and discard the session.
5. Pivot: use the clean workstation to run active-recon tools without exposing your real host/IP.

## Inputs → Outputs
- **In:** none — it's an operating system, not a query tool.
- **Out:** none per-subject — a ready-configured OSINT workstation.
- **Empty/negative result looks like:** N/A — success is a booted, tool-equipped desktop. Failure is usually a boot/VM or image-integrity issue.

## Gotchas & OpSec
- Human-in-the-loop: none for use; you handle image verification and boot media.
- OpSec: **defensive** — separates the investigator from the host. It does not anonymise you by itself; add a VPN/Tor and keep real and sock-puppet identities apart.
- Smaller independent distro: update the bundled tools (they can age) and verify the download image before trusting it.
- Documentation is primarily Spanish — a plus for Spanish speakers, a barrier otherwise.

## Overlaps ("do both")
- Overlaps with `[[septor-linux]]` and `[[tracelabs-osint-vm]]` — same "preconfigured OSINT/anonymity environment" niche; pick by language/toolset preference, or run any of them as a `[[virtualbox]]` guest.

## Trust & verifiability
`trust: community` — a genuine, actively maintained community distro. Reliable as a convenience toolset, but as with any smaller distro, verify the image and don't assume the bundled tools are current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
