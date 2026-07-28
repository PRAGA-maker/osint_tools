---
id: intrec-pack
name: IntRec-Pack
description: Use when you want to stand up an OSINT/recon toolkit quickly — an installer/manager that downloads and sets up a curated bundle of intelligence-gathering tools and dependencies.
url: https://github.com/NullArray/IntRec-Pack
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Bootstrapping a working OSINT/recon environment — installs and manages a set of common gathering tools and their dependencies from one script.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (installer/manager script); the tools it installs are themselves free/open-source.
opsec: passive
opsecNote: The installer itself just fetches and sets up software — passive. Real OpSec depends entirely on which installed tools you then run and how; a tool that later scans or contacts targets is active, so judge OpSec per-tool at use time.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community project by GitHub user NullArray; it automates installing third-party tools, so review the script and the tools it pulls before running, ideally in a disposable VM.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- IntRec-Pack
- Intelligence and Reconnaissance Package
tags:
- osint-automation
- toolkit-installer
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# IntRec-Pack

> An installer/manager that bootstraps an OSINT and reconnaissance environment — one script to fetch, set up and update a bundle of common intelligence-gathering tools.

## When to use
You're building or refreshing a research machine and want the common recon tooling installed without hunting each repo down by hand. IntRec-Pack ("Intelligence and Reconnaissance Package") automates downloading and configuring a curated set of OSINT tools plus their dependencies. It's infrastructure/setup, not an investigative lookup — you run it once to get a working toolkit, then use the individual tools for actual case work.

## How to use it (`bestInteractionPattern`: cli)
1. Review the repo first: read `https://github.com/NullArray/IntRec-Pack` to see exactly which tools it installs.
2. Clone it and run the installer from a terminal (ideally inside a disposable VM/container).
3. Choose which tool categories/tools to install when prompted; let it resolve dependencies.
4. Once set up, invoke the individual installed tools for your investigation — IntRec-Pack's job ends at provisioning.
5. Re-run periodically to update the bundled tools.

## Inputs → Outputs
- **In:** none (it's a provisioning tool — you choose what to install)
- **Out:** an installed, ready-to-use set of OSINT/recon tools on your machine
- **Empty/negative result looks like:** install failures — usually a moved/renamed upstream repo, a broken dependency, or an unsupported OS; install the affected tool manually.

## Gotchas & OpSec
- It pulls and runs **third-party code**; review the script and the tools it installs, and prefer a sandboxed VM.
- Being an aggregator of other repos, individual tools can be stale or unmaintained upstream — verify each before relying on it.
- OpSec is per-tool: the installer is passive, but tools you then run may actively touch targets.

## Overlaps ("do both")
- Complements the individual OSINT CLIs it bundles — IntRec-Pack sets them up; you run each one for the actual investigation. Treat it as the provisioning layer beneath the rest of your toolkit.

## Trust & verifiability
`trust: community` — an unaffiliated community installer; it's only as trustworthy as the upstream tools it fetches. Inspect the code, pin/verify what it installs, and run it isolated from sensitive data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intrec-pack |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
