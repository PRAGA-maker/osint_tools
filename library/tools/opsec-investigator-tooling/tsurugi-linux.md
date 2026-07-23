---
id: tsurugi-linux
name: Tsurugi Linux
description: Use when you need a ready DFIR/OSINT workstation for evidence analysis — a preloaded forensic platform, not a lookup tool.
url: https://tsurugi-linux.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A digital-forensics and OSINT workstation VM with forensic and investigation tools preinstalled.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free. Distributed as a full DFIR distro (Tsurugi Linux), a lightweight "Acquire" edition, and a Windows tool bundle. No account.
opsec: passive
opsecNote: Tsurugi is a workstation you run locally — reading/analysing evidence is inherently passive and touches no target. It's built for forensic soundness (write-blocking, hashing). As with any investigation VM, isolate it and mind that any online OSINT tools you launch from it have their own active footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Established, community-recognised DFIR-focused distribution with a dedicated OSINT module. The distro is reputable; individual bundled tools vary in currency — evaluate each.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- kali-linux-os
aliases:
- Tsurugi
tags:
- vm
- linux-distro
- dfir
- forensics
source: ultimate-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Tsurugi Linux

> A DFIR-first Linux distribution with a strong OSINT module — a ready-made, forensically-sound workstation for analysing evidence and running investigations, rather than a tool that answers a query.

## When to use
You need a forensic/investigation workstation with the right tooling already assembled and configured for soundness: disk/memory forensics, file-metadata analysis, timeline building, and a bundled OSINT toolkit. Reach for Tsurugi when the work is *evidence handling and analysis* (imaging, carving, metadata) more than live web recon — that's where it's stronger than a general pentest distro.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download from https://tsurugi-linux.org/ — pick the full distro, the lightweight "Acquire" edition (for imaging), or the Windows bundle. Verify the download.
2. Run it as a VM or live-USB; snapshot before working so you can reset to a clean state.
3. Use its forensic tools with write-blocking/hashing to acquire and analyse evidence soundly, and its OSINT module for investigation tasks.
4. Keep evidence handling documented (hashes, chain of custody) — the distro is built to support that.
5. Pivot: findings (extracted metadata, artifacts, identifiers) feed your case; online OSINT tools launched here behave as they normally would (mind their footprint).

## Inputs → Outputs
- **In:** N/A — it's an operating environment/toolbox
- **Out:** a configured DFIR/OSINT workstation; actual selectors come from the tools you run inside it
- **Empty/negative result looks like:** N/A — Tsurugi provides capability, not answers.

## Gotchas & OpSec
- It's a platform, not a person-finder; its value is forensic analysis and having the toolset ready.
- Run isolated (VM/live-USB) and snapshot between cases; keep evidence handling documented.
- Bundled ≠ maintained: verify a given tool's currency before relying on it.

## Overlaps ("do both")
- Complements `[[kali-linux-os]]` — Kali leans offensive/recon, Tsurugi leans forensic/analysis. Use Tsurugi for sound evidence work, Kali for active enumeration.

## Trust & verifiability
`trust: trusted` — a well-regarded DFIR distribution. Trust the platform and its forensic design; judge each bundled tool's reliability and maintenance individually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tsurugi-linux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
