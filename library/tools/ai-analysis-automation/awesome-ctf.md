---
id: awesome-ctf
name: awesome-ctf
description: Use when you need to learn or upskill CTF/forensics/recon techniques — returns a curated reference list of tools and resources, not subject data.
url: https://github.com/apsdehal/awesome-ctf
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding vetted CTF, forensics, stego, and recon tools/resources to learn a technique.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free open-source GitHub "awesome list"; no account.
opsec: passive
opsecNote: Passive reference reading — it's a public GitHub list of links, involving no target interaction. It teaches methods and points to tools; the OpSec of each linked tool is that tool's own concern.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular community-curated "awesome" list on GitHub; usefulness depends on volunteer upkeep, so some links drift or die over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- awesome-ctf list
tags:
- related-awesome-lists
- reference
- ctf
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# awesome-ctf

> A curated GitHub "awesome list" of Capture-the-Flag resources — forensics, steganography, cryptography, web, and recon tools grouped by category.

## When to use
This is a **reference/learning resource**, not a lookup tool. Reach for it when you need to learn or find the right tool for a technique that overlaps OSINT — file forensics, steganography extraction, metadata analysis, encoding/decoding, or web recon — rather than when you're processing a selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/apsdehal/awesome-ctf.
2. Use the README's category index (Forensics, Steganography, Crypto, Web, etc.) to jump to a topic.
3. Follow links to specific tools; check each tool's own repo/site for current status (list entries can be stale).
4. Pivot: a forensics/stego tool you find here becomes part of your analysis workflow on a recovered file or image.

## Inputs → Outputs
- **In:** none (a topic/technique you're researching)
- **Out:** none (curated links to tools/resources — not subject selectors)
- **Empty/negative result looks like:** a category with sparse or dead links — cross-check against other awesome-lists or a fresh search.

## Gotchas & OpSec
- It's a link directory, not a tool — it finds nothing about a person by itself.
- Volunteer-maintained: some entries are outdated or point to abandoned projects; verify each tool is alive.
- CTF-oriented, so not everything transfers to real investigations — pick the forensics/recon subset relevant to OSINT.

## Overlaps ("do both")
- Pairs with other curated "awesome" OSINT lists — awesome-ctf is stronger on forensics/stego/crypto tooling, while OSINT-specific lists cover people/infrastructure discovery.

## Trust & verifiability
`trust: community` — a well-known but volunteer-curated GitHub list; treat it as a starting index and verify the liveness and reputation of each linked tool yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-ctf |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
