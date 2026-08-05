---
id: osint-vm-inforensics
name: OSINT VM (Inforensics)
description: Use when you want a pre-built, isolated investigation environment — a VM preloaded with OSINT tools (and AI agents) — so collection runs off your host and off your real identity; supports the whole workflow rather than returning selectors.
url: https://github.com/Inforensics/osint-vm
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-made, disposable virtual machine bundling OSINT tooling and AI agents for investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source project on GitHub; you supply the host and a hypervisor (VirtualBox/VMware/etc.).
opsec: passive
opsecNote: The whole point is OpSec — running collection inside a disposable VM keeps browser fingerprints, cookies, and downloaded files off your real machine and lets you snapshot/roll back after touching risky sites. It does NOT mask your IP by itself; route the VM's traffic through a VPN/Tor. Treat any bundled AI agents' data handling with care (don't feed them sensitive case data that leaves the VM).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: A community/vendor (Inforensics) GitHub project; inspect the build scripts and pinned tool versions before trusting it for real casework.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Inforensics OSINT VM
- osint-vm
tags:
- investigation-environment
- vm
source: gh-topic-osint-resources
lastVerified: '2026-08-05'
enrichment: full
---

# OSINT VM (Inforensics)

> A pre-built, disposable virtual machine loaded with OSINT tooling (and AI agents) — a clean, isolated environment to run investigations from.

## When to use
At the start of any investigation where you want isolation and repeatability instead of installing tools on your daily machine. Rather than assembling a toolkit yourself, you spin up this VM, which comes with common OSINT utilities pre-installed, do your collection inside it, then snapshot or destroy it afterward. It's infrastructure/opsec, not a lookup — it produces no selectors, it hosts the tools that do.

## How to use it (`bestInteractionPattern`: docker)
1. Clone https://github.com/Inforensics/osint-vm and read its build instructions/scripts.
2. Build/import the VM image into your hypervisor (or run its containerised components per the repo).
3. Take a clean snapshot; route the VM's network through your VPN/Tor.
4. Run your OSINT workflow inside the VM using its bundled tools; keep each investigation in its own snapshot/identity.
5. When done, roll back or delete the VM so nothing persists on your host.

## Inputs → Outputs
- **In:** none (it's an environment)
- **Out:** none directly — findings come from the tools you run inside it
- **Empty/negative result looks like:** N/A — success is "I collected in isolation and left no trace on my host."

## Gotchas & OpSec
- **Isolation, not anonymity:** the VM contains your activity but does not hide your IP — add a VPN/Tor layer.
- Verify the repo's tool versions and scripts before use; bundled tools can go stale or carry their own risks.
- Bundled AI agents may call external services — don't feed them sensitive case data that would leave the VM.

## Overlaps ("do both")
- Alternative to other investigator distros (e.g. Tsurugi/CSI Linux-style builds); pick one as your standard environment and run your other tools inside it.

## Trust & verifiability
`trust: community` — a community project whose value is convenience; audit its contents before trusting it for real casework, and treat it as a container, not a guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-vm-inforensics |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
