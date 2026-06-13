---
id: isolate-the-investigation-in-a-disposable-vm
name: Isolate the investigation in a disposable VM
description: Use when Set up before substantive collection begins, especially for cases touching adversarial infrastructure.
type: technique
summary: TOFM recommends running investigations inside a virtual machine to isolate them from your normal computer use and to keep all notes and screenshots organized in one place. Because VMs are disposable, you can delete the whole environment when the case is done. This compartmentalizes operational risk and keeps case evidence from leaking into personal systems.
missingPersonsRelevance: low
phase: opsec
pivotFrom: []
steps:
- Spin up a dedicated VM for the investigation.
- Keep all notes, screenshots, and case materials inside the VM.
- Use a VPN if the investigation reaches infrastructure run by actors you want to stay concealed from.
- Delete the VM when the investigation concludes.
signals:
- No case data resides on your personal/host system
pitfalls:
- Storing case evidence on your personal machine
- Reusing the same VM across unrelated cases, cross-contaminating context
tags:
- vm
- compartmentalization
- opsec
- vpn
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM: VMs isolate investigations, hold notes/screenshots, and are disposable; use a VPN for adversary-managed infrastructure.'
trust: community
source: tofm
---

# Isolate the investigation in a disposable VM

> TOFM recommends running investigations inside a virtual machine to isolate them from your normal computer use and to keep all notes and screenshots organized in one place. Because VMs are disposable, you can delete the whole environment when the case is done. This compartmentalizes operational risk and keeps case evidence from leaking into personal systems.

**When to use:** Set up before substantive collection begins, especially for cases touching adversarial infrastructure.

## Steps
- Spin up a dedicated VM for the investigation.
- Keep all notes, screenshots, and case materials inside the VM.
- Use a VPN if the investigation reaches infrastructure run by actors you want to stay concealed from.
- Delete the VM when the investigation concludes.

## Signals it's working
- No case data resides on your personal/host system

## Pitfalls
- Storing case evidence on your personal machine
- Reusing the same VM across unrelated cases, cross-contaminating context

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
