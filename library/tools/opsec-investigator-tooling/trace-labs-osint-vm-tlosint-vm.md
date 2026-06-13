---
id: trace-labs-osint-vm-tlosint-vm
name: Trace Labs OSINT VM (tlosint-vm)
description: Kali-based OSINT Linux distribution pre-loaded with the Trace Labs-endorsed OSINT toolset for CTF and missing-persons investigations.
url: https://github.com/tracelabs/tlosint-vm
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Ready-to-go investigator workstation with curated OSINT tools, Obsidian vault, Tor and OpSec hardening.
selectorsIn: []
selectorsOut: []
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Official Trace Labs VM build; canonical list of endorsed tools is in scripts/tlosint-tools.sh.
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
lastVerified: ''
enrichment: stub
---

# Trace Labs OSINT VM (tlosint-vm)

> Kali-based OSINT Linux distribution pre-loaded with the Trace Labs-endorsed OSINT toolset for CTF and missing-persons investigations.

- **URL:** https://github.com/tracelabs/tlosint-vm
- **Best for:** Ready-to-go investigator workstation with curated OSINT tools, Obsidian vault, Tor and OpSec hardening.
- **Source:** harvested from `tracelabs-repos`

Builds VirtualBox/VMware/OVA images. Provisioning script installs ExifTool, Sherlock, SpiderFoot, PhoneInfoga, Sublist3r, metagoofil, sn0int, Owlculus, steghide/stegseek/stegosuite, translate-shell, Tor/torbrowser, Brave with the Forensic OSINT extension, plus OpSec tools (anonsurf, macchanger, mat2, torsocks). Also ships an Obsidian TL-Vault for case notes.

_Enrichment: stub. If stub, complete per `schema/templates/tool.template.md`._
