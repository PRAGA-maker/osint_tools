---
id: subgraph-os
name: Subgraph OS
description: Use when you want a hardened, Tor-routed Linux OS to run investigations from — an OpSec/anonymity workstation, not a lookup tool (no selectors in/out).
url: https://subgraph.com/index.en.html
category: ai-analysis-automation
path:
- ai-analysis-automation
- virtual-machines
bestFor: A hardened Tor-integrated Linux environment for compartmentalised, anonymous investigative work.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open-source. Downloadable as an installer, live-disk, or VM image.
opsec: passive
opsecNote: This is itself an OpSec tool — it forces traffic through Tor, sandboxes apps (Oz), and hardens the kernel, so running your investigation inside it protects YOUR attribution. It performs no queries against a target. Because the project is dormant, security updates may be stale — do not rely on it as your sole anonymity layer for high-risk work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source project (Subgraph). Long stuck at an alpha stage with no evidence of active maintenance (site © 2023 but no recent releases); treat as dormant/experimental.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- tails
- whonix
- tor-browser
aliases:
- Subgraph
tags:
- opsec
- anonymity-os
- virtual-machines
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Subgraph OS

> A security-hardened, Tor-by-default Linux distribution meant as an anonymous workstation — an OpSec platform to *run* investigations from, not a tool you query.

## When to use
You want to conduct sensitive OSINT from an environment that resists deanonymisation and malware: default Tor routing, application sandboxing (Oz), a hardened kernel (grsecurity/PaX), and an outbound application firewall. Consider it when compartmentalising a high-risk investigation — but note it is dormant, so for most users a maintained alternative below is the safer choice.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the Subgraph OS alpha image from subgraph.com.
2. Run it as a live-disk (no install), install it to a machine, or boot it in a VM.
3. Work inside the hardened environment: browse via Tor, run apps within their Oz sandboxes, and watch the application firewall for unexpected outbound connections.
4. Keep sensitive activity compartmentalised to this OS and away from your attributable daily system.
5. Because it is dormant, pair it with — or substitute — an actively maintained anonymity OS for anything high-stakes.

## Inputs → Outputs
- **In:** none (it's an operating environment, not a query tool)
- **Out:** a hardened, Tor-routed workstation (no selectors)
- **Empty/negative result looks like:** n/a — the "output" is the protected environment itself.

## Gotchas & OpSec
- **Dormant/alpha:** no evidence of active maintenance; kernel/browser/Tor components may lag on security fixes. Do not treat it as a current, fully-patched anonymity layer.
- Anonymity is only as good as your discipline inside it — logging into attributable accounts still deanonymises you regardless of Tor.
- Verify downloads against published signatures where available.

## Overlaps ("do both")
- Prefer actively maintained `[[tails]]` (amnesic live OS) or `[[whonix]]` (isolated Tor gateway VM) for real operational use; use `[[tor-browser]]` alone when you just need anonymous browsing on your existing OS.

## Trust & verifiability
`trust: community` — open-source and inspectable, but effectively abandoned at alpha. Fine to study or run experimentally; for protecting a live investigation, rely on a maintained OpSec OS instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subgraph-os |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (environment) → (hardened workstation) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
