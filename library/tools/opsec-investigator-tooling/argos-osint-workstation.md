---
id: argos-osint-workstation
name: Argos OSINT Workstation
description: Use when you want a ready-to-work investigator machine and want to auto-provision 30+ OSINT tools on a clean Ubuntu VM — returns a configured workstation, not a per-selector lookup.
url: https://github.com/SOsintOps/Argos
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Standing up a disposable, tool-loaded OSINT investigation VM from a clean Ubuntu install.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (CC BY-NC-SA 4.0); non-commercial use only.
opsec: passive
opsecNote: The setup itself is local, but it installs Firefox privacy extensions and many active-recon tools (Sherlock, Amass, SpiderFoot). Run it inside a throwaway VM you reach over a VPN/sock-puppet network, never on your day-to-day machine, so later investigative traffic is not tied to your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: ~160+ stars, actively maintained beta by the SOsintOps community; review setup.sh before running since it installs software as your user.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Argos
- SOsintOps Argos
tags:
- workstation-setup
- ubuntu
- tooling-bundle
source: gh-topic-footprinting
lastVerified: '2026-08-04'
enrichment: full
---

# Argos OSINT Workstation

> A one-command provisioner that turns a clean Ubuntu 24.04 VM into a loaded OSINT investigation workstation.

## When to use
You are setting up (or resetting) the *environment* you investigate from, not chasing a specific selector. Reach for Argos when you want a disposable VM that already has the common OSINT stack — username enumeration (Sherlock), subdomain/attack-surface discovery (Amass, SpiderFoot), and Firefox privacy extensions — instead of installing each tool by hand. It is infrastructure for a case, run once per fresh machine.

## How to use it (`bestInteractionPattern`: cli)
1. Create a clean Ubuntu 24.04 LTS (or Ubuntu Budgie 24.04) VM — VirtualBox is the tested target; install Guest Additions first, set system language to English.
2. Clone and run the setup script:
   ```bash
   git clone https://github.com/SOsintOps/Argos ~/Downloads/Argos
   chmod +x ~/Downloads/Argos/setup.sh
   ~/Downloads/Argos/setup.sh
   ```
3. Read `setup.sh` before executing — it installs 30+ packages and browser extensions as your user; confirm nothing is unexpected.
4. Let it run (needs internet); it writes timestamped install logs you can check for failed tool installs.
5. Snapshot the VM once provisioned so you can revert to a clean, un-attributed state between cases.

## Inputs → Outputs
- **In:** none (an environment provisioner, not a lookup)
- **Out:** a configured Ubuntu workstation with an OSINT toolchain and hardened Firefox
- **Empty/negative result looks like:** install log shows a tool failing to build (often an upstream/apt issue) — the rest of the workstation still provisions; re-run or install the one tool manually.

## Gotchas & OpSec
- Human-in-the-loop: none for the install, but every downstream tool it deploys has its own opsec profile.
- OpSec: keep this in a VM reached over a VPN/sock-puppet network and snapshot it — the point is a clean, disposable, non-attributable base so a case's active recon never touches your real host or IP.
- Pinned to Ubuntu 24.04; other distros/versions are unsupported and may half-install.

## Overlaps ("do both")
- Complements individual tools it bundles (e.g. `[[spiderfoot]]`, `[[sherlock]]`) — Argos gets them onto the machine; those tools do the actual per-selector work.

## Trust & verifiability
`trust: community` — an actively maintained community project (SOsintOps); it installs third-party software, so the trust ceiling is that of the tools it pulls in. Read the script and pin/verify sources before running.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | argos-osint-workstation |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
