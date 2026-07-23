---
id: backbox
name: BackBox
description: Use when you want an Ubuntu-based security/OSINT workstation as an alternative to Kali — a platform to run tools from, not a lookup itself.
url: https://www.backbox.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: An Ubuntu-based penetration-testing and security-analysis distro with recon/OSINT tools preinstalled.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (community edition). Ubuntu-based; runs as install, VM, or live image. No account.
opsec: active
opsecNote: BackBox is just the platform — its OpSec profile is whatever the tools you run inside it do, and many recon/pentest tools are active/intrusive. Run it isolated (VM/live-USB), route sensitive traffic through a VPN/Tor, and only point active tools at systems you're authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Established, long-standing Ubuntu-based security distribution. The distro is reputable and actively maintained; individual bundled tools vary in quality — judge each on its own.
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
- BackBox Linux
tags:
- Virtual Machines/Linux distributions
- security-distro
- toolkit
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# BackBox

> An Ubuntu-based security and penetration-testing distribution — a lighter, Debian/Ubuntu-flavoured alternative to Kali that ships recon, analysis, and OSINT tools ready to go. A platform, not a query tool.

## When to use
You want a ready security/OSINT workstation but prefer an Ubuntu base (familiar package management, lighter footprint) over Kali. Use it as the isolated environment you run recon and analysis tools from, keeping your host machine clean and resettable.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download from https://www.backbox.org (installer or VM/live image) and verify the download.
2. Run as a **VM or live-USB** for investigations; snapshot before work so you can roll back.
3. Harden OpSec first: VPN/Tor for sensitive traffic, sock-puppet identity, and check what each tool sends before running it.
4. Launch the bundled recon/OSINT/security tools from the menus or CLI — BackBox hosts them; the tools do the collection.
5. Pivot: results come from the individual tools you run; feed those onward and reset/snapshot the VM between cases.

## Inputs → Outputs
- **In:** N/A — it's an operating system/toolbox
- **Out:** a configured environment; actual selectors come from the tools you run inside it
- **Empty/negative result looks like:** N/A — BackBox provides capability, not answers.

## Gotchas & OpSec
- **Active by default**: bundled pentest/recon tools probe targets directly and are logged there — authorisation and burner infrastructure are your responsibility.
- Run it isolated (VM/live-USB), not as a daily driver; snapshot for easy reset.
- Bundled ≠ endorsed: verify each tool's currency and behaviour.

## Overlaps ("do both")
- A direct alternative to `[[kali-linux-os]]` (and `[[tsurugi-linux]]` for forensics) — pick the base you prefer; the toolsets overlap heavily. Pair with an anonymity layer like Tails when a session must be trace-free.

## Trust & verifiability
`trust: trusted` — a maintained, reputable Ubuntu-based security distro. Trust the platform; evaluate each bundled tool's reliability individually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | backbox |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
