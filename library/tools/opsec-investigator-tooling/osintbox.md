---
id: osintbox
name: osintBOX
description: Use when you want an OSINT-ready workstation fast — provisions a Parrot OS install with popular OSINT tools preinstalled (a setup script, not an investigative lookup).
url: https://github.com/Dimaslg/osintBOX
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Standing up an OSINT-ready Parrot OS VM/distro quickly by auto-installing a curated toolset.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free open-source provisioning script on GitHub; you run it on your own Parrot OS install/VM. No account.
opsec: passive
opsecNote: Building the workstation is offline/passive. Run it inside a dedicated, disposable VM (not your daily machine) and pair with a VPN/sock-puppet setup before doing live investigation from it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community provisioning script (Dimaslg); audit it before running, as it installs many third-party tools from the internet.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- osintBOX
tags:
- distro
- provisioning
- parrot-os
- setup
source: gh-topic-osint-framework
lastVerified: '2026-08-04'
enrichment: full
---

# osintBOX

> A setup script that turns a Parrot OS box into an OSINT-ready workstation by auto-installing a curated toolset — infrastructure, not an investigative tool itself.

## When to use
You are building a dedicated investigation environment and want the common OSINT tools installed in one pass rather than by hand. Use it once to provision a disposable VM; it does not search or return anything about a subject.

## How to use it (`bestInteractionPattern`: cli)
1. Spin up a fresh Parrot OS VM (dedicated to investigation, snapshot-able).
2. Clone https://github.com/Dimaslg/osintBOX and **read the script** to see what it installs and from where.
3. Run the provisioning script; it fetches and installs the bundled OSINT tools.
4. Snapshot the clean VM, then configure VPN/sock-puppet networking before any live work.

## Inputs → Outputs
- **In:** none (a provisioning action, not a selector)
- **Out:** a Parrot OS workstation with OSINT tools installed
- **Empty/negative result looks like:** install failures for individual tools (upstream repos moved/removed) — expected for an older script; install the failed tools manually.

## Gotchas & OpSec
- Human-in-the-loop: none, but you need a Parrot OS host/VM and should audit the script.
- OpSec: provisioning is passive; the tools you later run from the box are what carry OpSec risk — segregate the VM and use a VPN/sock puppet.
- Older provisioning scripts bit-rot as upstream tools change — expect some manual fixups.

## Overlaps ("do both")
- Similar in spirit to other OSINT distro/toolkit provisioners (Tsurugi, Buscador-style setups): pick one to build the workstation; they overlap, so you do not need several.

## Trust & verifiability
`trust: community` — a community setup script; safe enough for a disposable VM after you audit it, but it pulls many third-party tools, so isolate it from your main system.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintbox |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
