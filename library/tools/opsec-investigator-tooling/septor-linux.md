---
id: septor-linux
name: Septor Linux
description: Use when you need a preconfigured Tor-routed live OS for anonymous OSINT work — returns a hardened Debian/KDE workstation that pushes all traffic through Tor.
url: https://septor.sourceforge.io
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-made anonymous investigation OS that routes traffic through Tor out of the box, for OpSec-sensitive research from a clean environment.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open-source; downloaded as an ISO from SourceForge. No cost, no account.
opsec: passive
opsecNote: This is a defensive OpSec tool — it exists to protect the investigator. Running it live (USB, no persistence) plus Tor routing gives a clean, non-attributable environment. Verify the ISO checksum/signature before booting, and note the project is slow-moving (last release 2022 on kernel 5.10), so update packages and treat the shipped browser as potentially dated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Independent community distro maintained by a small team; well-known in the OSINT/privacy scene but not a large audited project like Tails. Prefer Tails/Whonix when threat model is high.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- hugin
- tails
- whonix
aliases:
- Septor
- Septor OS
tags:
- Virtual Machines/Linux distributions
- anonymity-os
- tor
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Septor Linux

> A Debian-based, KDE Plasma live distro that routes everything through Tor — a Tails-style anonymous workstation for OSINT, aimed at investigator OpSec rather than any lookup.

## When to use
You want to run an investigation from a disposable, non-attributable environment where network traffic is forced through Tor and no browsing residue lands on your real machine. Boot Septor from USB, work inside it, discard the session. It finds nothing itself — it is the *environment* you run other tools from. Choose it when you like a full KDE desktop with privacy apps preloaded; choose Tails/Whonix when you need the most-audited, highest-assurance option.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the ISO from https://septor.sourceforge.io (SourceForge project page).
2. Verify the published checksum/signature against your download before trusting it.
3. Write it to a USB stick (e.g. with balenaEtcher/`dd`) and boot the target machine from it — run live (no persistence) for maximum hygiene.
4. On the KDE desktop, use the bundled Tor Browser, OnionShare, Thunderbird, VeraCrypt, KGpg/Kleopatra, and Mat2 (metadata scrubber) for anonymous research and evidence handling.
5. After the session, shut down and, if you used persistence, wipe it. Pivot: use the clean environment to safely run active-recon tools without exposing your real IP/identity.

## Inputs → Outputs
- **In:** none — it is an operating system, not a query tool.
- **Out:** none per-subject; it provides a Tor-routed workstation to operate from.
- **Empty/negative result looks like:** N/A — success is a booted desktop whose traffic exits via Tor (confirm at `check.torproject.org`).

## Gotchas & OpSec
- Human-in-the-loop: none for operation, but you must verify the ISO and manage boot media yourself.
- OpSec: **passive/defensive** — protects the investigator. Caveat: the project is infrequently updated (2022-era base), so a shipped browser can lag Tor Browser's security fixes; update or reinstall before serious use.
- Not a substitute for discipline: correlating your Tor session with real-name logins still deanonymizes you. Keep sock-puppet and real identities strictly separate.

## Overlaps ("do both")
- Overlaps with `[[tails]]` and `[[whonix]]` — same "anonymous OS" niche; Tails is the amnesic gold standard and Whonix isolates via a gateway VM. Use Septor for a comfortable KDE workflow, the others when assurance matters most.
- Pairs with `[[hugin]]` and other tools you'd run *inside* the environment.

## Trust & verifiability
`trust: community` — a small independent team's distro, respected in the privacy community but not heavily audited. For high-threat work, verify the ISO and prefer a larger-audience anonymity OS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | septor-linux |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
