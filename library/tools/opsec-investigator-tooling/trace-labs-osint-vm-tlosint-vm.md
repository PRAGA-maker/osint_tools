---
id: trace-labs-osint-vm-tlosint-vm
name: Trace Labs OSINT VM (tlosint-vm)
description: Use when you want a ready-made, OpSec-hardened investigator workstation — a Kali-based VM pre-loaded with the Trace Labs OSINT toolset for missing-persons and CTF work.
url: https://github.com/tracelabs/tlosint-vm
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-to-go, OpSec-hardened investigator workstation with a curated OSINT toolset, Obsidian case vault, Tor and anonymisation utilities.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; you build or download the image and run it in VirtualBox/VMware. The only cost is disk and the host virtualisation software.
opsec: passive
opsecNote: The VM itself is an environment, not a query — its OpSec value is that it centralises anonymisation (Tor, anonsurf, macchanger, mat2 metadata scrubbing) so your investigative traffic and files don't leak your identity. OpSec still depends on the individual tools you run inside it and whether you route them through Tor/VPN; the VM enables good practice but doesn't guarantee it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Official Trace Labs build; Trace Labs is a well-known non-profit running missing-persons OSINT CTFs, and the endorsed toolset is defined in the repo's provisioning script.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tlosint
- Trace Labs OSINT VM
- tlosint-live
tags:
- vm
- kali
- tracelabs
- investigator-platform
- opsec
source: tracelabs-repos
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- gumshoe
- h8mail-trace-labs-fork
- the-osint-field-manual-tofm
- trace-labs-awesome-osint
---

# Trace Labs OSINT VM (tlosint-vm)

> A Kali-based Linux VM pre-loaded with the Trace Labs-endorsed OSINT toolset — a turnkey, OpSec-hardened investigator workstation for missing-persons work and Search Party CTFs.

## When to use
You want a clean, dedicated investigation environment rather than installing OSINT tools piecemeal on your daily machine. The VM ships the tools an investigator reaches for, plus anonymisation and note-taking, so you can spin up an isolated, disposable workstation for a case and tear it down afterwards. It's not a lookup tool — it's the platform you run the lookups from, and its value is bundling capability + OpSec in one place.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the prebuilt OVA (or build it from the repo's script) and import into VirtualBox/VMware.
2. Boot the VM; take a snapshot so you can revert to a clean state per case.
3. Route traffic through Tor/anonsurf (and/or a VPN) before investigating; randomise MAC with macchanger if on untrusted networks.
4. Use the bundled tools for the task — e.g. ExifTool, Sherlock, SpiderFoot, PhoneInfoga, Sublist3r, metagoofil, sn0int — and keep case notes in the included Obsidian TL-Vault.
5. Scrub file metadata with mat2 before sharing outputs; revert the snapshot when done.

## Inputs → Outputs
- **In:** n/a — it is an environment; inputs/outputs belong to the individual tools you run inside it
- **Out:** n/a — a hardened workstation and toolset
- **Empty/negative result looks like:** n/a — success is a working, isolated, anonymised environment; if a bundled tool is broken/outdated, update it inside the VM.

## Gotchas & OpSec
- The VM enables OpSec but doesn't enforce it — you must actually route tools through Tor/VPN and avoid logging into personal accounts.
- Bundled tools can age between releases; update or reinstall inside the VM as needed.
- Use snapshots and per-case isolation so artefacts from one investigation don't bleed into another.

## Overlaps ("do both")
- It is the host for many tools catalogued separately here — e.g. `[[whatsmyname-python]]`, `[[instaloader-2]]`, `[[spiderpig]]`; use the VM as the OpSec-safe place to run them.

## Trust & verifiability
`trust: trusted` — the official build from Trace Labs, a reputable non-profit in the missing-persons OSINT community; the endorsed toolset is transparent in the repo.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace-labs-osint-vm-tlosint-vm |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
