---
id: awesome-anti-forensic
name: awesome-anti-forensic
description: Use when you need a catalogue of anti-forensic and evasion tools/techniques — to recognise how a subject hid, wiped, or spoofed data, and which analysis tools counter it. Reference, not an analyzer.
url: https://github.com/remiflavien1/awesome-anti-forensic
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A curated reference of anti-forensic tools and techniques (data hiding, wiping, spoofing, anti-analysis).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free open "awesome list" on GitHub; no account, no cost.
opsec: passive
opsecNote: Passive reading of a public GitHub list. Nothing is run and nothing about a case is transmitted. The tools it links are dual-use — study them to recognise evasion, and use any offensively only within your authority.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated GitHub awesome-list; it aggregates third-party tools it did not author, so vet each linked project independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- malware-analysis-tools
- exiftool
aliases:
- awesome-anti-forensic
- anti-forensics list
tags:
- related-awesome-lists
- anti-forensics
- reference
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# awesome-anti-forensic

> A curated GitHub list of anti-forensic tooling and techniques — read it to understand *how* a subject may have hidden, wiped, or spoofed evidence, and which counter-tools exist.

## When to use
You're analysing artefacts and something looks deliberately obscured — scrubbed metadata, wiped free space, timestamp tampering, steganography, log manipulation, anti-VM/anti-debug tricks. This list catalogues the tools and techniques attackers use to do exactly that, which helps you (a) recognise the evasion pattern in front of you and (b) find the analysis tools that defeat it. It's a knowledge map, not something you run against a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/remiflavien1/awesome-anti-forensic.
2. Browse the categorised sections (data hiding/steganography, secure deletion, metadata/timestamp manipulation, anti-analysis/anti-VM, network evasion, etc.).
3. Match what you're seeing in the evidence to a technique, then follow the link to the specific tool to understand its artefacts and countermeasures.
4. Use the matching detection/analysis tool to confirm and reverse the evasion where possible.
5. Pivot: consult `[[malware-analysis-tools]]` for analysis tooling, and `[[exiftool]]` when the evasion is metadata scrubbing/spoofing.

## Inputs → Outputs
- **In:** — (a reference; you bring the artefact/technique question)
- **Out:** curated anti-forensic tools and techniques, categorised (no selectors)
- **Empty/negative result looks like:** n/a — a static list; if a niche technique isn't covered, follow its links to broader forensics resources.

## Gotchas & OpSec
- Dual-use content: the same tools that hide evidence can be studied to detect it. Use anything offensively only with authorisation.
- Awesome-lists drift — some links rot or go unmaintained; verify a tool still exists and works before relying on it.
- OpSec: passive reading only; the risk lives in the tools, handled elsewhere in a controlled environment.

## Overlaps ("do both")
- Pairs with `[[malware-analysis-tools]]` (the analysis side) and `[[exiftool]]` (to detect metadata scrubbing/spoofing this list describes) — use this to name the evasion, those to counter it.

## Trust & verifiability
`trust: community` — a community awesome-list aggregating third-party tools it did not build; reliable as an index of what exists, but vet each linked project's provenance and maintenance yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-anti-forensic |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
