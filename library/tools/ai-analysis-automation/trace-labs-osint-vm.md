---
id: trace-labs-osint-vm
name: Trace Labs OSINT VM
description: Use when you want a ready-to-run, purpose-built OSINT toolkit for a missing-person case — a Kali-based VM preloaded with the tools used in Trace Labs Search Party CTFs.
url: https://www.tracelabs.org/initiatives/osint-vm
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A pre-configured investigator workstation tuned for missing-persons OSINT
selectorsIn:
- name
- username
- image
- social-profile
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free download (Kali Linux base, MIT/community tooling); you supply the host and a VM hypervisor.
opsec: passive
opsecNote: A toolbox, not a service — its OpSec depends on the tools you run inside it. Run behind a VPN/Tor as appropriate and treat the VM as your operational sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Maintained by Trace Labs, a nonprofit that crowdsources OSINT to help find missing persons.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- TraceLabs VM
- Trace Labs Kali VM
tags:
- vm
- missing-persons
- investigator-platform
- ctf
source: ultimate-osint
lastVerified: ''
enrichment: full
---

# Trace Labs OSINT VM

> A Kali-based virtual machine that bundles the exact OSINT tooling Trace Labs uses in its Search Party missing-persons CTFs — a turnkey investigator workstation.

## When to use
Use it when you are starting hands-on OSINT work and don't want to install and configure dozens of tools yourself. Ideal when you have a `name`, `username`, or `image` of a missing person and need a sandboxed environment with username enumeration, image/EXIF, social-profile, and geolocation tooling already in place. Especially relevant if you are participating in a Trace Labs Search Party event.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the VM from the Trace Labs initiatives page and import it into VirtualBox/VMware.
2. Boot it (Kali Linux base) and update the toolset; review the included tooling list.
3. Run individual tools against your selectors — e.g. username enumeration, reverse image search, EXIF extraction, social-profile pivots.
4. Pivot: outputs (social profiles, associates, EXIF geodata) feed your case notes and Trace Labs submission format.

## Inputs → Outputs
- **In:** `name`, `username`, `image`, `social-profile`
- **Out:** `social-profile`, `associate`, `metadata-exif` (plus whatever the bundled tools produce)
- **Empty/negative result looks like:** the VM itself never "returns" data — empty results come from the individual tools you run inside it.

## Gotchas & OpSec
- Human-in-the-loop: none to boot the VM, but every tool inside has its own auth/rate-limit/captcha considerations.
- OpSec: this is your operational machine. Route traffic through a VPN/Tor as the case requires, use sock-puppet accounts, and keep the VM isolated from your personal identity.

## Overlaps ("do both")
- Pairs with `[[ncptf-national-child-protection-task-force]]`: the VM is the toolkit, NCPTF/Trace Labs are the human coordination layer.

## Trust & verifiability
`trust: trusted` — distributed and maintained by Trace Labs, a well-known nonprofit in the missing-persons OSINT community.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace-labs-osint-vm |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, image, social-profile → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
