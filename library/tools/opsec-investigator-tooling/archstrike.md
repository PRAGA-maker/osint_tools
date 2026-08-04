---
id: archstrike
name: ArchStrike
description: Use when you want an Arch Linux environment preloaded with security/OSINT tooling — provides an installable distro and package repository, not a per-selector lookup.
url: https://archstrike.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Standing up a hardened Arch-based workstation stocked with pentest and OSINT packages for investigative work.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source — a package repository plus a live/install ISO; no licence or account.
opsec: passive
opsecNote: This is your own analysis environment, not a query against a target, so it leaks nothing to a subject. OpSec value is on your side — run investigations from a dedicated, disposable ArchStrike VM rather than your daily machine, and route traffic through a VPN/Tor as your engagement requires.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community-run Arch Linux security repository; actively maintained (recent package updates) but a volunteer project — verify package signatures and pull only from official mirrors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ArchStrike Linux
- Arch Strike
tags:
- linux-distro
- security-toolkit
- pentest
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ArchStrike

> An Arch Linux security distribution and add-on repository — the Arch-world counterpart to Kali/Parrot, giving you a curated toolbox rather than a single lookup.

## When to use
You don't point ArchStrike at a `name` or `email`; you use it to *build the machine you investigate from*. Reach for it when you want a clean, reproducible workstation that already has pentest and OSINT packages (recon, network, forensics, wireless) available through one repository, and you prefer the Arch "install only what you need" philosophy over a heavyweight preloaded distro. It's foundation/tooling, so its missing-persons relevance is indirect: it's where your other tools live.

## How to use it (`bestInteractionPattern`: cli)
1. Choose your path: install the ArchStrike **ISO** for a fresh dedicated box/VM, or add the **repository** to an existing Arch install.
2. To add the repo: follow the site's setup (import the ArchStrike signing key, append the repo to `/etc/pacman.conf`, sync with `pacman -Syy`).
3. Browse available packages on the site's package list (tools such as airgeddon, evil-winrm, commix, plus recon/OSINT utilities) and install with `pacman -S <tool>`.
4. Use the mirrorlist generator to pick fast, official mirrors.
5. Operate: run your actual OSINT tools from this environment; snapshot the VM so you can revert to a clean state between cases.

## Inputs → Outputs
- **In:** none (it's an environment, not a selector-driven lookup)
- **Out:** none directly — it provisions the tools that produce outputs
- **Empty/negative result looks like:** N/A; the relevant failure mode is a repo/key sync error, fixed by re-importing the signing key and using an official mirror.

## Gotchas & OpSec
- Not a lookup tool — indexing it under investigator tooling is correct; don't expect it to return records.
- OpSec: keep it in a disposable VM; the point is a clean, controlled base for investigations.
- Arch is rolling-release: keep it updated, and verify package signatures to avoid supply-chain risk.

## Overlaps ("do both")
- Complements other security distros (Kali, Parrot, Tsurugi): ArchStrike is the Arch-based option for the same job — a ready investigator workstation; pick one as your base and layer the specific OSINT tools in this library on top.

## Trust & verifiability
`trust: community` — a maintained community project with signed packages and official mirrors; trustworthy as infrastructure provided you pull from the real repo and verify keys, but it's volunteer-run, not a vendor product.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archstrike |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
