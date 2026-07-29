---
id: osintlab
name: OSINTLAB
description: Use when you have a fresh Kali workstation and want a ready recon toolkit — a bash installer that deploys ~50 OSINT tools (subdomain, email, breach, social) in one pass.
url: https://github.com/Purpl3-Dev/OSINTLAB
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Bulk-provisioning ~50 common OSINT/recon tools on a Kali Linux workstation with one script.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source on GitHub; no account required (individual tools it installs may have their own API-key needs).
opsec: passive
opsecNote: Running the installer only touches package repos and the tools' own GitHub/PyPI sources, not any investigation target. Review install.sh before running — you are executing a third-party script as your recon user; run it in a disposable VM you keep separate from your identity.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: Small community repo (~39 stars, few commits) by an individual dev; it just orchestrates other well-known tools, so audit install.sh and trust the underlying tools, not the wrapper.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- OSINTLAB
- Purpl3-Dev OSINTLAB
tags:
- installer
- provisioning
- setup
source: gh-topic-osint-framework
lastVerified: '2026-07-29'
enrichment: full
---

# OSINTLAB

> A one-shot bash installer that stands up ~50 OSINT/recon tools on Kali Linux, so a fresh box becomes an investigation workstation in a single run.

## When to use
Not a lookup tool — an environment bootstrapper. Reach for it when you're spinning up a clean Kali VM for a case and want the usual OSINT arsenal (subdomain enumeration, email/username investigation, breach checking, social-media recon) installed at once instead of cloning and configuring 50 repos by hand.

## How to use it (`bestInteractionPattern`: cli)
1. On a Kali Linux VM, clone the repo: `git clone https://github.com/Purpl3-Dev/OSINTLAB`.
2. **Read `install.sh` first** — confirm what it installs and that nothing looks tampered with.
3. Run `bash install.sh`. It skips tools Kali already ships; use the separate `kali_default_tools.sh` on non-Kali distros.
4. Resolve any manual dependencies the README flags (some tools conflict and need hand-tuning).
5. Use the installed tools individually for actual investigation.

## Inputs → Outputs
- **In:** none (it provisions software, it doesn't take a selector)
- **Out:** an installed toolkit of ~50 OSINT utilities
- **Empty/negative result looks like:** install errors / dependency conflicts on individual tools — the README warns some need manual setup; a failed tool means fix that tool, not that the script is broken.

## Gotchas & OpSec
- Kali-tailored; on other distros expect gaps.
- You are running an unaudited third-party script as a privileged user — review it and run in a disposable, identity-separated VM.
- It only installs tools; the API keys, OPSEC, and legality of using each installed tool are on you.

## Overlaps ("do both")
- Complements curated tool lists (like this library) — OSINTLAB gets the binaries onto disk; the library tells you which to reach for and how.

## Trust & verifiability
`trust: community` — a small single-author convenience wrapper; trust the individual upstream tools it pulls, and audit `install.sh` before executing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintlab |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
