---
id: qubes
name: Qubes OS
description: Use when you need a security-by-compartmentalization operating system to isolate risky OSINT work (malware, sketchy links, sock puppets) into disposable VMs — a hardened investigator workstation.
url: https://www.qubes-os.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Running investigations in isolated, disposable VMs so a malicious file or link can't compromise your host or cross-contaminate identities.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; the only cost is compatible hardware (needs decent RAM and virtualization support).
opsec: passive
opsecNote: This is investigator opsec, not a target lookup. Qubes isolates each task/persona in its own VM (with disposable VMs for one-off risky actions) so malware detonation or a compromised sock-puppet stays contained. Route networking through a VPN/Whonix qube for anonymity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Well-regarded open-source security OS with a long track record and public audits; endorsed in the privacy/security community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Qubes OS
- QubesOS
tags:
- privacy-and-encryption-tools
- operating-system
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Qubes OS

> A "reasonably secure" desktop OS built on Xen that runs each activity in its own isolated VM (qube) — the investigator workstation for handling malware, hostile links and separated identities safely.

## When to use
Your work involves things that can bite back — detonating a suspicious attachment, opening a shady link, running a persona that must never touch your real identity, or analysing hostile material. Qubes lets you do each in a dedicated or disposable VM, so a compromise is contained to that qube and can't reach your host, your other cases, or your true attribution.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Check hardware compatibility, then install Qubes OS from https://www.qubes-os.org (verify the ISO signature).
2. Organise work into qubes by trust level: e.g. a "work" qube, per-persona qubes, and **disposable VMs** for one-off risky opens.
3. Route networking through a VPN or the bundled Whonix qubes (Tor) so investigative traffic isn't tied to your host IP.
4. Open unknown files/links in a disposable VM that is destroyed on close — nothing persists to infect you.
5. Keep each sock-puppet identity in its own qube to prevent cross-contamination of cookies, logins and fingerprints.

## Inputs → Outputs
- **In:** n/a — this is your operating environment, not a selector lookup
- **Out:** compartmentalised, disposable execution environments for investigative tasks
- **Empty/negative result looks like:** not applicable; the payoff is that a malicious file or a burned persona is confined to a single qube.

## Gotchas & OpSec
- Steep learning curve and specific hardware requirements (RAM, IOMMU/virtualization) — not a quick install.
- Isolation is only as good as your discipline: mixing personas in one qube, or copying files carelessly between qubes, defeats the model.
- It secures *you*; it is not an OSINT data source and returns no target information.

## Overlaps ("do both")
- Complements `[[mullvad-browser]]`, VPNs, and Whonix — Qubes provides the isolated compartments, those provide the anonymized/hardened browsing inside them.

## Trust & verifiability
`trust: trusted` — mature open-source security OS with public documentation and audits; its isolation properties are well studied and widely relied upon.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qubes |
