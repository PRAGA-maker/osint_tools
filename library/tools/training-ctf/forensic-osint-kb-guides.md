---
id: forensic-osint-kb-guides
name: Forensic OSINT KB Guides
description: Use when you need process guidance for defensible OSINT — returns how-to guides on evidence preservation, chain-of-custody, and court-ready reporting.
url: https://www.forensicosint.com/osint-guide
category: training-ctf
path:
- training-ctf
bestFor: Learning to capture and document online evidence so it holds up for legal/court use.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: The knowledge-base guides are free to read; Forensic OSINT also sells a paid capture tool, but the guidance content is open.
opsec: passive
opsecNote: Reading guidance touches no target. The value is process — apply the OpSec practices each guide describes (clean capture environment, hashing, documentation) when you do the actual collection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Vendor-published knowledge base (Forensic OSINT, a browser-capture tool company). Practical, defensibility-focused guidance; naturally oriented toward their product, so treat tool mentions as one option.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- hunchly
- osint-techniques
- forensicosint-com
- forensicosint-com-3
aliases:
- Forensic OSINT guide
- forensicosint.com
tags:
- methodology
- evidence-preservation
- reporting
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Forensic OSINT KB Guides

> A knowledge base on doing OSINT *defensibly* — capturing online evidence, preserving chain of custody, and producing reports that survive legal scrutiny.

## When to use
When your investigation may feed a legal process (court, HR, safeguarding, a missing-persons case handed to authorities) and how you collect matters as much as what you find. These guides cover preserving digital evidence, hashing and timestamping captures, documenting chain of custody, and writing court-ready reports — the process discipline that turns findings into usable evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.forensicosint.com/osint-guide.
2. Read the guides relevant to your task: evidence capture/preservation, metadata handling, chain-of-custody documentation, reporting.
3. Turn the guidance into a repeatable workflow — clean capture environment, full-page + metadata capture, hashing, contemporaneous notes.
4. Apply it during collection so every artefact is preserved and documented as you go (not reconstructed later).
5. Pivot: use with a capture tool (`[[hunchly]]` or the vendor's own) that implements these practices automatically.

## Inputs → Outputs
- **In:** none (a methodology/knowledge resource)
- **Out:** process guidance, checklists, and reporting templates for defensible OSINT
- **Empty/negative result looks like:** the specific legal/jurisdictional nuance you need isn't covered — supplement with jurisdiction-specific legal advice; guidance is general, not legal counsel.

## Gotchas & OpSec
- Vendor-published, so it leans toward their capture product — the *principles* are broadly applicable; the specific tool is one of several.
- Guidance is not legal advice; evidentiary standards vary by jurisdiction and case — confirm requirements with counsel.
- Value is in the discipline: capture and document contemporaneously; retrofitting chain-of-custody after the fact rarely holds.

## Overlaps ("do both")
- Pairs with a capture tool like `[[hunchly]]` (automatic evidence logging while you browse) and method hubs like `[[osint-techniques]]`. Do both: learn the process here, enforce it with a tool that timestamps and hashes automatically.

## Trust & verifiability
`trust: community` — practical, well-regarded vendor guidance on evidence handling. Sound as process material; treat product recommendations as one option and defer to legal counsel on admissibility.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensic-osint-kb-guides |
