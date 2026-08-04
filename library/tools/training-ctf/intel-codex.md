---
id: intel-codex
name: Intel-Codex
description: Use when you want structured SOPs and learning paths for OSINT, forensics, and reverse engineering — provides a free reference knowledge base, not a per-selector lookup.
url: https://github.com/gl0bal01/intel-codex
category: training-ctf
path:
- training-ctf
bestFor: A free operational manual of standard operating procedures and learning paths for digital investigators.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (MIT). Best viewed as an Obsidian vault, but the markdown files read fine directly on GitHub or in any editor.
opsec: passive
opsecNote: A reference repository you read/clone locally — it queries nothing and leaks nothing about any subject. It even emphasises OpSec and legal compliance in its own procedures.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-maintainer open-source knowledge base of SOPs and case studies; well-structured and MIT-licensed, but community-authored guidance to apply with judgement, not authoritative doctrine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- intel codex
- gl0bal01 intel-codex
tags:
- knowledge-base
- sop
- training
- methodology
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Intel-Codex

> A free, open-source operational manual for digital investigators — 40+ standard operating procedures and structured learning paths spanning OSINT, forensics, malware analysis, and reverse engineering.

## When to use
This is a *methodology* resource, not a data tool. Reach for it when you need a repeatable procedure or want to level up: platform-specific investigation guides (Twitter, Instagram, Telegram, Discord), SOPs for evidence handling and case management, blockchain-tracing and RE workflows, and six-week learning paths per specialisation. Use it to structure an investigation, onboard, or check that your process is sound — then execute with the concrete tools elsewhere in this library.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/gl0bal01/intel-codex (or clone it).
2. Browse the sections: investigations (per-platform OSINT SOPs), security operations, case studies, templates, and learning paths.
3. For the full experience, open the folder as an **Obsidian vault** (free) to follow the internal links; otherwise read the markdown on GitHub.
4. Pick the SOP matching your task, follow its steps, and use its case-management/evidence templates.
5. Apply the procedure using the actual lookup/analysis tools it references.

## Inputs → Outputs
- **In:** none (a reference/knowledge base, not a selector-driven lookup)
- **Out:** none directly — procedures, checklists, and templates that guide your workflow
- **Empty/negative result looks like:** N/A; if a topic isn't covered, supplement with other methodology sources (e.g. OSINT frameworks/curricula).

## Gotchas & OpSec
- It's guidance, not a tool — it won't return data; pair each SOP with the real tools it names.
- Single-maintainer community content: apply judgement and keep to current best practice and local law.
- Best navigated in Obsidian; raw on GitHub the internal `[[links]]` won't be clickable.

## Overlaps ("do both")
- Complements hands-on OSINT frameworks and the tools in this library: Intel-Codex tells you *how* to run an investigation; the individual tool skills here are *what* you run at each step — use the SOP to sequence them.

## Trust & verifiability
`trust: community` — a well-organised, MIT-licensed community knowledge base; treat its SOPs as solid starting doctrine to adapt, and always defer to current legal/operational requirements for your jurisdiction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intel-codex |
| category | training-ctf |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
