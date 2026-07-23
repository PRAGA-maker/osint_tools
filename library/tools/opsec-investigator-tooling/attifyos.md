---
id: attifyos
name: AttifyOS
description: Use when you need a ready-made toolkit for IoT/embedded-device security testing — a Linux distro pre-loaded with firmware, radio and hardware analysis tools so you don't assemble them yourself.
url: https://github.com/adi0x90/attifyos
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A pre-built Linux distribution bundling the tools needed to assess IoT and embedded-device security.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; distributed as a downloadable VM image / build instructions. No account.
opsec: active
opsecNote: A toolkit distro — OpSec depends entirely on what you run from it. Firmware/radio/network testing against devices you don't own can be intrusive and illegal; only assess hardware you own or are explicitly authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community IoT-pentest distro associated with Attify; a convenient curated toolset, though not as actively updated as mainstream security distros — verify individual tools' currency.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Attify OS
- adi0x90/attifyos
tags:
- Virtual Machines/Linux distributions
- iot-security
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# AttifyOS

> A Linux distribution pre-loaded with IoT/embedded security tooling — firmware extraction, radio (BLE/Zigbee/RF), hardware and network analysis — so you have a working IoT-testing bench without hand-assembling the toolchain.

## When to use
Your investigation involves a physical smart device — a camera, router, wearable, or other IoT gadget — and you need to examine its firmware, radio traffic, or network behavior. AttifyOS saves the setup: it ships the common IoT-assessment tools (firmware unpackers, BLE/Zigbee sniffing, binary analysis, MITM tooling) in one VM, so you can boot it and start rather than installing each tool. It's specialist tooling, tangential to people-search but relevant to device-forensics angles of a case.

## How to use it (`bestInteractionPattern`: cli)
1. Download the AttifyOS VM image (or build it from the repo) and boot it in a VM.
2. Bring in the target artifact — a firmware image, a captured radio dump, or the device on a lab network you control.
3. Use the bundled tools: unpack firmware (binwalk/firmware-mod-kit), analyze binaries, sniff/replay radio, or MITM the device's traffic.
4. Extract findings — hardcoded credentials, endpoints/`domain`s the device contacts, exposed services.
5. Pivot: endpoints/domains the device phones home to feed infra tooling; extracted accounts feed further OSINT.

## Inputs → Outputs
- **In:** a device, its firmware image, or captured device traffic (things you own/are authorized to test)
- **Out:** firmware contents, hardcoded secrets, contacted endpoints/`domain`s, protocol/behavior findings (via the bundled tools)
- **Empty/negative result looks like:** encrypted/packed firmware you can't unpack, or a device with no extractable artifacts — expect partial results; IoT assessment is tool- and target-specific.

## Gotchas & OpSec
- Authorization is essential: testing radio/firmware/network of devices you don't own can be intrusive and unlawful. Stay to hardware you own or are explicitly engaged to assess.
- The distro is a curated bundle that isn't updated as often as mainstream security distros — check that individual tools are current, or install updates.
- OpSec: active by nature — what you run can transmit and interfere; work in an isolated lab.

## Overlaps ("do both")
- Pairs with general security distros (Kali) and standalone firmware tools (binwalk) — AttifyOS pre-curates the IoT-specific set, but you can achieve the same on a general distro by installing the tools you need.

## Trust & verifiability
`trust: community` — an open, community IoT-pentest distro; the value is the curated toolset, with the caveat that it's less actively maintained than mainstream distros, so verify tool versions before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | attifyos |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
