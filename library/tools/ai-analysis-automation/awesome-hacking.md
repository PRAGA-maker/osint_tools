---
id: awesome-hacking
name: awesome-hacking
description: Use when you need to discover a technique or tool for a specific security/forensics task — returns a curated index of hacking tutorials, tools, and practice resources.
url: https://github.com/carpedm20/awesome-hacking
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding the right category of tool/tutorial (recon, forensics, crypto, web) when you don't yet know what to reach for.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (MIT); it is a GitHub README index, not a hosted service.
opsec: passive
opsecNote: Passive — you browse a public GitHub page. It links out to third-party tools; vet and sandbox anything you download from those links before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community "awesome list" (~17k stars, MIT). It is a curated index of external resources, not a vetted toolchain — quality of linked tools varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- carpedm20/awesome-hacking
tags:
- related-awesome-lists
- reference
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# awesome-hacking

> A curated GitHub index of hacking/security tutorials, tools, and practice platforms — a jumping-off point when you need capability discovery, not a tool itself.

## When to use
You have a task ("deobfuscate this", "analyse this disk image", "enumerate this network") but don't yet know which tool or tutorial fits. awesome-hacking is a discovery index: it points you at the right category of resource. It holds no data about people — its OSINT value is meta (finding tooling), so relevance to a specific person-search is indirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/carpedm20/awesome-hacking.
2. Use the README's table of contents to jump to the relevant domain: system/reverse-engineering, web, network, forensics, cryptography, CTF, etc.
3. Follow the curated links to specific tools, tutorials, Docker images, or practice sites.
4. Vet each linked resource independently (stars, last-commit, reputation) before relying on it.
5. Pivot: bring the chosen tool back into your workflow; treat the list as a map, not an endorsement.

## Inputs → Outputs
- **In:** none (a capability question, not a selector)
- **Out:** none (links to external tools/tutorials, no subject data)
- **Empty/negative result looks like:** the category you want isn't covered — meaning consult a more specialised awesome-list or a live tool directory instead.

## Gotchas & OpSec
- It is an index of *external* resources; some links rot or point to abandoned/unsafe tools — verify before running anything.
- Not an intelligence source: it will not find or enrich anything about a person.
- MIT-licensed and community-maintained; coverage skews toward offensive-security/CTF material.

## Overlaps ("do both")
- Complements the live tools already catalogued in this library — use awesome-hacking to discover a capability, then prefer the specific, verified tool entry here if one exists.

## Trust & verifiability
`trust: community` — a popular but unvetted curated list; every linked tool must be judged on its own merits, so treat entries as leads rather than recommendations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-hacking |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
