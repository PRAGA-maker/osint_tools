---
id: whonix
name: Whonix
description: Use when you need a Tor-only, leak-proof anonymity environment for high-risk investigation — provides a two-VM isolated workstation, not a per-subject lookup.
url: https://www.whonix.org/wiki/Main_Page
category: ai-analysis-automation
path:
- ai-analysis-automation
- virtual-machines
bestFor: A two-VM (Gateway + Workstation) system that forces all traffic through Tor to prevent IP/DNS leaks.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; runs as two VMs (VirtualBox/KVM) or on Qubes OS.
opsec: passive
opsecNote: Whonix is your own workstation — running it touches no subject. Its whole purpose is investigator-side: the Gateway VM forces every packet from the Workstation through Tor, so even a misbehaving tool cannot leak your real IP/DNS. Note that some sites block Tor exit nodes and Tor use is itself visible to destinations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing, well-reviewed open-source anonymity project (maintained alongside Kicksecure); verify ISO/OVA downloads against the project's signed checksums.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- parrotsec-os
aliases:
- Whonix
tags:
- anonymity
- tor
- virtual-machine
- opsec
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Whonix

> Two VMs, one job: force every byte of your Workstation's traffic through Tor via an isolated Gateway, so nothing you run can leak your real IP or DNS.

## When to use
You're conducting sensitive recon where an accidental IP/DNS leak would burn the operation or endanger you, and you want stronger isolation than a single VM plus a VPN. Whonix separates the network path (Gateway VM) from where you work (Workstation VM), so even a compromised or misconfigured tool on the Workstation physically cannot see or leak your real network identity. It's the platform your investigation runs on, not a lookup tool itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Whonix from https://www.whonix.org and import both VMs (Gateway + Workstation) into VirtualBox/KVM, or use the Qubes-Whonix templates.
2. Boot the **Gateway** first (it connects to Tor), then the **Workstation** — it has no direct network, only the Gateway.
3. Do your work inside the Workstation; all its traffic is transparently Tor-routed, and DNS is handled to avoid leaks.
4. Snapshot the Workstation so you can revert to a clean state between cases.
5. Pivot: Whonix is the anonymity layer — the actual selector work happens in the tools you run inside it, each with its own OpSec still to consider.

## Inputs → Outputs
- **In:** N/A — it's an operating-system/VM distribution
- **Out:** a Tor-only, leak-resistant working environment
- **Empty/negative result looks like:** N/A — evaluate the tools you run inside it, not Whonix itself.

## Gotchas & OpSec
- Tor-only routing means **Tor-blocking or Tor-hostile sites** may not work or may flag you; some investigations need a bridge or a different posture.
- Anonymity is about behaviour too — logging into a personal account inside Whonix deanonymizes you regardless of Tor.
- Keep it updated and verify downloads with the project's signatures; a tampered image defeats the purpose.

## Overlaps ("do both")
- A peer to [[parrotsec-os]] and Tails: Whonix's strength is the two-VM leak-proof Tor isolation, versus Parrot's general tool-loaded desktop or Tails' amnesic live-boot model. Choose by threat model.

## Trust & verifiability
`trust: community` — a mature, widely-scrutinized open-source project; the anonymity guarantee is only as good as your download integrity and your own behaviour inside the VM.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whonix |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
